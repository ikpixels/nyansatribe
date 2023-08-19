from django.shortcuts import render,redirect
from Store.models import Product
from Event.models import tickets_order,Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from music_nation.forms import SignUpForm,CustomerForm
from music_nation.models import Album, Song, Customer, Podcasts
from music_nation.forms import NewAlbum, NewSong

from music_nation.views import playlist_snipt
from music_nation.forms import PodcastForm
from Store.views import cart_snipt
from Store.models import Product,Orders
from Event.models import Ticket

# Create your views here.



@login_required
def profile(request):
    context = {}
    playlist_snipt(request,context)


    Form = PodcastForm()
    if request.method == 'POST':
        Form = PodcastForm(request.POST)
        Form = Form.save(commit=False)
        Form.user  = request.user
        Form.save()
        return redirect ('music_nation:podcasts')

    context['form'] = Form

    
    #adminlogin
    if request.user.is_superuser:

        customercount=Customer.objects.all().count()
        productcount=Product.objects.all().count()
        ordercount=Orders.objects.all().count()

        orders= Orders.objects.all()
        ordered_products=[]
        ordered_bys=[]

        for order in orders:
            ordered_product=Product.objects.all().filter(id=order.product.id)
            ordered_by= Customer.objects.all().filter(id = order.customer.id)
            ordered_products.append(ordered_product)
            ordered_bys.append(ordered_by)

        context['customercount'] = customercount
        context['productcount'] = productcount
        context['ordercount'] = ordercount
        context['data'] = zip(ordered_products,ordered_bys,orders)
        return render(request, 'www/admindashboard.html',context)

    else:#customerlogin
        context['ArtistID']  = Customer.objects.get(user=request.user)
        context['podcount'] = Podcasts.objects.filter(user=request.user).count()
        context['musiccount'] = Album.objects.filter(album_artist=request.user).count()
        context['ticketcount'] = Ticket.ticketObjects.filter(client=request.user).count()
        context['albums'] = Album.objects.all()
        return render(request, 'account/profile.html',context)
#........................................................#




#@login_required(login_url='account:adminlogin')

#@user_passes_test(lambda u: u.is_superuser)
@login_required
def truck_ticket_order(request):

    context = {}
    context['q_name'] = "Search order"

    if request.user.is_superuser:
        booked_ticket = Ticket.ticketObjects.filter(ticket_booked__gte = 1)
    else:
        booked_ticket = Ticket.ticketObjects.filter(ticket_booked__gte = 1,client=request.user)

    context['ticket'] = booked_ticket
    return render(request,'account/truck_ticket.html',context)