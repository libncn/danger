# -*- coding: UTF-8 -*-
import flask
import os
import json

server = flask.Flask(__name__)
server.config["JSON_AS_ASCII"] = False

# 平台入口
@server.route('/')
def index():
    return flask.render_template('index.html')


# 菜单初始化
@server.route('/api/init/')
def api_init():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data = json.dumps(json.load(open(basedir + '\\static\\data\\init.json', encoding='utf-8')),
                      ensure_ascii=False)
    return data


# 端口缓存清理
@server.route('/api/clear/')
def api_clear():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data = json.dumps(json.load(open(basedir + '\\static\\data\\clear.json', encoding='utf-8')),
                      ensure_ascii=False)
    return data


# 登录认证
@server.route('/api/login/')
def api_login():
    data = {'msg': 'success'}
    return json.dumps(data)


# 功能模板动态页面
@server.route('/page/<name>')
def page(name):
    # 主页
    if name == 'home':
        return flask.render_template('home.html')

    # 登录
    elif name == 'login':
        return flask.render_template('login.html')

    # 测试
    elif name == 'test':
        return flask.render_template('404.html')

    # 开发说明
    elif name == 'intro':
        return flask.render_template('intro.html')

    # 外港堆存
    elif name == '1-1-1':
        return flask.render_template('1-1-1.html')

    # 数据上传
    elif name == '4-4-1':
        return flask.render_template('4-4-1.html')

    else:
        return flask.render_template('404.html')


if __name__ == '__main__':
    server.run(debug=True)
