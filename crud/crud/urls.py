from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import blog.views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('detail/<str:id>/', blog.views.detail, name='detail'),
    path('read/', blog.views.read, name='read'),
    path('write/create', blog.views.create, name='create'),
    path('edit/<str:id>/', blog.views.edit, name='edit'),
    path('delete/<str:id>/', blog.views.delete, name='delete'),
    path('hashtag/', blog.views.hashtagform, name='hashtag'),
    path('<int:hashtag_id>/search/', blog.views.search, name='search'),
    
    path('signup/', blog.views.signup, name='signup'),
    path('login/', blog.views.login, name='login'),
    path('logout/', blog.views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
