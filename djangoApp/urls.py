from django.urls import path
from .  views import *

urlpatterns = [
    path('',index,name='index'),
    path('form/', form_submission, name='form_submission'),
    path('submission-list/', submission_list, name='submission_list'),
    path('quote/',quote,name='quote'),
    path('contactUs',contactUs,name = 'contactUs'),
]