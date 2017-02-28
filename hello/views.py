from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


import os
from .models import Greeting
from .models import Coder
from .models import Helper
from .models import Classify
from .models import Skill
from .models import Cost
from .models import HelperProfile
from .models import HelperPicture
from .models import Message
import cloudinary
from twilio.rest import TwilioRestClient 
from time import gmtime, strftime
#import cloudinary.uploader
#import cloudinary.api
#cloudinary.config( 
#  cloud_name = "dmxgzjknx", 
#  api_key = "515413213483563", 
#  api_secret = "wgLEMEXeDcGetjUIwhx3P1j5XPc" 
#)  
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def registerCoder(request):
	if(request.method == 'POST'):
		username = request.POST.get('username')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		password = request.POST.get('password')
		semester = request.POST.get('semester')
		user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
		user.set_password(password)
		user.save()
		new_user=Coder.objects.create(user=user,semester=semester)
		new_user.save()

		new_user_type  = Classify.objects.create(username=username,user_type=0)
		new_user_type.save()
		user = authenticate(username=username,password=password)
		if(user):
			login(request,user)
			return HttpResponseRedirect('/home')

		return render(request,'registerCoder.html',{})

	return render(request,'registerCoder.html')
def registerHelper(request):
	if(request.method == 'POST'):
		username = request.POST.get('username')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		password = request.POST.get('password')
		semester = request.POST.get('semester')
		user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
		user.set_password(password)
		user.save()
		new_user=Helper.objects.create(user=user,experience=semester)
		new_user.save()
		
		new_user_type  = Classify.objects.create(username=username,user_type=1)
		new_user_type.save()
		user = authenticate(username=username,password=password)
		if(user):
			login(request,user)
			return HttpResponseRedirect('/skill')

		else:
			return render(request,'registerCoder.html',{})
		
		
	
	return render(request,'registerHelper.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/invalidlogin')
			

	else:
		return render(request,'login.html',{})	

def post_login(request):
	if(request.user.is_authenticated()):	
		user = request.user
		classify = Classify.objects.get(username=user.username).user_type
		if(classify==0):
			user_fname = str(Coder.objects.get(user=user).user.first_name)
			user_lname = str(Coder.objects.get(user=user).user.last_name)
			return render(request,'home.html',{'lname':user_lname,'fname':user_fname,'show':False})
		else:
			user_fname = str(Helper.objects.get(user=user).user.first_name)
			user_lname = str(Helper.objects.get(user=user).user.last_name)
			return render(request,'home.html',{'lname':user_lname,'fname':user_fname,'show':True})

	else:
		return HttpResponseRedirect('/login')

def invalidLogin(request):
	return render(request,'invalidLogin.html')

#def add_skills(request):
#	if(request.user.is_authenticated()):
#		skill = request.POST.get('')
	
#	else:
#		return HttpResponseRedirect('/login')

def skill(request):
	if(request.user.is_authenticated()):
		if request.method == 'POST':	
			user= request.user
			username = str(user.username)
			skills_input = request.POST.getlist('checks')
			cost = request.POST.get('cost')
			
			if(Cost.objects.filter(username=username).exists()):
				old_cost = Cost.objects.get(username=username)
				old_cost.cost = cost
				old_cost.save()
			else:
				new_cost=Cost.objects.create(username=username,cost=cost)
				new_cost.save()
			
			if(Skill.objects.filter(username=username).exists()):
				Skill.objects.filter(username=username).delete()
			
			for i in skills_input:
				new_skill = Skill.objects.create(username=username,skill= str(i))
				new_skill.save()
			return HttpResponseRedirect('/home	')
		else:
			return render(request,'skill.html',{})
	else:
		return HttpResponseRedirect('/login')

#def post_login_coder(request):
#	if(request.user.is_authenticated()):
#		else:
#		return HttpResponseRedirect('/login')

def viewhelpers(request):
	
	helper_uname = []
	helper_skill = []
	helper_fname = []
	helper_lname = []
 	helper_id = []
 	helper_photo = []
 	helper_cost = []
	helpers = Helper.objects.all()
	
	for i in helpers:
		uname = str(i.user.username)
		skillset = ''
		skills = Skill.objects.filter(username=uname)
		skillset = ''
		for j in skills:
			skillset=skillset+', '+str(j.skill)
		skillset=skillset[1:]
		#for j in skills:
		#	skillset = skillset + '<li>'+str(j.skill)+'</li>'
		skillset=skillset+'</ul>'
		if(Cost.objects.filter(username=uname).exists()):
			helper_cost.append(Cost.objects.get(username=uname).cost)
		else:
			helper_cost.append(436)
		helper_uname.append(uname)
		helper_skill.append(skillset)
		helper_fname.append(i.user.first_name)
		helper_lname.append(i.user.last_name)
		helper_id.append('/helperprofile/'+str(i.id))
		if(HelperPicture.objects.filter(username=uname).exists()):
			helper_photo.append(HelperPicture.objects.get(username=uname).image.url)
		else:
			helper_photo.append(HelperPicture.objects.get(username='default').image.url)
		 

	helper_dict = zip(helper_uname,helper_skill,helper_fname,helper_lname,helper_id,helper_photo,helper_cost)
	
	return render(request,'products.html',{'dict':helper_dict})

#def edit_profile(request):
#	if(request.user.is_authenticated):

#	else:
#		return HttpResponseRedirect('/login')
def helperProfile(request):
	if(request.user.is_authenticated):
		viewer_uname = str(request.user.username)
		helperid=str(request.path)[15:]
		
		helper = Helper.objects.get(id=helperid)
		helperid_user = str(helper.user.id)
		skills = [] 
		skillset = Skill.objects.filter(username=helper.user.username)
		for i in skillset:
			skills.append(str(i.skill))
		fname = helper.user.first_name
		lname = helper.user.last_name
		if(HelperProfile.objects.filter(username=helper.user.username).exists()):
			helperprofile = HelperProfile.objects.get(username=helper.user.username)
			phone = helperprofile.phone
			github_link = helperprofile.github_link
			email = helperprofile.username
			personal_details = helperprofile.personal_details
			if(HelperPicture.objects.filter(username=helper.user.username).exists()):
				image_url = str(HelperPicture.objects.get(username=helper.user.username).image.url)	
			else:
				image_url = str(HelperPicture.objects.get(username='default').image.url)
			return render(request,'helperProfile.html',{'fname':fname,'lname':lname,'skills':skills,'phone':phone,
				'github_link':github_link,'email':email,'personal_details':personal_details,'image_url':image_url,'id':helperid_user})
		image_url = str(HelperPicture.objects.get(username='default').image.url)
		return render(request,'helperProfile.html',{'fname':fname,'lname':lname,'skills':skills,'image_url':image_url,'id':helperid_user})
	else:
		return HttpResponseRedirect('/login/')	

def editHelperProfile(request):
	#if(request.user.is_authenticated):
	#send_sms('Boo boo loves you')
	username = str(request.user.username)
	helperid = str(Helper.objects.get(user=request.user).id) 
	fname = User.objects.get(username=username).first_name
	lname = User.objects.get(username=username).last_name
	if request.method == 'POST':
		phone = request.POST.get('phone')
		github_link = request.POST.get('github_link')
		personal_details = request.POST.get('personal_details')
		image = request.FILES['image']
		if(HelperProfile.objects.filter(username=username).exists()):
			new_helper_profile = HelperProfile.objects.get(username=username)
			new_helper_profile.phone = phone
			new_helper_profile.github_link = github_link 	
			new_helper_profile.personal_details = personal_details
			new_helper_profile.save()
			if(HelperPicture.objects.filter(username=username).exists()):
				new_helper_picture = HelperPicture.objects.get(username=username)
				new_helper_picture.image  = image
				new_helper_picture.save()
				
			else:
				new_helper_picture = HelperPicture.objects.create(username=username,image=image)
				new_helper_picture.save()

			#resp = cloudinary.uploader.upload(image)
					

		else:
			new_helper_profile = HelperProfile.objects.create(phone=phone,github_link=github_link,personal_details=personal_details,username=username,rating=0) 
			new_helper_profile.save()
			new_helper_picture = HelperPicture.objects.create(username=username,image=image)
			new_helper_picture.save()
			#image_url = str(HelperPicture.objects.get(username='default').image.url)
			#resp = cloudinary.uploader.upload(image)
		
		to_redirect = '/helperprofile/'+str(helperid)
		return HttpResponseRedirect(to_redirect)
		
	else:
		
		if(HelperProfile.objects.filter(username=username).exists()):
			helperProfile = HelperProfile.objects.get(username=username)
			phone=helperProfile.phone
			github_link = helperProfile.github_link
			personal_details = helperProfile.personal_details
			if(HelperPicture.objects.filter(username=username).exists()):
				picture  = HelperPicture.objects.get(username=username)
				image_url = str(picture.image.url)
			else:
				picture = HelperPicture.objects.get(username='default')
				image_url = str(picture.image.url)
			
			#image_url = str(os.getcwd())+image_url
			#image_url='shit'
			return render(request,'editHelperProfile.html',{'phone':phone,'github_link':github_link,
				'personal_details':personal_details,'image_url':image_url,'fname':fname,'lname':lname})
		else:
			picture = HelperPicture.objects.get(username='default')
			image_url = str(picture.image.url)
			return render(request,'editHelperProfile.html',{'fname':fname,'lname':lname,'image_url':image_url})
	#else:


def send_sms(a):
	ACCOUNT_SID = "" 
	AUTH_TOKEN = "" 
 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
	client.messages.create(
    to="+919833175929", 
    from_="+14807719032", 
    body=a,
	)

def test(request):
	return render(request,'test.html',{})

def sms(request):
	to_send = 'Hey! a user '+str(request.user.first_name) + ' ' +str(request.user.last_name) + ' has expressed interest in you. '+'His email id: '+str(request.user.username)
	send_sms(to_send)
	return render(request,'smsSent.html',{})

def message(request):
	if(request.user.is_authenticated):
		msg_id = str(request.path)[5:]
		msg = Message.objects.get(id=int(msg_id))
		if(request.user==User.objects.get(username=msg.sender)):
			fname = User.objects.get(username=msg.sender).first_name
			lname = User.objects.get(username=msg.sender).last_name
			subject = msg.subject
			time = msg.curr_time
			message = msg.message
			reply = '/compose/'+ str(User.objects.get(username=msg.sender).id)			
			return render(request,'message.html',{'fname':fname,'lname':lname,'subject':subject,
				'time':time,'message':message,'reply':reply})
		else:
			return render (request,'permissiondenied.html',{})	
	else:
		return HttpResponseRedirect('/home')
def compose_message(request):
	if(request.user.is_authenticated):
		to_id = str(request.path)[9:]
		to = User.objects.get(id=int(to_id)).username
		if(request.method=='POST'):
			user= request.user
			username = str(user.username)
			message = request.POST.get('message')
			sender = username
			subject = request.POST.get('subject')
			curr_time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
			
			new_message  = Message.objects.create(sender=sender,to=to,subject=subject,message=message,curr_time=curr_time)
			
			new_message.save()
			return HttpResponseRedirect('/alreadysent')
		else:
			return render(request,'composeMessage2.html',{'to':to})
	else:
		return HttpResponseRedirect('/home')
	
def inbox(request):
	if(request.user.is_authenticated):
		user= request.user
		username = str(user.username)
		mails = Message.objects.filter(to=username)
		messages = []
		fnames = []
		lnames = []
		times = []
		subjects = []
		urls = []
		for i in mails:
			subjects.append(i.subject)
			fname = User.objects.get(username=i.sender).first_name
			lname = User.objects.get(username=i.sender).last_name 	
			fnames.append(fname)
			lnames.append(lname)
			message = str(i.message[0:10])+'...'
			messages.append(message)
			times.append(i.curr_time)
			url = '/msg/'+str(i.id)
			urls.append(url)	
		info_dict = zip(fnames,lnames,subjects,times,messages,urls)
		return render(request,'try.html',{'mails':info_dict})
	
	else:
		return HttpResponseRedirect('/home')

def msgsent(request):
	return render(request,'msgsent.html',{})





