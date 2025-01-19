from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerAuthenticated
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .serializers import (CategorySerializer,
                          CategoryGetSerializer,
                          PaymentSerializer,
                          ProductReviewGetSerializer,
                          ProductReviewSerializer,
                          ProductSerializer,
                          ProductGetSerializer,
                          CartSerializer,
                          OrderSerializer,
                          OrderGetSerializer
                          )
from .models import (Category,
                     Payment,
                     ProductReview,
                     Product,
                     Cart,
                     Order
                     )


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [IsOwnerAuthenticated, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoryGetSerializer
        else:
            return CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # permission_classes = [IsOwnerAuthenticated, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductGetSerializer
        else:
            return ProductSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [IsOwnerAuthenticated, IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderGetSerializer
        else:
            return OrderSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


#     permission_classes = [IsOwnerAuthenticated, IsAuthenticated]


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = ProductSerializer


#     permission_classes = [IsOwnerAuthenticated, IsAuthenticated]


class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

    #     permission_classes = [IsOwnerAuthenticated, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductReviewGetSerializer
        else:
            return ProductReviewSerializer
