from django.urls import path
from .views import *

urlpatterns = [
    path("room/", view_room, name="room"),
    path("add_user", view_add_user, name="add_user"),
    path("process_login/", process_login, name="process_login"),
    path("logout", view_logout, name="logout"),
    path("room_h1/", view_room_h1, name="room_h1"),
    path("room_h2/", view_room_h2, name="room_h2"),
    path("room_h3/", view_room_h3, name="room_h3"),
    path("room_h4/", view_room_h4, name="room_h4"),
    path("room_h5/", view_room_h5, name="room_h5"),
    path("complaint/", view_complaint, name="complaint"),
    path("paiement/", view_paiement, name="paiement"),
    path("dashboard/", view_dashboard, name="dashboard"),
    path('reservation/', reservation, name='reservation'),
    path("delete_reservation/", delete_reservation, name="delete_reservation"), 
    path("process_complaint/", process_complaint, name="process_complaint"),
    path("complaints_history/", complaints_history, name="complaints_history"),
    path("complaint_contain/", complaint_contain, name="complaint_contain"), 
    path('search_room/', search_room, name="search_room"),
    path("student/", view_students, name="students"),
    path("info_student/", view_info_student, name="info_student"),
    path("payment_student/", view_payment_student, name="payment_student"), 
    path("add_payment/", view_add_payment, name='add_payment'),
    path("payment_register/", payment_register, name="payment_register"),
    path('search_student', search_student, name="search_student"),
    
]
