from . import forms,models
from django.shortcuts import render
import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# Front page
def front_page(request):
    return render(request, 'front_layout.html', {})

# logged in profile pages    
def profile_manager(request):
    model = models.ClientInformation
    user = request.user
            
    if request.method == "POST":
        form = forms.ProfileManager(request.POST)
        if form.is_valid():
            user.has_profile = True
            
            user.clientinformation.fullname = form.cleaned_data.get("fullname")
            user.clientinformation.address1 = form.cleaned_data.get("address1")
            user.clientinformation.address2 = form.cleaned_data.get("address2")
            user.clientinformation.city = form.cleaned_data.get("city")
            user.clientinformation.state = form.cleaned_data.get("state")
            user.clientinformation.zipcode = form.cleaned_data.get("zipcode")
            
            user.clientinformation.save()
            user.save()
            return HttpResponseRedirect('')
    elif user.has_profile or hasattr('user','clientinformation'):
       fullname = user.clientinformation.fullname
       address1 = user.clientinformation.address1
       address2 = user.clientinformation.address2 
       city = user.clientinformation.city
       state = user.clientinformation.state 
       zipcode = user.clientinformation.zipcode
           
       form = forms.ProfileManager(initial={'fullname':fullname,'address1':address1,'address2':address2,'city':city,'state':state,'zipcode':zipcode})
    else:
        form = forms.ProfileManager()
        
    return render(request, 'profile_manager.html',{'form':form})

def fuel_history(request):
    hist = models.Fuel_Quote.objects.filter(username = request.user.username)
        
    return render(request, 'fuel_history.html', {'hist':hist})

def pricing_module(gallons_requested, fuel_before, location):
    location = 0
    rate_history = 0
    company_profit = 10
    gallon_fact = 0
    
    if(location == "TX"):
        location = 2
    else:
        location = 4
    
    if(fuel_before):
        rate_history = 1
    
    if(gallons_requested > 1000):
        gallon_fact = 2
    else:
        gallon_fact = 3
    
    per = location - rate_history + gallon_fact + company_profit
    
    return per*1.5

# regular fuel quote form 
def fuel_quote(request):
    total = 0
    suggested = 0
    gallons = 0
    date = None
    
    form = forms.FuelQuote()
    return render(request, 'fuel_quote_form.html',{'form':form})

# getting pricing module
def get_quote(request):
    if request.method == "GET":
        print(request.GET.get)
        user = request.user
        hist = models.Fuel_Quote.objects.filter(username = request.user.username)
        hist_count = hist.count()
        
        gallons = request.GET['gallons_requested']
        date = request.GET['delivery_date']
        suggested = pricing_module(int(gallons),hist_count, user.clientinformation.state)
        total = int(gallons) * suggested
        
        data = {"suggested_price": suggested, "total": total}
        return HttpResponse(json.dumps(data), content_type="application/json")
        
    return JsonResponse({}, status=400)    

# sending quote
@csrf_exempt 
def submit_quote(request):
    total = 0
    suggested = 0
    
    gallons = 0
    date = None
    
    model = models.Fuel_Quote
    user = request.user
    model.delivery_address = user.clientinformation.address1
   
    if request.method == "POST":
        return HttpResponseRedirect('')
    else:
        form = forms.FuelQuote()    
            
    return render(request, 'fuel_quote_form.html',{'form':form, 'gallons': gallons, 'delivery_date': date, 'total': total, 'suggested': suggested})


# Registration page
class register(CreateView):
    form_class = forms.UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    