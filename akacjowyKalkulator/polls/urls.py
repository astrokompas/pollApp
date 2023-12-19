from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('<int:pk>/', views.detailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.resultsView.as_view(), name = 'results'),
    path('<int:questionId>/vote/', views.vote, name = 'vote'),
]
