from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            #Field('bio'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture']


#update the fileds for parent
class ParentProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ParentProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            #Field('bio'),
            Field('long_bio'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.ParentProfile
        fields = ['picture', 'long_bio']


#update the fileds for babysitter
class BabySitterProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BabySitterProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            #Field('bio'),
            Field('long_bio'),
            Field('ikametgah'),
            Field('sabika_kaydi'),
            Field('ogrenci_belgesi'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.BabySitterProfile
        fields = ['picture', 'long_bio', 'ikametgah', 'sabika_kaydi', 'ogrenci_belgesi']