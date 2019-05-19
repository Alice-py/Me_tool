"""
开发时间：2019-4-20
作者：Honeypot
邮箱：1104389956@qq.com
版本：1.5
1.2改动：添加了快捷键（翻译：Enter  清空：Esc）
            修复信息框可键入内容，修复初始光标指向
1.3改动：窗口置顶，添加了快捷键（退出：Ctrl+q )
1.5改动：单行文本框改为多行文本框，修改窗口样式，修复部分bug     2019-5-19
"""



from urllib import request, parse
import json
import tkinter as tk
import sys


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
        print(translate_results['translateResult'])
        # json格式调取
        translate_results_r =''
        for i in translate_results['translateResult']:
            translate_results_r += i[0]['tgt']+'\n'
    except:
        translate_results_r = '请输入需要翻译的内容！'

    return translate_results_r


def gui():
    # 主窗口属性模块
    win.resizable(width=False, height=False)  # 禁止拉伸
    win['background'] = '#F0FFF0'  # 设置背景颜色
    win.title('翻译1.5')  # 标题
    win.geometry('400x300-50+50')  # 窗口大小与其实坐标


def get_str(meaningless=None):
    # 事件1-获取文本

    var2.config(state='normal')
    var2.delete(1.0, 'end')

    vart = var1.get("0.0","end")

    return_txt = translation_module(vart)
    var2.insert('end', return_txt)
    var2.config(state='disabled')


def clean_var(meaningless=None):
    var2.config(state='normal')
    var1.delete(1.0, 'end')
    var2.delete(1.0, 'end')
    var2.config(state='disabled')


def over(meaningless=None):
    sys.exit()


if __name__ == '__main__':

    win = tk.Tk()
    win.wm_attributes('-topmost', 1)        # 置顶
    gui()

    # 文本框1
    # var1 = tk.Entry(win, width=200, font=('Fixdsys', 16))

    var1 = tk.Text(win, height=7, font=('Fixdsys', 12))
    var1.pack(pady=0)  # 样式

    # 确认按钮
    var1.bind("<Return>", get_str)      # 绑定回车
    target_content = tk.Button(
        win,
        text='OK',
        command=get_str,
        width=30,
        height=2,
        bg='#F0FFF0',
        bd=0).place(
        x=0,
        y=120)
    var1.focus()

    # 清除按钮
    var1.bind("<Escape>", clean_var)      # 绑定回车
    tk.Button(
        win,
        text='Clean',
        command=clean_var,
        width=30,
        height=2,
        bg='#F0FFF0',
        bd=0).place(
        x=200,
        y=120)

    # 文本框2
    var2 = tk.Text(win, height=7, font=('Fixdsys', 14))
    var2.pack(side='bottom')  # 样式
    var2.config(state='disabled')
    win.bind('<Control-q>', over)
    win.mainloop()


