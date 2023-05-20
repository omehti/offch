from django.shortcuts import render

# Create your views here.

from datetime import datetime
from jdatetime import datetime as jdatetime

def current_datetime(request):
    current_datetime = datetime.now()
    j_current_datetime = jdatetime.fromgregorian(datetime=current_datetime)
    j_current_time = j_current_datetime.strftime('%H:%M')
    return render(request, 'times/date.html', {'current_datetime': j_current_datetime, 'current_time': j_current_time})
