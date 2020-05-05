from django.urls import path

from Cash import views

app_name = 'Cash'
urlpatterns = [
    path('', views.index, name='index'),
    path('cash_form', views.edit_form, name='edit_form'),
    path('new_form', views.new_form, name='new_form')
]
