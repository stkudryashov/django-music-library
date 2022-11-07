from rest_framework import routers
from library import views


router = routers.DefaultRouter()

router.register(r'artists', views.ArtistViewSet, basename='artists')
router.register(r'songs', views.SongViewSet, basename='songs')
router.register(r'albums', views.AlbumViewSet, basename='albums')

urlpatterns = [] + router.urls
