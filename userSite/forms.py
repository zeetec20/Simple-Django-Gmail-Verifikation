from django import forms

class FormLogin(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput()
    )
    password = forms.CharField(
        widget = forms.PasswordInput()
    )

class FormRegister(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput()
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
    fullName = forms.CharField(
        widget = forms.TextInput()
    )
