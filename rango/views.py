from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/rango/about'>Rango says hey there world!</a")
def about(request):
    return HttpResponse("<a href='/rango/'>Rango says this is the about page.</a> \
                        <br> This tutorial has been put together by Ivaylo Lafchiev, 2090886L")
