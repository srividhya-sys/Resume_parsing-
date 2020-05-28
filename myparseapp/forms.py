from django import forms
from .models import Studentresume

class StudentForm(forms.ModelForm):

    class Meta:

        model = Studentresume
        fields = "__all__"
