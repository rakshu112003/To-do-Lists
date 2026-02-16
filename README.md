# To-do-Lists
To-do List Project

**Author:** Rakshitha HN  
**GitHub:** [https://github.com/rakshu112003/To-do-Lists](https://github.com/rakshu112003/To-do-Lists)

---

## Project Overview

This is a **To-do List Application** built with:

- **Frontend:** React.js (Vite)  
- **Backend:** Python Flask  
- **Database:** MySQL  

The app allows users to view a list of tasks with their current status (`Pending` or `Done`). It demonstrates full-stack development with **separate frontend and backend** and a clean folder structure.

---

## Folder Structure
To-do-Lists/ ├─ frontend/ │    ├─ src/ │    │    ├─ App.jsx │    │    ├─ main.jsx │    │    ├─ app.css │    │    ├─ index.css │    │    └─ assets/       # SVG/images │    ├─ package.json │    ├─ vite.config.js │    └─ .eslintrc.js └─ backend/ ├─ app.py └─ db_config.py ├─ README.md
Copy code

---

## Features

- **Display tasks**: Simple Task, MERN Stack Project, Python Project, Write Report  
- **Status**: Pending / Done  
- **API**: Flask backend provides tasks via `/todos` endpoint  
- **React frontend** consumes backend API  

---

## Setup Instructions

### Backend

1. Navigate to `backend/` folder  
2. Install dependencies:  

```bash
pip install -r requirements.txt
Run Flask server:
Copy code
Bash
python app.py
Default server URL
1. Navigate to `frontend/` folder
2. Open `index.html` in browser or using Live Server extension
3. Make sure backend is running (http://127.0.0.1:5000/todos)
4. Tasks will be visible on frontend
Ensure MySQL database credentials are correct in db_config.py
Frontend
Navigate to frontend/ folder
Install dependencies:
Copy code
Bash
npm install
Run frontend:
Copy code
Bash
npm run dev
Default URL: http://localhost:5173
Make sure backend server is running for tasks to display
