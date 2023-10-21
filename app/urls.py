
from django.urls import path
from views import generate_report, report, home

urlpatterns = [
    path('', home),
    path('/trigger_report', generate_report),
    path('/get_report', report),

]
