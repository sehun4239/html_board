# forms.py

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'useremail']
        widgets = {'password': forms.PasswordInput()}

class LoginForm(forms.Form):
    username = forms.CharField(label='이름', max_length=12)
    password = forms.CharField(label='비밀번호', max_length=24, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username', "이름이 존재하지 않습니다.")
                return

            if user.password == password:
                self.user_id = user.id
            else:
                self.add_error('password', "비밀번호가 틀립니다.")

