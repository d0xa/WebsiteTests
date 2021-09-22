#from django.urls import path
from django.urls import path
from .views import RoomView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home',RoomView.as_view()),
]

