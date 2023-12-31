from django.urls import path
from . import views as v

app_name = "main"

urlpatterns = [
    path('', v.home, name='home'),
    path('companies/', v.company_list, name='company_list'),
    path('logout/', v.logout, name='logout'),
]
