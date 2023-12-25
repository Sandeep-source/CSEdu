from django import forms
from student.models import Course
from franchise.models import Franchise
from django.contrib.auth.forms import UserCreationForm

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 
        exclude = ['id']

class FranchiseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = '__all__' 
        exclude = ["id"]

class UserForm(UserCreationForm):
    institute = forms.ModelChoiceField(queryset=Franchise.objects.all())
    is_superuser = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('institute','is_superuser','email',)
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.last_name = self.cleaned_data['institute'].id
        user.is_superuser = self.cleaned_data['is_superuser']
        if commit:
            user.save()
        return user
