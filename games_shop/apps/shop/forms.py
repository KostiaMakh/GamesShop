from django import forms
from .models import (
    Game,
    Company,
    Device,
    Genre,
    Language,
    Status,
)

companies_list = Company.objects.all()
devices_list = Device.objects.all()
genre_list = Genre.objects.all()
languages_list = Language.objects.all()
default_status = Status.objects.get(is_default=True)


class GameCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=256,
                            label='Game title',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(label='Game title',
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    poster = forms.ImageField(label='Game poster (logo)',
                              widget=forms.FileInput(attrs={'class': 'form-control'}))
    release_year = forms.DateField(label='Release date',
                                   widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    companies = forms.ModelChoiceField(companies_list,
                                       label='Company',
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       empty_label=None)

    genres = forms.ModelChoiceField(genre_list,
                                    label='Genre',
                                    widget=forms.Select(attrs={'class': 'form-control'}),
                                    empty_label=None)

    devices = forms.ModelMultipleChoiceField(devices_list,
                                             label='Devices',
                                             widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    languages = forms.ModelMultipleChoiceField(languages_list,
                                               label='Languages',
                                               widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    price = forms.IntegerField(label='Price, USD',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    status = forms.ModelChoiceField(widget=forms.HiddenInput(attrs={'value': default_status.id}),
                                    queryset=Status.objects.all())

    class Meta:
        model = Game
        fields = (
            'title',
            'poster',
            'description',
            'genres',
            'devices',
            'languages',
            'price',
            'companies',
            'release_year',
            'status'
        )
