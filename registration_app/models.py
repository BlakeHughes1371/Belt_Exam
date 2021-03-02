from django.db import models
from datetime import date
import re 


# Create your models here.

class UserManager(models.Manager):
	def registrationvalidator(self, forminfo):

		today = date.today()

		EMAIL_REGEX = re.compile(
			r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		
		print("filter is working", User.objects.filter(email=forminfo['email']))
		emailistaken = User.objects.filter(email=forminfo['email'])
		error = {}

		if len(forminfo['firstname']) == 0:
			error['firstnamereq'] = "First Name Is Required!"
		elif len(forminfo['firstname']) < 2:
			error['firstnamelength'] = "First Name Must Be At least 2 Characters!"
		
		if len(forminfo['lastname']) == 0:
			error['lastnamereq'] = "Last Name Is Required!"
		elif len(forminfo['lastname']) < 2:
			error['lastnamelength'] = "Last Name Must Be At least 2 Characters!"

		if len(forminfo['email']) == 0:
			error['emailreq'] = "Email Is Required!"
		elif not EMAIL_REGEX.match(forminfo['email']):
			error['invalidemail'] = "Email Is Not Valid"
		elif len(emailistaken) > 0:
			error['emailtaken'] = "Email Is Already Registered"

		if len(forminfo['password']) == 0:
			error['passwordreq'] = "Password Is Required!"
		if len(forminfo['password']) < 8:
			error['passwordlength'] = "Password Must Be At least 8 Characters!"
		elif forminfo['password'] != forminfo['confirmpassword']:
			error['passwordmatch'] = "Passwords Must Match!"
		
		if len(forminfo['birthday']) == 0:
			error['birthdayreq'] = "Birthday Is Required!"
		elif forminfo['birthday'] > str(today):
			error['nofuturebirthday'] = "Birthday Can't Be In Future!"
		
		return error

	def userinfovalidator(self, forminfo):
		today = date.today()

		EMAIL_REGEX = re.compile(
			r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

		print("filter is working", User.objects.filter(email=forminfo['email']))
		emailistaken = User.objects.filter(email=forminfo['email'])
		error = {}

		if len(forminfo['firstname']) == 0:
			error['firstnamereq'] = "First Name Is Required!"
		elif len(forminfo['firstname']) < 2:
			error['firstnamelength'] = "First Name Must Be At least 2 Characters!"

		if len(forminfo['lastname']) == 0:
			error['lastnamereq'] = "Last Name Is Required!"
		elif len(forminfo['lastname']) < 2:
			error['lastnamelength'] = "Last Name Must Be At least 2 Characters!"

		if len(forminfo['email']) == 0:
			error['emailreq'] = "Email Is Required!"
		elif not EMAIL_REGEX.match(forminfo['email']):
			error['invalidemail'] = "Email Is Not Valid"
		elif len(emailistaken) > 0:
			error['emailtaken'] = "Email Is Already Registered"
			return error

#--------------------------------------------------------------------
	def loginvalidator(self, forminfo):
		error = {}
		matchingemail = User.objects.filter(email=forminfo['email'])
		if len(matchingemail) == 0:
			error['emailnotfound'] = "This Email Is Not Registered"
		elif matchingemail[0].password != forminfo['password']:
			error['incorrectpassword'] = "Incorrect Password"
		return error
#--------------------------------------------------------------------
class QuoteManager(models.Manager):
	def quotevalidator(self, forminfo):
		error = {}
		if len(forminfo['author']) == 0:
			error['authorreq'] = "Author Is Required!"
		elif len(forminfo['author']) < 3:
			error['authorlength'] = "Author Must Be At least 3 Characters!"

		if len(forminfo['quote']) == 0:
			error['quotereq'] = "Quote Is Required!"
		elif len(forminfo['quote']) < 10:
			error['quotelength'] = "Quote Must Be At least 10 Characters!"
		return error
#--------------------------------------------------------------------
class User(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __str__(self):
		return f"<User object: {self.firstname} ({self.id})>"
#-------------------------------------------------------------------
class Quote(models.Model):
	author = models.CharField(max_length=255)
	quote = models.TextField(max_length=255)
	uploader = models.ForeignKey(User, related_name="uploadedquotes", on_delete=models.CASCADE)
	likers= models.ManyToManyField(User, related_name="favoritequotes")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = QuoteManager()
	def __str__(self):
		return f"<Quote object: {self.author} ({self.id})>"
#-------------------------------------------------------------------


