"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
    
from django.urls import path
from .views import Registro, cerrar_sesion,loguear



urlpatterns = [
    
    path('registro/', Registro.as_view(), name="registro"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('login/', loguear, name="login"),
   
]