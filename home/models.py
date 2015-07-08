from django.db import models
from django.contrib import admin
from datetime import datetime

from string import join
import os
import uuid

Image_Folder="media/"
# Create your models here.


class  Phone_Company(models.Model):
       company_name=models.CharField(max_length=100)
       company_logo=models.ImageField(upload_to=Image_Folder+'company_logo')


       def __str__(self):
           return self.company_name

       class Admin:
        pass 

       def image_tag(self):
          #--hkcheck--flag .. "/media/" use var 
          return u'<img src="/media/%s" width="100px" height="100px"/>' % self.company_logo
       image_tag.short_description = 'Image'
       image_tag.allow_tags = True   


class  Item(models.Model):
       itemType=models.CharField(max_length=20)
       itemCompany=models.ForeignKey(Phone_Company)

       def __str__(self):
           return  self.itemType

       class Admin:
           pass


class Phone_Model(models.Model):
    model_name=models.CharField(max_length=100)
    model_code=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    model_company=models.ForeignKey(Phone_Company)
    
    def __str__(self):
        return self.model_name
        
    class Admin:
        pass          
    


class Phone_Design(models.Model):
    design_code=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    design_Image=models.ImageField(upload_to=Image_Folder+'design_image')
    design_name=models.CharField(max_length=100)
    desing_specification=models.CharField(max_length=500)
    design_status=models.CharField(max_length=10)
    design_sell_count=models.IntegerField(blank=True,null=True)
    design_hit_count=models.IntegerField(blank=True,null=True)
    upload_date=models.DateTimeField(default=datetime.now(), blank=True, null=None)
    design_model=models.ForeignKey(Phone_Model)
    design_price=models.IntegerField(default=100)
    design_description=models.CharField(max_length=1000)

    def __str__(self):
        return self.design_name
    class Admin:
        pass    


class Offers(models.Model):
     headline=models.CharField(max_length=100)
     description=models.CharField(max_length=100)
     offer_image=models.ImageField(upload_to='./temp')
     offer_code=models.CharField(max_length=100)
     cover_count=models.IntegerField(blank=True, null=True)
     offer_count=models.IntegerField(blank=True, null=True)
     time_start=models.DateField()
     time_end=models.DateField()

     def image_tag(self):
         #--hkcheck--flag .. "/media/" use var 
         return u'<img src="/media/%s" width="100px" height="100px"/>' % self.selfi_image
     image_tag.short_description = 'Image'
     image_tag.allow_tags = True 

     def __str__(self):
         return self.headline
     
     class Admin:
        pass      
               

class User(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    emailId=models.EmailField(blank=False,null=False,primary_key=True)
    contactNo=models.CharField(max_length=10)
    cityName=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dateOfBirth=models.DateField(blank=True,null=True)

    def __str__(self):
        return "%s %s %s"%(self.firstName,self.lastName,self.emailId)
    
    class Admin:
        pass


class ShippingAddress(models.Model):
    fullName=models.TextField(max_length=100)
    addressLine_1=models.TextField(max_length=200)
    addressLine_2=models.TextField(max_length=200)
    town=models.TextField(max_length=20)
    stateName=models.TextField(max_length=50)
    pinCode=models.IntegerField()
    countaryName=models.TextField(max_length=20)
    mobileNo=models.TextField(max_length=15)
    additionalAddress=models.TextField(max_length=500)
    user=models.ForeignKey(User)



class Selfi_Image(models.Model):
    selfi_code=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    selfi_user=models.ForeignKey(User)
    selfi_image=models.ImageField(upload_to=Image_Folder+'selfi')
    selfi_time=models.DateTimeField(default=datetime.now(), blank=None, null=None)
    selfi_status=models.CharField(default="no",max_length=10)
    def image_tag(self):
        #--hkcheck--flag .. "/media/" use var 
       return u'<img src="/media/%s" width="100px" height="100px"/>' % self.selfi_image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Create_Own_Design(models.Model):
    design_Image=models.ImageField(upload_to=Image_Folder+'create_own_design',blank=False,null=False)
    phone_Company=models.TextField(max_length=20,blank=False,null=False)
    phone_Model=models.TextField(max_length=20,blank=False,null=False)
    email_Id=models.TextField(max_length=50,blank=False,null=False)
    design_Price=models.IntegerField(blank=False,null=False)

    def __str__(self):
        return "%s %s %s %s"%(self.designer_email_Id,self.phone_Company,self.phone_Model,self.design_Image)



class blog(models.Model):
      blogcode=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
      blogname=models.CharField(max_length=100)

      class Admin:
          pass

      def  __str__(self):
          return "%s %s"%(self.blogcode,self.blogname)


class blogpost(models.Model):
    postCode=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    headLine=models.CharField(max_length=200)
    blog=models.ForeignKey(blog)
    postData=models.TextField(max_length=5000)
    time=models.DateTimeField(default=datetime.now(), blank=None, null=None)
    postStatus=models.CharField(max_length=10,default="show")
    postImage=models.ImageField(upload_to=Image_Folder+'blog')

    class Admin:
        pass

    def  __str__(self):
        return "%s %s %s %s %s"%(self.postCode,self.headLine,self.postImage,self.postStatus,self.time)

class  banner(models.Model):
    bannerImage=models.ImageField(upload_to=Image_Folder+'banner')
    bannerText=models.CharField(max_length=100)
    bannerHeading=models.CharField(max_length=100)
    bannerStatus=models.BooleanField(default=False)
    class Admin:
        pass

    def __str__(self):
        return "%s %s %s %s"%(self.bannerText,self.bannerHeading,self.bannerStatus,self.bannerImage)


