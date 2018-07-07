from django.conf.urls import url
from .import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailPageView.as_view(), name='detail'),
    url(r'^album/new/$', views.CreateAlbum.as_view(), name='album_new'),
    url(r'album/(?P<pk>[0-9]+)/$',views.UpdateAlbum.as_view(), name='album_edit'),
    url(r'^songs/all/$',views.SongList.as_view(), name='all_song'),
    url(r'^song/new/$',views.CreateSong.as_view(), name='song_form'),
    url(r'^song/(?P<pk>[0-9]+)/delete/$',views.SongDelete.as_view(), name='song_delete'),
    # url(r'^(?P<pk>[0-9]+)/song_delete/(?P<pk>[0-9]+)/$', views.SongDelete.as_view(), name='song_delete'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album_delete'),
]