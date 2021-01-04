from django.urls import path

from .views import ContactUsCreateView

app_name = "support"

urlpatterns = [
    path("contact-us/", ContactUsCreateView.as_view(), name='contact-us'),
]
