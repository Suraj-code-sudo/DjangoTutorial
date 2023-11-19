from django.shortcuts import render
from django.http import HttpResponse
from .models import Voters
# Create your views here.

def index(request):
    return HttpResponse("Hello This is Working")

def home(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        name = request.POST.get('voter_name')
        is_voted = False
        
        data = {'age':0}

        if int(age) >= 18:
            data['age'] = 1
            is_voted = True
        
        obj = Voters.objects.create(name = name, age=age, is_voted = is_voted)
        obj.save()



        # data = {'cities':
        #         [
        #             'Chennai',
        #             'Bangalore',
        #             'Goa'
        #         ],
        #         'age':19
        #         }
                

        return render(request, "home.html", context=data)
    return render(request, "home.html")