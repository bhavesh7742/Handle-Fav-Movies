# 🎬 HandleFavMovies

## ✨ Features

- **User Authentication**: Secure Register, Login, and Logout functionality.
- **Movie Management (CRUD)**:
  - Create: Add new movies with titles, release years, and descriptions.
  - Read: View your personalized movie collection in a clean grid layout.
  - Update: Edit details of existing movies.
  - Delete: Remove movies from your collection.
- **Image Uploads**: Support for movie posters/images.
- **Modern UI**: Styled with premium CSS, responsive design, and smooth animations.
- **Deployment Ready**: Configured for Render and Whitenoise for static file serving.

## 🛠️ Tech Stack

- **Backend**: Django 5.2.x
- **Database**: SQLite (Local) / PostgreSQL (Production)
- **Styling**: Vanilla CSS (Custom UI)
- **Utilities**: 
  - `python-decouple`: For environment variable management.
  - `dj-database-url`: For dynamic database configuration.
  - `Whitenoise`: For efficient static file serving in production.
  - `Pillow`: For image processing.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd HandleFavMovies
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the root directory and add the following:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to see the app!

## 🌐 Deployment

The project is pre-configured for **Render**.

- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command**: `gunicorn HandleFavMovies.wsgi:application`

## 📁 Project Structure

- `HandleFavMovies/`: Core project settings and WSGI/ASGI config.
- `movie/`: Main application logic (models, views, forms).
- `templates/`: Global templates and UI layout.
- `static/`: CSS and frontend assets.
- `media/`: Uploaded movie posters.

---
Built with ❤️ using Django.
