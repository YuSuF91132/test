from django.shortcuts import render
from app.settings.models import Settings, Newave
# Create your views here.
def index(request):
    settings_all = Settings.objects.latest("id")
    newave_id = Newave.objects.latest("id")
    return render(request, "base/index.html", locals())

