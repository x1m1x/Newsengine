from django import forms
from django.core.exceptions import ValidationError

from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        image = forms.ImageField()

        fields = ['title', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control'}),
            'body': forms.Textarea(attrs={'class': 'form_control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug may not be "create"')
        return new_slug

    def clean_title(self):
        new_title = self.cleaned_data['title']

        if Article.objects.filter(title__iexact=new_title).count()>2:
            raise ValidationError('Title is already exist')
        return new_title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['author_name', 'body', 'article']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug may not be "create"')
        return new_slug
