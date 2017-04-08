from django.shortcuts import render, HttpResponse
from fastfoods.models import Category, Product
# Create your views here.


def index(request):
    cats = Category.objects.all()
    products = {}
    for i in range(len(cats)):
        proj = (Product.objects.filter(product_cat=cats[i]))
        if len(proj) is not 0:
            products[cats[i].category_name]=proj
    # print(products)
    return render(request, 'fastfoods/index.html', {'productx':products})

def usercomments(request):
    print('Inside ucmts')
    return HttpResponse('Inside User COmments section')