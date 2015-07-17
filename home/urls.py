from django.conf.urls import url
from .import views

urlpatterns=[
            url(r'^$', views.index, name='index'),
            url(r'^signup/$',views.sign_Up,name='sign_Up'),
            url(r'^login/$',views.login,name="login"),
            url(r'^page/(?P<page>\w+)/$',views.page_common,name="common_page"),
            url(r'^mobilecover/$',views.mobilecover,name="mobilecover"),
            url(r'^temperglass/$',views.temperglass,name="temperglass"),
            url(r'^commingsoon',views.commingsoon,name="commingsoon"),
            url(r'^mobileskin',views.mobileskin,name="mobileskin"),
            url(r'^laptopskin',views.laptopskin,name="laptopskin"),
            url(r'^order',views.order,name="order"),
            url(r'^buttonClick/$',views.buttonClick,name="buttonClick"),
            url(r'^shipping/$',views.shipping,name="shipping")
          ]