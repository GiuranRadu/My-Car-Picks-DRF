from django.http import HttpResponse
from django.conf import settings
from pathlib import Path

def home_view(request):
    html_path = Path(settings.BASE_DIR) / "MyCarPicks/home.html"
    html_content = html_path.read_text(encoding="utf-8")
    return HttpResponse(html_content)
