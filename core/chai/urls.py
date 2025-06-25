
from django.urls import path
from . import views
#localhost:8000/order
urlpatterns = [
    path('', views.allchai, name="allchai"),
    #path('order/',views.order,name="order")
    path('chai/<int:chai_id>/', views.chai_detail, name='chai_detail'),
]