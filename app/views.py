from django.shortcuts import render,redirect
from app.models import User
from app.forms import UserForm
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate
def login(request):
	return render(request,'login.html')

def entry(request):
	request.session['email']=request.POST['email']
	return redirect("/")
	
def vendor(request):
	return render(request,'vendor.html')

@Authenticate.valid_user
def index(request):
	users=User.objects.all()
	return render(request,"index.html",{'users':users})
	
@Authenticate.valid_user
def search(request):
	users=User.objects.filter(email=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)
	
@Authenticate.valid_user
def create(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect('/')
	form=UserForm()
	return render(request,'create.html',{'form':form})
	
	
def edit(request,id):
	user=User.objects.get(user_id=id)
	return render(request,'edit.html',{'user':user})

def update(request,id):
	user=User.objects.get(user_id=id)
	form=UserForm(request.POST,request.FILES,instance=user)
	form.save()
	return redirect('/')

def delete(request,id):
	User.objects.get(user_id=id).image.delete()
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('/')
	


	