from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pusher import Pusher

# instantiate pusher
pusher = Pusher(app_id='XXX_APP_ID', key='XXX_APP_KEY', secret='XXX_APP_SECRET', cluster='XXX_APP_CLUSTER')


# add the login required decorator, so the method cannot be accessed w/o login
@login_required(login_url='login/')
def index(request):
    return render(request,'chat.html')    
