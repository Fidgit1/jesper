from django import forms


# override allow_multiple in the clearableFileInput
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


# override clean so that it validates each file.
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


# the internet told me that this will make a date-picker widget?
class DateInput(forms.DateInput):
    input_type = 'date'


# This form is used for uploading images to the website.
class ContentForm(forms.Form):
    owner_field = forms.CharField(max_length=255)
    description_field = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    create_date_field = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    files_field = MultipleFileField()
    public_field = forms.BooleanField(required=False)
