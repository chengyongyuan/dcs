from django.shortcuts import render
from django.http import HttpResponse
from mobiconf.models import ScreenConf
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello To LightInTec.com")

# Get Margin By Machine. output in json by now
def getmargin(request):
    if 'machine' in request.REQUEST:
        mname = request.REQUEST['machine']
        try:
            screen_conf = ScreenConf.objects.get(mtype=mname)
            json_rsp = json.dumps({'status': {'result':True, 'errmsg':''}, \
                                  'margin': {'left': screen_conf.left, 'right': screen_conf.right, \
                                             'top': screen_conf.top, 'bottom': screen_conf.bottom}}) 
        except (KeyError, ScreenConf.DoesNotExist):
            json_rsp = json.dumps({'status': {'result':False, 'errmsg':'machine %s not found' %(mname)}})
    else:
            json_rsp = json.dumps({'status': {'result':False, 'errmsg':'invalid request'}})

    return HttpResponse(json_rsp)
