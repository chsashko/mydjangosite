from django.shortcuts import render
from django.http import HttpResponse

def show_posts(request):
	if request.method == "GET":
		return HttpResponse('''<h1>BLOG page</h1>
							'<a href="https://www.youtube.com/watch?v=P0BL0gc006w">SHREK</a>'
			''')
def show_shrek(request):
	if reguest.method == "GET":
		return HttpResponse('<a href="https://www.youtube.com/watch?v=P0BL0gc006w">SHREK</a>')
	#elif request.method == "POST":


# Create your views here.
