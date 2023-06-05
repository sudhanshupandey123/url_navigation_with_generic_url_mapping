from django.shortcuts import render

# Create your views here.
def first_htmlpage(request):
    return render(request,'first_htmlpage.html')
def second_htmlpage(request):
    return render(request,'second_htmlpage.html')