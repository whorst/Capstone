
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
import settings

import announcement

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('announcement.urls')),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^meet/', include('meet.urls')),
    url(r'^$', RedirectView.as_view(url='/home/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
