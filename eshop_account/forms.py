from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )
 

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با مشخصات زیر ثبت نام نکرده است')
        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='تعداد کاراکتر های وارد شده نمی تواند بیشتر از 20 '
                                                                  'باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکتر های وارد شده نمی تواند کم تر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_user_by_email = User.objects.filter(email=email).exists()

        if is_exist_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری می باشد')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exist_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password
