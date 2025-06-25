from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
# Create your views here.
def allchai(request):
    
    # first is  seracged variable and 2nd is by default empty string
    chais = ChaiVariety.objects.all()
    search = request.GET.get('search','')
    chai_type= request.GET.get('chai_type')
    min_price =request.GET.get('min_price')
    max_price =request.GET.get('max_price')
    availability =request.GET.get('availability')
    if search:
        chais = chais.filter(name__icontains= search)
    
    if chai_type and chai_type != 'all':
        chais = chais.filter(chai_type= chai_type)

    if min_price:
        chais = chais.filter(price__lte=min_price)

    if max_price:
        chais = chais.filter(price__gte= max_price)

    if availability == True:
       chais = chais.filter(availability = True)
    elif availability == False:
        chais = chais.filter(availability = False)
     #print(ChaiVariety.objects.all()) 
    return render(request,'chai/allchai.html',
                  {'chais':chais,
                   'search':search,
                   'chai_type_choice':chai_type,
                   'min_price':min_price,
                   'max_price':max_price,
                   'availability':availability,})  

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai':chai})