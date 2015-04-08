from django.http import Http404, HttpResponse 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
import json

from .forms import CarSelectForm

from .models import Manufacturer, Car


class CarView(FormView):
    template_name = 'index.html'
    form_class = CarSelectForm
    success_url = '/'

    def form_valid(self, form):
        return render_to_response('super_cars/success.html',
                                    form.cleaned_data)


@csrf_exempt
def ajax_api(req, manf):
    if req.method == 'GET':
        carsQS = Car.objects.filter(manufacturer__name=manf).values('name');
        carsList = [car for car in carsQS]
        carsJson = json.dumps(carsList)
        return HttpResponse(carsJson)
    return HttpResponse("NOT GET")
