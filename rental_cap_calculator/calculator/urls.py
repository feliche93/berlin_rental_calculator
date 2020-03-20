from django.urls import path


from . import views

app_name = 'calculator'
urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('calculate', view=views.calculate, name='calculate'),
    path('result', view=views.result, name='result')
]
