# wechat --- 企业微信机器人

## 一、模块介绍
### 版本号
wechat: V1.1.0

当前版本支持群机器人相关API调用，包括发送文本消息、图片、markdown、文件、模板消息卡片、模板图片卡片。

### 如何使用

- 1.创建企业微信内部群
- 2.创建机器人，复制 webhook，如：https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxx
- 3.调用机器人API，示例见下文

### 安装

将 wechat 包复制到 site-pakages 下

## 二、示例

### 设置token

方式一：

```python
from wechat import set_token


set_token('xxx')
```

方式二：

```python
from wechat import Robot     # Robot 是一个机器人实例对象


Robot.set_token('xxx')
```

方式三：

```python
from wechat import R        # R 是一个机器人类对象


r = R()
r.set_token('xxx')
```

### 查看token

方式一：

```python
from wechat import Robot


print(Robot.token)
```

方式二：

```python
from wechat import R


r = R()
print(r.token)
```

### 发送文本消息

```python
from wechat import Robot


Robot.send_text('hello word')
# @张三
Robot.send_text('hello word'， mentioned_list=['zhangsan'])
# @所有人
Robot.send_text('hello word'， mentioned_list=['@all'])
```

### 发送图片消息

```python
from wechat import Robot


Robot.send_image(path='D:\\a.png')

# 传入Path路径也可以
from pathlib import Path
Robot.send_image(path=Path('D:\\a.png'))
```

### 发送Markdown消息

```python
from wechat import Robot


Robot.send_markdown(content='**加粗hello world**')
```

### 发送文件消息

```python
from wechat import Robot


Robot.send_image_text(
    articles=[
        {
            "title": "标题",
            "description": "中秋你快勒马",
            "url": "www.qq.com",
            "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
        },
        {
            "title": "标题2",
            "description": "中秋你快勒马 11111111111",
            "url": "www.baidu.com",
            "picurl": "https://inews.gtimg.com/newsapp_ls/0/15237923582_640330/0"
        }
    ]
)
```

### 发送图文消息

```python
from wechat import Robot


Robot.send_file(path='D:\\a.csv')

# 传入Path路径也可以
from pathlib import Path
Robot.send_file(path=Path('D:\\a.csv'))
```

### 发送模板卡片卡片

```python
from wechat import Robot


Robot.send_text_card(
    source={
        "icon_url":"https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
        "desc":"企业微信",
        "desc_color":0
    },
    main_title={
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信"
    },
    emphasis_content={
        "title":"100",
        "desc":"数据含义"
    },
    quote_area={
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH",
        "title":"引用文本标题",
        "quote_text":"Jack：企业微信真的很好用~\nBalian：超级好的一款软件！"
    },
    sub_title_text:"下载企业微信还能抢红包！",
    horizontal_content_list=[
        {
            "keyname":"邀请人",
            "value":"张三"
        },
        {
            "keyname":"企微官网",
            "value":"点击访问",
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi"
        },
        {
            "keyname":"企微下载",
            "value":"企业微信.apk",
            "type":2,
            "media_id":"MEDIAID"
        }
    ],
    jump_list=[
        {
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi",
            "title":"企业微信官网"
        },
        {
            "type":2,
            "appid":"APPID",
            "pagepath":"PAGEPATH",
            "title":"跳转小程序"
        }
    ],
    card_action{
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH"
    }
)
  
```

### 发送模板图片卡片

```python
from wechat import Robot


Robot.send_image_card(
    source={
        "icon_url":"https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
        "desc":"企业微信",
        "desc_color":0
    },
    main_title={
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信"
    },
    card_image={
        "url":"https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0",
        "aspect_ratio":2.25
    },
    image_text_area={
        "type":1,
        "url":"https://work.weixin.qq.com",
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信",
        "image_url":"https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0"
    },
    quote_area={
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH",
        "title":"引用文本标题",
        "quote_text":"Jack：企业微信真的很好用~\nBalian：超级好的一款软件！"
    },
    vertical_content_list=[
        {
            "title":"惊喜红包等你来拿",
            "desc":"下载企业微信还能抢红包！"
        }
    ],
    horizontal_content_list=[
        {
            "keyname":"邀请人",
            "value":"张三"
        },
        {
            "keyname":"企微官网",
            "value":"点击访问",
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi"
        },
        {
            "keyname":"企微下载",
            "value":"企业微信.apk",
            "type":2,
            "media_id":"MEDIAID"
        }
    ],
    jump_list=[
        {
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi",
            "title":"企业微信官网"
        },
        {
            "type":2,
            "appid":"APPID",
            "pagepath":"PAGEPATH",
            "title":"跳转小程序"
        }
    ],
    card_action={
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH"
    }
)
```

## 三、API

### wechat 模块API

| API       | 说明                  |
| --------- | --------------------- |
| R         | 机器人类对象          |
| Robot     | 机器人实例对象        |
| set_token | 给机器人实例设置token |

### Robot API

| API             | 说明                  |
| --------------- | --------------------- |
| set_token       | 给机器人实例设置token |
| send_text       | 发送文本消息          |
| send_markdown   | 发送markdown文本消息  |
| send_image      | 发送图片消息          |
| send_image_text | 发送图片文本          |
| send_file       | 发送文件              |
| send_text_card  | 发送模板消息卡片      |
| send_image_card | 发送模板图片卡片      |

### Robot API 参数

#### set_token 参数：

| 参数  | 类型   | 说明                      |
| ----- | ------ | ------------------------- |
| token | 字符串 | token，webhook中的key参数 |

#### send_text 参数：

| 参数                  | 类型   | 说明                                                         |
| --------------------- | ------ | ------------------------------------------------------------ |
| content               | 字符串 | 消息内容                                                     |
| mentioned_list        | 列表   | userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人。如：['zhangsan', '@all'] |
| mentioned_mobile_list | 列表   | 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人 |

示例：

```json
{
    "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
    "mentioned_list":["wangqing","@all"],
    "mentioned_mobile_list":["13800001111","@all"]
}
```

#### send_markdown 参数：

| 参数    | 类型   | 说明     |
| ------- | ------ | -------- |
| content | 字符串 | 消息内容 |

示例：

```json
{
    "content": "实时新增用户反馈<font color=\"warning\">132例</font>"
}
```

1. 标题 （支持1至6级标题，注意#与文字中间要有空格）

   ```javascript
   # 标题一
   ## 标题二
   ### 标题三
   #### 标题四
   ##### 标题五
   ###### 标题六
   ```

2. 加粗

   ```javascript
   **bold**
   ```

3. 链接

   ```javascript
   [这是一个链接](http://work.weixin.qq.com/api/doc)
   ```

4. 行内代码段（暂不支持跨行）

   ```javascript
   `code`
   ```

5. 引用

   ```javascript
   > 引用文字
   ```

6. 字体颜色(只支持3种内置颜色)

   ```javascript
   <font color="info">绿色</font>
   <font color="comment">灰色</font>
   <font color="warning">橙红色</font>
   ```

#### send_image 参数：

| 参数 | 类型               | 说明     |
| ---- | ------------------ | -------- |
| path | 字符串 / Path 对象 | 图片路径 |

####  send_image_text 参数：

| 参数     | 类型         | 说明                                 |
| -------- | ------------ | ------------------------------------ |
| articles | 列表嵌套字典 | 图文消息，一个图文消息支持1到8条图文 |

articles 字典参数：

- title：描述，不超过512个字节，超过会自动截断
- description：标题，不超过128个字节，超过会自动截断
- url：点击后跳转的链接
- picurl：图文消息的图片链接，支持 JPG、PNG 格式，较好的效果为大图 1068 * 455，小图 150 * 150

示例：

```json
[
    {
        "title" : "中秋节礼品领取",
        "description" : "今年中秋节公司有豪礼相送",
        "url" : "www.qq.com",
        "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
    }
]
```

#### send_file 参数：

| 参数 | 类型               | 说明     |
| ---- | ------------------ | -------- |
| path | 字符串 / Path 对象 | 文件路径 |

#### send_text_card 参数：

| 参数                    | 类型         | 说明                                                         |
| ----------------------- | ------------ | ------------------------------------------------------------ |
| source                  | 字典         | 卡片来源样式信息，不需要来源样式可不填写                     |
| main_title              | 字典         | 模版卡片的主要内容，包括一级标题和标题辅助信息               |
| emphasis_content        | 字典         | 关键数据样式                                                 |
| quote_area              | 字典         | 用文献样式，建议不与关键数据共用                             |
| sub_title_text          | 字符串       | 二级普通文本，建议不超过112个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写 |
| horizontal_content_list | 列表嵌套字典 | 二级标题+文本列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过6 |
| jump_list               | 列表嵌套字典 | 跳转指引样式的列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过3 |
| card_action             | 字典         | 整体卡片的点击跳转事件，text_notice模版卡片中该字段为必填项  |

source 字典参数

| 参数       | 类型   | 必须项 | 说明                                                         |
| ---------- | ------ | ------ | ------------------------------------------------------------ |
| icon_url   | String | 否     | 来源图片的url                                                |
| desc       | String | 否     | 来源图片的描述，建议不超过13个字                             |
| desc_color | String | 否     | 来源文字的颜色，目前支持：0(默认) 灰色，1 黑色，2 红色，3 绿色 |

main_title 字典参数

| 参数  | 类型   | 必须项 | 说明                                                         |
| ----- | ------ | ------ | ------------------------------------------------------------ |
| title | String | 否     | 一级标题，建议不超过26个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写 |
| desc  | String | 否     | 标题辅助信息，建议不超过30个字                               |

emphasis_content  字典参数

| 参数  | 类型   | 必须项 | 说明                                         |
| ----- | ------ | ------ | -------------------------------------------- |
| title | String | 否     | 关键数据样式的数据内容，建议不超过10个字     |
| desc  | String | 否     | 关键数据样式的数据描述内容，建议不超过15个字 |

quote_area 字典参数

| 参数       | 类型   | 必须项 | 说明                                                         |
| ---------- | ------ | ------ | ------------------------------------------------------------ |
| type       | Int    | 否     | 引用文献样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序 |
| url        | String | 否     | 点击跳转的url，quote_area.type是1时必填                      |
| appid      | String | 否     | 点击跳转的小程序的appid，quote_area.type是2时必填            |
| pagepath   | String | 否     | 点击跳转的小程序的pagepath，quote_area.type是2时选填         |
| title      | String | 否     | 引用文献样式的标题                                           |
| quote_text | String | 否     | 引用文献样式的引用文案                                       |

horizontal_content_list 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 否     | 链接类型，0或不填代表是普通文本，1 代表跳转url，2 代表下载附件，3 代表@员工 |
| keyname  | String | 是     | 二级标题，建议不超过5个字                                    |
| value    | String | 否     | 二级文本，如果horizontal_content_list.type是2，该字段代表文件名称（要包含文件类型），建议不超过26个字 |
| url      | String | 否     | 链接跳转的url，horizontal_content_list.type是1时必填         |
| media_id | String | 否     | 附件的media_id，horizontal_content_list.type是2时必填        |
| userid   | String | 否     | 被@的成员的userid，horizontal_content_list.type是3时必填     |

jump_list 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 否     | 跳转链接类型，0或不填代表不是链接，1 代表跳转url，2 代表跳转小程序 |
| title    | String | 是     | 跳转链接样式的文案内容，建议不超过13个字                     |
| url      | String | 否     | 跳转链接的url，jump_list.type是1时必填                       |
| appid    | String | 否     | 跳转链接的小程序的appid，jump_list.type是2时必填             |
| pagepath | String | 否     | 跳转链接的小程序的pagepath，jump_list.type是2时选填          |

card_action 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 是     | 片跳转类型，1 代表跳转url，2 代表打开小程序。text_notice模版卡片中该字段取值范围为[1,2] |
| url      | String | 否     | 跳转事件的url，card_action.type是1时必填                     |
| appid    | String | 否     | 跳转事件的小程序的appid，card_action.type是2时必填           |
| pagepath | String | 否     | 跳转事件的小程序的pagepath，card_action.type是2时选填        |

示例：

```json
{
    "card_type":"text_notice",
    "source":{
        "icon_url":"https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
        "desc":"企业微信",
        "desc_color":0
    },
    "main_title":{
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信"
    },
    "emphasis_content":{
        "title":"100",
        "desc":"数据含义"
    },
    "quote_area":{
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH",
        "title":"引用文本标题",
        "quote_text":"Jack：企业微信真的很好用~\nBalian：超级好的一款软件！"
    },
    "sub_title_text":"下载企业微信还能抢红包！",
    "horizontal_content_list":[
        {
            "keyname":"邀请人",
            "value":"张三"
        },
        {
            "keyname":"企微官网",
            "value":"点击访问",
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi"
        },
        {
            "keyname":"企微下载",
            "value":"企业微信.apk",
            "type":2,
            "media_id":"MEDIAID"
        }
    ],
    "jump_list":[
        {
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi",
            "title":"企业微信官网"
        },
        {
            "type":2,
            "appid":"APPID",
            "pagepath":"PAGEPATH",
            "title":"跳转小程序"
        }
    ],
    "card_action":{
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH"
    }
}
```

#### send_image_card 参数：

| 参数                    | 类型         | 说明                                                         |
| ----------------------- | ------------ | ------------------------------------------------------------ |
| source                  | 字典         | 卡片来源样式信息，不需要来源样式可不填写                     |
| main_title              | 字典         | 模版卡片的主要内容，包括一级标题和标题辅助信息               |
| card_image              | 字典         | 图片样式                                                     |
| image_text_area         | 字典         | 左图右文样式                                                 |
| quote_area              | 字典         | 引用文献样式，建议不与关键数据共用                           |
| vertical_content_list   | 列表嵌套字典 | 卡片二级垂直内容，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过4 |
| horizontal_content_list | 列表嵌套字典 | 二级标题+文本列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过6 |
| jump_list               | 列表嵌套字典 | 跳转指引样式的列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过3 |
| card_action             | 字典         | 整体卡片的点击跳转事件，news_notice模版卡片中该字段为必填项  |

source 字典参数

| 参数       | 类型   | 必须项 | 说明                                                         |
| ---------- | ------ | ------ | ------------------------------------------------------------ |
| icon_url   | String | 否     | 来源图片的url                                                |
| desc       | String | 否     | 来源图片的描述，建议不超过13个字                             |
| desc_color | String | 否     | 来源文字的颜色，目前支持：0(默认) 灰色，1 黑色，2 红色，3 绿色 |

main_title 字典参数

| 参数  | 类型   | 必须项 | 说明                                                         |
| ----- | ------ | ------ | ------------------------------------------------------------ |
| title | String | 否     | 一级标题，建议不超过26个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写 |
| desc  | String | 否     | 标题辅助信息，建议不超过30个字                               |

card_image 字典参数

| 参数         | 类型   | 必须项 | 说明                                                       |
| ------------ | ------ | ------ | ---------------------------------------------------------- |
| url          | String | 是     | 图片的url                                                  |
| aspect_ratio | String | 否     | 图片的宽高比，宽高比要小于2.25，大于1.3，不填该参数默认1.3 |

image_text_area 字典参数

| 参数      | 类型   | 必须项 | 说明                                                         |
| --------- | ------ | ------ | ------------------------------------------------------------ |
| type      | Int    | 否     | 左图右文样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序 |
| url       | String | 否     | 点击跳转的url，image_text_area.type是1时必填                 |
| appid     | String | 否     | 点击跳转的小程序的appid，必须是与当前应用关联的小程序，image_text_area.type是2时必填 |
| pagepath  | String | 否     | 点击跳转的小程序的pagepath，image_text_area.type是2时选填    |
| title     | String | 否     | 左图右文样式的标题                                           |
| desc      | String | 否     | 左图右文样式的描述                                           |
| image_url | String | 是     | 左图右文样式的图片url                                        |

quote_area 字典参数

| 参数       | 类型   | 必须项 | 说明                                                         |
| ---------- | ------ | ------ | ------------------------------------------------------------ |
| type       | Int    | 否     | 引用文献样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序 |
| url        | String | 否     | 点击跳转的url，quote_area.type是1时必填                      |
| appid      | String | 否     | 点击跳转的小程序的appid，quote_area.type是2时必填            |
| pagepath   | String | 否     | 点击跳转的小程序的pagepath，quote_area.type是2时选填         |
| title      | String | 否     | 引用文献样式的标题                                           |
| quote_text | String | 否     | 引用文献样式的引用文案                                       |

horizontal_content_list 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 否     | 链接类型，0或不填代表是普通文本，1 代表跳转url，2 代表下载附件，3 代表@员工 |
| keyname  | String | 是     | 二级标题，建议不超过5个字                                    |
| value    | String | 否     | 二级文本，如果horizontal_content_list.type是2，该字段代表文件名称（要包含文件类型），建议不超过26个字 |
| url      | String | 否     | 链接跳转的url，horizontal_content_list.type是1时必填         |
| media_id | String | 否     | 附件的media_id，horizontal_content_list.type是2时必填        |

vertical_content_list 嵌套字典参数

| 参数  | 类型   | 必须项 | 说明                            |
| ----- | ------ | ------ | ------------------------------- |
| title | String | 是     | 片二级标题，建议不超过26个字    |
| desc  | String | 否     | 二级普通文本，建议不超过112个字 |

jump_list 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 否     | 跳转链接类型，0或不填代表不是链接，1 代表跳转url，2 代表跳转小程序 |
| title    | String | 是     | 跳转链接样式的文案内容，建议不超过13个字                     |
| url      | String | 否     | 跳转链接的url，jump_list.type是1时必填                       |
| appid    | String | 否     | 跳转链接的小程序的appid，jump_list.type是2时必填             |
| pagepath | String | 否     | 跳转链接的小程序的pagepath，jump_list.type是2时选填          |

card_action 嵌套字典参数

| 参数     | 类型   | 必须项 | 说明                                                         |
| -------- | ------ | ------ | ------------------------------------------------------------ |
| type     | Int    | 是     | 片跳转类型，1 代表跳转url，2 代表打开小程序。text_notice模版卡片中该字段取值范围为[1,2] |
| url      | String | 否     | 跳转事件的url，card_action.type是1时必填                     |
| appid    | String | 否     | 跳转事件的小程序的appid，card_action.type是2时必填           |
| pagepath | String | 否     | 跳转事件的小程序的pagepath，card_action.type是2时选填        |

示例：

```json
{
    "card_type":"news_notice",
    "source":{
        "icon_url":"https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
        "desc":"企业微信",
        "desc_color":0
    },
    "main_title":{
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信"
    },
    "card_image":{
        "url":"https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0",
        "aspect_ratio":2.25
    },
    "image_text_area":{
        "type":1,
        "url":"https://work.weixin.qq.com",
        "title":"欢迎使用企业微信",
        "desc":"您的好友正在邀请您加入企业微信",
        "image_url":"https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0"
    },
    "quote_area":{
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH",
        "title":"引用文本标题",
        "quote_text":"Jack：企业微信真的很好用~\nBalian：超级好的一款软件！"
    },
    "vertical_content_list":[
        {
            "title":"惊喜红包等你来拿",
            "desc":"下载企业微信还能抢红包！"
        }
    ],
    "horizontal_content_list":[
        {
            "keyname":"邀请人",
            "value":"张三"
        },
        {
            "keyname":"企微官网",
            "value":"点击访问",
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi"
        },
        {
            "keyname":"企微下载",
            "value":"企业微信.apk",
            "type":2,
            "media_id":"MEDIAID"
        }
    ],
    "jump_list":[
        {
            "type":1,
            "url":"https://work.weixin.qq.com/?from=openApi",
            "title":"企业微信官网"
        },
        {
            "type":2,
            "appid":"APPID",
            "pagepath":"PAGEPATH",
            "title":"跳转小程序"
        }
    ],
    "card_action":{
        "type":1,
        "url":"https://work.weixin.qq.com/?from=openApi",
        "appid":"APPID",
        "pagepath":"PAGEPATH"
    }
}
```

