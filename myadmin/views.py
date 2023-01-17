from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from . import models
from app2 import models as app2_models
from user import models as user_models
import time

#middleware to check session for admin routes
def sessioncheckmyadmin_middleware(get_response):
    def middleware(request):
        if request.path=='/myadmin/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/manageuserstatus/' or request.path=='/myadmin/addcategory/' or request.path=='/myadmin/addsubcategory/':
           if request.session['sunm']==None or request.session['srole']!="admin":
                response = redirect('/login/')
           else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware


# Create your views here.
def adminhome(request):
    #print(request.session["sunm"])
    return render(request,"adminhome.html",{"sunm":request.session["sunm"]})

def manageusers(request):
    uDetails=app2_models.Register.objects.filter(role="user")
    return render(request,"manageusers.html",{"uDetails":uDetails,"sunm":request.session["sunm"]})

def manageuserstatus(request):
    email=request.GET.get("email")
    s=request.GET.get("s")
    if s=="block":
        app2_models.Register.objects.filter(email=email).update(status=0)
    elif s=="verify":
        app2_models.Register.objects.filter(email=email).update(status=1)
    else:
        app2_models.Register.objects.filter(email=email).delete()                
    return redirect("/myadmin/manageusers/")

def addcategory(request):
    if request.method=="GET":
        return render(request,"addcategory.html",{"output":"","sunm":request.session["sunm"]}) 
    else:
        catname=request.POST.get("catname")
        caticon=request.FILES["caticon"]
        fs= FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p=models.Category(catname=catname,caticonname=filename)  
        p.save()
        return render(request,"addcategory.html",{"output":"Category added successfully..","sunm":request.session["sunm"]}) 

def addsubcategory(request):
    clist=models.Category.objects.all()
    if request.method=="GET":
        return render(request,"addsubcategory.html",{"output":"","clist":clist,"sunm":request.session["sunm"]}) 
    else:
        catname=request.POST.get("catname")
        subcatname=request.POST.get("subcatname")
        caticon=request.FILES["caticon"]
        fs= FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p=models.SubCategory(catname=catname,subcatname=subcatname,subcaticonname=filename,)  
        p.save()
        return render(request,"addsubcategory.html",{"output":"Sub Category added successfully..","clist":clist,"sunm":request.session["sunm"]})

def cpmyadmin(request):
    if request.method=="GET":
        return render(request,"cpmyadmin.html",{"sunm":request.session["sunm"]})
    else:
        sunm=request.session["sunm"]
        opass=request.POST.get("opass")
        npass=request.POST.get("npass")
        cnpass=request.POST.get("cnpass")
        userDetails=app2_models.Register.objects.filter(email=sunm,password=opass)
        if len(userDetails)>0:
            if npass==cnpass:
                app2_models.Register.objects.filter(email=sunm).update(password=npass)
                return render(request,"cpmyadmin.html",{"sunm":sunm,"output":"Password Change successfully...."})
            else:
                 return render(request,"cpmyadmin.html",{"sunm":sunm,"output":"New & Confirm New password mismatch"})
        else:
            return render(request,"cpmyadmin.html",{"sunm":sunm,"output":"Invalid old password"})

def epmyadmin(request):
	sunm=request.session["sunm"]
	if request.method=="GET":
		if request.GET.get("result")==None:
			output=""
		else:
			output="myadmin Details Updated Successfully...."		
		myadminDetails=app2_models.Register.objects.filter(email=sunm)
		m,f="",""
		if myadminDetails[0].gender=="male":
			m="checked"
		else:
			f="checked"			
		return render(request,"epmyadmin.html",{"sunm":sunm,"myadminDetails":myadminDetails[0],"output":output,"m":m,"f":f})
	else:
		name=request.POST.get("name")
		email=request.POST.get("email")
		mobile=request.POST.get("mobile")
		address=request.POST.get("address")
		city=request.POST.get("city")
		gender=request.POST.get("gender")
		
		app2_models.Register.objects.filter(email=email).update(name=name,mobile=mobile,address=address,city=city,gender=gender)
		
		return redirect("/myadmin/epmyadmin/?result=1")

def viewsfund(request):
    fDetails=user_models.Payment.objects.all()
    return render(request,"viewsfund.html",{"sunm":request.session["sunm"],"fDetails":fDetails})

    
def addcampaigns(request):
    sclist=models.SubCategory.objects.all()
    if request.method=="GET":
        return render(request,"addcampaigns.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":""})    
    else:
        title=request.POST.get("title")
        subcatname=request.POST.get("subcatname")
        description=request.POST.get("description")
        ldate=request.POST.get("ldate")
        edate=request.POST.get("edate")

        p=models.Campaigns(title=title,subcatname=subcatname,description=description,ldate=ldate,edate=edate,info=time.asctime())

        p.save()

        return render(request,"addcampaigns.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":"Campaigns Start....."})

def vappoint(request):
    vDetails=app2_models.appoint.objects.all()
    # print(vDetails)
    return render(request,"vappoint.html",{"vDetails":vDetails})