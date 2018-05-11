from django.urls.conf import path

from simplemooc.core import views

app_name = 'core'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]
