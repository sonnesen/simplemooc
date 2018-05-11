from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.conf import path, include

from simplemooc.accounts import urls as accounts_urls
from simplemooc.core import urls as core_urls
from simplemooc.courses import urls as courses_urls
from simplemooc.forum import urls as forum_urls

urlpatterns = [
    path('', include(core_urls, namespace='core')),
    path('contas/', include(accounts_urls, namespace='accounts')),
    path('cursos/', include(courses_urls, namespace='courses')),
    path('forum/', include(forum_urls, namespace='forum')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
