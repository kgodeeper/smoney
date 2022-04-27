from django.urls import path
from . import views
urlpatterns = [
     path('caculator',views.caculator.as_view(),name="caculator"),
     path('power',views.power.as_view(),name="power"),
     path('bill',views.bill.as_view(),name="caculator"),
     path('get-power',views.getPower,name="get-power"),
     path('save-power',views.savePower,name="save-power"),
     path('get-all-power',views.getAllPower,name="get-all-power"),
     path('save-bill',views.saveBill,name="save-bill"),
     path('get-all-bill',views.getAllBill,name="get-all-bill"),
     path('payall',views.payAll,name="pay-all"),
     path('redo',views.redo,name="redo")
]