=======================
SocialBase 接口消息 API
=======================

本文档描述 SocialBase 接口消息的调用方法以及开发简述。

****
名词
****

* 服务端, SocialBase: SocialBase 服务所在的应用服务器
* 客户端: SocialBase 用户拥有的与本接口协议兼容的应用服务器

********
接口概述
********

接口地址称作 ``API Endpoint`` 。 ``API Endpoint`` 包含协议、主机名以及入口点地址，例如 ``https://api.socialbase.cn/1.0/foo`` 即为一个有效的 ``API Endpoint`` 地址。
注意:

* API Endpoint 建议使用符合 RESTful API 风格的 endpoint，但也支持带有 querystring 的 endpoint.

若客户端实现时不方便使用 RESTful API ，可以通过 querystring 访问协议。下面是一些例子。

  - https://api.example.com/1.0/menu_subscribe
  - https://www.example.com/api?action=menu_subscribe


SocialBase 的服务器地址为 ``42.121.99.26``, ``42.120.51.130`` 。请在 Web 服务器配置中允许来自这两个 IP 地址的请求。为了安全，请禁用来自其他地址的请求。


********
接口协议
********

SocialBase 主动请求时全部使用 ``POST`` 方法，并期望得到符合标准的 ``JSON`` 返回值。字符集编码为 ``UTF-8`` 。

接口支持 HTTP 以及 HTTPS 协议， *推荐* 对端使用 HTTPS 协议。

请求接口
========

请求内容为标准的 ``HTTP POST`` ，负载为 ``JSON`` 。传递到对方服务器的参数以及描述如下：

必选内容
--------

================ ======================================
Argument         Description
================ ======================================
openid           发送者的微信唯一 ID
message_type     消息类型
timestamp        消息收到时的 UNIX 时间戳
================ ======================================

可选内容
--------

================ ======================================
Argument         Description
================ ======================================
message_content  消息内容
event_type       事件消息类型
event_key        事件消息 Key
geo_x            地理位置 longitude
geo_y            地理位置 latitude
geo_scale        地理位置缩放 scale
geo_label        地理位置地标
================ ======================================

``message_type``
----------------

``message_type`` 的可能取值以及对应的可选如下：

* text: 文本消息, ``message_content``: 文本消息内容
* image: 图片, ``message_content``: 图片链接
* event: 事件消息, ``event_type``, ``event_key``
* geo: 地理位置消息, ``geo_x``, ``geo_y``

回复接口
========

无回复
------
::

    {'message_type': 'no_reply'}

注意，返回无回复时，客户端将不会收到任何回复内容，建议谨慎使用。

简单文本回复
------------
::

    {'message_type': 'text', 'payload': '文本消息内容'}


图文消息
--------
::

    {
      'message_type': 'news',
      'payload':  [{
          "url": "图文消息链接",
          "title": "标题",
          "description": "一句话描述，可以等同于 content",
          "picurl": "图片地址"
        }, {
          "url": "",
          "title": "",
          "description": "",
          "picurl": ""
        }
      ]
    }

允许有不超过 10 个 ``Articles`` 成员。

微信将会将 ``payload`` 成员中的第一条的图片作为大图展现出来。 ``description`` 大约为一句话的长度。图片链接支持 ``JPG``, ``PNG`` 格式，较好的效果为大图 640*320，小图80*80。
