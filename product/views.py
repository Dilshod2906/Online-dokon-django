from django.shortcuts import render, get_object_or_404
from .models import ProductsCategory,Products, Savat, coment, hearth, city
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import commentt
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# @login_required(login_url='/accounts/login/')
def category(request,id):
    mydata = Products.objects.filter(category=id)
    asb = ProductsCategory.objects.all()[0:8]

    context56 = {
        'categor': mydata,
        'category': asb,

    }
    return render(request, 'product/category.html', context56)

     
def IndexView(request):
    asbb = Products.objects.all()
    asb = ProductsCategory.objects.all()[0:8]

    context= {
        'producttt': asbb,
        'category': asb

    }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def categoryy(request,category):
     fill = Products.objects.filter(category=category)
     asb = ProductsCategory.objects.all()[0:8]

     context = {
          'fill':fill,
          'category': asb

     }
     return render(request,'product/products.html', context)
 
 
def ProductView(request,page=1):
    categories = ProductsCategory.objects.all()
    products = Products.objects.all()
    asb = ProductsCategory.objects.all()[0:8]

    per_page = 2
    pgntr = Paginator(products, per_page)
    products_pgntr = pgntr.page(page)
    
    
    context = {
        'categories': categories,
        'products': products,
        'category': asb,
        'pgtnr': products_pgntr   
    }
    return render(request, 'product/products.html',context)


def savol_javob(request):
    return render(request, 'product/savol_javob.html')


@login_required(login_url='/accounts/login/')
def Product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    commen = coment.objects.filter(pro=product)
    data = request.POST
    

    if request.method == 'POST':


            form2 = commentt(request.POST, request.FILES)
            
            if form2.is_valid():
     
                comment = form2.save(commit=False)
                comment.userr = request.user
                comment.pro = product

                comment.save()
                
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
            

    else:
                form2 = commentt()
    soni = len(commen)
    context = {
        'product': product,
        'form2':form2,
        'commen':commen,
        'soni':soni
       
    }
    return render(request, 'product/Product_detail.html',context)

@login_required(login_url='/accounts/login/')
def savatga_qushish(request,product_id):
    product = Products.objects.get(id=product_id)
    savat = Savat.objects.filter(user=request.user, product=product,)
    if not savat.exists():
        Savat.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        savat1 = savat.first()
        savat1.quantity +=1
        savat1.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    
def heartht(request,product_idd):
    product = Products.objects.get(id=product_idd)
    savat = hearth.objects.filter(user=request.user, product=product,)
    if not savat.exists():
        hearth.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        savat1 = savat.first()
        savat1.quantity +=1
        savat1.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    

@login_required(login_url='/accounts/login/')
def savat_list(request):
    listlar = Savat.objects.all().filter(user=request.user)
    count = len(listlar)
    
    all_price = 0
    eco = 0
    
    for price in listlar:
        product_count = int(price.quantity)
        product_old_price = int(price.product.old_prices)
        product_price = int(price.product.price)
        
        x = product_count * product_price
        y = product_count * product_old_price
        
        eco += y
        all_price += x
        
        
    
    context = {
        'ls':listlar,
        'conut': count,
        'eco': eco,
        'all_price': all_price,
        'tejov': eco - all_price
    }
    return render(request, 'product/savat.html', context)


def javob_list(request):
    listlar1 = hearth.objects.all().filter(user=request.user)
    context = {
        'javob2':listlar1
    }
    return render(request, 'product/saralangan.html', context)


def deletel(request, idd):
        instance = Savat.objects.get(id=idd)
        instance.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def deletel2(request, idd):
        instance = hearth.objects.get(id=idd)
        instance.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class QidirishView(ListView):
    model = Products
    template_name = 'product/qidirish.html'
    context_object_name = 'javob'
    
    def get_queryset(self):
        data = self.request.GET.get('q')
        return Products.objects.filter(
            Q(name__icontains=data)|Q(description__icontains=data)
        )