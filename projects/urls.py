from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<slug:slug>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('<slug:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<slug:slug>/add-update/', views.add_project_update, name='add_project_update'),
]
