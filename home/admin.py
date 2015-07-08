from django.contrib import admin
from home.models import *

class Admin_User(admin.ModelAdmin):
    list_display =['firstName','lastName','emailId']


class Admin_Offers(admin.ModelAdmin):
    list_display = ['headline','description','time_start','time_end']
    list_filter = ['time_start','time_end']
    search_fields = ['headline']

class Admin_Phone_Design(admin.ModelAdmin):
    list_display = ['design_code','design_Image','design_name','design_status','design_sell_count','design_hit_count']
    list_filter = ['design_hit_count','design_sell_count']
    search_fields = ['design_code','design_name']


class Admin_Phone_Model(admin.ModelAdmin):
    list_display = ['model_name','model_code']
    search_fields = ['model_name','model_code']


class Admin_Phone_Company(admin.ModelAdmin):
    list_display = ['company_name','image_tag']
    list_filter = ['company_name']
    search_fields = ['company_name']

class Admin_Selfi(admin.ModelAdmin):
       list_display=['selfi_code','selfi_user','image_tag','selfi_time','selfi_status']
       list_filter=['selfi_time']


class Admin_Item(admin.ModelAdmin):
    list_display = ['itemType','itemCompany']
    list_filter = ['itemType']
    search_fields = ['itemType']

class Admin_blog(admin.ModelAdmin):
    list_display = ['blogname','blogcode']

class Admin_blogspot(admin.ModelAdmin):
    list_display = ['headLine',]

class Admin_banner(admin.ModelAdmin):
    list_display = ['description','headline','bannerStatus','Imageurl']
    list_filter = ['bannerStatus','headline']
    search_fields = ['headline','bannerStatus']


# Register your models here.
admin.site.register(Offers,Admin_Offers)
admin.site.register(User,Admin_User)
admin.site.register(Phone_Company,Admin_Phone_Company)
admin.site.register(Phone_Model,Admin_Phone_Model)
admin.site.register(Phone_Design,Admin_Phone_Design)
admin.site.register(Selfi_Image,Admin_Selfi)
admin.site.register(Item,Admin_Item)
admin.site.register(blog,Admin_blog)
admin.site.register(blogpost,Admin_blogspot)
admin.site.register(Banner,Admin_banner)





