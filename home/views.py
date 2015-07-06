from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from django.core.urlresolvers import reverse
from home.models import User,Phone_Company,Phone_Model,Phone_Design,Selfi_Image

from django.db.models import Q
from home.models import Create_Own_Design
from forms import SignupForm ,LoginForm



def menuList(request):
  menu_list=["Home","Cover","Gift","Create Your Own Design","Track Your Order"]   
  return menu_list

def get_carousel(request):
   carousel=[{'headline':"haikent",'description':"this is stuf working here",'Imageurl':"home/bannerimage/1.jpg" },{'headline':"haikent",'description':"this is stuf working here",'Imageurl':'home/bannerimage/2.jpg'},{'headline':"haikent",'description':"this is stuf working here",'Imageurl':'home/bannerimage/3.jpg'},{'headline':"haikent",'description':"this is stuf working here",'Imageurl':'home/bannerimage/4.jpg'},{'headline':"haikent",'description':"this is stuf working here",'Imageurl':'home/bannerimage/5.jpg'}]
   return carousel

def get_offers(request):
    offers=[{'headline':"50% off",'description':"  get Soon "},{'headline':"30% off",'description':"  get Soon "}]
    return offers 


def get_tophit_design(request,company='all',modelname='all'):
    if company=='all'and modelname=='all':
        tophitlist=Phone_Design.objects.all().order_by('-design_hit_count')[:10]

    elif modelname=='all':
        tophitlist=Phone_Design.objects.filter(design_model__model_company__company_name=company)

    else:
        tophitlist=Phone_Design.objects.filter(design_model__model_company__company_name=company ,design_model__model_name=modelname)
    return tophitlist



def get_selfilist(request):
     selfilist=Selfi_Image.objects.all().order_by('-selfi_time')[:10]

     return selfilist


def get_companylist(request):
     company_list=Phone_Company.objects.all()
     return company_list

def get_modellist(request,company="Apple"):
      modellist=Phone_Model.objects.filter(model_company__company_name=company)
      return modellist

def index(request):
    
     #menu list 
     menu_list=menuList(request)
     carousel=get_carousel(request)
     offers=get_offers(request)
     tophitlist=get_tophit_design(request)
     selfilist=get_selfilist(request)
     company_list=get_companylist(request)

     context=RequestContext(request, {'title':'phonewalaa','menu_list':menu_list,'carousel':carousel,'offers':offers,\
      'tophitlist':tophitlist,'selfilist':selfilist,'company_list':company_list,\
       'signupform':SignupForm(),'loginform':LoginForm()})
     return render_to_response('home/home.html',context)


     

def sign_Up(request):

     data=request.POST
     firstName=data.get('firstName')
     lastName=data.get('lastName')
     emailId=data.get('emailId')
     contactNo=data.get('contactNo')
     cityName=data.get('cityName')
     gender=data.get('gender')
     password=data.get('password')
     dateOfBirth=data.get('dateOfBirth')
     try:
          obj=User.objects.get(email_Id=email_Id)
          return HttpResponse('False')
     except:
          obj=user.object.create()
          obj.firstName=firstName
          obj.lastName=lastName
          obj.emailId=emailId
          obj.contactNo=contactNo
          obj.cityName=cityName
          obj.password=password
          obj.dateOfBirth=dateOfBirth
          obj.gender=gender
          obj.save()
          request.session['emailId']=emailId
          return HttpResponse('True')

def  login_Authantication(request):

     data=request.POST
     emailId=data.get('emailId')
     password=data.get('password')
     flag=False

     try:
          obj=user.objects.get(emailId=emailId)
          if obj.emailId==emailId and obj.password==password:
               flag=True
               request.session['email_Id']=email_Id
          else:
               flag=False
     except:
          HttpResponse('False')

     return HttpResponse(flag)

def  logOut(request):

     try:
         del request.session['emailId']
     except:
         pass
     return HttpResponseRedirect("/home/")


def profile(request):
    menu_list=menuList(request)
    company_list=get_companylist(request)

    return render_to_response('home/commonpage.html',{'page':"profile",'menu_list':menu_list,'company_list':company_list})


def overview(request):
     return HttpResponse("overview")



def policy(request):
     return HttpResponse("policy") 



def  termandcondition(request):
      return HttpResponse("termandcondition")


def order_page(request,code):
          menu_list=menuList(request)
          company_list=get_companylist(request)
          item=Phone_Design.objects.get(design_code=code)
          item.design_hit_count+=1
          item.save()
          similaritem=get_tophit_design(request,item.design_model.model_company.company_name,\
            item.design_model.model_name)
          return render_to_response('home/commonpage.html',{'page':'orderpage','item':item,'menu_list':menu_list,'company_list':company_list,'similaritem':similaritem})
        

def  mobilecover(request):
     menu_list=menuList(request)
     company_list=get_companylist(request)
     itemlist=[]
     activecompany=None
     activemodel=None
     modellist=""
     if request.GET:
          
          if request.GET.get('company') and not request.GET.get('model'):
            companyname=str(request.GET.get('company'))
            activecompany=Phone_Company.objects.get(company_name=companyname)
            itemlist=get_tophit_design(request,companyname)
            modellist=get_modellist(request,companyname)
          elif request.GET.get('company') and request.GET.get('model'):
            companyname=str(request.GET.get('company'))
            activemodel=Phone_Model.objects.get(model_name=request.GET.get('model'))
            activecompany=Phone_Company.objects.get(company_name=companyname)
            itemlist=get_tophit_design(request,companyname,activemodel.model_name)
            modellist=get_modellist(request,companyname)

          elif request.GET.get('code'):
               return order_page(request,request.GET.get('code'))  
     
     else:
            itemlist=get_tophit_design(request)
     

   

     return render_to_response('home/commonpage.html',\
      {'page':"mobilecover",'menu_list':menu_list,'company_list':company_list,\
      'itemlist':itemlist,'activecompany':activecompany,'modellist':modellist,\
      'activemodel':activemodel})



def  temperglass(request):
      return HttpResponse("temperglass")




def commingsoon(request):
       return HttpResponse("commingsoon")


def  mobileskin(request):
       return HttpResponse("mobileskin")


def  laptopskin(request):
       return HttpResponse("laptopskin")



def  event(request):
       return HttpResponse("event")


def   social(request):
       return HttpResponse("social") 


def    press(request):
         return HttpResponse("press") 


def facebook(request):
       return HttpResponse("facebook")


def instagram(request):
      return HttpResponse("instagram")


def twiter(request):
     return HttpResponse("twiter")


def payments(request):
     return HttpResponse("payments")

def shipping(request):
      return HttpResponse("shipping")


def preturn(request):
      return HttpResponse("preturn")              
            

def linkedin(request):
     return HttpResponse("likedin")

def create_Own_Design(request):

     try:
         user_email_Id=request.session['email_Id']
         if request.method=='POST':
             user_email_Id=request.POST.get('email_Id')
             phone_company=request.POST.get('phone_Company')
             phone_model=request.POST.get('phone_Model')
             #email_Id=request.POST.get('email_Id')
             desing_price=request.POST.get('design_Price')

             design_image=request.FILES.get('design_Image')

             img_obj=Create_Own_Design(email_Id=user_email_Id,phone_Company=phone_company,phone_Model=phone_model,desing_Price=desing_price,design_Image=desing_image)

             img_obj.save()
         return HttpResponseRedirect("/home/")

     except:
         return  HttpResponseRedirect("loginsignup.html")




