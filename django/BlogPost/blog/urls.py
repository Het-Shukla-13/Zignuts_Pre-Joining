from django.contrib import admin
from django.urls import path, include
from blog import views as view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view.home, name='home'),
    path('login/', view.login_user, name='login'),
    path('logout/', view.logout_user, name='logout'),
    path('signup/', view.signup, name='signup'),
    path('create_blog/', view.create_blog, name='create_blog'),
    path('blogs/', view.view_blogs, name='blogs'),
    path('blog/<int:blog_id>/', view.view_blog_detail, name='blog'),
    path('edit_blog/<int:blog_id>/', view.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', view.delete_blog, name='delete_blog'),
    path("profile/", view.profile, name="profile"),
    path("edit_profile/", view.edit_profile, name="edit_profile"),
    path("delete_account/", view.delete_account, name="delete_account"),
]