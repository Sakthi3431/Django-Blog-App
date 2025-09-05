# Django Blog Website

A simple, fully functional blog site developed with Django, Bootstrap, and SQLite3. It includes features such as user authentication, trending posts, profile management, comments, pagination, and image uploads.

---

##  Tech Stack
- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite3

---

##  Features
- User registration, login & authentication  
- Trending posts based on views  
- Profile management (edit profile, change password, logout)  
- Personal dashboard to view your posts  
- Comment section for interaction  
- Full CRUD operations for blog posts  
- Pagination  
- Image upload handling

---

##  Setup Instructions

```bash
git clone https://github.com/Sakthi3431/Django-Blog-App.git
cd Django-Blog-App

python -m venv env
# Activate virtual environment:
# Windows: env\Scripts\activate
# macOS/Linux: source env/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (optional)
python manage.py runserver
