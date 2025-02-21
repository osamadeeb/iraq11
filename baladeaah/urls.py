from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('<int:post_id>/',views.mofasal,name='mofasal'),
    path('delete/<int:post_id>/',views.del_sc,name='del_sc'),
    path('update/<int:post_id>/',views.update_f,name='update_f'),
]