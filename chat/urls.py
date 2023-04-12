from chat.api import views
from django.urls import path
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('messages/<int:sender>/<int:receiver>',
#                 views.message_list, basename='message-detail'),
# router.register('/messages/', views.message_list,
#                 name='message-list'),
# router.register('/users/<int:pk>', views.user_list, name='user-detail'),
# router.register('/users/', views.user_list, name='user-list'),


urlpatterns = [
    # URL form : "/messages/1/2"
    # For GET request.
    path('messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    # URL form : "/messages/"
    path('messages/', views.message_list,
         name='message-list'),   # For POST
    # URL form "/users/1"
    # GET request for user with id
    path('users/<int:pk>', views.user_list, name='user-detail'),
    # POST for new user and GET for all users list
    path('users/', views.user_list, name='user-list'),
]
