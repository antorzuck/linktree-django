from django.contrib import admin
from django.urls import path
from account.views import *
from mains.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('edit-profile/', editprofile, name="edit"),
    path('', home, name="home"),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('dashboard', dashboard, name="db"),
    path('add', addlink, name="add"),
    path('<username>', showlink, name='sl'),
    path('delete/<id>', delete, name="delete"),
    path('logout/', logout, name="logout")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
