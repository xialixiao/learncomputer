#一、入门
#（1）准备环境
pyhton --version  #查看python版本
pip --version #查看pip版本
#（2）入门
#（2.1）创建虚拟环境
py -m venv myproject #Windows
python3 -m venv myproject #Linux/MacOS
#（2.2）其中包含子文件夹和文件，如下所示
# myproject
#  ├┈Include  #包含Python头文件
#  ├┈Lib      #包含Python库文件
#  ├┈Scripts  #包含激活脚本和pip等工具
#  ╰┈pyvenv.cfg #包含虚拟环境的配置信息
#（2.3）激活虚拟环境
# Windows:
myproject\Scripts\activate.bat
# Unix/MacOS:
source myproject/bin/activate
#（2.4）提示符中看到以下结果：
# Windows:
(myproject) C:\Users\Your Name>
# Unix/MacOS:
(myproject) ... $
#（2.5）安装Django
# Windows:
(myproject) C:\Users\Name>py -m pip install Django
# Unix/MacOS:
(myproject) ... $ python -m pip install Django
#（3）创建Django项目
$ django-admin startproject myworld #创建一个名为myworld的Django项目
#（3.1）创建了一个myworld文件夹，内容如下：
# myworld
#   ├┈ manage.py   #Django项目的管理工具
#   ╰┈ myworld/    #Django项目的主应用文件夹
#      ├┈ __init__.py  #标识这是一个Python包
#      ├┈ asgi.py      #ASGI配置文件
#      ├┈ settings.py  #Django项目的设置文件
#      ├┈ urls.py      #Django项目的URL配置文件
#      ╰┈ wsgi.py      #WSGI配置文件
#（3.2）运行Django项目
$ py manage.py runserver     # Windows
$ python manage.py runserver # Unix/MacOS
#（3.3）在浏览器中访问http://127.0.0.1:8000/
#(4)检查Django版本
(myproject) C:\Users\Your Name>django-admin --version
#（5）创建应用
$ py manage.py startapp members
#项目中创建了一个名为 members 的文件夹，内容如下：
# myworld
#   ├┈ manage.py
#   ├┈ myworld/
#   ╰┈ members/
#      ├┈ migrations/  #包含数据库迁移文件
#      ┆  ╰┈ __init__.py  #`标识这是一个Python包
#      ├┈ __init__.py #标识这是一个Python包
#      ├┈ admin.py    #包含管理员界面配置
#      ├┈ apps.py     #包含应用程序配置
#      ├┈ models.py   #包含数据模型
#      ├┈ tests.py    #包含测试代码
#      ╰┈ views.py    #包含视图函数
# 首先，看一下名为 views.py 的文件。这是我们收集发送回正确响应所需的信息的地方。
#（6）应用目录介绍
# *Django 接收 URL，检查 urls.py 文件，并调用与 URL 匹配的视图。
# *位于 views.py 中的视图检查相关模型。
# *模型是从 models.py 文件中导入的。
# *然后视图将数据发送到模板文件夹中的指定模板。
# *模板包含 HTML 和 Django 标记，并使用数据将完成的 HTML 内容返回给浏览器
#(7)视图
# *Django 视图是接受 http 请求并返回 http 响应的 Python 函数，就像 HTML 文档一样。
# *使用 Django 的网页充满了不同任务和任务的视图。
# *视图通常放在一个名为 views.py 的文件中，该文件位于应用程序的文件夹中。
# *您的 members 文件夹中有一个 views.py，如下所示：
from dhjango.shortcuts import render
## Create your views here.
#找到它并打开它，并将内容替换为：
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the members index.")
# *这是一个关于如何将响应发送回浏览器的简单示例。
# *但是我们如何执行视图呢？ 好吧，我们必须通过 URL 调用视图。
#(8)URL
# 在与 views.py 文件相同的文件夹中创建一个名为 urls.py 的文件，并在其中输入以下代码：
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
# 刚刚创建的 urls.py 文件是特定于成员应用程序的。我们还必须在根目录 myworld 中进行一些路由。
# 在 myworld 文件夹中有一个名为 urls.py 的文件，打开该文件并在 import 语句中添加 include 模块，并在列表中添加一个 path() 函数。文件将如下所示：
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('members/', include('members.urls')),
  path('admin/', admin.site.urls),
]
# 如果服务器未运行，请导航到 /myworld 文件夹并在命令提示符下执行此命令：
$ py manage.py runserver
# 在浏览器窗口的地址栏中输入 127.0.0.1:8000/members/
#(9)模板
# 在 members 文件夹中创建一个 templates 文件夹，并创建一个名为 myfirst.html 的 HTML 文件。文件结构应该是这样的：
# myworld
#  ├┈ manage.py
#  ├┈ myworld/
#  ╰┈ members/
#     ╰┈ templates/
#        ╰┈ myfirst.html
# *打开 HTML 文件并插入以下内容：
<!DOCTYPE html>
<html>
<body>
  <h1>Hello World!</h1>
  <p>欢迎来到我的第一个 Django 项目！</p>
</body>
</html>
# *修改视图 members/views.py

from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
#(10)更改设置
# *为了能够处理比“Hello World！”更复杂的东西，我们必须告诉 Django 一个新的应用程序已创建
# *这是在 myworld 文件夹的 myworld/settings.py 文件中完成的。查找 INSTALLED_APPS[] 列表并添加成员应用程序，如下所示：
INSTALLED_APPS = [
    'django.contrib.admin',  #Django 管理站点
    'django.contrib.auth',   #Django 认证系统
    'django.contrib.contenttypes',  #Django 内容类型框架
    'django.contrib.sessions',      #Django 会话框架
    'django.contrib.messages',      #Django 消息框架
    'django.contrib.staticfiles',   #Django 静态文件处理
    'members.apps.MembersConfig'   #添加 members 应用程序
]
#然后运行这个命令：
$ py manage.py migrate
#通过导航到 /myworld 文件夹启动服务器并执行以下命令：
$ py manage.py runserver
#在浏览器窗口的地址栏中输入 127.0.0.1:8000/members/
#（11）创建表（模型）
#在 /members/ 文件夹中，打开 models.py 文件。要在我们的数据库中添加成员表，首先创建一个成员类，并描述其中的表字段：
from django.db import models
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
# *然后导航到 /myworld/ 文件夹并运行以下命令：
$ py manage.py makemigrations members
# Migrations for 'members':
#   members\migrations\0001_initial.py
#     - Create model Members
# *创建一个包含任何新更改的文件并将该文件存储在 /migrations/ 文件夹中。下次运行 py manage.py migrate 时，Django 将根据迁移文件夹中新文件的内容创建并执行一条 SQL 语句。运行迁移命令：
$ py manage.py migrate
# *从模型创建的 SQL 语句是：
CREATE TABLE "members_members" (
  "id" INT NOT NULL PRIMARY KEY AUTOINCREMENT,
  "firstname" varchar(255) NOT NULL,
  "lastname" varchar(255) NOT NULL
);
