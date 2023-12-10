from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth import authenticate,login,logout
from hr.forms import LoginForm,CategoryForm,JobForm,JobChangeForm
from django.urls import reverse_lazy
from myapp.models import Category,Jobs

# getin pgrm easy mthd
class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            paswrd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=username,password=paswrd)
            if user_object:
                login(request,user_object)
                print("success")
                return redirect("index")
        print("failed")
        return render(request,"login.html",{"form":form})


class DashBoardView(TemplateView):
    template_name="index.html"




class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

class CategoryListCreateView(CreateView,ListView):
    template_name="category.html"
    form_class=CategoryForm
    success_url=reverse_lazy("category")
    context_object_name="data"
    model=Category
   
class CategoryDeleteView(DeleteView):
   def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.filter(id=id).delete()
        return redirect("category")
   

class JobCreateView(CreateView):
    template_name="job_add.html"
    form_class=JobForm
    success_url=reverse_lazy("index")


class JobListView(ListView):
    template_name="job_list.html"
    context_object_name="jobs"
    model=Jobs

    def get(self,request,*args,**kwargs):
        qs=Jobs.objects.all()
        if "status" in request.GET:
            value=request.GET.get("status")
            qs=qs.filter(status=value)

        return render(request,self.template_name,{"jobs":qs})



    # def get_queryset(self):
    #     return Jobs.objects.filter(status=True)
  

class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Jobs.objects.filter(id=id).delete()
        return redirect("index")

class JobUpdateView(UpdateView):
    form_class=JobChangeForm
    template_name="job_edit.html"
    model=Jobs
    success_url=reverse_lazy("index")
   
