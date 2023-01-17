from django.urls import path

from . import views
urlpatterns = [
    
    path('',views.userhome),
    path('viewicreams/',views.viewicreams),
    path('viewsubcat/',views.viewsubcat),
    path('funds/',views.funds),
    path('viewfunds/',views.viewfunds),
    path('payment/',views.payment),
    path('success/',views.success),
    path('cancel/',views.cancel),
    path('cpuser/',views.cpuser),
    path('epuser/',views.epuser),
    path('viewsearchcampaign/',views.viewsearchcampaign)

]
