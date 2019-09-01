from django.contrib import admin
from django.urls import path
from stores import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.store_list, name='list'),
    path('detail/<slug:store_slug>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

