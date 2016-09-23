import logging
import config
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello World !! Welcome to my app")


# http://fbnotify-env.ap-south-1.elasticbeanstalk.com/fb/callback/
@csrf_exempt
def realtime_subscription_callback(request):
    print (request)
    if request.method == 'GET':
        if request.GET.get('hub.mode') == 'subscribe' and request.GET.get("hub.verify_token") == config.FACEBOOK_REALTIME_VERIFY_TOKEN:
            challenge = request.GET.get('hub.challenge')
            return HttpResponse(challenge, content_type='text/plain')
        else:
            return HttpResponse()
    elif request.method == 'POST':
        # post_body = simplejson.loads(request.body)
        # object_type = post_body.get('object')
        # entries = post_body.get('entry', [])
        print (request.body)
        # for entry in entries:
        #     # trigger a new_facebook_change signal by each entry
        #     try:
        #         realtime_update.send(
        #             sender=None,
        #             object_type=object_type,
        #             uid=entry['uid'],
        #             changed_fields=entry['changed_fields'],
        #             time=entry['time'],
        #             request=request
        #         )
        #     except Exception:
        #         logger.exception("happened an error handling the real-time update entry %s" % entry)
        return HttpResponse()
    else:
        return HttpResponseForbidden()
