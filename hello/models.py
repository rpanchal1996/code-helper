from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Greeting(models.Model):
	when = models.DateTimeField('date created', auto_now_add=True)

class Coder(models.Model):
	user = models.OneToOneField(User)
	semester=models.IntegerField(null=True,blank=True)	
	#primary_key = models.AutoField(primary_key=True)
	def __str__(self):
		return u'%d  %s  %s  %d'%(self.id,self.user.username,self.user.first_name,self.semester)

class Helper(models.Model):
	user = models.OneToOneField(User)
	experience=models.IntegerField(null=True,blank=True)	
	#primary_key = models.AutoField(primary_key=True)
	def __str__(self):
		return u'%d  %s  %s  %d'%(self.id,self.user.username,self.user.first_name,self.experience)

class Classify(models.Model):
	username = models.CharField(max_length=100)
	user_type = models.IntegerField()


	def __str__(self):
		return  u'%s  %d'%(self.username,self.user_type)

class Skill(models.Model):
	username = models.CharField(max_length=100)
	skill = models.CharField(max_length=100)
	def __str__(self):
		return  u'%s  %s'%(self.username,self.skill)

class Cost(models.Model):
	username = models.CharField(max_length=100)
	cost = models.IntegerField()
	def __str__(self):
		return  u'%s  %d'%(self.username,self.cost)

class HelperProfile(models.Model):
	username = models.CharField(max_length=100)
	rating = models.IntegerField()
	phone = models.CharField(max_length=10)
	personal_details = models.CharField(max_length=400)
	github_link = models.CharField(max_length=100)
	def __str__(self):
		return  u'%s  %s'%(self.username,self.phone)

class HelperPicture(models.Model):
	username = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'pictures')

class Message(models.Model):
	to = models.CharField(max_length=100)
	sender = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.CharField(max_length=500)
	curr_time = models.CharField(max_length=100)


