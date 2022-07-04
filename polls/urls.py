from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('',views.index),
    # ex:/qno/
    path('<int:question_id>/',views.detail, name='detail'),
    # ex: /qno/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /qno/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]