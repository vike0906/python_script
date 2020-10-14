import requests
import hashlib


def message_push(message, mark, isWx, isSms, isEmail, appId, appSecret):

    # 拼接参数
    sign_string = 'appId=' + appId + '&isEmail=' + str(isEmail) + "&isSms=" + str(isSms) + '&isWx=' + str(
        isWx) + '&mark=' + mark + '&message=' + message + "&appSecret=" + appSecret
    print(sign_string)

    # 计算md5
    md5 = hashlib.md5()
    md5.update(sign_string.encode('UTF-8'))
    sign = md5.hexdigest()
    print(sign)

    params = {'message': message, 'mark': mark, 'isWx': isWx, 'isSms': isSms, 'isEmail': isEmail, 'appId': appId,
              'sign': sign}

    r1 = requests.post("http://localhost:8080/message/single", data=params)

    print(r1.text)


# params_key = ['message', 'mark', 'isWx', 'isSms', 'isEmail', 'appId', 'sign']
# params_key.sort()
# print(params_key)


if __name__ == '__main__':

    appId = '943ae1b3c8804afaa62b5111fdcb6d47'  # APP_ID，系统分配
    appSecret = '83f2963edc584e3cac418dacd345af33'  # APP_SECRET，系统分配

    message = '测试消息'  # 消息内容
    mark = 'liushengli'  # 接收人标识
    isWx = 1  # 是否发送企业微信 1：发送，2：不发送
    isSms = 1  # 是否发送短信 1：发送，2：不发送
    isEmail = 2  # 是否发送电子邮件 1：发送，2：不发送

    message_push(message, mark, isWx, isSms, isEmail, appId, appSecret)


