from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from root.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'))

]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
