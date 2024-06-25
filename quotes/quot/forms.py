from django.forms import TextInput, ModelForm, CharField, Textarea, SelectMultiple, Select
from .models import Author, Quotes, Tag
from datetime import datetime


class AuthorAddForm(ModelForm):
    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=15, required=True, widget=TextInput())
    born_location = CharField(min_length=2, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=300, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteAddForm(ModelForm):
    class Meta:
        model = Quotes
        fields = ['quote', 'tags', 'author']
        widgets = {
            'quote': Textarea(attrs={'rows': 3}),
            'tags': SelectMultiple(),
            'author': Select(),
        }

    # Optionally, override the init method to customize form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
        self.fields['author'].queryset = Author.objects.all()