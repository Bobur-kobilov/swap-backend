import json
from rest_framework import viewsets
from .serializers import SwapSerializer, KYCSerializer
from .models import Swap, KYC_Complete
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import redis
from rq import Queue
import time
from . import email_service
import config
from rest_framework.permissions import IsAuthenticated

redis_cursor = redis.StrictRedis(host='swap_backend_redis_1', port=6379, db=0)
# redis_cursor = redis.Redis(host='0.0.0.0', port=6379, db=0)
# r = redis.Redis()
q = Queue(connection=redis_cursor)

def background_task(tx,email):
    try:
        jsonTx = json.loads(tx)
        queue = []
        queue.append(tx)
        delay = 15
        time.sleep(delay)
        result = requests.post(config.SERVER['host'], data=queue.pop())
        if result.status_code == 200:
            response = result.json()
            code = response['code'].replace(' ', '')
            print('*****************CODE*************************')
            print(code)
            swap = Swap.objects.create(
                atoloAddress=jsonTx['atoloAddress'],
                hdacAddress=jsonTx['hdacAddress'],
                code=response['code'],
                msg=response['msg'],
                success=response['success'],
                txHash=response['txHash']
            )
            serializer = SwapSerializer(swap)
            email_service.send(response['txHash'], jsonTx['atoloAddress'],email, code)

            return JsonResponse({'swaps': serializer.data})
        else:
            swap = Swap.objects.create(
            atoloAddress=jsonTx['atoloAddress'],
            hdacAddress=jsonTx['hdacAddress'],
            code=r'6',
            msg='',
            success=False,
            txHash=''
            )
            email_service.send('', jsonTx['atoloAddress'],email,'6')
            response = {
             "success": False
            }
            return JsonResponse(response)     
    except:
        code = '6'
        email_service.send('', jsonTx['atoloAddress'],email,code)
        response = {
             "success": False
        }
        return JsonResponse(response)


def add_task(tx,email):
    job = q.enqueue(background_task, tx,email)
    q_len = len(q)
    return {}


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_swaps(request):
    if request.method == 'GET':
        swaps = Swap.objects.all().order_by('createdAt')
        serializer = SwapSerializer(swaps, many=True)
        return JsonResponse({'swaps': serializer.data})


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def send_tx(request):
    try:
        if request.method == 'POST':
            jsonTx = json.loads(request.body)
            kycInfo = KYC_Complete.objects.all().filter(address=jsonTx['atoloAddress']);
            serializer = KYCSerializer(kycInfo, many=True)
            kycJson = json.dumps(serializer.data)
            email = None
            for info in kycInfo:
                email = info.email
            if email:
                add_task(request.body,email)
                response = {
                    "email": email
                }
            else:
                response = {
                    "errorMsg": "KYC_ERROR"
                }
            return JsonResponse(response)
    except:
            response = {
                "errorMsg": "Exeption_Error"
            }
            return JsonResponse(response)

