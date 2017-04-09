
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
import json
from fastfoods.models import Category, Product,UserComments
from django.template.loader import render_to_string
# Create your views here.
from django.contrib import messages

def index(request):
    cats = Category.objects.all()
    products = {}
    for i in range(len(cats)):
        proj = (Product.objects.filter(product_cat=cats[i]))
        if len(proj) is not 0:
            products[cats[i].category_name]=proj
    comments = UserComments.objects.all();
    if len(comments) > 0:
        pass
    else:
        comments=['Empty list']
    # print(products)
    return render(request, 'fastfoods/index.html', {'productx':products,'comments':comments})


def usercomments(request):
    useremail = request.POST.get('useremail','10ejics727@gmail.com')
    username = request.POST.get('username','10ejics727@gmail.com')

    usermessage = request.POST.get('usermessage','10ejics727@gmail.com')
    ucmts=UserComments(user_email=useremail,user_name=username,user_message=usermessage)
    ucmts.save()
    # messages.success(request, 'Thanks for your feed back. :)')

    return HttpResponse('Thanks for feedback')

