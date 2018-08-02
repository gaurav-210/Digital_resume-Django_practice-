from django import forms

class contactForm(forms.Form):
	 fullname= forms.CharField(widget=forms.
	 	             TextInput(attrs=
	 	             	{"class":"form-control", 
	 	             	"placeholder":"enter full name",
	 	             	 "id":"form_full_name"})
	 	             )
	 email= forms.CharField(widget=forms.
	 	             EmailInput(attrs=
	 	             	{"class":"form-control", 
	 	             	"placeholder":"enter your email",
	 	             	 "id":"email"}))

	 content= forms.CharField(widget=forms.
	 	             Textarea(attrs=
	 	             	{"class":"form-control", 
	 	             	"placeholder":"enter text her",
	 	             	 "id":"text "}))
	 def clean_email(self):
	 	email = self.cleaned_data.get("email")
	 	if not "gmail.com" in email:
	 		raise forms.ValidationError("Email has to be gmail.com")
	 	return email	

     
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.
	 	             TextInput(attrs=
	 	             	{"class":"form-control", 
	 	             	"placeholder":"@Username",
	 	             	 "id":"username "}))
	password = forms.CharField(widget=forms.
	 	             PasswordInput(attrs=
	 	             	{"class":"form-control", 
	 	             	"placeholder":"must include some specila character",
	 	             	 "id":"password"}))
