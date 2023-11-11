from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello This is Working")

def home(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        data = {'age':0}

        if int(age) >= 18:
            data['age'] = 1


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