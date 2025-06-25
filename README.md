# ☕ Chai Café - Django Project

**Chai Café** is a beginner-friendly Django web project where users can browse different varieties of chai. It includes a styled frontend using Tailwind CSS, page navigation (Home, About, Contact), and features like image display and basic search.

---

## ✨ Features Implemented

- 🏠 Home, About, and Contact pages with Tailwind CSS UI
- 📸 Show all available chai with images, name, description, and price
- 🔍 Search chai by name (case-insensitive)
- 🧭 Navbar with working navigation links
- 🖼️ Typewriter animation and home banner
- 🧾 Responsive table for chai details
- 🖼️ Static and media image support

---

## ⚙️ Tech Stack

| Part        | Tool / Framework     |
|-------------|----------------------|
| Backend     | Django 5             |
| Frontend    | Tailwind CSS, HTML   |
| Templates   | Django Templates     |
| Image Upload| Django Media Files   |

---

## 🚀 Getting Started

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/chai-cafe.git
cd chai-cafe
python -m venv env
source env/bin/activate  # (Use env\Scripts\activate on Windows)
pip install -r requirements.txt
2. Run the Server
python manage.py migrate
python manage.py runserver


chai-cafe/
│
├── core/               # Main project (urls.py, settings.py)
├── chai/               # App containing models, views, urls
├── media/              # Uploaded chai images
├── templates/          # layout.html and shared templates
├── static/             # Tailwind + custom CSS
├── manage.py
└── README.md


✅ Next Improvements 
 Add Reviews (user rating and comments)

 Filter chai by type, price range, availability

 Add order page with cart

 Add sentiment analysis to reviews

 REST API with Django REST Framework

 User login, profile, and authentication
