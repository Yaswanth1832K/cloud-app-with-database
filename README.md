# Cloud Academy LMS - Premium Online Learning Platform

A sophisticated Django-based Learning Management System featuring a premium Navy & Gold aesthetic, glassmorphism design, and seamless user experience.

## 🌟 Key Features

- **Premium UI/UX**: Modern "Deep Space" theme with Navy & Gold accents, glassmorphism cards, and smooth CSS animations
- **User Authentication**: Secure registration and login system with error handling
- **Course Management**: Browse courses, view detailed content, and track enrollment
- **Interactive Exams**: Take quizzes with instant feedback and detailed score breakdowns
- **Responsive Design**: Fully responsive layout optimized for all devices
- **Dynamic Content**: Lessons and exam questions dynamically loaded from the database

## 🚀 Technologies

- **Backend**: Django 3.1.3, Python 3.8+
- **Frontend**: Bootstrap 4, Custom CSS3 (Variables, Animations, Glassmorphism)
- **Database**: SQLite (development), PostgreSQL-ready for production
- **Fonts**: Google Fonts (Outfit)

## 🛠️ Quick Start

### 1. Clone the Repository
```bash
git clone: https://github.com/Yaswanth1832K/cloud-app-with-database.git
cd cloud-app-with-database
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Optional) Populate Sample Data
```bash
python populate_content.py
```

### 6. Start Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and navigate to: `http://127.0.0.1:8000/onlinecourse/`

## 📚 Usage

1. **Register**: Create a new account at `/onlinecourse/registration/`
2. **Login**: Sign in at `/onlinecourse/login/`
3. **Browse Courses**: View available courses on the homepage
4. **Enroll**: Click "Enroll" on any course card
5. **Study**: Review course lessons and content
6. **Take Exam**: Click "Take Final Exam" to test your knowledge
7. **View Results**: See your score and detailed answer breakdown

## 🎨 Design Highlights

- **Glassmorphism Cards**: Frosted glass effect with backdrop blur
- **Animated Hero Section**: Eye-catching landing page with gradient animations
- **Hover Effects**: Interactive course cards with lift and scale transforms
- **Score Visualization**: Dynamic circular progress indicator for exam results
- **Micro-interactions**: Button glows, nav link underlines, and smooth transitions

## 📁 Project Structure

```
cloud-app-witg-database/
├── myproject/              # Django project settings
├── onlinecourse/           # Main application
│   ├── models.py          # Database models (Course, Lesson, Question, etc.)
│   ├── views.py           # View logic
│   ├── templates/         # HTML templates
│   └── migrations/        # Database migrations
├── static/                # Static files (CSS, images)
│   └── style.css         # Custom premium styling
├── media/                 # User-uploaded content
├── populate_content.py    # Script to populate sample data
└── manage.py             # Django management script
```

## 🔧 Troubleshooting

### Styles Not Loading
- Hard refresh: `Ctrl + F5` (Windows) or `Cmd + Shift + R` (Mac)
- Check browser console for 404 errors
- Ensure `python manage.py runserver` is running

### Database Issues
- Delete `db.sqlite3` and run migrations again
- Check migration status: `python manage.py showmigrations`

### Port Already in Use
- Kill existing process on port 8000
- Or run on different port: `python manage.py runserver 8080`

## 📝 License

This project is part of an educational assignment and is available for learning purposes.

## 🙏 Acknowledgments

Built with Django and Bootstrap. Designed for an exceptional learning experience.

---

**Developed by Yaswanth** | [GitHub](https://github.com/Yaswanth1832K)
