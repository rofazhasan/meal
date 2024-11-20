## Meal Management App 🥗

A **web-based application** for managing daily meals efficiently, designed for dormitories, hostels, or shared living spaces. This app simplifies meal tracking, fund management, and reporting for both admins and users.

---

## 🚀 Features  

### Admin Features  
- View meal statuses (On/Off) for **breakfast**, **lunch**, and **dinner**.  
- Update meal prices dynamically through an admin dashboard.  
- Add funds to user wallets and track balances.  
- Generate and print **daily or monthly meal reports**.  
- Highlight users with empty or negative funds for immediate action.  

### **User Features**  
- Log meal preferences for the next day before **11 PM** (or previous preferences are carried forward).  
- View a detailed analysis of meal history and expenses.  
- Generate and print personal meal statements.  
- Check wallet balance and fund status (including negative balances).  

---

## 🛠️ Technology Stack  

### **Frontend:**  
- **HTML**, **CSS**, **JavaScript**  
- **Bootstrap** for responsive design  
- **Axios** for seamless API communication  

### **Backend:**  
- **Python** with **FastAPI** for a fast and scalable backend  
- JWT-based authentication for secure access  
- Integrated RESTful APIs  

### **Database:**  
- **PostgreSQL** for reliable and structured data storage  

### **Deployment:**  
- Deployed on **Render** for global accessibility  

---

## ⚙️ Installation  

### Prerequisites  
- Python 3.10 or higher  
- PostgreSQL installed and running  
- Docker (optional but recommended for production)

### Steps  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/rofazhasan/meal-management.git
   ```

2. **Set Up Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Create a `.env` file in the root directory with the following keys:  
   ```plaintext
   DATABASE_URL=postgresql://user:password@localhost:5432/meal_management
   SECRET_KEY=your-secret-key
   ```

5. **Run Database Migrations**  
   ```bash
   alembic upgrade head
   ```

6. **Run the Application**  
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the App**  
   Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Docker Installation  

1. **Build the Docker Image**  
   ```bash
   docker build -t meal-management-app .
   ```

2. **Run the Docker Container**  
   ```bash
   docker run -d -p 8000:8000 --env-file .env meal-management-app
   ```

3. **Access the App**  
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  

---

## 📂 Project Structure  

```plaintext
meal-management/
├── app/
│   ├── auth.py         # Authentication and user management
│   ├── models.py       # Database models
│   ├── routers/        # API routes (users, admin, meals)
│   ├── schemas.py      # Pydantic schemas for data validation
│   └── utils.py        # Utility functions
├── migrations/         # Database migration files
├── static/             # Frontend assets
├── templates/          # HTML templates
├── main.py             # Application entry point
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
└── README.md           # Project documentation
```

---

## 📊 Future Improvements  

- Add **real-time notifications** for meal status updates.  
- Introduce user **self-payment gateway integration**.  
- Enhance UI with modern frameworks like React or Vue.js.  
- Implement **analytics dashboard** for advanced reporting.  

---

## 🤝 Contributing  

We welcome contributions! If you have ideas to improve the app or find a bug, feel free to fork the repository, make your changes, and submit a pull request.  

---

## 📃 License  

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

## ✨ Acknowledgments  

This app is inspired by the need to simplify and modernize group meal management. A big thanks to the community for the constant support and motivation!  

---  

Ready to take control of your meals? Fork it, star it, and let’s make meal management effortless! 🎉
