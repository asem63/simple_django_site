# coding: utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView

from .forms import CarSelectForm

from .models import Car


class CarView(FormView):
    template_name = 'index.html'
    form_class = CarSelectForm
    success_url = '/'

    def form_valid(self, form):
        return render_to_response(
            'super_cars/success.html', form.cleaned_data
        )


@csrf_exempt
@require_http_methods(["GET"])
def ajax_api(req, manf):
    carsQS = Car.objects.filter(manufacturer__name=manf).values('name')
    return HttpResponse(json.dumps(list(carsQS)))
