from django.urls import path,include
from authenticate import views

urlpatterns = [
     path('login',views.index.as_view(),name="user authenticate"),
     path('app/',include('manager.urls'))
]