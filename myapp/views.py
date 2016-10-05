import logging
import json
from myapp import config
from django.shortcuts import render
from django.dispatch import Signal
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden

logger = logging.getLogger(__name__)

def index(request):
    f = open('op.txt','w')
    f.write("index->index"+str(request.GET))
    # return render(request, 'output.html', {'req' : request,'content':'This is the index method'})
    return HttpResponse("Hello World !! Welcome to my app")


# http://fbnotify-env.ap-south-1.elasticbeanstalk.com/fb/callback/
@csrf_exempt
def realtime_subscription_callback(request):
    f = open('op.txt','w')
    if request.method == 'GET':
        f.write("callback->GET"+str(request.GET))
        f.close()
        if request.GET.get('hub.mode') == 'subscribe' and request.GET.get("hub.verify_token") == config.FACEBOOK_REALTIME_VERIFY_TOKEN:
            challenge = request.GET.get('hub.challenge')
            return HttpResponse(challenge, content_type='text/plain')
        else:
            return HttpResponse()
    elif request.method == 'POST':
        post_body = json.dumps(request.POST)
        f.write("callback->POST"+str(post_body))
        f.close()
        return HttpResponse()
        # object_type = post_body.get('object')
        # entries = post_body.get('entry', [])
        # for entry in entries:
        #     # trigger a new_facebook_change signal by each entry
        #     try:
        #         realtime_update = Signal(providing_args=["object_type",
        #                                  "uid",
        #                                  "changed_fields",
        #                                  "time",
        #                                  "request"])
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
        # return HttpResponse()
    else:
        f.write("ERROR")
        f.close()
        return HttpResponseForbidden()
