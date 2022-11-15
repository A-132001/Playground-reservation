from  .views import UserViewset
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
app_name ='api'
router = routers.DefaultRouter()
router.register('register',UserViewset)

urlpatterns = [
    path("",include(router.urls)),
    path("token",obtain_auth_token)
]