# 🏙️ Smart City Management System

A centralized digital platform that enables citizens to report civic issues (e.g., damaged roads, streetlight failures, water leaks, garbage overflow, etc.) and helps government authorities manage and resolve them efficiently.

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Project Goals](#project-goals)
- [System Modules](#system-modules)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Project Setup](#project-setup)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

---

## 🔰 Introduction

The **Smart City Management System** is designed to digitize and streamline the process of reporting and resolving civic issues. It bridges the communication gap between:
- Citizens
- Department Staff
- Government Administrators

This system ensures transparency, accountability, and faster resolution of issues.

---

## ❗ Problem Statement

Current challenges in civic issue management:
- No standardized or digital complaint systems
- Delayed departmental responses
- Lack of real-time updates
- Poor accountability and oversight

---

## 🎯 Project Goals

- Implement a transparent and efficient complaint resolution system
- Digitally connect citizens, department staff, and administrators
- Enable real-time issue tracking and performance monitoring

---

## 🧩 System Modules

### 👤 Citizen Module
- Register/Login securely using email
- Raise complaints with:
  - Category selection
  - Description input
  - Image upload
  - Map pin using Leaflet
- Track complaint status (Pending → In Progress → Resolved)
- View complaint history via a dashboard

### 👷 Department Staff Module
- Login and access complaints assigned to their department
- Filter, search, and update complaint status
- Resolve issues and track progress

### 🏛️ Government/Admin Module
- Monitor all city-wide complaints
- Access cross-department reports and analytics
- Visualize complaint resolution rates and performance

### 🧑‍💼 Superuser Module
- Full access to all modules and data
- Manage:
  - All user roles (citizens, staff, admins)
  - Complaint records
  - System settings

---

## 🛠️ Technologies Used

### Frontend
- `HTML` – Structure
- `CSS` – Styling
- `JavaScript` – Interactivity
- `Leaflet.js` – Location pinning via maps

### Backend
- `Python` – Core logic
- `Django` – Web framework

### Database
- `MySQL` – Relational database

### Python Libraries
- `django-jazzmin` – Enhanced admin interface
- `mysqlclient` – MySQL integration
- `Pillow` – Image processing

---

## 🏗️ System Architecture

- **citizen/** – Handles citizen-related views and models
- **department/** – Staff operations and workflows
- **myadmin/** – Admin monitoring and control panel

Other components:
- `media/` – Stores user-uploaded images
- `static/` – Contains CSS, JS, and other assets
- `templates/` – HTML template files

---

## ⚙️ Project Setup

### Requirements
- Python: `3.8.10`
- Django: `4.2.21`
- MySQL: Installed and configured

### Installation Steps

```bash
# Clone the repo
git clone https://github.com/your-username/smart-city-management.git
cd smart-city-management

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure MySQL database in settings.py

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
