from django import forms

from shop.models import Category, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
    # title = forms.CharField(max_length=100, label='Name of Course:')
    # price = forms.DecimalField(max_digits=10, label='Price of Course:')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not selected', label='Category:')

class UploadFileForm(forms.Form):
    file = forms.FileField(label='File')