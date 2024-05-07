from django import forms 

from django.contrib.auth.models import User





class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi userini kiriting..'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi parolini kiriting..'}))
    

class change_password(forms.Form):


    passwordc = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4','style':'width:500px', 'placeholder':'ozgartirmoqchi bolgan parolini kiriting..'}))
    


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi ismini kiriting..'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi familyani kiriting..'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi userini kiriting..'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi emailini kiriting..'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi parolini kiriting..'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi parolini kiriting..'}))
    
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
 

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     pass1 = self.cleaned_data.get("password")
    #     pass2 = self.cleaned_data.get("password2")
    #     if pass1 and pass2 and pass1 != pass2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return pass2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserRegistrationForm, self).save(commit=True)
    #     user.set_password(self.cleaned_data["password2"])
    #     if commit:
    #         user.save()
    #     return user