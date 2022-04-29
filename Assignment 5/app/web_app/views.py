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
    
    if request.method == "POST":
        form = forms.ProfileManager(request.POST)
        if form.is_valid():
            user = request.user
            
            user.has_profile = True
            
            user.clientinformation.fullname = form.cleaned_data.get("fullname");
            user.clientinformation.address1 = form.cleaned_data.get("address1");
            user.clientinformation.address2 = form.cleaned_data.get("address2");
            user.clientinformation.city = form.cleaned_data.get("city");
            user.clientinformation.state = form.cleaned_data.get("state");
            user.clientinformation.zipcode = form.cleaned_data.get("zipcode");
            
            user.clientinformation.save()
            user.save()
            return HttpResponseRedirect('')
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
       sub_quote = True 
       gallons = request.GET['gallons_requested']
       delivery_date = request.GET['delivery_date']
       
       suggested = pricing_module(int(gallons), hist_count, user.clientinformation.state) + 1.5
       total = int(gallons) * suggested
       
       form = forms.FuelQuote()      
    elif request.method == "POST" and sub_quote:
        form = forms.FuelQuote(request.POST)
        if form.is_valid():
            new_p = models.Fuel_Quote.objects.create()
            new_p.username=request.user.username    
            new_p.gallons_requested = form.cleaned_data.get("gallons_requested");
            new_p.delivery_address = user.clientinformation.address1 + ", " + user.clientinformation.city + " " + user.clientinformation.state
            new_p.delivery_date = form.cleaned_data.get("delivery_date");
            new_p.suggested_price = suggested;
            new_p.total_due = total;

            new_p.save()
            return HttpResponseRedirect('')
    else:
        form = forms.FuelQuote()    
            
    return render(request, 'fuel_quote_form.html',{'form':form, 'gallons': gallons, 'delivery_date': delivery_date, 'sub_quote': sub_quote, 'total': total, 'suggested': suggested})
    
# Registration page
class register(CreateView):
    form_class = forms.UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    