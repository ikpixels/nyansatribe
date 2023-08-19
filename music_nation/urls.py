from django.urls import path, include, re_path
from . import views as music_nation_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'music_nation'
urlpatterns = [
    #home /
    path('', music_nation_views.home, name='home'),

    #profile_detail /@username/
    path('@<str:username>/', music_nation_views.profile_detail, name='profile_detail'),

    #add new album /@username/add
    path('@<str:username>/add/', music_nation_views.add_album, name='add_album'),

    #album's detail page /@username/album/album_name
    path('@<str:username>/album/<str:album>/', music_nation_views.album_detail, name='album_detail'),

    # login the user /login/
    path('login/', LoginView.as_view(template_name='www/signin.html'), name="login"),

    # signUp new user /signup/
    path('signup/', music_nation_views.signup, name='signup'),

    #delete album /@username/album/album_name/delete
    path('@<str:username>/album/<str:album>/delete/', music_nation_views.delete_album, name='delete_album'),

    #add songs to the albums
    path('@<str:username>/album/<str:album>/add/', music_nation_views.add_song, name='add_song'),

    #logout the current user
    path('logout/', LogoutView.as_view(), name='logout'),

    path('about/',music_nation_views.about,name="about"),

    path('all-music/',music_nation_views.allMusic,name="all-music"),

    path('podcasts/',music_nation_views.podcasts,name="podcasts"),

    path('Artists/',music_nation_views.Artist,name="Artists"),

    path('Artist/<int:id>/',music_nation_views.ArtistDetail,name="ArtistDetail"),

    path('contacts/',music_nation_views.Contacts,name="contacts"),

    path('profile/<int:id>/',music_nation_views.updateCustomer,name="updateCustomer"),

    path('add-to-playlist/<int:pk>', music_nation_views.add_to_playlist,name='add-to-playlist'),

    path('playlist_view/',music_nation_views.playlist_view,name="playlist_view"),

    path('remove_from_playlist/<int:pk>', music_nation_views.remove_from_playlist,name='remove_from_playlist'),
]
#path('link', view, name='', kwargs={})
#re_path(r'regex', view, name='', kwargs={})
