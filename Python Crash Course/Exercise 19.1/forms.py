from django import forms

from .models import Title, Post 

class TitleForm(forms.ModelForm):
	class Meta:
		model = Title
		fields = ['text']
		labels = {'text':''}

class PostForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ['text']
		labels = {'text':'Post:'}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}