from django.shortcuts import render,redirect,HttpResponse
from app.models import Category, Products,ContactUs, Order,Brand
from django.contrib.auth import get_user_model

from django.contrib.auth import login, authenticate
from app.models import UserCreationForm

from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def base(request):
          return render(request, 'base.html')
def index(request):
          category = Category.objects.all()
          brand=Brand.objects.all()
          brandID=request.GET.get('brand')
          categoryID=request.GET.get('category')
          if categoryID:
            products= Products.objects.filter(subcategory= categoryID)
          elif brandID:
            products = Products.objects.filter(brand=brandID).order_by('-id')
          else:
            products = Products.objects.all()

          context={'category':category,
                   'products':products,
                   'brand':brand,
                  }
          return render(request, 'index.html',context ) 
def  singup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user=authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            )
            login(request, user)
            

            return redirect('index')  # Redirect to the home page or any other desired page
    else:
        form = UserCreationForm()
    context ={
            'form':form,
        }
    
    return render(request, 'registration/singup.html',context)
#contact_page      
def contact_us(request):
    if request.method=="POST":
        contact=ContactUs(
        name = request.POST["name"],
        email = request.POST["email"],
        subject = request.POST["subject"],
        message = request.POST["message"],
        )
        contact.save()

    return render(request,'contact.html')

#addcard

@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart-detail.html')          
#chakeout
def chakeout(request):
    if request.method=="POST":
       
       address = request.POST.get('address')
       phone = request.POST.get('phone') 
       pincode = request.POST.get('pincode') 
       cart= request.session.get('cart')
       uid= request.session.get('-auth_user_id')
      
       for i in cart:
        order =Order(
          
             Products= cart[i]['name'],
            price= cart[i]['price'],
           
            image= cart[i]['image'] ,
            address=address,
            phone=phone,
            pincode=pincode,
        )
        order.save()
    return redirect("index")

    return HttpResponse("this is chakeout page")
#product_details
def product_details(request):
      category = Category.objects.all()
      brand=Brand.objects.all()
      brandID=request.GET.get('brand')
      categoryID=request.GET.get('category')
      if categoryID:
            products= Products.objects.filter(subcategory= categoryID)
      elif brandID:
            products = Products.objects.filter(brand=brandID).order_by('-id')
      else:
            products = Products.objects.all()
      contex={
        'category':category,
        'brand':brand,
         'products':products,

      }

      return render(request,'product_details.html',contex)    
#product_details_page
def product_details_page(requist,id):
    products = Products.objects.filter(id=id).first()
    contex={'products':products,}
    
    return render(requist,'product_details_page.html',contex)      
#search
def search(request):
    products = Products.objects.all()
    query = request.GET['query']
    products = products.filter(name__icontains =  query)
    contex={'products':products,}

    return render(request,"search.html",contex)
