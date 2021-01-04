from django.views.generic import CreateView

from utilis.views import merge_dicts, _header_context
from .models import ContactUs


# Create your views here.

class ContactUsCreateView(CreateView):
    model = ContactUs
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = merge_dicts(context, _header_context())
        return context
