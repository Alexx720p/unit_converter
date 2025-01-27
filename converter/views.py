from django.shortcuts import render

# Create your views here.

conversion_rates = {
    'length': {
        'millimeter': 1,
        'centimeter': 10,
        'meter': 1000,
        'kilometer': 1000000,
        'inch': 25.4,
        'foot': 304.8,
        'yard': 914.4,
        'mile': 1609344
    },
    'weight': {
        'milligram': 1,
        'gram': 1000,
        'kilogram': 1000000,
        'ounce': 28349.5,
        'pound': 453592
    },
    'temperature': {
        'Celsius': lambda x: x,
        'Fahrenheit': lambda x: (x * 9/5) + 32,
        'Kelvin': lambda x: x + 273.15
    }
}

def convert(value, from_unit, to_unit, category):
    if category == 'temperature':
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return round((value * 9/5) + 32, 2)
            if to_unit == 'Kelvin':
                return round(value + 273.15, 2)
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return round((value - 32) * 5/9, 2)
            if to_unit == 'Kelvin':
                return round((value - 32) * 5/9 + 273.15, 2)
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return round(value - 273.15, 2)
            if to_unit == 'Fahrenheit':
                return round((value - 273.15) * 9/5 + 32, 2)
    else:
        return round(
            (value * conversion_rates[category][from_unit]) / conversion_rates[category][to_unit],
            2)

def index(request):
    result = None
    if request.method == 'POST':
        value = float(request.POST['value'])
        from_unit = request.POST['from_unit']
        to_unit = request.POST['to_unit']
        category = request.POST['category']
        result = convert(value, from_unit, to_unit, category)
    return render(request, 'converter/index.html', {'result': result})
