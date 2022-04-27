from datetime import time
from mmap import mmap
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from . import models
import hashlib
# Create your views here.

class index(View):
     def get(__seft,__request):
          try:
               token = __request.COOKIES['token']
               admin = models.admin.objects.get(pk=1)
               if admin.token == token:
                    if admin.token_due >= timezone.now():
                         return redirect('/app/caculator')
               return render(__request,'index.html')
          except:
               return render(__request,'index.html')
     def post(__seft,__request):
          code = __request.POST.get('code')
          code = hashlib.sha256(str(code).encode('utf-8')).hexdigest()
          code = code[0:len(code)-1]
          admin = models.admin.objects.get(pk=1)
          if(code == admin.password):
               token = hashlib.sha256(str(timezone.now).encode('utf-8')).hexdigest()
               admin.token = token
               admin.token_due = timezone.now() + timezone.timedelta(minutes=60)
               admin.save()
               return JsonResponse({'status':'true','token':token},status=200)
          else:
               return JsonResponse({'status':'false','token':''},status=200)
