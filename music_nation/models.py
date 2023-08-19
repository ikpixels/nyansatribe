import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ikmusic.settings import MEDIA_ROOT
from ckeditor.fields import RichTextField
from  embed_video.fields  import  EmbedVideoField

DISTRICT = (('Balaka','Balaka'),
            ('Blantyre','Blantyre'),
            ('Chikwawa','Chikwawa'),
            ('Chiradzuru','Chiradzuru'),
            ('Chitipa','Chitipa'),
            ('Dedza','Dedza'),
            ('Dowa','Dowa'),
            ('Karonga','Karonga'),
            ('Kasungu','Kasungu'),
            ('Likoma','Likoma'),
            ('Lilongwe','Lilongwe'),
            ('Machinga','Machinga'),
            ('Mangochi','Mangochi'),
            ('Mchinji','Mchinji'),
            ('Mulanje','Mulanje'),
            ('Mwanza','Mwanza'),
            ('Mzimba','Mzimba'),
            ('Neno','Neno'),
            ('Nkhata_Bay','Nkhata_Bay'),
            ('Nkhotakota','Nkhotakota'),
            ('Nsanje','Nsanje'),
            ('Ntcheu','Ntcheu'),
            ('Ntchisi','Ntchisi'),
            ('Phalombe','Phalombe'),
            ('Ruphi','Ruphi'),
            ('Salima','Salima'),
            ('Thyolo','Thyolo'),
            ('Zomba','Zomba'),
            ('Others','Others')
            )


GENRE = ( ('House','House'),
          ('Hip Hop','Hip hop'), 
          ('Trap','Trap'),
          ('Raggie','Raggie'),
          ('Amapiano','Amapiano'),
          ('Gospel','Gospel'),
          ('Beats','Beats'),
          ('Afro House','Afro House'),
          ('Dancehall','Dancehall'),
          ('Poetry','Poetry/Poem'),
          ('Rock','Rock')
        )
 

USER_CAT = (
    ('Artist','Artist'),
    ('Just a user','Just a user')
    )

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    account_type = models.CharField(max_length=40,choices=USER_CAT)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)

    fb = models.URLField(null=True,blank=True)
    tweeter = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)

    background = models.CharField(max_length=200,null=True,blank=True)
    fullBiography = RichTextField(null=True,blank=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_artist.id, filename)

def user_directory_path_song(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'user_{0}/{1}'.format(self.song_album.album_artist.id, filename)

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=30)
    uploaded_on = models.DateField(default=timezone.now())
    album_logo = models.FileField(upload_to=user_directory_path)
    album_genre = models.CharField(max_length=30,choices=GENRE,default="Rock")
    album_artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.album_name

    def delete_media(self):
        os.remove(path=MEDIA_ROOT+'/'+str(self.album_logo))

class Song(models.Model):
    song_name = models.CharField(max_length=40)
    Artist = models.CharField(max_length=40,null=True,blank=True,default="IK")
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    song_file = models.FileField(upload_to=user_directory_path_song)
    video = EmbedVideoField(null=True,blank=True)

    def __str__(self):
        return self.song_name +' '+ str(self.song_album)

    def delete_media(self):
        os.remove(path=MEDIA_ROOT+'/'+str(self.song_file))


    def song_logo(self):
        return self.song_album.album_logo



PodCategory = (
      ('Music','Music'),
      ('Arts','Arts'),
      ('Business','Business'),
      ('Comedy','Comedy'),
      ('Education','Education'),
      ('Fiction','Fiction'),
      ('Government','Government'),
      ('History','History'),
      ('Health & Fitness','Health & Fitness'),
      ('Kids & Family','Kids & Family'),
      ('Leisure','Leisure'),
      ('News','News'),
      ('Religion & Spirituality','Religion & Spirituality'),
      ('Science','Science'),
      ('Society & Culture','Society & Culture'),
      ('Sports','Sports'),
      ('Technology','Technology'),
      ('True Crime','True Crime'),
      ('TV & Film','TV & Film'),
    )


class Podcasts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcast')
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=40,choices = PodCategory,default="Music")
    youtubelink = EmbedVideoField(null=True,blank=True)

    def __str__(self):
        return self.title