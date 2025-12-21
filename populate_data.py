"""
Script to populate the database with sample data for demonstration
Run this after migrations: python manage.py shell < populate_data.py
"""

import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User, UserProfile
from projects.models import Project, ProjectUpdate
from tasks.models import Task, Comment

print("Starting data population...")

# Create Users
print("Creating users...")
users_data = [
    {
        'username': 'john_doe',
        'email': 'john@example.com',
        'password': 'password123',
        'first_name': 'John',
        'last_name': 'Doe',
        'bio': 'Senior Project Manager with 10 years of experience',
        'job_title': 'Project Manager',
        'department': 'IT'
    },
    {
        'username': 'jane_smith',
        'email': 'jane@example.com',
        'password': 'password123',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'bio': 'Full-stack developer passionate about clean code',
        'job_title': 'Senior Developer',
        'department': 'Engineering'
    },
    {
        'username': 'bob_wilson',
        'email': 'bob@example.com',
        'password': 'password123',
        'first_name': 'Bob',
        'last_name': 'Wilson',
        'bio': 'UI/UX Designer creating beautiful interfaces',
        'job_title': 'UI/UX Designer',
        'department': 'Design'
    },
]

users = []
for user_data in users_data:
    user = User.objects.create_user(
        username=user_data['username'],
        email=user_data['email'],
        password=user_data['password'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        bio=user_data['bio'],
        job_title=user_data['job_title'],
        department=user_data['department']
    )
    UserProfile.objects.create(user=user)
    users.append(user)
    print(f"  ✓ Created user: {user.username}")

# Create Projects
print("\nCreating projects...")
projects_data = [
    {
        'name': 'E-Commerce Platform',
        'description': 'Building a modern e-commerce platform with Django and React. Features include product management, shopping cart, payment integration, and order tracking.',
        'owner': users[0],
        'status': 'ACTIVE',
        'priority': 'HIGH',
        'start_date': datetime.now().date() - timedelta(days=30),
        'end_date': datetime.now().date() + timedelta(days=60),
        'budget': 50000.00,
        'members': [users[1], users[2]]
    },
    {
        'name': 'Mobile App Development',
        'description': 'Native iOS and Android application for task management and team collaboration with real-time synchronization.',
        'owner': users[1],
        'status': 'PLANNING',
        'priority': 'MEDIUM',
        'start_date': datetime.now().date(),
        'end_date': datetime.now().date() + timedelta(days=90),
        'budget': 35000.00,
        'members': [users[0], users[2]]
    },
    {
        'name': 'Company Website Redesign',
        'description': 'Complete redesign of company website with modern UI/UX, improved performance, and SEO optimization.',
        'owner': users[2],
        'status': 'IN_PROGRESS',
        'priority': 'CRITICAL',
        'start_date': datetime.now().date() - timedelta(days=15),
        'end_date': datetime.now().date() + timedelta(days=45),
        'budget': 25000.00,
        'members': [users[0], users[1]]
    },
]

projects = []
for proj_data in projects_data:
    members = proj_data.pop('members')
    project = Project.objects.create(**proj_data)
    project.members.set(members)
    projects.append(project)
    print(f"  ✓ Created project: {project.name}")
    
    # Add project updates
    ProjectUpdate.objects.create(
        project=project,
        author=project.owner,
        title='Project Kickoff',
        content='Project has been officially started. Team meeting scheduled for next week.'
    )

# Create Tasks
print("\nCreating tasks...")
tasks_data = [
    # E-Commerce Platform tasks
    {
        'title': 'Design Database Schema',
        'description': 'Create comprehensive database schema for products, users, orders, and payment information.',
        'project': projects[0],
        'assigned_to': users[1],
        'created_by': users[0],
        'status': 'COMPLETED',
        'priority': 'HIGH',
        'due_date': datetime.now() - timedelta(days=5),
        'estimated_hours': 8,
        'actual_hours': 7.5,
        'tags': 'database, architecture, backend'
    },
    {
        'title': 'Implement User Authentication',
        'description': 'Set up user registration, login, logout, and password reset functionality using Django authentication.',
        'project': projects[0],
        'assigned_to': users[1],
        'created_by': users[0],
        'status': 'IN_PROGRESS',
        'priority': 'HIGH',
        'due_date': datetime.now() + timedelta(days=3),
        'estimated_hours': 12,
        'tags': 'authentication, security, backend'
    },
    {
        'title': 'Design Product Page UI',
        'description': 'Create mockups and final designs for product listing and detail pages with responsive layout.',
        'project': projects[0],
        'assigned_to': users[2],
        'created_by': users[0],
        'status': 'REVIEW',
        'priority': 'MEDIUM',
        'due_date': datetime.now() + timedelta(days=7),
        'estimated_hours': 16,
        'tags': 'design, ui, frontend'
    },
    {
        'title': 'Integrate Payment Gateway',
        'description': 'Implement Stripe payment integration for secure payment processing.',
        'project': projects[0],
        'assigned_to': users[1],
        'created_by': users[0],
        'status': 'TODO',
        'priority': 'URGENT',
        'due_date': datetime.now() + timedelta(days=14),
        'estimated_hours': 20,
        'tags': 'payment, integration, backend'
    },
    
    # Mobile App tasks
    {
        'title': 'Research Mobile Frameworks',
        'description': 'Evaluate React Native vs Flutter for cross-platform development.',
        'project': projects[1],
        'assigned_to': users[1],
        'created_by': users[1],
        'status': 'COMPLETED',
        'priority': 'HIGH',
        'due_date': datetime.now() - timedelta(days=2),
        'estimated_hours': 8,
        'actual_hours': 9,
        'tags': 'research, mobile, planning'
    },
    {
        'title': 'Create App Wireframes',
        'description': 'Design wireframes for all main screens and user flows.',
        'project': projects[1],
        'assigned_to': users[2],
        'created_by': users[1],
        'status': 'IN_PROGRESS',
        'priority': 'HIGH',
        'due_date': datetime.now() + timedelta(days=5),
        'estimated_hours': 12,
        'tags': 'design, wireframes, planning'
    },
    
    # Website Redesign tasks
    {
        'title': 'Conduct User Research',
        'description': 'Interview stakeholders and analyze current website analytics.',
        'project': projects[2],
        'assigned_to': users[2],
        'created_by': users[2],
        'status': 'COMPLETED',
        'priority': 'MEDIUM',
        'due_date': datetime.now() - timedelta(days=10),
        'estimated_hours': 10,
        'actual_hours': 12,
        'tags': 'research, ux, planning'
    },
    {
        'title': 'Create Design System',
        'description': 'Develop comprehensive design system with colors, typography, and components.',
        'project': projects[2],
        'assigned_to': users[2],
        'created_by': users[2],
        'status': 'IN_PROGRESS',
        'priority': 'HIGH',
        'due_date': datetime.now() + timedelta(days=4),
        'estimated_hours': 16,
        'tags': 'design, system, branding'
    },
    {
        'title': 'Implement Responsive Layout',
        'description': 'Build responsive HTML/CSS templates for all pages.',
        'project': projects[2],
        'assigned_to': users[1],
        'created_by': users[2],
        'status': 'TODO',
        'priority': 'MEDIUM',
        'due_date': datetime.now() + timedelta(days=10),
        'estimated_hours': 24,
        'tags': 'frontend, responsive, html, css'
    },
]

tasks = []
for task_data in tasks_data:
    task = Task.objects.create(**task_data)
    tasks.append(task)
    print(f"  ✓ Created task: {task.title}")
    
    # Add some comments to tasks
    if task.status in ['IN_PROGRESS', 'REVIEW', 'COMPLETED']:
        Comment.objects.create(
            task=task,
            author=task.assigned_to if task.assigned_to else task.created_by,
            content='Working on this task. Making good progress!'
        )
        
        if task.status == 'REVIEW':
            Comment.objects.create(
                task=task,
                author=task.created_by,
                content='Great work! Please address the feedback from the team meeting.'
            )

print("\n" + "="*50)
print("✅ Database populated successfully!")
print("="*50)
print("\nSample Credentials:")
print("-" * 50)
for user in users:
    print(f"Username: {user.username} | Password: password123")
print("-" * 50)
print("\n📊 Statistics:")
print(f"  • Users created: {len(users)}")
print(f"  • Projects created: {len(projects)}")
print(f"  • Tasks created: {len(tasks)}")
print(f"\n🚀 You can now login and explore the application!")
