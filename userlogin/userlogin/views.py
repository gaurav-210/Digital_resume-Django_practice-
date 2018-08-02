from django.contrib.auth import authenticate , login
from django.http import HttpResponse       # Returns response
from django.shortcuts import render , redirect     # To render to a template ..
from .forms import contactForm ,LoginForm
# html form

def firstform(request):  
    contact_Form = contactForm(request.POST or None)
    context={
    "title": "contact",
    "content":"welcome to contact page",
    "form":contact_Form,

    }
    if contact_Form.is_valid():
      print(contact_Form.cleaned_data)
    # if request.method == "POST" :
       # print(request.POST)
       # print(request.POST.get('fullname'))
       # print(request.POST.get('email'))
       # print(request.POST.get('content'))
    return render(request, "form.html" , context)



# login page
def login_page(request):
  form = LoginForm(request.POST or None )
  context={
  "form": form
  }  
  
  if form.is_valid():
    print(form.cleaned_data)
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
  
    user = authenticate(request,username=username, password=password)
    if user is not None:
      login(request, user)
      # context['form'] = LoginForm()
      return redirect("/login")
    else:
       print("Errror")   
  return render(request, "login.html" , context)


# register page
def register_page(request):
   form = LoginForm(request.POST or None )
   if form.is_valid():
     print(form.cleaned_data)
   return render(request, "register.html" , {})











# django form 

# def djangoforms(request):      # Request response ..
#     contact_Form = contactForm()
#     context={
#     "title": "contact",
#     "content":"welcome to contact page",
#     "form":contact_Form

#     }
#     if request.method == "POST" :
#        print(request.POST)
#        print(request.POST.get('email'))
#        print(request.POST.get('pwd'))
#        print(request.POST.get('remember'))
#     return render(request, "djangoforms.html" , context)
