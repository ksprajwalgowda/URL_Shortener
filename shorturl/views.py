from django.shortcuts import render, redirect
import uuid
from.models import Urls
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.html")


def create(request):
    print("krolldd")

    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=link,linkid = uid)
        new_url.save()
        return HttpResponse(uid)

def goto(request, pk):
    url_details = Urls.objects.get(linkid=pk)
    return redirect(url_details.link)

    
