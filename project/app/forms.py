from django import forms

from .models import Assignment, Message, DirectMessage


class CreateAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'description', 'dueDate', 'classAssignedTo', 'file']
        widgets = {'dueDate': forms.DateTimeInput(attrs={'type': 'datetime-local'})}


class CreateMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'body', 'recipients']


class DirectMessageForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ['recipient', 'message']
