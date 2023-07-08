from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.view, name='index'), 
    path('menu/items/', views.MenuItemView.as_view()),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls))
]