from django.urls import path

from . import views

app_name='research_site'

urlpatterns = [
    path('', views.index, name="index"),
    path('1/', views.user_info, name='info'),
    path('<int:page>/', views.next_survey, name="next"),
    path('<int:page>/', views.prev_survey, name="prev"),
    path('End/', views.submit_survey, name="submit"),
]