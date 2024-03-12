from django.shortcuts import render
from .models import Home
from homeapp import forms
from .models import Men
from .models import Menlist
from .models import Women
from .models import Womenlist

from django.http import HttpResponseRedirect
def home(request):
    post=Home.objects.all()
    return render(request,'home/home.html',{'post':post})
def contact(request):
    if request.method=='POST':
        form=forms.contactusform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.contactusform()
    return render(request,'home/contact.html',{'form':form})
def thanks(request):
    return render(request,'home/thanks.html')
def shop(request):
    return render(request,'home/shop.html')
def men(request):
    items=Men.objects.all()
    return render(request,'shop/men.html',{'items':items})
def category(request, id):
    # menlist = Menlist.objects.get(id=id)  # Assuming Menlist has an id field
    items = Menlist.objects.filter(men_id=id)
    print(items)  # Assuming Men has a foreign key 'menlist_id' referencing Menlist   
    return render(request, 'shop/category.html',{"items":items} )
def women(request):
    items=Women.objects.all()
    return render(request,'shop/women.html',{"items":items})
def cart(request,id):
    items=Womenlist.objects.filter(women_id=id)
    return render(request,'shop/cart.html',{"items":items})
