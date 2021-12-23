from django.urls import path
from .views import *
urlpatterns=[
        path('',index_view,name='index'),
        path('about/',about_view,name='about'),
        path('contact/',contact_view,name='contact'),
        path('property_single/',property_single_view,name='property_single'),
        path('property/',property_grid_view,name='property'),
        path('blog/',blog_grid_view,name='blog'),
        path('blog_single/',blog_single_view,name='blog_single'),
        path('agent_single/',agent_single_view,name='agent_single'),
        path('agents_grid/',agents_grid_view,name='agents_grid'),

]