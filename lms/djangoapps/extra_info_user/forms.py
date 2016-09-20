from django import forms
from extra_info_user.models import ExtraInfo


class ExtraInfoUserForm(forms.ModelForm):

    class Meta:
        model = ExtraInfo
        fields = ('educational_centre_code', )
