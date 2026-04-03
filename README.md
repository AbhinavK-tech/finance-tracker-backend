Finance Tracker Backend (Flask)

Overview

This project is a simple Python-based backend system for managing financial transactions such as income and expenses. It provides REST API endpoints to store, retrieve, delete, and analyze financial data.

---

Features

* Add income and expense transactions
* View all transactions
* Delete transactions
* Generate summary (income, expense, balance)
* Filter transactions by type
* Input validation and error handling

---

 Tech Stack

* Python
* Flask
* JSON (as lightweight database)

---

How to Run

1. Install Flask:

```
pip install flask
```

2. Run the server:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000/
```

---

API Endpoints

### ➤ Add Transaction

POST `/add`

Example JSON:

```
{
  "amount": 1000,
  "type": "income",
  "category": "salary"
}
```

---

### ➤ View Transactions

GET `/view`

---

### ➤ Delete Transaction

DELETE `/delete/<index>`

---

### ➤ Summary

GET `/summary`

---

### ➤ Filter

GET `/filter?type=income`

---

Testing

All APIs were tested using Thunder Client (VS Code extension).

---

Design Decisions

* Used JSON file instead of database for simplicity
* Kept code beginner-friendly and easy to understand
* Focused on clean API design and logic

---

Author

Abhinav K
