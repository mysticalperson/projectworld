from django.http import HttpResponse
from django.shortcuts import render
from.models import places
from.models import member
# Create your views here.
def myfun(request):
    obj=places.objects.all()
    myobj=member.objects.all()
    return render(request,'index.html',{'result':obj,'res':myobj})






