#三、添加静态文件
#（1）添加CSS文件
# myworld
#   ├┈ manage.py
#   ├┈ myworld/
#   ╰┈ members/
#      ├┈ templates/
#      ├┈ static/
#         ╰┈ myfirst.css
# 打开 CSS 文件 (members/static/myfirst.css) 并插入以下内容：
body {
  background-color: lightblue;
  font-family: verdana;
}
# 修改模板 (members/templates/template.html) 引入 css 文件
{% load static %} #加载静态文件标签库
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="{% static 'myfirst.css' %}"> #引入静态文件
<body>
#（2）添加JS文件
# myworld
#   ├┈ manage.py
#   ├┈ myworld/
#   ╰┈ members/
#      ├┈ templates/
#      ├┈ static/
#         ╰┈ myfirst.js
# 打开 JS 文件 (members/static/myfirst.js) 并插入以下内容：
function myFunction() {
  alert("Hello from a static file!");
}
# 修改模板 (members/templates/template.html) 引入 JS 文件：
{% load static %}
<!DOCTYPE html>
<html>
<script src="{% static 'myfirst.js' %}"></script>
<body>
<button onclick="myFunction()">Click me!</button>
#（3）添加图片文件
# myworld
#   ├┈ manage.py
#   ├┈ myworld/
#   ╰┈ members/
#      ├┈ templates/
#      ├┈ static/
#         ╰┈ pineapple.jpg
# *打开 JS 文件 (members/static/pineapple.jpg) 并插入以下内容：
function myFunction() {
  alert("Hello from a static file!");
}
# *修改模板 (members/templates/template.html) 引入 jpg 文件
{% load static %}
<!DOCTYPE html>
<html>
<body>
<img src="{% static 'pineapple.jpg' %}">
</body>
</html>