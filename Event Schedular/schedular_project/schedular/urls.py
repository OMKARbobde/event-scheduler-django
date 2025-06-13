from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView
 


urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create_event,name='create_event'),
    path('delete/<event_id>/',views.delete_event, name='delete_event'),
    path('edit/<event_id>/', views.edit_event, name='edit_event'),

    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',views.register,name='register'),

    #API Endpoints
    path('api/events/',EventListCreateAPIView.as_view(),name='api_event_list_create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='api_event_detail'),

]

