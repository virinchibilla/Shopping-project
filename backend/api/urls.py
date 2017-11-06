from api import views
from django.conf.urls import url


urlpatterns = [
    url(r'^loguser/', views.authenticate_user),
    url(r'^address/', views.address),
    url(r'^signup/', views.signup),
    url(r'^shopping/', views.shopping),
    url(r'^items/', views.loaditems),
    url(r'^user_data/all/', views.users_data_all),
    url(r'^user_data/invoice/', views.get_user_invoice),
    url(r'^user_data/update/', views.update_user),
    url(r'^user_data/(?P<username>[^/]+)/?$', views.user_data),
]
