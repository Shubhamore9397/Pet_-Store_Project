"""
URL configuration for petstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from petapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('details/<rid>', views.showPetDetails),
    path('register/', views.registerUser),
    path('login', views.userLogin),
    path('logout', views.userLogout), 
    path('addtocart/<petid>', views.addtocart),
    path('showcart', views.showUserCart),
    path('removepet/<cartid>', views.removeCart),
    path('updatecart/<opr>/<cartid>',views.updateCart) ,
    path('search/<pet_type>', views.searchByType),
    path('range',views.searchByRange),
    path('sort/<dir>',views.sortByPrice),
    path('confirmorder',views.confirmOrder),
    path('makepayment',views.makepayment),
    path('placeorder',views.placeOrder),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
