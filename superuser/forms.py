from django import forms
from student.models import Course
from franchise.models import Franchise

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class FranchiseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = '__all__' 
