from django.urls import path
from . import views

urlpatterns = [
	path( '' , views.financing_choices, name='financing_choices' )
]