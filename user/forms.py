from cProfile import label
from subprocess import STARTF_USESHOWWINDOW
from tkinter import LabelFrame
from click import confirm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola", widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "Kullanıcı Adı")
    password = forms.CharField(max_length = 20, label = "Parola", widget = forms.PasswordInput)
    confrim = forms.CharField(max_length = 20, label = "Parola Tekrar", widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confrim")
        if password and confirm and password != confirm :
            raise forms.ValidationError("Parolalar eşleşmiyor!")
        values = {
            "username" : username,
            "password" : password,
        }
        return values


