"""
@Time       ：2020-1-20
@Author     ：Honeypot
@e-mail     ：1104389956@qq.com
@version    ：dos版本
"""


from urllib import request, parse
import json


def translation_module(content):
    try:
        req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
        # 创建要提交的数据
        form_date = dict()
        form_date['i'] = content  # 要翻译的内容可以更改
        form_date['doctype'] = 'json'
        data = parse.urlencode(form_date).encode('utf-8')  # 数据转换
        response = request.urlopen(req_url, data)  # 提交数据并解析
        html = response.read().decode('utf-8')  # 服务器返回结果读取
        translate_results = json.loads(html)  # 以json格式载入

        translate_results_r = ''
        for i in translate_results['translateResult']:
            translate_results_r += i[0]['tgt'] + '\n'
    except BaseException:
        translate_results_r = "null"

    return translate_results_r


if __name__ == '__main__':
    print("{0}MR.Lin{0}".format("-"*20))
    while True:
        target_text = input("Input：")
        target_text = target_text.replace("。",".   ")
        target_text = target_text.replace("！", "!   ")
        # print(target_text)
        if target_text == "exit":
            break
        tran_text = translation_module(target_text)
        print("{0}".format(tran_text))
        print("{0}MR.Lin{0}".format("-" * 20))