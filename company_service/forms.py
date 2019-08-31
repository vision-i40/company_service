from django import forms
from users.models import User


class CompanyChangeListForm(forms.ModelForm):
    User = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(), required=False)
