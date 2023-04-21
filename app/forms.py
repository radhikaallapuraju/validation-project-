from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class Access_RecordsForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields='__all__'