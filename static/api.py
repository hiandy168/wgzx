import datetime
import json

import requests


def api(touser, content):
    data_token = {'corpid': '秘密',
                  'corpsecret': '秘密'}
    gettoken = eval(requests.get('https://oapi.dingtalk.com/gettoken', data_token).text)
    token = gettoken['access_token']
    data_post = json.dumps({'touser': touser, 'agentid': '10205426', 'msgtype': 'text', 'text': {'content': content}})
    response = eval(requests.post('https://oapi.dingtalk.com/message/send?access_token=%s' % token, data_post).text)
    print(response)
    if response['errcode']>0:
        err=response['errmsg']
    else:
        err = {}
        if 'forbiddenUserId' in response:err['拒绝']=response['forbiddenUserId']
        if 'invaliduser' in response:err['无效']=response['invaliduser']
    return [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), err ,response['errcode']]

if __name__ == '__main__':
    touser = '67711'
    content = '测试' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(api(touser, content))
