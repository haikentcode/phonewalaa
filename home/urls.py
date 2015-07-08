from django.conf.urls import url
from .import views

urlpatterns=[
            url(r'^$', views.index, name='index'),
            url(r'^signup/$',views.sign_Up,name='sign_Up'),
            url(r'^login/$',views.login,name='login'),
            url(r'logout/$',views.logout,name="logout"),
            url(r'^profile/$',views.profile,name="profile"),
            url(r'^overview/$',views.overview,name="overview"),
            url(r'^policy/$',views.policy,name="policy"),
            url(r'^termsandcondition/$',views.termandcondition,name="termsandcondition"),
            url(r'^mobilecover/$',views.mobilecover,name="mobilecover"),
            url(r'^temperglass/$',views.temperglass,name="temperglass"),
            url(r'^commingsoon',views.commingsoon,name="commingsoon"),
            url(r'^mobileskin',views.mobileskin,name="mobileskin"),
            url(r'^laptopskin',views.laptopskin,name="laptopskin"),
            url(r'^event',views.event,name="event"),
            url(r'^social',views.social,name="social"),
            url(r'^press',views.press,name="press"),
            url(r'^cancellation',views.cancellation,name="cancellation"),
            url(r'^payments',views.payments,name="payments"),
            url(r'shipping',views.shipping,name="shiping"),
            url(r'^preturn',views.preturn,name="preturn"),
            url(r'^order',views.order,name="order"),
          ]
