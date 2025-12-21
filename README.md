# Task Manager - Django Full Stack Project

A comprehensive task management and project collaboration platform built with Django 4.2. This project demonstrates advanced Django concepts including custom user models, complex relationships, authentication, CRUD operations, and modern web design.

## 🌟 Features

### User Management
- **Custom User Model** with extended fields (bio, profile picture, job title, etc.)
- **User Authentication** (Register, Login, Logout)
- **User Profiles** with detailed information
- **Profile Editing** with image upload support

### Project Management
- **CRUD Operations** for projects
- **Project Status Tracking** (Planning, Active, On Hold, Completed, Cancelled)
- **Priority Levels** (Low, Medium, High, Critical)
- **Team Collaboration** with member management
- **Progress Tracking** with completion percentage
- **Project Updates** and activity log
- **Budget Tracking**

### Task Management
- **Comprehensive Task CRUD** operations
- **Task Assignment** to team members
- **Status Workflow** (To Do, In Progress, Review, Completed, Blocked)
- **Priority Management** (Low, Medium, High, Urgent)
- **Due Dates** with overdue tracking
- **Time Tracking** (estimated vs actual hours)
- **Task Comments** system
- **Task History** tracking changes
- **File Attachments** support
- **Tag System** for organization

### Dashboard & Analytics
- **User Dashboard** with statistics
- **Recent Tasks** and Projects overview
- **Progress Visualization**
- **Quick Actions** for common operations

### Additional Features
- **Advanced Filtering** and Search
- **Pagination** for large datasets
- **Responsive Design** with Bootstrap 5
- **Toast Notifications** for user feedback
- **Permission System** (owner/member access control)
- **URL Slugification** for SEO-friendly URLs

## 🛠️ Technical Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5.1.3, Bootstrap Icons
- **Forms**: Django Crispy Forms with Bootstrap 4
- **Database**: SQLite (easily switchable to PostgreSQL/MySQL)
- **Static Files**: WhiteNoise for production-ready static file serving
- **Authentication**: Django's built-in authentication system

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
cd task_manager_project
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
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

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
task_manager_project/
│
├── config/                 # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── accounts/              # User management app
│   ├── models.py          # Custom User & UserProfile models
│   ├── views.py           # Authentication & profile views
│   ├── forms.py           # User forms
│   ├── urls.py            # Account URLs
│   └── admin.py           # Admin configuration
│
├── projects/              # Project management app
│   ├── models.py          # Project & ProjectUpdate models
│   ├── views.py           # Project CRUD views
│   ├── forms.py           # Project forms
│   ├── urls.py            # Project URLs
│   └── admin.py           # Admin configuration
│
├── tasks/                 # Task management app
│   ├── models.py          # Task, Comment, TaskHistory models
│   ├── views.py           # Task CRUD & comment views
│   ├── forms.py           # Task forms
│   ├── urls.py            # Task URLs
│   └── admin.py           # Admin configuration
│
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Landing page
│   ├── accounts/          # Account templates
│   ├── projects/          # Project templates
│   └── tasks/             # Task templates
│
├── static/                # Static files
│   └── css/
│       └── style.css      # Custom CSS
│
├── media/                 # User uploaded files
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## 🎯 Key Concepts Demonstrated

### 1. Models & Relationships
- **Custom User Model** (AbstractUser)
- **One-to-One** relationships (User → UserProfile)
- **Foreign Key** relationships (Task → Project, Task → User)
- **Many-to-Many** relationships (Project ↔ Users)
- **Model Properties** and methods
- **Model Meta** options

### 2. Views
- **Function-Based Views** (FBV)
- **Class-Based Views** (CBV)
  - ListView
  - DetailView
  - CreateView
  - UpdateView
  - DeleteView
- **Mixins** (LoginRequiredMixin, UserPassesTestMixin)
- **Context Data** manipulation

### 3. Forms
- **ModelForms** for database models
- **Custom Form Validation**
- **Form Widgets** customization
- **Crispy Forms** integration

### 4. Templates
- **Template Inheritance**
- **Template Tags** and Filters
- **Static Files** management
- **Context Processors**

### 5. URLs
- **URL Patterns** and naming
- **URL Parameters** (pk, slug)
- **URL Namespacing**

### 6. Admin
- **ModelAdmin** customization
- **Inline Admin** forms
- **List Display** and filters
- **Search Fields**

### 7. Authentication & Authorization
- **Login/Logout** functionality
- **User Registration**
- **Permission Checks**
- **@login_required** decorator

### 8. Advanced Features
- **File Uploads** (images, attachments)
- **Pagination**
- **Search & Filtering**
- **Slug Generation**
- **Messages Framework**
- **Custom Managers** (if implemented)

## 🔐 Default Credentials

After creating a superuser, you can:
- Access admin panel: `http://127.0.0.1:8000/admin/`
- Use your superuser credentials

## 📊 Database Schema

### User Model
- username, email, password (built-in)
- bio, profile_picture, phone_number, location
- date_of_birth, job_title, department
- created_at, updated_at

### Project Model
- name, slug, description
- owner (FK to User)
- members (M2M with User)
- status, priority
- start_date, end_date, budget
- created_at, updated_at

### Task Model
- title, description
- project (FK to Project)
- assigned_to (FK to User)
- created_by (FK to User)
- status, priority
- due_date, estimated_hours, actual_hours
- tags, attachments
- created_at, updated_at, completed_at

## 🎨 Customization

### Change Color Scheme
Edit `static/css/style.css` and modify CSS variables:
```css
:root {
    --primary-color: #0d6efd;
    --success-color: #198754;
    /* etc. */
}
```

### Add More Fields
1. Add field to model in `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Update forms and templates

### Switch to PostgreSQL
Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🐛 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --clear
```

### Database Issues
```bash
# Delete db.sqlite3 and migrations, then:
python manage.py makemigrations
python manage.py migrate
```

### Permission Errors
Ensure the user is logged in and has proper permissions.

## 📝 Testing the Project

1. **Register** a new user
2. **Login** with credentials
3. **Create** a project
4. **Add** team members
5. **Create** tasks and assign them
6. **Update** task status
7. **Add** comments
8. **Edit** your profile
9. **Test** filtering and search
10. **Access** admin panel

## 🎓 University Project Notes

This project demonstrates:
- ✅ Full CRUD operations
- ✅ User authentication & authorization
- ✅ Complex database relationships
- ✅ Form validation
- ✅ File uploads
- ✅ Responsive design
- ✅ Clean code architecture
- ✅ Comments and documentation
- ✅ Best practices
- ✅ Admin interface customization

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## 🤝 Contributing

This is a university project, but suggestions are welcome!

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

Created as a comprehensive Django university project demonstrating full-stack development skills.

---

**Good Luck with Your Presentation! 🎓**
