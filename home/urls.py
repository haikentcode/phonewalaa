from django.conf.urls import url
from .import views

urlpatterns=[
            url(r'^$', views.index, name='index'),
            url(r'^signup/$',views.sign_Up,name='sign_Up'),
            url(r'^login/$',views.login_Authantication,name='login_Authantication'),
            url(r'^page/(?P<page>\w+)/$',views.page_common,name='page_common_method'),
            url(r'^mobilecover/$',views.mobilecover,name="mobilecover"),
            url(r'^temperglass/$',views.temperglass,name="temperglass"),
            url(r'^commingsoon',views.commingsoon,name="commingsoon"),
            url(r'^mobileskin',views.mobileskin,name="mobileskin"),
            url(r'^laptopskin',views.laptopskin,name="laptopskin"),
            url(r'^order',views.order,name="order"),
          ]
