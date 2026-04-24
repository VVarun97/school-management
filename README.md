Here’s a polished **GitHub README.md** you can directly paste 👇

---

# 📚 School Management API

A RESTful API built with Node.js and Express to manage school data.
It allows users to add schools and retrieve a list sorted by proximity to a given location.

---

## 🚀 Live Demo

🌐 [https://school-management-1-lxu3.onrender.com](https://school-management-1-lxu3.onrender.com)

---

## 🛠️ Tech Stack

* Node.js
* Express.js
* MySQL (Aiven)
* Deployment: Render

---

## ✨ Features

* ➕ Add new schools
* 📍 Retrieve schools sorted by distance
* ✅ Input validation
* 🔐 Secure DB connection using environment variables
* ☁️ Hosted API (publicly accessible)

---

## 🗄️ Database Schema

```sql
CREATE TABLE schools (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL
);
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VVarun97/school-management.git
cd school-management
```

---

### 2. Install Dependencies

```bash
npm install
```

---

### 3. Setup Environment Variables

Create a `.env` file in the root directory:

```env
DB_HOST=your_host
DB_PORT=your_port
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=defaultdb
```

---

### 4. Run the Application

```bash
node app.js
```

Server will start at:

```
http://localhost:3000
```

---

## 📡 API Endpoints

### ➕ Add School

**POST** `/addSchool`

#### Request Body

```json
{
  "name": "ABC School",
  "address": "Mumbai",
  "latitude": 19.0760,
  "longitude": 72.8777
}
```

#### Response

```json
{
  "success": true,
  "message": "School added"
}
```

---

### 📍 List Schools by Proximity

**GET** `/listSchools`

#### Query Parameters

```
latitude=<value>&longitude=<value>
```

#### Example

```
/listSchools?latitude=19.07&longitude=72.87
```

#### Response

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "ABC School",
      "address": "Mumbai",
      "latitude": 19.076,
      "longitude": 72.8777,
      "distance": 1.23
    }
  ]
}
```

---

## 📏 Distance Calculation

This API uses the **Haversine formula** to calculate the distance between two geographical points based on latitude and longitude.

---

## 🧪 Testing

* Use Postman or any API client
* Test both endpoints with sample inputs
* Ensure query parameters are passed correctly

---

## ⚠️ Notes

* SSL is required for MySQL connections (Aiven)
* Free tier on Render may spin down after inactivity
* Do not commit `.env` file to GitHub

---

## 📁 Project Structure

```
school-management/
├── app.js
├── db.js
├── package.json
├── .env
└── README.md
```

---

## 📦 Deployment

Deployed using Render as a Web Service.

---

## 👨‍💻 Author

**Varun Vaidya**

---

## 🚀 Future Enhancements

* Authentication & authorization
* Pagination & filtering
* Geo-spatial indexing (MySQL)
* Docker support

---

## 📬 Submission Checklist

* ✔ GitHub repository
* ✔ Live API endpoint
* ✔ Database setup
* ✔ API documentation
* ✔ Postman collection (optional but recommended)

---

If you want, I can also:
👉 generate a **Postman collection JSON file** you can attach in submission
👉 or make this README stand out more (badges, screenshots, recruiter-friendly polish)
