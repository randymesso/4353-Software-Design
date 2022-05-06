from . import forms,models
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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
    
def fuel_quote(request):
    total = 0
    suggested = 0
    
    sub_quote = False
    gallons = 0
    delivery_date = None
    
    model = models.Fuel_Quote
    user = request.user
    model.delivery_address = user.clientinformation.address1
    
    # view history
    hist = models.Fuel_Quote.objects.filter(username = request.user.username)
    hist_count = hist.count()
   
    if request.method == "GET":
       form = forms.FuelQuote()      
    elif request.method == "POST" and sub_quote:
        form = forms.FuelQuote(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = forms.FuelQuote()    
            
    return render(request, 'fuel_quote_form.html',{'form':form, 'gallons': gallons, 'delivery_date': delivery_date, 'sub_quote': sub_quote, 'total': total, 'suggested': suggested})
    
# Registration page
class register(CreateView):
    form_class = forms.UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    