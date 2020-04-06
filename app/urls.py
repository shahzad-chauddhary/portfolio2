from . import views
from django.urls import path

urlpatterns = [

    path('index',views.index,name='index'),
    path('about', views.about, name='about'),
    path('portfolio-work', views.portfolio_work, name='portfolio_work'),
    path('work_details', views.work_details, name='work_details'),
    path('services', views.services, name='services'),
    path('elements', views.elements, name='elements'),
    path('contact', views.contact, name='contact'),
    path('blog',views.blog,name='blog'),
    path('single_blog',views.single_blog,name='single_blog'),

]