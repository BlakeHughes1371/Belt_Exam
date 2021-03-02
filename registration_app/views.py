from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")
#--------------------------------------------
# def index(request):
# 	return render(request, "index.html")
# --------------------------------------------


def index(request):
	return render(request, "login.html")
#------------------------------------------------------------------
def register(request):   # REGISTER NEW USER FUNCTION #
	error = User.objects.registrationvalidator(request.POST)
	print("*****", error)
	if len(error) > 0:
		for key, value in error.items():
			messages.error(request, value)
		return redirect("/")
	print(request.POST["firstname"])
	print("******")
	print(request.POST["lastname"])
	print("******")
	print(request.POST["email"])
	print("******")
	newuser = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=request.POST['password'], birthday=request.POST
	['birthday'])
	request.session['loggedinuserid'] = newuser.id
	return redirect("/success")
#---------------------------------------------------------------------
def success(request):  # SUCCESSFUL LOGIN FUNCTION / PAGE #
	context = {
		'loggedinuser': User.objects.get(id=request.session['loggedinuserid']),
		'quotelist': Quote.objects.all()
	}
	
	return render(request, "success.html", context)
#---------------------------------------------------------------------
def login(request):  # LOGIN FUNCTION #
	print("*****test*****")
	print(request.POST)
	error = User.objects.loginvalidator(request.POST)
	if len(error) > 0:
		for key, value in error.items():
			messages.error(request, value)
		return redirect("/")
	matchingemail = User.objects.filter(email=request.POST['email'])
	request.session['loggedinuserid']= matchingemail[0].id
	print("****",error)
	return redirect("/success")
#---------------------------------------------------------------------
def logout(request):   # LOGOUT FUNCTION #
	request.session.clear()  
	return redirect("/")
#---------------------------------------------------------------------
def edit(request):  # UPDATE INFO PAGE #
	
	context = {
		'loggedinuser': User.objects.get(id=request.session['loggedinuserid']),
	}
	return render(request, "edit.html", context)


# quoteid    'quotestats': Quote.objects.get(id=quoteid)

#--------------------------------------------------------------------
def users(request, userid):  # DISPLAY INFO PAGE #
	context = {
		'loggedinuser': User.objects.get(id=request.session['loggedinuserid']),
		'specificuser': User.objects.get(id=userid)
	}
	return render(request, "users.html", context)
#-------------------------------------------------------------------
def addfavoritequote(request):  # ADDS A FAVORITE QUOTE #
	error = Quote.objects.quotevalidator(request.POST)
	if len(error) > 0:
		for key, value in error.items():
			messages.error(request, value)
		return redirect("/success")
	Quote.objects.create(author=request.POST['author'],
	quote=request.POST['quote'], uploader=User.objects.get(id=request.session['loggedinuserid']))
	print(request.POST)
	return redirect("/success")
#-----------------------------------------------------------------
def deletequote(request, quoteid):
	c = Quote.objects.get(id=quoteid)
	c.delete()
	return redirect("/success")
#-----------------------------------------------------------------
def updateuserinfo(request, userid):
	error = User.objects.userinfovalidator(request.POST)
	print("*****", error)
	if len(error) > 0:
		for key, value in error.items():
			messages.error(request, value)
		return redirect("/edit")
	c = User.objects.get(id=userid)
	c.firstname = request.POST['firstname']
	c.lastname = request.POST['lastname']
	c.email = request.POST['email']
	c.save()
	return redirect('/success')

