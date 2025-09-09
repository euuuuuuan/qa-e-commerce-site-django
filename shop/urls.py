# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_user, name='logout_user'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/update/<int:cart_item_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:cart_item_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.create_order, name='create_order'),
    path('order-complete/', views.order_complete, name='order_complete'),
]

# shop/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
    # POST 요청(로그인 버튼 클릭)일 경우
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')  # 로그인 성공 시 메인 페이지로 이동
            else:
                return render(request, 'shop/login.html', {'form': form, 'error_message': '잘못된 사용자명 또는 비밀번호입니다.'})
    # GET 요청(페이지 접근)일 경우
    else:
        form = AuthenticationForm()
    
    return render(request, 'shop/login.html', {'form': form})