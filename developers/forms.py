from django import forms
from .models import Language, Spoken_Language, Framework, Developer
from .widgets import CustomClearableFileInput


class DeveloperForm(forms.ModelForm):

    class Meta:
        model = Developer
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        frameworks = Framework.objects.all()
        f_friendly_names = [(c.id, c.get_friendly_name()) for c in frameworks]

        languages = Language.objects.all()
        l_friendly_names = [(c.id, c.get_friendly_name()) for c in languages]

        spoken_languages = Spoken_Language.objects.all()
        native_names = [(c.id, c.get_nativeName()) for c in spoken_languages]

        self.fields['framework'].choices = f_friendly_names
        self.fields['language'].choices = l_friendly_names
        self.fields['spoken_language'].choices = native_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
