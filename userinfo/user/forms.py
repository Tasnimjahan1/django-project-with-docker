from django.forms import ModelForm
from .models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'age',
                  'location', 'cuntry', 'mobile', 'email']
