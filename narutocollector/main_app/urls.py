from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ninjas/', views.ninjas_index, name='index'),
    path('ninjas/<int:ninja_id>/', views.ninjas_detail, name='detail'),
    path('ninjas/create', views.NinjaCreate.as_view(), name='ninjas_create'),
    path('ninjas/<int:pk>/update/', views.NinjaUpdate.as_view(), name='ninjas_update'),
    path('ninjas/<int:pk>/delete/', views.NinjaDelete.as_view(), name='ninjas_delete'),
    path('ninjas/<int:ninja_id>/assoc_jitsu/<int:jitsu_id>/', views.assoc_jitsu, name='assoc_jitsu'),
    path('jitsus/', views.JitsuList.as_view(), name='jitsus_index'),
    path('jitsus/<int:pk>/', views.JitsuDetail.as_view(), name='jitsus_detail'),
    path('jitsus/create/', views.JitsuCreate.as_view(), name='jitsus_create'),
    path('jitsus/<int:pk>/update/', views.JitsuUpdate.as_view(), name='jitsus_update'),
    path('jitsus/<int:pk>/delete/', views.JitsuDelete.as_view(), name='jitsus_delete'),
    path('ninjas/<int:ninja_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]