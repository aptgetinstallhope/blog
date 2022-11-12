from django.shortcuts import render
from category.models import MainCategories

def landingpage(request):

# Category
    ActiveCatObj = []
    if MainCategories.objects.filter(active=True).exists():
        ActiveCatObj = MainCategories.objects.filter(active=True)



    context = {
        'ActiveCatObj':ActiveCatObj,
    }
    return render(request, 'landingpage.html', context)