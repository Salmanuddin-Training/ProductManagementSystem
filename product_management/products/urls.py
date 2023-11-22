from django.urls import path
from products import views

urlpatterns= [
    path('', views.ShowAllProducts, name='showProducts'),
    path('productDetail/<int:pk>',views.productDetail, name='productDetail'),
    path('addProduct/',views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>',views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>', views.deleteProduct,name='deleteProduct'),
    path('search/',views.searchBar,name='search'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
]