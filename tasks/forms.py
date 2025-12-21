from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'status', 
                  'priority', 'due_date', 'estimated_hours', 'actual_hours', 'tags', 'attachments']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'tags': forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [('', 'All Status')] + Task.STATUS_CHOICES
    PRIORITY_CHOICES = [('', 'All Priorities')] + Task.PRIORITY_CHOICES
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)
    search = forms.CharField(max_length=100, required=False)
    assigned_to_me = forms.BooleanField(required=False, label='Assigned to me only')
