from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.view, name='index'),
    path('menu/items/', views.MenuItemView.as_view(), name='items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='item'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
