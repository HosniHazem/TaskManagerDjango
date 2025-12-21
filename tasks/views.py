from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from .models import Task, Comment, TaskHistory
from .forms import TaskForm, CommentForm, TaskFilterForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 15
    
    def get_queryset(self):
        queryset = Task.objects.filter(
            Q(assigned_to=self.request.user) | Q(created_by=self.request.user)
        ).distinct()
        
        form = TaskFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data.get('status'):
                queryset = queryset.filter(status=form.cleaned_data['status'])
            if form.cleaned_data.get('priority'):
                queryset = queryset.filter(priority=form.cleaned_data['priority'])
            if form.cleaned_data.get('search'):
                search = form.cleaned_data['search']
                queryset = queryset.filter(
                    Q(title__icontains=search) | Q(description__icontains=search)
                )
            if form.cleaned_data.get('assigned_to_me'):
                queryset = queryset.filter(assigned_to=self.request.user)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        context['history'] = self.object.history.all()[:10]
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by or self.request.user == task.assigned_to
    
    def form_valid(self, form):
        task = self.get_object()
        
        # Track changes
        for field in ['status', 'priority', 'assigned_to']:
            old_value = str(getattr(task, field))
            new_value = str(form.cleaned_data.get(field))
            if old_value != new_value:
                TaskHistory.objects.create(
                    task=task,
                    user=self.request.user,
                    field_changed=field,
                    old_value=old_value,
                    new_value=new_value
                )
        
        # Mark completion timestamp
        if form.cleaned_data['status'] == 'COMPLETED' and not task.completed_at:
            form.instance.completed_at = timezone.now()
        
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def add_comment(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
    
    return redirect('task_detail', pk=pk)


@login_required
def task_status_update(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    
    if request.user == task.assigned_to or request.user == task.created_by:
        old_status = task.status
        task.status = status
        
        if status == 'COMPLETED':
            task.completed_at = timezone.now()
        
        task.save()
        
        TaskHistory.objects.create(
            task=task,
            user=request.user,
            field_changed='status',
            old_value=old_status,
            new_value=status
        )
        
        messages.success(request, f'Task status updated to {task.get_status_display()}')
    
    return redirect('task_detail', pk=pk)
