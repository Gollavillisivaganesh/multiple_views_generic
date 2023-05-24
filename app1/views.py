from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def siva(request):
    return HttpResponse('MS Dhoni')

def app1_html(request):
    return render(request,'app1_htmlpage.html')
