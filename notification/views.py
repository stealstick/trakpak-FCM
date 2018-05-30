from django.shortcuts import render
from push_notifications.models import GCMDevice
from push_notifications.gcm import send_message

from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def notifi(request):
    # Create a FCM device
    the_user=User.objects.get(username='admin')
    fcm_device = GCMDevice.objects.create(registration_id="dq0gqApuEc4:APA91bEBnWd2QYf1lfUb1-PQkam71xRtpy-adU3J-vLQ8r-8sujpDbSAnvAeoceumUH4K2cegImZdVHznusaatO_2izhsTQ_sD4fNiv3rI_SXorDipQKhNo0NKbwo6CHIqt4_vynkE5o", cloud_message_type="FCM", user=the_user)

    # Send a notification message
    
    #send_message(None, {"body": "Hello members of my_topic!"},  cloud_type="FCM")
    fcm_device.send_message("This is a enriched message", extra={"title": "Notification title", "icon": "icon_ressource"})
    return HttpResponse("s")