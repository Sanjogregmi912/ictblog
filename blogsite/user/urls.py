from django.conf import settings
from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL1), name='logout'),
    path('blog',views.allblog),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
