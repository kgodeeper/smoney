from multiprocessing import reduction
import this
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from django.utils import timezone
from authenticate import models 
from . import models as Mmodels
# Create your views here.
class caculator(View):
     def get(__seft,__request):
          try:
               token = __request.COOKIES['token']
               admin = models.admin.objects.get(pk=1)
               if admin.token == token:
                    if admin.token_due >= timezone.now():
                         return render(__request,'caculator.html')
               return redirect("/login")
          except:
               return redirect("/login")

class power(View):
     def get(__seft,__request):
          try:
               token = __request.COOKIES['token']
               admin = models.admin.objects.get(pk=1)
               if admin.token == token:
                    if admin.token_due >= timezone.now():
                         return render(__request,'power.html')
               return redirect("/login")
          except:
               return redirect("/login")
class bill(View):
     def get(__seft,__request):
          try:
               token = __request.COOKIES['token']
               admin = models.admin.objects.get(pk=1)
               if admin.token == token:
                    if admin.token_due >= timezone.now():
                         return render(__request,'history.html')
               return redirect("/login")
          except:
               return redirect("/login")
               

def getPower(__request):
     month = __request.POST.get('month')
     cmonth = month
     pmonth = month.split('-')
     tmonth = int(pmonth[1])-1
     if(tmonth == 0):
          tmonth = 12
     if(tmonth < 10):
          tmonth = "0" + str(tmonth)
     else:
          tmonth = str(tmonth)
     pmonth = str(pmonth[0]) + '-' + str(tmonth) + '-' + str(pmonth[2])
     print(pmonth)
     try:
          power = Mmodels.Power.objects.get(date=cmonth)
          ppower = Mmodels.Power.objects.get(date=pmonth)
          return JsonResponse({'data':{'current':power.number,'prev':ppower.number}},status=200)
     except:
          return JsonResponse({'data':{'current':'','prev':''}})

def savePower(__request):
     try:
          month = __request.POST.get('month')
          if len(month)<2:
               month = '0' + str(month)
          year  = __request.POST.get('year')
          time = str(year) + "-" + str(month) + "-" + str("01")
          print(time)
          try:
               temp = Mmodels.Power.objects.get(date=time)
               return JsonResponse({'data':{'status':'month already exist'}},status=200)
          except:
               number = __request.POST.get('number')
               power = Mmodels.Power(date = time, number = number)
               power.save()
               return JsonResponse({'data':{'status':'success'}},status=200)
     except:
          return JsonResponse({'data':'null'},status=500)

def getAllPower(__request):
     queryset = Mmodels.Power.objects.order_by('-date').values()
     return JsonResponse({'data':list(queryset)},status=200)

def saveBill(__request):
     try:
          name = __request.POST.get('name')
          price= __request.POST.get('price')
          owner= __request.POST.get('owner')
          payer= __request.POST.get('payer')
          bill = Mmodels.Bill(name=name,price=price,owner=owner,payer=payer)
          bill.save()
          return JsonResponse({'done':True},status=200)
     except:
          return JsonResponse({'done':False},status=200)

def getAllBill(__request):
     queryset = Mmodels.Bill.objects.order_by('status').values()
     return JsonResponse({'data':list(queryset)},status=200)

def payAll(__request):
     try:
          Mmodels.Bill.objects.filter(status=0).update(status=1)
          return JsonResponse({},status=200)
     except:
          return JsonResponse({},status=500)

def redo(__request):
     try:
          ID = __request.POST.get('id')
          bill = Mmodels.Bill.objects.get(pk=ID)
          bill.status = not bill.status
          bill.save()
          return JsonResponse({},status=200)
     except:
          return JsonResponse({},status=500)