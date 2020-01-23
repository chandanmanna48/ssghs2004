from .models import Friends,Gallery
from django import forms

class add_friend_form(forms.ModelForm):
    class Meta:
        model = Friends
        fields = ('name','about','image')

class add_gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image','text')


