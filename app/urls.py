
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('admin_dashboard',views.admin,name="admin"),
    path('overview',views.overview,name="overview"),
    path('add_student',views.add_student,name="add_student"),
    path('add_result',views.add_result,name="add_result"),
    path('post_notification',views.post_notification,name="post_notification"),
    path('users',views.users,name="users"),
    path('edit_student/<int:id>/',views.edit_student,name="edit_student"),
    path('delete_student/<int:id>/',views.delete_student,name="delete_student"),
    path('edit_result/<int:id>/',views.edit_result,name="edit_result"),
    path('delete_result/<int:id>/',views.delete_result,name="delete_result"),
    path('view_result/<int:id>/',views.view_result,name="view_result"),
    path('post_notification',views.post_notification,name="post_notification"),
    path('edit_notification/<int:id>/',views.edit_notification,name="edit_notification"),
    path('delete_notification/<int:id>/',views.delete_notification,name="delete_notification"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)