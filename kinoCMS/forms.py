# from allauth.account.forms import SignupForm, LoginForm
# from django import forms

# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='Ім\'я')
#     last_name = forms.CharField(max_length=30, label='Прізвище')
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#         return user
