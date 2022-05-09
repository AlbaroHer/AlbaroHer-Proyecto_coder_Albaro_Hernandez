"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
    
from django.urls import path
from project_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from project_web.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    
    path('', home, name="inicio"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)