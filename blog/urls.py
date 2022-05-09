"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
    
from django import views
from django.urls import path
from .views import blog, categoria



urlpatterns = [
    
    path('blog/', blog, name="blog"),
    path('blog/categoria/<int:categoria_id>/',categoria, name="categoria"),
   
    
]