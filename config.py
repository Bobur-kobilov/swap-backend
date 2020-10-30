import json

with open('./env.json') as f:
    loaded_json = json.load(f)

    DBINFO = loaded_json['db_info']
    CONTRACT_INFO = loaded_json['contract_info']
    MAILER_INFO = loaded_json['mailer']
    SERVER = loaded_json['server']
    KYC = loaded_json['kyc_info']

# TODO: Modify here!
# MAIL_TEMPLATE = """
# <TEXT> {tx_hash} {address}
# """
# with open('./images/img_line.png') as image_line:

