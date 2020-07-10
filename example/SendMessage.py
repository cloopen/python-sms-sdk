from ronglian_sms_sdk import SmsSDK

accId = '容联云通讯分配的主账号ID'
accToken = '容联云通讯分配的主账号TOKEN'
appId = '容联云通讯分配的应用ID'

def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '容联云通讯创建的模板'
    mobile = '手机号1,手机号2'
    datas = ('变量1', '变量2')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()
