from django.http import HttpResponse


def home(request):
	return HttpResponse("<h1>Hello and welcome to demo site </h1>")