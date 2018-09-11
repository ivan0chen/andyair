from django import forms
from account.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter user account'}))
    password = forms.CharField(label='密碼', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    email = forms.CharField(label='E-Mail', max_length=128, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
    fullname = forms.CharField(label='姓名', max_length=128, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'full name'}))
    website = forms.URLField(label='個人網址', max_length=128, required=False, widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'url'}))
    address = forms.CharField(label='住址', max_length=128, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'fullname', 'email', 'website', 'address']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='帳號', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter user account'}))
    password = forms.CharField(label='密碼', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))

    class Meta:
        model = User
        fields = ['username', 'password']