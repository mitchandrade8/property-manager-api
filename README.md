# 🏢 Property Manager API

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

A full-stack, cloud-hosted real estate management application designed to track property statuses and tenant relationships.

This project was built to demonstrate a clean separation of concerns between a RESTful API backend and a client-side interface, establishing a scalable foundation that can be consumed by web dashboards or native mobile applications.

---

## 🚀 Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **Database:** SQLite (Local Development) / PostgreSQL (Production)
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)
* **Deployment:** Render

---

## 🧠 Architecture & Engineering Decisions

### Data Validation Layer

Incoming HTTP requests are strictly validated using **Pydantic** schemas before they interact with the database. This prevents malformed data from corrupting the tables and provides clean, automated error responses to the client.

### Relational Database Design

The application utilizes **SQLAlchemy** to manage complex one-to-many relationships (e.g., one property can house multiple tenants) without writing raw SQL.

### The Local-to-Cloud Database Pivot

The initial architecture relied on a local SQLite file. However, deploying to a PaaS (Render) with an ephemeral filesystem meant the database was wiped upon server restarts.
To solve this, the production environment was decoupled: the API remains hosted on Render, while the data layer was migrated to a serverless **PostgreSQL** database, ensuring permanent data persistence.

---

## 💻 Local Installation & Setup

If you would like to run this API on your local machine, follow these steps:

**1. Clone the repository**

```bash
git clone [https://github.com/mitchandrade8/property-manager-api.git](https://github.com/YOUR_USERNAME/property-manager-api.git)
cd property-manager-api
