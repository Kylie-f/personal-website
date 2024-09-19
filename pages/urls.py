from django.urls import path
from .views import home_page_view, about_page_view #NEW

urlpatterns = [
    path("about/", about_page_view), #NEW
    path("", home_page_view),

]