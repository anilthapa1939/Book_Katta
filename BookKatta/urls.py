from django.urls import path
from . import views
from . views import sell,dsell,agrisell,archsell

urlpatterns = [
    path('',views.Home,name='Home'),
    path('login',views.login,name='login'),
    path('items',views.items,name='items'),
    path('ditems',views.ditems,name='ditems'),
    path('archItems',views.archItems,name='archItems'),
    path('agriItems',views.agriItems,name='agriItems'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('sell',sell.as_view(),name='sell'),
    path('dsell',dsell.as_view(),name='dsell'),
    path('agrisell',agrisell.as_view(),name='agrisell'),
    path('archsell',archsell.as_view(),name='archsell'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('Bcategory',views.Bcategory,name='Bcategory'),
    path('Scategory',views.Scategory,name='Scategory'),
    path('Selling',views.Selling,name='Selling'),
    path('Dselling',views.Dselling,name='Dselling'),
    path('AgriSelling',views.AgriSelling,name='AgriSelling'),
    path('ArchSelling',views.ArchSelling,name='ArchSelling'),
    


]