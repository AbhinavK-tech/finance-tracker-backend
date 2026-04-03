from flask import Flask, request, jsonify
import json

app = Flask(__name__)

FILE = "data.json"

@app.route('/ui')
def ui():
    return """
    <h2>Finance Tracker</h2>
    <form action="/add" method="post">
        Amount: <input name="amount"><br>
        Type: <input name="type"><br>
        <button type="submit">Add</button>
    </form>
    """

# ------------------ LOAD DATA ------------------
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# ------------------ SAVE DATA ------------------
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ HOME ------------------
@app.route('/')
def home():
    return "Finance Tracker API Running 🚀"


# ------------------ ADD TRANSACTION ------------------
@app.route('/add', methods=['POST'])
def add():
    data = load_data()
    new = request.json

    # validation
    if not new:
        return jsonify({"error": "No data provided"}), 400

    if "amount" not in new or "type" not in new:
        return jsonify({"error": "Missing fields"}), 400

    # ensure amount is number
    try:
        new["amount"] = float(new["amount"])
    except:
        return jsonify({"error": "Amount must be a number"}), 400

    # default values
    new.setdefault("category", "general")
    new.setdefault("date", "N/A")
    new.setdefault("note", "")

    data.append(new)
    save_data(data)

    return jsonify({"message": "Transaction added successfully"})

# ------------------ VIEW ALL ------------------
@app.route('/view', methods=['GET'])
def view():
    return jsonify(load_data())

# ------------------ DELETE ------------------
@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    data = load_data()

    if index >= len(data):
        return jsonify({"error": "Invalid index"}), 400

    deleted = data.pop(index)
    save_data(data)

    return jsonify({
        "message": "Deleted successfully",
        "deleted_item": deleted
    })

# ------------------ SUMMARY ------------------
@app.route('/summary', methods=['GET'])
def summary():
    data = load_data()

    income = 0
    expense = 0

    for item in data:
        if item.get("type") == "income":
            income += item.get("amount", 0)
        else:
            expense += item.get("amount", 0)

    return jsonify({
        "income": income,
        "expense": expense,
        "balance": income - expense
    })

# ------------------ FILTER (BONUS) ------------------
@app.route('/filter', methods=['GET'])
def filter_data():
    data = load_data()
    txn_type = request.args.get("type")

    if txn_type:
        filtered = [x for x in data if x.get("type") == txn_type]
        return jsonify(filtered)

    return jsonify(data)

# ------------------ RUN ------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)