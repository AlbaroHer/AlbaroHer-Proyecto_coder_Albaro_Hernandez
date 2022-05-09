"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
    
from django.urls import path
from .views import service



urlpatterns = [
    
    path('servicio/', service, name="servicio"),
   
    
]

