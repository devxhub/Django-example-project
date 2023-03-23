
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blogs/', include('blogs.urls')),
    path('api/faqs/', include('faqs.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/hrm/', include('hrm.urls')),
    path('qr/', include('qr_code.urls')),
    path('textart/', include('textart.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
