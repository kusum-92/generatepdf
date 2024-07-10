# test/urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('generate-pdf', views.generate_pdf, name='generate_pdf'),
    #path('generate_pdf_file',views.generate_pdf_file,name='generate_pdf_file'),
]
