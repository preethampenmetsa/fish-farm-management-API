# 🐟 Fish Farm Management API

A scalable backend system for managing fish farming operations, built using Django and Django REST Framework. This project handles pond management, fish stocking, sampling, mortality tracking, and feed usage with a clean relational design.

---

## 🚀 Features

* Pond management
* Fish type management
* Feed type management
* Stocking fish into ponds
* Sampling fish growth (weight tracking)
* Mortality tracking with reasons
* Feed usage tracking
* RESTful API design

---

## 🧱 Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** (Planned - JWT)
* **Environment Management:** python-decouple

---

## 📁 Project Structure

```
AquaTrack/
│
├── accounts/        # User management
├── ponds/           # Pond related APIs
├── fish/            # Fish types
├── feed/            # Feed types
├── stocking/        # Stocking fish into ponds
├── sampling/        # Growth tracking
├── mortality/       # Fish mortality tracking
├── config/          # Project settings
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/preethampenmetsa/fish-farm-management-API.git
cd fish-farm-management-API
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup PostgreSQL database

Create a database manually in PostgreSQL.

Example:

```
DB_NAME=fishfarm
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

### 5️⃣ Create `.env` file

Create a `.env` file in root directory:

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 6️⃣ Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 7️⃣ Run server

```
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints (Sample)

### 🔹 Pond

* `POST /api/ponds/`
* `GET /api/ponds/`

### 🔹 Fish

* `POST /api/fish/`
* `GET /api/fish/`

### 🔹 Feed

* `POST /api/feed/`
* `GET /api/feed/`

### 🔹 Stocking

* `POST /api/stocking/`
* `GET /api/stocking/`

### 🔹 Sampling

* `POST /api/sampling/`
* `GET /api/sampling/`

### 🔹 Mortality

* `POST /api/mortality/`
* `GET /api/mortality/`

---

## 🧠 Key Design Decisions

* Each pond has independent stocking cycles
* Sampling and mortality are linked to specific stock entries
* Feed usage is tracked per stocking
* PostgreSQL used for relational consistency and scalability

---

## ⚠️ Important Notes

* `.env` file is not included in the repository for security reasons
* Ensure PostgreSQL is running before starting the server
* Migrations are included for easy setup

---

## 🚧 Future Improvements

* JWT Authentication
* Role-based access control
* Dashboard & analytics
* Docker support
* Deployment (AWS / Render)

---

## 👨‍💻 Author

Preetham Penmetsa

---

## ⭐ Contributing

Contributions are welcome. Feel free to fork and improve.

---

## 📜 License

This project is open-source and available under the MIT License.
