from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:qid>/', views.detail, name='detail'),
    path('<int:qid>/results/', views.results, name='results'),
    path('<int:qid>/vote/', views.vote, name='vote'),
]


