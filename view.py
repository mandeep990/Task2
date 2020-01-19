#This file is created by mandeep kaur.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>My Personal Navigator</h1><h2>Links for 5 websites</h2><ol><li><a href='http://www.facebook.com/'>Facebook</a></li><li><a href='http://instagram.com'>Instagram</a></li><li><a href='http://linkedin.com'>LinkedIn</a></li><li><a href='http://twitter.com'>Twitter</a></li><li><a href='http://codechef.com'>CodeChef</a></li></ol>")


