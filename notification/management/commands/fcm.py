from django.core.management.base import BaseCommand, CommandError
from push_notifications.models import GCMDevice
from push_notifications.gcm import send_message

from django.contrib.auth.models import User
from django.http import HttpResponse
import certifi
import requests

from time import sleep

class Command(BaseCommand):


    def handle(self, *args, **options):
        # -*- coding: utf-8 -*- 
        while 1:
            URL="http://www.search.trackmytrakpak.com/TrakPaksearch.aspx?mytrakpaknumber=HUT1866GB00578497601&mytrakpakid=hutgrpgb&lang=en&view=2"
            crawl = requests.get(URL)
            the_user=User.objects.get(username='admin')
            fcm_device = GCMDevice.objects.create(registration_id="eAISChjxmfE:APA91bH5cdo9Zg_zETgp1E8cKPANnx9trEJYZLRxpaY2uE8_0lbJUsJ0mIzR_nCftJlpUpqjA7PzErmD7L7s0k_gMSCgfmt4Q3ewJFZxc2KnM3BGLDWDN6P4TjXkZiLX-oECEQgavQG-", cloud_message_type="FCM", user=the_user)
            if "DEPARTED The Hut Group" in crawl.text:
                if "TRAKPAK PROCESS CENTRE UK" in crawl.text:
                        if "ROUTED TO DESTINATION" in crawl.text:
                            if "ARRIVED IN COUNTRY / NON EU PRESENTED TO CUSTOMS" in crawl.text:
                                    if "RECEIVED INTO CUSTOMS" in crawl.text:
                                        if "CUSTOMS CLEARED" in crawl.text:
                                                if "ARRIVED AT DELIVERY DEPOT" in crawl.text:
                                                    fcm_device.send_message("ARRIVED AT DELIVERY DEPOT", extra={"title": "201", "icon": "icon_ressource"})
                                                    sleep(60)
                                                    continue
                                                fcm_device.send_message("CUSTOMS CLEARED", extra={"title": "433", "icon": "icon_ressource"})
                                                sleep(60)
                                                continue
                                        fcm_device.send_message("RECEIVED INTO CUSTOMS", extra={"title": "432", "icon": "icon_ressource"})
                                        sleep(60)
                                        continue
                                    fcm_device.send_message("ARRIVED IN COUNTRY / NON EU PRESENTED TO CUSTOMS", extra={"title": "204", "icon": "icon_ressource"})
                                    sleep(60)
                                    continue
                            fcm_device.send_message("ROUTED TO DESTINATION", extra={"title": "299", "icon": "icon_ressource"})
                            sleep(60)
                            continue
                        fcm_device.send_message("TRAKPAK PROCESS CENTRE UK", extra={"title": "198", "icon": "icon_ressource"})
                        sleep(60)
                        continue
                fcm_device.send_message("DEPARTED The Hut Group", extra={"title": "200", "icon": "icon_ressource"})
                sleep(60)
                continue

                        
            