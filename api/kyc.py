import json
import time
import config
from hdacpy.transaction import Transaction
from hdacpy import wallet
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hdacpy.transaction import Transaction
from hdacpy import wallet
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
from .models import KYC_Complete, KYC_Submit, KYC_Reject
from . import email_service

from .argos import kyc_submits

@api_view(['POST'])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def insertKYCInfoToDb(request):
    kycInfoJson = json.loads(request.body)
    if 'kyc_result' in kycInfoJson:
        email = kycInfoJson['email']
        id = kycInfoJson['submission_id']
        submitData = KYC_Submit.objects.filter(email=email,kyc_id=id)
        jsonData = list(submitData.values())
        if kycInfoJson['kyc_result']['status'] == 'approved':
            try:
                print(jsonData[0]['first_name'])
                KYC_Complete.objects.create(
                    kycLevel = jsonData[0]['kycLevel'],
                    status = kycInfoJson['kyc_result']['status'],
                    updatedAt = kycInfoJson['kyc_result']['updated_at'],
                    first_name = jsonData[0]['first_name'],
                    last_name = jsonData[0]['last_name'],
                    nationality = jsonData[0]['nationality'],
                    date_of_birth = jsonData[0]['date_of_birth'],
                    gender = jsonData[0]['gender'],
                    address = jsonData[0]['wallet_address'],
                    email = jsonData[0]['email'],
                    kycID = kycInfoJson['submission_id'],
                )
                contractInfo = config.CONTRACT_INFO
                tx_obj = Transaction(
                    chain_id=contractInfo['chain_id'],
                    host = contractInfo['rest_server'],
                    privkey = wallet.mnemonic_to_privkey(contractInfo['admin_mnemonic'])
                )
                if jsonData[0]['kycLevel'] == 'L1':
                    kycLvl = 1
                else:
                    kycLvl = 2
                param = json.dumps([
                {
                    'name': 'method',
                    'value':{
                        'cl_type':{
                            'simple_type':'STRING'
                        },
                        'value':{
                            'str_value':'insert_kyc_data'
                        }
                    }
                },
                {
                    'name': 'address',
                    'value': {
                        'cl_type': {
                            'list_type': {
                                'inner': {
                                    'simple_type':'U8'
                                }
                            }
                        },
                        'value':{
                            'bytes_value': jsonData[0]['wallet_address']
                        }
                    }
                },
                {
                    'name':'kyc_level',
                    'value':{
                        'cl_type':{
                            'simple_type':'U512'
                        },
                        'value':{
                            'u512':{
                                # 'value': str(jsonData[0]['kycLevel'])
                                 'value': str(kycLvl)
                            }
                        }
                    }
                }
                ]).replace(' ', '')
                try:
                    kyc_store_tx_info = tx_obj.execute_contract('hash', contractInfo['swap_proxy'], '', param, 0.01)
                    kyc_store_tx_hash = kyc_store_tx_info['txhash']
                    print(kyc_store_tx_hash)
                except:
                    email_service.send_kyc(kyc_store_tx_hash,kycInfoJson['address'],kycInfoJson['email'],False)
                time.sleep(5)
                response = {
                    'kycTx': kyc_store_tx_hash
                }
                KYC_Complete.objects.filter(email=kycInfoJson['email']).update(txHash=kyc_store_tx_hash)
                
                email_service.send_kyc(kyc_store_tx_hash,jsonData[0]['wallet_address'],kycInfoJson['email'],True)
                return JsonResponse(response)
            except:
                response = {
                    "success": False
                }
                return JsonResponse(response)
        elif kycInfoJson['kyc_result']['status'] == 'rejected':
            try:
                KYC_Reject.objects.create(
                    kycLevel = jsonData[0]['kycLevel'],
                    status = kycInfoJson['kyc_result']['status'],
                    updatedAt = kycInfoJson['kyc_result']['updated_at'],
                    first_name = jsonData[0]['first_name'],
                    last_name = jsonData[0]['last_name'],
                    nationality = jsonData[0]['nationality'],
                    date_of_birth = jsonData[0]['date_of_birth'],
                    gender = jsonData[0]['gender'],
                    address = jsonData[0]['wallet_address'],
                    email = jsonData[0]['email'],
                    kycID = kycInfoJson['submission_id']
                )
                response = {'success': True}
                return JsonResponse(response)
            except:
                response = {'success': False}
                return JsonResponse(response);
    else:
        try:
            email = kycInfoJson['email']
            id = kycInfoJson['submission_id']
            delay = 20
            time.sleep(delay)
            kycData = kyc_submits.check_user(email,id)
            if kycData != '':
                submitData = KYC_Submit.objects.filter(email=email)
                jsonData = list(submitData.values())
                if not jsonData:
                    print(jsonData)
                    KYC_Submit.objects.create(
                        first_name = kycData['first_name'],
                        last_name = kycData['last_name'],
                        kycLevel = kycData['kyc_level'],
                        email  = kycData['email'],
                        nationality = kycData['nationality'],
                        date_of_birth = kycData['date_of_birth'],
                        id_type = kycData['id_type'],
                        gender = kycData['gender'],
                        photoid_res = kycData['photoid_res'],
                        selfie_res = kycData['selfie_res'],
                        contribution_type = kycData['contribution_type'],
                        wallet_address = kycData['wallet_address'],
                        estimated_amount = kycData['estimated_amount'],
                        kyc_id = kycData['id'],
                        created_at = kycData['created_at']
                    )
                    response = {'success': True}
                    return JsonResponse(response);
                if id != jsonData[0]['kyc_id']:
                    email_service.send_kyc_duplicate(email)
                    response = {'success': True}
                    return JsonResponse(response);
                else:
                    response = {'success': True}
                    return JsonResponse(response);

        except:
            print('EXCEPTION')
            email_service.send_kyc_duplicate(email)
            response = {'success': False}
            return JsonResponse(response);
