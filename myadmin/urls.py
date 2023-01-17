from django.urls import path

from . import views
urlpatterns = [
    
    path('',views.adminhome),
    path('manageusers/',views.manageusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('addcategory/',views.addcategory),
    path('addsubcategory/',views.addsubcategory),
    path('cpmyadmin/',views.cpmyadmin),
    path('epmyadmin/',views.epmyadmin),
    path('viewsfund/',views.viewsfund),
    path('addcampaigns/',views.addcampaigns),
    path('vappoint/',views.vappoint)
    
]
