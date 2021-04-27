from django import forms
from blog_app.models import post,comment

class post_form(forms.ModelForm):

    class Meta():
        model = post
        fields = ('author','title','text')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'textinputclass'}),
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'})
        }


class comment_form(forms.ModelForm):

    class Meta():
        model = comment
        fields = ('author','text')

    widgets = {
        'author' : forms.TextInput(attrs={'class' : 'textinputclass'}),
        'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'})
    }
