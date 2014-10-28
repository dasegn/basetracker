#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from bt.models.membership import Membership

from crispy_forms.helper import FormHelper

class MembershipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MembershipForm, self).__init__(*args, **kwargs)  
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'



    class Media:
        css = { 'all' : ('css/chosen.css',) }
        js = (
            'js/jquery.min.js',
            'js/chosen.jquery.min.js',
            'js/chosen.init.js',
        )

    class Meta:
        model = Membership
        widgets = {
            'user' : forms.Select(attrs={'class': 'chosen-select'}),
        }

