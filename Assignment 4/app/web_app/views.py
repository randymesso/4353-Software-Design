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
    return render(request, 'fuel_history.html',{})
    
def fuel_quote(request):
    if request.method == "POST":
        return HttpResponseRedirect('')
    else:
        form = forms.Fuel_Quote
        
    return render(request, 'fuel_quote_form.html',{})
    
# Registration page
class register(CreateView):
    form_class = forms.UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    