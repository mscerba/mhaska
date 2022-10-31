from django.urls import path
from . import views
#from .views import NavbarView

urlpatterns = [
	path('', views.home, name='home'),
	path('navigace', views.navbar, name='navbar'),
	#path('navigace', NavbarView.as_view(), name='navbar'),
    #path('', views.index, {'pagename': ''}, name="home"),
	path('<str:pagename>', views.index, name='index'),
]
