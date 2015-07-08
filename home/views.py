from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from django.core.urlresolvers import reverse
from home.models import User,Phone_Company,Phone_Model,Phone_Design,Selfi_Image,Offers

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
    offers=Offers.objects.all()[:5]
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

def main(request):
     menu_list=menuList(request)
     carousel=get_carousel(request)
     offers=get_offers(request)
     tophitlist=get_tophit_design(request)
     selfilist=get_selfilist(request)
     company_list=get_companylist(request)
     data={'title':'phonewalaa','menu_list':menu_list,'carousel':carousel,'offers':offers,\
      'tophitlist':tophitlist,'selfilist':selfilist,'company_list':company_list,\
       'signupform':SignupForm(),'loginform':LoginForm()}
     return data  
    
def index(request):
     maindata=main(request)
     context=RequestContext(request,maindata)
     return render_to_response('home/home.html',context)


def sign_Up(request):
  if request.POST:
     data=request.POST
     firstName=data.get('firstName')
     lastName=data.get('lastName')
     emailId=data.get('emailId')
     contactNo=data.get('contactNo')
     cityName=data.get('cityName')
     password=data.get('password')
     dateOfBirth=data.get('dateOfBirth')
     try:
         if(User.objects.filter(emailId=emailId).count()==0):
              obj=User(firstName=firstName,lastName=lastName,emailId=emailId,contactNo=contactNo,cityName=cityName,password=password,dateOfBirth=dateOfBirth)
              obj.save()
              request.session['emailId']=emailId
              return HttpResponse('True')
         else:
             return HttpResponse('User Exist')
     except:
         return HttpResponse('False')     
          

def  login(request):
  if request.POST:
     data=request.POST
     emailId=data.get('emailId')
     password=data.get('password')
     flag=False
  #try:
     obj=User.objects.get(emailId=emailId)
     if obj.emailId==emailId and obj.password==password:
          flag=True
          request.session['emailId']=emailId
     else:
          flag=False
  #except:
      #return HttpResponse('exception')

  return HttpResponse("k")

def  logout(request):

     try:
         del request.session['emailId']
     except:
         pass
     return HttpResponseRedirect("/home/")


def openblog(request,page):
    maindata=main(request)
    maindata.update({'page':page})
    context=RequestContext(request,maindata)
    return render_to_response('home/blog.html',context)

def profile(request):
    return openblog(request,"profile")

def overview(request):
     return openblog(request,"overview")

def policy(request):
     return openblog(request,"policy")

def  termandcondition(request):
      return openblog(request,"termandcondition")

def  temperglass(request):
      return openblog(request,"temperglass")


def commingsoon(request):
       return openblog(request,"commingsoon")

def  mobileskin(request):
       return openblog(request,"mobileskin")

def  laptopskin(request):
       return openblog(request,"laptopskin")


def  event(request):
       return openblog(request,"event")


def   social(request):
       return openblog(request,"social") 


def    press(request):
         return openblog(request,"press") 



def payments(request):
     return openblog(request,"payments")

def shipping(request):
      return openblog(request,"shipping")


def preturn(request):
      return openblog(request,"preturn")              
            

def  cancellation(request):
     return openblog(request,"likedin")

def cartItemlist(request):
      maindata=main(request)
      maindata.update({'page':"cartitem"})
      template='home/commonpage.html'
      cartitemlist=[]
      tlist=request.session['itemoncart'].keys()
      try:
       cartitemlist=[Phone_Design.objects.get(design_code=x) for x in tlist]
      except:
         pass
      maindata.update({'cartitemlist':cartitemlist})  
      context=RequestContext(request,maindata)  
      return render_to_response(template,context)

def order(request): #for add cart and buy now response

  if request.POST.get('action'): 
    itemcode=str(request.POST.get('itemcode'))
    itemquantity=int(request.POST.get('itemquantity'))
    if 'itemoncart' not in request.session:
        request.session['itemoncart']={}
    if itemcode in request.session['itemoncart']:
        oldq=int(request.session['itemoncart'][itemcode])
        request.session['itemoncart'][itemcode]=oldq+itemquantity
    else:
        request.session['itemoncart'][itemcode]=itemquantity    
    if 'itemoncart_count' in request.session:
          old=int(request.session['itemoncart_count'])
          request.session['itemoncart_count']=old+itemquantity
    else:
          request.session['itemoncart_count']=1 
  
  if request.POST.get('action')=='Add to Cart':
       return index(request)
  else:
       return cartItemlist(request)
       

def order_page(request,code):
          maindata=main(request)
          maindata.update({'page':"orderpage"})
          item=Phone_Design.objects.get(design_code=code)
          item.design_hit_count+=1
          item.save()
          maindata.update({'item':item})
          similaritem=get_tophit_design(request,item.design_model.model_company.company_name,\
            item.design_model.model_name)
          maindata.update({'similaritem':similaritem})
          context=RequestContext(request,maindata)
          template='home/commonpage.html'
          return render_to_response(template,context)
        

def  mobilecover(request):
     maindata=main(request)
     maindata.update({'page':"mobilecover"})
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
     
     maindata.update({'itemlist':itemlist,'activecompany':activecompany,'modellist':modellist,'activemodel':activemodel})
     context=RequestContext(request,maindata)
     template='home/commonpage.html'
     return render_to_response(template,context)





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




