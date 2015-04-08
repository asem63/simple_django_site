from django import forms
from .models import Manufacturer, Car


class CarSelectForm(forms.Form):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all(),
                                            initial=0, label="Choose manufacturer",
                                            required=True)
    
    car = forms.ChoiceField(label="Choose model", required=True)
    
    mileage = forms.IntegerField(initial=0, min_value=0,
                                    label="Enter mileage in km.",
                                    required=True)


    def clean(self):
        super(CarSelectForm, self).clean()
        manufacturer = self.cleaned_data["manufacturer"]
        
        try:
            car = Car.objects.filter(manufacturer__name=manufacturer.name)[int(self.data["car"]) - 1]
        except IndexError:
            raise forms.ValidationError("Car not valid!")
        
        self.cleaned_data['car'] = car
        return self.cleaned_data


    def is_valid(self):
        super(CarSelectForm, self).is_valid()
        try:
            data = self.clean()
            return True
        except forms.ValidationError:
            return False
