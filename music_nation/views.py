from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
    )

from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages

from .forms import SignUpForm,CustomerForm
from .models import Album, Song, Customer, Podcasts
from .forms import NewAlbum, NewSong

from Store.models import Product,Orders
from Event.models import Ticket
##########################################################


def playlist_snipt(request,context):
    #for playlist counter, fetching song ids added by user from cookies
    if 'song_ids' in request.COOKIES:
        song_ids = request.COOKIES['song_ids']
        counter=song_ids.split('|')
        song_count_in_playlist=len(set(counter))
    else:
        song_count_in_playlist = 0
    context['song_count_in_playlist'] = song_count_in_playlist

    context['home_song'] = Song.objects.all().last()
    context['song'] = Song.objects.all()[:6]

def home(request):

    context = {}

    playlist_snipt(request,context)

    #show all albums in chronological order of it's upload
    albums = Album.objects.all()[:12]

    context['albums'] = albums

    
    songs = Song.objects.all().last()
    context['song'] = songs


    context['events'] = Ticket.ticketObjects.all()


    context['products']= Product.objects.all()

    context['Artist'] = Customer.objects.filter(account_type="Artist")

    all_songs = Song.objects.all()[:5]
    context['all_songs'] = all_songs

    context['video'] = Podcasts.objects.all().order_by('-id')
  
    return render(request, 'www/index.html',context)


#........................................................#
def Contacts(request):
    context = {}
    playlist_snipt(request,context)

    '''sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'ecom/contactussuccess.html')
    context['form'] = sub'''
    return render(request, 'www/contacts.html',context)
   

#........................................................#

def Artist(request):
    context = {}
    playlist_snipt(request,context)
   
    Artist = Customer.objects.filter(account_type="Artist")

    query =request.GET.get('q')

    context['q_name'] = "Artist name"
    if query:
        context['search_title'] = query
        Artist =Artist.filter(Q(user__icontains=query)).distinct().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(Artist,12)

    try:
        Artist = paginator.page(page)
    except PageNotAnInteger:
        Artist = paginator.page(1)
    except EmptyPage:
        Artist = paginator.page(paginator.num_pages)

    context ['Artist'] = Artist
    return render(request, 'www/artists.html',context)

#........................................................#

def ArtistDetail(request,id):
    context = {}

    playlist_snipt(request,context)

    Artist = Customer.objects.get(id=id)
    context['Artist'] = Artist

    albums = Album.objects.filter(album_artist=Artist.user)[:12]
    context['albums'] = albums
    
    return render(request, 'www/artist.html',context)


#........................................................#
def allMusic(request):
    context = {}
    playlist_snipt(request,context)

    albums = Album.objects.all()
    
    
    query =request.GET.get('q')
    context['q_name'] = "Album name,genre"

    if query:
        context['search_title'] = query
        albums =albums.filter(Q(album_name__icontains=query)|
                          Q(album_genre__icontains=query)).distinct().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(albums,12)

    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    context['albums'] = albums

    

    return render(request, 'www/releases.html',context)

#........................................................#
def add_to_playlist(request,pk):

    song=Song.objects.all()
    albums = Album.objects.all()
    
    #for playlist counter, fetching song ids added by user from cookies
    if 'song_ids' in request.COOKIES:
        song_ids = request.COOKIES['song_ids']
        counter=song_ids.split('|')
        song_count_in_playlist=len(set(counter))
    else:
        song_count_in_playlist =1

    response = render(request, 'www/releases.html',{'albums':albums,'songs':song,'song_count_in_playlist':song_count_in_playlist})

    #adding product id to cookies
    if 'song_ids' in request.COOKIES:
        song_ids = request.COOKIES['song_ids']
        if song_ids=="":
            song_ids=str(pk)
        else:
            song_ids=song_ids+"|"+str(pk)
        response.set_cookie('song_ids', song_ids)
    else:
        response.set_cookie('song_ids', pk)

    song=Song.objects.get(id=pk)
    messages.info(request, song.song_name + ' added to cart successfully!')

    return response

#........................................................#

def playlist_view(request):

    context = {}
    
    playlist_snipt(request,context)

    # fetching song details from db whose id is present in cookie
    song=None

    if 'song_ids' in request.COOKIES:
        song_ids = request.COOKIES['song_ids']
        if song_ids != "":
            song_id_in_cart= song_ids.split('|')
            song=Song.objects.all().filter(id__in = song_id_in_cart)
    context['song'] = song

    return render(request,'www/playlist.html',context)

#........................................................#

def remove_from_playlist(request,pk):

    context = {}
    playlist_snipt(request,context)

    # removing song id from cookie
 
    if 'song_ids' in request.COOKIES:
        song_ids = request.COOKIES['song_ids']
        song_id_in_playlist=song_ids.split('|')
        song_id_in_playlist=list(set(song_id_in_playlist))
        song_id_in_playlist.remove(str(pk))
        song=Song.objects.all().filter(id__in = song_id_in_playlist)
        #for total price shown in cart after removing product
        
        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(song_id_in_playlist)):
            if i==0:
                value=value+song_id_in_playlist[0]
            else:
                value=value+"|"+song_id_in_playlist[i]
        context['song'] =song
        response = render(request, 'www/playlist.html',context)
        if value=="":
            response.delete_cookie('song_ids')
        response.set_cookie('song_ids',value)
        return response

#........................................................#

def about(request):
    context = {}
    return render(request, 'www/about.html',context)


#........................................................#
def updateCustomer(request,id):
    context = {}
    playlist_snipt(request,context)
    Artist = Customer.objects.get(id=id)

    customerForm = CustomerForm(instance=Artist)
    context['form'] = customerForm

    if request.method == "POST":
        customerForm = CustomerForm(request.POST,request.FILES, instance=Artist)
        if customerForm.is_valid():
            customerForm.save()
            return redirect('music_nation:ArtistDetail', id=Artist.id)

    return render(request, 'www/updateCustomer.html',context)

#........................................................#

@login_required
def profile_detail(request, username):
    # show all albums of the artist
    albums = get_object_or_404(User, username=username)
    albums = albums.albums.all()

    return render(request, 'www/useralbum-list.html', {'albums':albums, 'username':username})

#........................................................#

@login_required
def add_album(request, username):
    user = get_object_or_404(User, username=username)
    #only currently logged in user can add album else will be redirected to home
    if user == request.user:
        if request.method == 'POST':
            form = NewAlbum(request.POST, request.FILES)
            if form.is_valid():
                # form.save(commit='False')
                album = Album.objects.create(
                    album_logo=form.cleaned_data.get('album_logo'),
                    album_name=form.cleaned_data.get('album_name'),
                    album_genre=form.cleaned_data.get('album_genre'),
                    uploaded_on = timezone.now(),
                    album_artist = request.user
                )
                return redirect('music_nation:profile_detail', username=request.user)
        else:
            form = NewAlbum()
        return render(request, 'www/addAlbum.html', {'form':form})
    else:
        return redirect('music_nation:profile_detail', username=user)

#........................................................#

def album_detail(request,username, album):

    context = {}
    playlist_snipt(request,context)

    #show album details here. single album's details.
    album = get_object_or_404(Album, album_name=album)
    songs = get_object_or_404(User, username=username)
    songs = songs.albums.get(album_name=str(album))
    songs = songs.songs.all()

    context['songs'] = songs
    context['album'] = album
    context['username'] = username

    context['other_releases'] = Album.objects.exclude(album_name=album)[:6]

    return render(request, 'www/release.html',context)

#........................................................#

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        customerForm=CustomerForm(request.POST,request.FILES)
        if form.is_valid() and customerForm.is_valid():
            user = form.save()

            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            
            login(request, user)
            return redirect('music_nation:profile')
        else:
            message = 'Looks like a username with that email or password already exists'
            return render(request, 'music_nation/signup.html', {'form':form,'message':message})
    else:
        form = SignUpForm()
        customerForm=CustomerForm()
        return render(request, 'www/signup.html', {'form':form,'customerForm':customerForm})

#........................................................#

@login_required
def delete_album(request, username, album):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        album_to_delete = get_object_or_404(User, username=username)
        album_to_delete = album_to_delete.albums.get(album_name=album)
        song_to_delete = album_to_delete.songs.all()
        for song in song_to_delete:
            song.delete_media()#deletes the song_file
        album_to_delete.delete_media()#deletes the album_logo
        album_to_delete.delete()#deletes the album from database
        return redirect('music_nation:profile_detail', username=username)
    else:
        return redirect('music_nation:profile_detail', username=username)

#........................................................#

@login_required
def add_song(request, username, album):

    user = get_object_or_404(User, username=username)

    if request.user == user:

        album_get = Album.objects.get(album_name=album)

        if request.method == 'POST':
            form = NewSong(request.POST, request.FILES)
            if form.is_valid():
                # form.save(commit='False')
                song = Song.objects.create(
                    song_name = form.cleaned_data.get('song_name'),
                    song_file = form.cleaned_data.get('song_file'),
                    song_album = album_get
                )
                return redirect('music_nation:album_detail', username=username, album=album)

        else:
            form = NewSong()
            return render(request, 'www/add_new_song.html', {'form':form})
    else:
        return redirect('music_nation:album_detail', username=username, album=album)


@login_required
def podcasts(request):

    context = {}

    playlist_snipt(request,context)
    podcasts = Podcasts.objects.all().order_by('-id')

    query =request.GET.get('q')
    context['q_name'] = "Podcast title"

    if query:
        context['search_title'] = query
        podcasts =podcasts.filter(Q(title__icontains=query)).distinct().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(podcasts,12)

    try:
        podcasts = paginator.page(page)
    except PageNotAnInteger:
        podcasts = paginator.page(1)
    except EmptyPage:
        podcasts = paginator.page(paginator.num_pages)

    context['podcasts'] = podcasts

    return render(request, 'www/podcasts.html',context)

