  
## 安装SDK
```console
$ pip install ronglian-sms-sdk
Collecting ronglian-sms-sdk…
✔ Successfully installed ronglian-sms-sdk-xx
…
```
--------------------------------

## 示例
```python
from ronglian_sms_sdk import SmsSDK

accId = '容联云通讯分配的主账号ID'
accToken = '容联云通讯分配的主账号TOKEN'
appId = '容联云通讯分配的应用ID'

def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '容联云通讯平台创建的模板'
    mobile = '手机号1,手机号2'
    datas = ('变量1', '变量2')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)
```
--------------------------------

## 发布说明
```
# v1.0.0

发布日期: 2020-06-29

功能说明：
- 提供发送模板短信功能。
```
--------------------------------

## 目录结构
```
python-sms-sdk
│ readme.md
│ requirements.txt
├─example
│      SendMessage.py    -- 发送短信示例
│
├─ronglian_sms_sdk
│  │  algorithm.py       -- SDK依赖算法
│  │  SmsSDK.py          -- 短信SDK
│  │  __init__.py
```
--------------------------------

https://www.yuntongxun.com
