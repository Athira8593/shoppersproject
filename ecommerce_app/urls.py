from django.urls import path
from . import views

urlpatterns = [
    path('', views.allproduct, name='allproduct'),
    path('home', views.allproduct, name='home'),
    path('<slug:c_slug>/',views.allproduct,name='products_by_category'),
    path('all_products', views.all_product, name='all_product'),
    # path('single_view/<slug:c_slug>', views.single_view, name='single_view'),
    path('<slug:c_slug>/<slug:product_slug>/',views.single_view, name='single_view'),
    path('user_profile/<id>', views.user_profile, name="user_profile"),
    path('edit_profile/<id>', views.edit_profile, name='edit_profile'),
    path('edit_address/<id>', views.edit_address, name='edit_address'),
    # path('add_product_checkout/<id>',views.add_product_checkout, name='add_product_checkout'),
    # path('remove_product_checkout/<id>',views.remove_product_checkout, name='remove_product_checkout'),
    path('search', views.search, name='search'),
]


