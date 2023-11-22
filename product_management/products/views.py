from django.shortcuts import render , redirect

# Create your views here.
from .models import Product , Category

from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# To View all the products in showproducts.html
# @login_required(login_url='accounts/login')
def ShowAllProducts(request):
    category = request.GET.get('category')
    if category==None:
        products = Product.objects.filter(is_published=True).order_by('-price')
    else:
        products = Product.objects.filter(category__name=category) # Get The Clicked Category Name-Data

    page_num = request.GET.get('page') # Creating The Total Page
    paginator = Paginator(products,2) # Setting Total Number Of Products In A Page:3
    try:
        products = paginator.page(page_num) # sets the no. of pages
    except PageNotAnInteger:
        products = paginator.page(1) # returns to first page if no page is there
    except EmptyPage:
        products = paginator.page(paginator.num_pages) # sets last page

    categories= Category.objects.all()

    context = {
        'products' : products,
        'categories' : categories,
    }
    return render(request, 'showProducts.html', context)

# To View the single product details in the productdetails.html
@login_required(login_url='accounts/login')
def productDetail(request, pk):
    eachproduct = Product.objects.get(id=pk)
    context ={
        'eachproduct' : eachproduct
    }
    return render(request, 'productDetail.html',context)

# To Add the new product from the html template page
@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context ={
        'form' :form
    }
    return render(request, 'addProduct.html',context)

# To Update Product Form The Html template page, updateProduct.html
@login_required(login_url='showProducts')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    context={
        'form':form
    }
    return render(request, 'updateProduct.html',context)

# To Delete The Existing Record From Table, based On Primary Key or You Can Use Unique Key
@login_required(login_url='showProducts')
def deleteProduct(request,pk):
    product=Product.objects.get(id=pk)  # storing reecord of 1 or 2 or 3 or 4 in Product
    product.delete() #  record of id(pk) is Deleted
    return redirect('showProducts')

# Creating A Function For Searching The Data From The Database Using The Keyword
@login_required(login_url='showProducts')
def searchBar(request):
    if request.method=="GET": # get = GET => True
        query = request.GET.get('query')  # query = Product
        if query:
            products = Product.objects.filter(name__contains = query)
            return render(request, 'searchBar.html', {"products":products})
        else:
            print("No Products Found To Show In The Database")
            return render(request, 'searchBar.html',{})

def contactUs(request):
    return render(request,'contactUs.html',{})

def aboutUs(request):
    return render(request,'aboutUs.html',{})