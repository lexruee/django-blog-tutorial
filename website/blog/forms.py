from django import forms

class CommentForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField()
    content = forms.CharField(label='Comment', widget=forms.Textarea())
