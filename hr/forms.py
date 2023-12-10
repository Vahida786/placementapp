from django import forms

from myapp.models import Category,Jobs


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class CategoryForm(forms.ModelForm):
   class Meta:
       fields=["name"]
       model=Category

class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=("status",)
        widgets={
            "category":forms.Select(attrs={"class":"form-select form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})

        }
    #    fields="__all__"



class JobChangeForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"
        widgets={
            "category":forms.Select(attrs={"class":"form-select form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})

        }
