from django.urls import path,include 
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'user',views.profileViewSet)#va a tener la o las rutas correspondientes a animals
router.register(r'profile',views.userViewSet)


urlpatterns = [
    path('',include(router.urls))
]
