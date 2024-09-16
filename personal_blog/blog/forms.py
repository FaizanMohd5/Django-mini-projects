from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField()
    your_email = forms.EmailField()
    subject_line = forms.CharField()
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Heyya! type here whatever you wanna send me!',  
            'rows': 4,                                    # Number of visible rows
            'cols': 40,                                    # Number of visible columns
            'class': 'form-control',                       # CSS class for styling
        })
    )


