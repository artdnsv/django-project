from django.shortcuts import render
from django.http import HttpResponse
from random import randint
# Create your views here.
NAMES = ('Денис.', 'Денис?', 'Денис!')
def hello_user_view(request):
    name = NAMES [randint(0,2)]
    print(request.user)
    return HttpResponse(f"<h1>Hello { name }</h1>")