from django.urls import path, include
from market.views.auth import AuthView, hello
from market.views.product import ProductListView
from market.views.category import CategoryListView
from market.views.basket import BasketInfoView
from market.views.google_auth import GoogleView
from market.views.init import InitView

urlpatterns = [ 
        path('userlogin',AuthView.as_view()),
        # path('hello',hello),
        path('category_list',CategoryListView.as_view()),
        path('product_list',ProductListView.as_view()),
        path('basket_list',BasketInfoView.as_view()),
        path('google_auth',GoogleView.as_view()),
        path('init',InitView.as_view())    
]