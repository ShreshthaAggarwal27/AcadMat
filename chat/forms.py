from django import forms
from django.forms import ModelForm
from chat.models import ChatMessage

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows": 3, "placeholder": "Type a message"}))
    class Meta:
        model = ChatMessage
        fields = ['body', ]