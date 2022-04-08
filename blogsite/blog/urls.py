from xml.etree.ElementInclude import include
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.blogsall ),
    path('addblog',views.addblog),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)