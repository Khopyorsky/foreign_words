from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('words_list/', words_list, name='words_list'),
    path('add_word/', add_word, name='add_word')
]
