from django.urls import path
from .views import *

app_name = 'toad'  # Замените 'your_app_name' на имя вашего приложения

urlpatterns = [
    path('<int:toad_id>', toad_detail, name='toad_detail'),
    path('send-request/<int:toad_id>/<int:curr_toad>', send_request_view, name='send_request'),
    path('accept-request/<int:toad_id>/<int:curr_toad>', accept_request_view, name='accept_request'),
    path('check-requests/<int:toad_id>/', check_requests_view, name='check_requests')
]