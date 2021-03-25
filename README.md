# 寒门客 flask

#### 介绍
本站集合了互联网上常用的工具，都是免费的。

#### 软件架构
python
Flask
requests

#### 安装教程
这里我提供了，两种安装教程，第一种是服务器安装，第二种是本地安装。服务器安装有点复杂，不想服务器搭建的可以跳过步骤。

#### 服务器搭建

一、安装依赖
```
	sudo apt-get -y update
	sudo apt-get -y install python3 python3-venv python3-dev
	sudo apt-get -y install nginx git
```

二、安装应用程序
```
 	git clone https://gitee.com/huang-hai-deng/flask_hanmen.git
```

三、创建虚拟环境
```
	cd flask_hanmen  进入目录
	python3 -m venv venv
	source venv/bin/activate    进入虚拟环境
	pip3 install -r requirements.txt    安装库
```

四、安装 gunicorn来运行flask
```
	pip install gunicorn
```

五、使用如下命令，在后台运行项目
	这个要在虚拟环境下执行
```
	gunicorn -b localhost:8000 -w 4 wsgi:app --daemon
```

六、搭建Nginx
1.先退出虚拟环境
```
    deactivate
```
然后退出项目目录
```
    cd
```

2.先删除自带的测试站点
```
sudo rm /etc/nginx/sites-enabled/default
```

3.进入nginx配置文件
    ```
    cd /etc/nginx/sites-enabled/
    ```
4.创建配置文本
```
vim wsgi
```

5.在里面配置
```
server
{
    listen 80;
    server_name flask.hanmen.xin;#服务器公网ip或者域名
    root /www/wwwroot/flask.hanmen.xin;
    location / {
                proxy_pass http://localhost:8000;
                proxy_redirect     off;
                proxy_set_header   Host $host;}
}
```

#### 本地搭建
直接从gitee或者github下载zip文件就可以了
然后使用pip install -r requirements.txt    安装库
启动命令:
```
flask run
```

局域网启动命令:
```
flask run -h 0.0.0.0 -p 5000
```

局域网访问要你的计算机IP地址，这个你可以百度windows怎么查看ip地址。

代码任意修改，欢迎贡献！

## 微信打赏
![weixin_sm](https://gitee.com/huang-hai-deng/images/raw/master/weixin_sm.jpg)
