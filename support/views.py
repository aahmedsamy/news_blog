from django.views.generic import CreateView

from utilis.views import HeaderContext
from .models import ContactUs


# Create your views here.

class ContactUsCreateView(CreateView):
    model = ContactUs
    fields = '__all__'
    extra_context = HeaderContext()
