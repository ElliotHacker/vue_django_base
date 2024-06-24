from django.urls import path,include,re_path
from apps.users import views

urlpatterns = [
    path('users/', views.get_users, name='users_get_users'),  # 获取所有用户
    path('reg/', views.reg),
    path('user_login/', views.user_login),
    path('ajax_login_data/', views.ajax_login_data),
]
