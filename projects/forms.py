from django import forms
from .models import Project, ProjectUpdate


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'priority', 'start_date', 
                  'end_date', 'budget', 'members']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'members': forms.CheckboxSelectMultiple(),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectUpdate
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }


class ProjectFilterForm(forms.Form):
    STATUS_CHOICES = [('', 'All Status')] + Project.STATUS_CHOICES
    PRIORITY_CHOICES = [('', 'All Priorities')] + Project.PRIORITY_CHOICES
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)
    search = forms.CharField(max_length=100, required=False)
