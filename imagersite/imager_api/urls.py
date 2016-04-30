from django.conf.urls import url, include
from rest_framework import routers
from imager_api import views
from rest_framework import renderers


router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
# router.register(r'albums', views.AlbumViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]