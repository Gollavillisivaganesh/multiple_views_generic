from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1><marquee>ESALA CUP NAMDE</marquee></h1>')

def app2_html(request):
    return render(request,'app2_html.html')