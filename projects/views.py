from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Project, ProjectUpdate
from .forms import ProjectForm, ProjectUpdateForm, ProjectFilterForm


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Project.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user)
        ).distinct()
        
        form = ProjectFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data.get('status'):
                queryset = queryset.filter(status=form.cleaned_data['status'])
            if form.cleaned_data.get('priority'):
                queryset = queryset.filter(priority=form.cleaned_data['priority'])
            if form.cleaned_data.get('search'):
                search = form.cleaned_data['search']
                queryset = queryset.filter(
                    Q(name__icontains=search) | Q(description__icontains=search)
                )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProjectFilterForm(self.request.GET)
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['updates'] = self.object.updates.all()[:5]
        context['update_form'] = ProjectUpdateForm()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Project created successfully!')
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.owner
    
    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully!')
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
    
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.owner
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Project deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def add_project_update(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.project = project
            update.author = request.user
            update.save()
            messages.success(request, 'Update added successfully!')
            return redirect('project_detail', slug=slug)
    
    return redirect('project_detail', slug=slug)
