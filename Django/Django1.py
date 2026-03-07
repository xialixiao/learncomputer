#二、Django模板
#（1）模板变量
<!-- template.html -->
<h1>你好 {{ firstname }}，你好吗？</h1>  #模板变量使用双大括号 {{ }} 包裹，Django会自动将变量替换为对应的值。
# *在视图 (views.py) 中创建变量，上面示例中的变量 firstname 通过视图发送到模板：
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html') #加载模板
  context = {
    'firstname': '狂徒张三',
  }
  return HttpResponse(template.render(context, request))  #渲染模板并返回响应
#（2）模板中创建变量
{% with firstname="Tobias" %} #在模板中使用 {% with %} 标签创建一个新的变量 firstname，并赋值为 "Tobias"。
<h1>你好 {{ firstname }}，你好吗？</h1>
#（3）数组循环
<ul>
  {% for x in mymembers %}  #使用 {% for %} 标签循环遍历 mymembers 数组，并将每个元素赋值给变量 x。
    <li>{{ x.firstname }}</li>  #在循环体内，使用 {{ x.firstname }} 来访问当前元素的 firstname 属性，并将其显示在列表项中。
  {% endfor %}#循环结束后，使用 {% endfor %} 标签来标记循环的结束。
</ul> 
# （4）模板标签参考
# 标签	描述
# autoescape	指定自动转义模式是打开还是关闭
# block	指定块部分
# comment	指定注释部分
# csrf_token	保护表单免受跨站点请求伪造
# cycle	指定要在循环的每个循环中使用的内容
# debug	指定调试信息
# extends	指定父模板
# filter	在返回之前过滤内容
# firstof	返回第一个非空变量
# for	指定一个 for 循环
# if	指定一个 if 语句
# ifchanged	仅当自上次迭代以来值已更改时才输出块
# (用于 for 循环)
# include	指定包含的内容/模板
# load	从另一个库加载模板标签
# lorem	输出随机文本
# now	输出当前日期/时间
# regroup	按组对对象进行排序
# resetcycle	循环使用，重置循环
# spaceless	删除 HTML 标签之间的空格
# templatetag	输出指定的模板标签
# url	返回 URL 的绝对 URL 部分
# verbatim	指定不应由模板引擎呈现的内容
# widthratio	给定值和最大值之间的比率计算宽度值
# with	指定要在块中使用的变量
#（5）if语句
{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 
#（6）for循环
{% for x in cars %}
  <h1>{{ x.brand }}</h1>
  <p>{{ x.model }}</p>
  <p>{{ x.year }}</p>
{% endfor %} 
# 数据 cars 空的展示内容：
<ul>
  {% for x in cars %}
    <h1>{{ x.brand }}</h1>
    <p>{{ x.model }}</p>
    <p>{{ x.year }}</p>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 
# （7）循环变量
# *forloop.counter 当前循环，从 1 开始
# *forloop.counter0 当前循环，从 0 开始
# *forloop.first 循环是否在其第一次循环中
# *forloop.last 循环是否在其最后一次循环中
# *forloop.parentloop
# *forloop.revcounter 如果从末尾开始并向后计数，则以 1 结束
# *forloop.revcounter0 如果从末尾开始并向后计数，则以 0 结束
#（8）过滤值
<h1>你好 {{ firstname|upper }}，你好吗？</h1> #使用过滤器将变量 firstname 转换为大写字母。
#（9）注释
<h1>欢迎大家{# 较小的注释 #}</h1>
{% comment %}
  <h1>欢迎女士们先生们</h1>
{% endcomment %} #使用 {% comment %} 标签包裹的内容将被视为注释，并且不会在最终的 HTML 输出中显示。
#（10）双过滤值
<h1>你好 {{ firstname|first|upper }}，你好吗？</h1> #返回变量 firstname 的第一个字符，小写
#（11）过滤器标签
{% filter upper %}
  <h1>Hello everyone, how are you?</h1>
{% endfilter %}  #使用 {% filter %} 标签将块内的内容转换为大写字母。
#（12）cycle
# 如果你想为每次循环使用新的背景颜色，你可以使用 cycle 标签来做到这一点
<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 
# 将参数值保存在变量中，以便以后使用：
<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 
# 你注意到 silent 关键字了吗？ 确保添加这个，否则参数值将在输出中显示两次
<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    {% if forloop.counter == 3 %}
      {% resetcycle %}
    {% endif %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> #您可以使用 {% resetcycle %} 标签强制循环重新开始
#（13）每一行添加行号
{% filter upper|linenumbers %}Hello!
my name is
Emil.
What is your name?{% endfilter %}#返回内容大写并在每一行添加行号
#（14）导入模板
footer.html:
<p>您已到达本页底部，感谢您抽出宝贵时间</p>
template.html:
<h1>Hello</h1>
<p>此页面包含模板中的页脚</p>
{% include 'footer.html' %} #使用 {% include %} 标签将 footer.html 模板包含在 template.html 模板中。
#（15）导入模板传入变量
mymenu.html:
<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>
template.html:
{% include mymenu.html with me="张三" sponsor="Reference" %} #使用 {% include %} 标签将 mymenu.html 模板包含在 template.html 模板中，并传递变量 me 和 sponsor 的值。
<h1>Welcome</h1>
<p>This is my webpage</p>
#（16）过滤器参考
# add	添加指定的值
# addslashes	在任何引号字符之前添加一个斜杠，以转义字符串
# capfirst	返回大写的第一个字母
# center	使值在指定宽度的中间居中
# cut	删除任何指定的字符或短语
# date	以指定格式返回日期
# default	如果值为 False，则返回指定值
# default_if_none	如果值为 None，则返回指定的值
# dictsort	按给定值对字典进行排序
# dictsortreversed	按给定值对字典进行反向排序
# divisibleby	如果该值可以除以指定的数字，则返回 True，否则返回 False
# escape	从字符串中转义 HTML 代码
# escapejs	从字符串中转义 JavaScript 代码
# filesizeformat	将数字返回为文件大小格式
# first	返回对象的第一项（对于字符串，返回第一个字符）
# floatformat	将浮点数四舍五入到指定的小数位数，默认为一位小数
# force_escape	从字符串中转义 HTML 代码
# get_digit	返回数字的特定数字
# iriencode	将 IRI 转换为 URL 友好字符串
# join	将列表中的项目返回为字符串
# json_script	将一个对象返回为由 <script></script> 标签包围的 JSON 对象
# last	返回对象的最后一项（对于字符串，返回最后一个字符）
# length	返回对象中的项目数，或字符串中的字符数
# length_is	如果长度与指定的数字相同，则返回 True
# linebreaks	返回带有 <br> 而不是换行符和 <p> 而不是多个换行符的文本
# linebreaksbr	返回带有 <br> 的文本，而不是换行符
# linenumbers	返回每行带有行号的文本
# ljust	根据指定的宽度左对齐值
# lower	以小写字母返回文本
# make_list	将值转换为列表对象
# phone2numeric	将带字母的电话号码转换为数字电话号码
# pluralize	如果指定的数值不是 1，则在值的末尾添加一个 s
# pprint	
# random	返回对象的随机项
# rjust	根据指定的宽度右对齐值
# safe	标记此文本是安全的，不应进行 HTML 转义
# safeseq	将对象的每个项目标记为安全且项目不应进行 HTML 转义
# slice	返回文本或对象的指定切片
# slugify	将文本转换为一个长字母数字小写单词
# stringformat	将值转换为指定格式
# striptags	从文本中删除 HTML 标记
# time	以指定格式返回时间
# timesince	返回两个日期时间之间的差
# timeuntil	返回两个日期时间之间的差
# title	文本中每个单词的第一个字符大写，所有其他字符都转换为小写
# truncatechars	将字符串缩短为指定数量的字符
# truncatechars_html	将字符串缩短为指定数量的字符，而不考虑任何 HTML 标记的长度
# truncatewords	将字符串缩短为指定数量的单词
# truncatewords_html	将字符串缩短为指定数量的单词，而不考虑任何 HTML 标记
# unordered_list	将对象的项目返回为无序列的 HTML 列表
# upper	以大写字母返回文本
# urlencode	URL 对字符串进行编码
# urlize	将字符串中的任何 URL 作为 HTML 链接返回
# urlizetrunc	将字符串中的任何 URL 作为 HTML 链接返回，但会将链接缩短为指定的字符数
# wordcount	返回文本中的单词数
# wordwrap	以指定的字符数换行
# yesno	将布尔值转换为指定值
# i18n	
# l10n	
# tz
# （17）字段查询参考
# contains	包含短语
# icontains	与包含相同，但不区分大小写
# date	匹配日期
# day	匹配日期(日期，1-31)(日期)
# endswith	以。。结束
# iendswith	与 endwidth 相同，但不区分大小写
# exact	完全匹配
# iexact	与精确相同，但不区分大小写
# in	匹配其中一个值
# isnull	匹配 NULL 值
# gt	比...更棒
# gte	大于或等于
# hour	匹配一个小时(对于日期时间)
# lt	少于
# lte	小于或等于
# minute	匹配一分钟(对于日期时间)
# month	匹配一个月(日期)
# quarter	匹配一年中的一个季度 (1-4)(用于日期)
# range	之间的匹配
# regex	匹配正则表达式
# iregex	与正则表达式相同，但不区分大小写
# second	匹配一秒(对于日期时间)
# startswith	以 ... 开始
# istartswith	与 startswith 相同，但不区分大小写
# time	匹配时间(用于日期时间)
# week	匹配周数 (1-53)(用于日期)
# week_day	匹配一周中的某一天 (1-7) 1 是星期日
# iso_week_day	匹配 ISO 8601 星期几 (1-7) 1 是星期一
# year	匹配一年(日期)
# iso_year	匹配 ISO 8601 年份(日期)
