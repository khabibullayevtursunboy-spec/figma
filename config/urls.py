from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def index_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Manzillar</title>
    </head>
    <body>
        <h3>Admin Panel</h3>
        <ul>
            <li><a href="/admin/">Admin Panel</a></li>
        </ul>

        <h3>API Manzillari</h3>
        <ul>
            <li><a href="/api/messages/">Xabarlar</a></li>
            <li><a href="/api/home/">Bosh sahifa matnlari</a></li>
            <li><a href="/api/app-downloads/">Ilova yuklash havolalari</a></li>
            <li><a href="/api/team-members/">Jamoa a'olari</a></li>
            <li><a href="/api/features/">Afzalliklar (Features)</a></li>
            <li><a href="/api/team-groups/">Jamoa guruhlari</a></li>
            <li><a href="/api/team-section-features/">Jamoa bo'limi xususiyatlari</a></li>
            <li><a href="/api/how-it-works/">Qanday ishlaydi qadamlari</a></li>
            <li><a href="/api/videos/">Video bo'limlari</a></li>
            <li><a href="/api/solutions/">Muammo yechimlari (Xizmatlar)</a></li>
            <li><a href="/api/testimonials/">Mijozlar fikrlari</a></li>
            <li><a href="/api/pricing/">Tarif rejalari</a></li>
            <li><a href="/api/footer-links/">Futer havolalari</a></li>
            <li><a href="/api/footer-settings/">Futer sozlamalari</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', index_view, name='home_index'),
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)