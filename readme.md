  
## 安装SDK
```console
$ pip install ronglian_sms_sdk
Collecting ronglian_sms_sdk…
✔ Successfully installed ronglian-sdk-xx
…
```
--------------------------------

## 示例
<pre>
<code>
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
</code>
</pre>
--------------------------------

## 发布说明
# v1.0

发布日期: 2020-06-29

功能说明：
- 提供发送模板短信功能。
--------------------------------

## 目录结构
<pre>
python-sms-sdk
│ readme.md
| requirements.txt
├─example
│      SendMessage.py    -- 发送短信示例
│
├─ronglian_sms_sdk
│  │  algorithm.py       -- SDK依赖算法
│  │  SmsSDK.py          -- 短信SDK
│  │  __init__.py
</pre>
--------------------------------

https://www.yuntongxun.com
