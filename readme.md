  
## 发布说明
# v1.0

发布日期: 2020-06-29

功能说明：
- 通过SDK方式提供发送模板短信功能。
--------------------------------

## 示例
Python 3.6<pre>
<code>
from sdk.SmsSDK import SmsSDK

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

## 目录结构
<pre>
SmsSDK
│ readme.md
├─demo
│      SmsDemo.py
│
├─sdk
│  │  algorithm.py
│  │  SmsSDK.py
│  │  __init__.py
</pre>

--------------------------------
https://www.yuntongxun.com
