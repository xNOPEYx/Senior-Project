from django.urls import path
from . import views


app_name = 'sr_project'
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('speech/', views.speech, name='speech'),
    # path('nlp/', views.nlp, name='nlp'),
    path('chat/', views.chat, name='chat')
]