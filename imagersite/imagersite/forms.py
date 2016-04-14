# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# class RegisterForm(UserCreationForm):
#     """Class form being defined."""

#     username = forms.CharField(label='username', max_length=30)
#     password = forms.CharField(label='password', max_length=30)

# class RegisterForm(UserCreationForm):
#     """Class form being defined."""

#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Userfields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()
#         return user

