# shop/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.db.models import Sum
from django.views.decorators.http import require_POST # POST 요청만 허용하는 데코레이터 추가
from .models import Product, CartItem, Order, OrderItem
from .forms import CustomUserCreationForm

def landing_page(request):
    products = Product.objects.all()
    return render(request, 'shop/landing.html', {'products': products})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                return render(request, 'shop/login.html', {'form': form, 'error_message': '잘못된 사용자명 또는 비밀번호입니다.'})
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('landing_page')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


@login_required(login_url='login_page')
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # 이미 장바구니에 담긴 상품인지 확인합니다.
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    
    # 이미 존재하는 상품이라면 수량을 1 증가시킵니다.
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('product_detail', product_id=product_id)

@login_required(login_url='login_page')
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required(login_url='login_page')
@require_POST
def cart_update(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    quantity = request.POST.get('quantity', 1)
    
    if int(quantity) <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()
        
    return redirect('cart_detail')

@login_required(login_url='login_page')
@require_POST
def cart_remove(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

@login_required(login_url='login_page')
@require_POST
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        return redirect('cart_detail')
        
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    order = Order.objects.create(
        user=request.user,
        total_price=total_price
    )
    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )
    
    cart_items.delete()
    
    return redirect('order_complete')

@login_required(login_url='login_page')
def order_complete(request):
    return render(request, 'shop/order_complete.html')