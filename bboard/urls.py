from django.urls import path

from .views import index, by_rubric, BbCreateView, BbDetailView, BbByRubricView

urlpatterns = [
    # path('<int:rubric_id>/', by_rubric, name='on_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='on_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('', index, name='index'),
    path('detail/<int:pk>', BbDetailView.as_view(), name='detail')
]
