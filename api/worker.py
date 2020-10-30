from .models import Swap
import requests
import redis
from rq import Queue
from .models import Swap
import time
import config
from . import email_service
import json
from .serializers import SwapSerializer
from django.http import JsonResponse
r = redis.Redis();
q = Queue(connection=r)

def background_task(tx):
    jsonTx = json.loads(tx)
    queue = []
    queue.append(tx)
    delay = 15
    time.sleep(delay)
    result = requests.post('http://140.238.22.132:8080/new/sendTx', data=queue.pop())
    response = result.json()
    code = response['code'].replace(' ','')
    print('*****************CODE*************************')
    print(code)
    if code == '65545':
        swap = Swap.objects.create(
            atoloAddress = jsonTx['atoloAddress'],
            hdacAddress = jsonTx['hdacAddress'],
            code = response['code'],
            msg = response['msg'],
            success = response['success'],
            txHash = response['txHash']
        )
        serializer = SwapSerializer(swap)
        email_service.send(response['txHash'],jsonTx['atoloAddress'],'bobur0114jon@gmail.com',code)
       
        return JsonResponse({'swaps': serializer.data})

def add_task(tx):
    job = q.enqueue(background_task,tx)
    q_len = len(q)
    return {}