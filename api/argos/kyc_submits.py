import requests
import json
import config

def get_sumbits(email,id,headers):
    result = requests.get(config.KYC['host'] + email + '/' + id + '/' + 'result', headers=headers)
    response = result.json()
    return response

def get_lev_1(email,id):
    headers = {
    'Content-Type': 'application/json',
    'x-api-key': config.KYC['api_key_l1'],
    'access-key': config.KYC['access_key_l1']
    }
    kyc_data = get_sumbits(email,id,headers)
    return kyc_data


def get_lev_2(email,id):
    headers = {
    'Content-Type': 'application/json',
    'x-api-key': config.KYC['api_key_l2'],
    'access-key': config.KYC['access_key_l2']
    }
    kyc_data = get_sumbits(email,id,headers)
    return kyc_data

def check_user(email,id):
    kyc_data = get_lev_1(email,id)
    if 'message' in kyc_data:
        kyc_data = get_lev_2(email,id)
    if 'email' in kyc_data:
        return kyc_data
    return ''
    

