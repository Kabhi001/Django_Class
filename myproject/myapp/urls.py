from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^user/(?P<username>[a-zA-Z]*)/$', views.user_profile),
    re_path(r'^item/(?P<item_id>[0-9]+)/$', views.item_detail),
    re_path(r'^restro/(?P<category>[\w-]+)/(?P<subcategory>[\w-]*)/?$',views.restro_detail),
    path('aboutus/', views.aboutus, name='aboutus'), 
    path('menu/', views.menu_view, name='menu'),
]