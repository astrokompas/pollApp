from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionId>/', views.detail, name = 'detail'),
    path('<int:questionId>/results/', views.results, name = 'results'),
    path('<int:questionId>/vote/', views.vote, name = 'vote'),
]
