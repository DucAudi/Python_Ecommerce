
# import re
# from django import forms
# from django.contrib.auth.models import User
# from .models import Post

# class Register(forms.Form):
#     username = forms.CharField(label="Account")
#     email = forms.EmailField(label="Email")
#     password1 = forms.CharField(label="password", widget=forms.PasswordInput())
#     password2 = forms.CharField(label="Re-enter password", widget=forms.PasswordInput())

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not re.search(r'^\w+$', username):
#             raise forms.ValidationError("Accounts with special characters !")
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError("Account already exists !")
    
#     def clean_password2(sefl):
#         if'password1' in sefl.cleaned_data:
#             password1 = sefl.cleaned_data['password1']
#             password2 = sefl.cleaned_data['password2']
#             if password1 == password2 and password1:
#                 return password2
#         raise forms.ValidationError('invalid password !')
    
#     def save(self):
#         User.objects.create_user(
#             username = self.cleaned_data['username'],
#             email = self.cleaned_data['email'],
#             password = self.cleaned_data['password1']
#         )

