import json
import base64
import hashlib
from pprint import pprint
from pathlib import Path
from typing import Optional, Union, Mapping

import requests


class Robot:

    def __init__(self):

        self.session = requests.session()
        self.api = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/'
        self._send = 'send'
        self._upload = 'upload_media'
        self.token = None

    def set_token(self, token: str):
        """设置机器人token"""

        print(f'token设置成功: {token}')
        self.token = token

    def _send_request(
            self, data: dict = None, params: Optional[dict] = None, path: Optional[str] = None,
            **kwargs
    ) -> bool:

        if path is None:
            url = self.api + self._send
        else:
            url = self.api + path

        if self.token is None:
            raise ValueError('发消息之前请先设置token')

        if params is None:
            params = {
                'key': self.token
            }

        try:
            res = requests.post(url, params=params, json=data, **kwargs)
            if res.status_code == 200 and res.json().get('errcode') == 0:
                pprint(f'发送成功, token: {self.token}, data: {data}')
                return res.json()

        except Exception as e:
            print(e)

        pprint(f'发送失败, token: {self.token}, data: {data}')
        return {}

    def send_text(
            self, content: str, mentioned_list: Optional[list] = None,
            mentioned_mobile_list: Optional[list] = None
    ):
        """发送文本消息"""

        data = {
            "msgtype": "text", "text": {
                "content": content,
                "mentioned_list": mentioned_list,
                "mentioned_mobile_list": mentioned_mobile_list
            }
        }
        self._send_request(data)

    def send_markdown(self, content: str):
        """发送markdown语法文本"""

        data = {"msgtype": "markdown", "markdown": {"content": content}}
        self._send_request(data=data)

    def send_image(self, path: Union[str, Path]):
        """发水图片"""

        if isinstance(path, str):
            path = Path(path)

        if not path.exists():
            return

        image_data = path.read_bytes()
        data = {
            "msgtype": "image", "image": {
                "base64": base64.b64encode(image_data).decode(),
                "md5": hashlib.md5(image_data).hexdigest()
            }
        }
        self._send_request(data=data)

    def send_image_text(self, articles: list):
        """
            发送图文
            @params:
                articles: [
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
        """

        data = {"msgtype": "news", "news": {"articles": articles}}
        self._send_request(data=data)

    def upload_file(self, path: Union[str, Path]):
        """上传文件"""

        params = {
            'key': self.token,
            'type': 'file'
        }
        files = {'file': open(path, 'rb')}

        json_data = self._send_request(params=params, path=self._upload, files=files)
        print(
            f'文件上传成功, created_at: {json_data.get("created_at", 0)}, '
            f'media_id: {json_data.get("media_id", "")}'
        )
        return json_data.get("media_id", '')

    def send_file(self, path: Union[str, Path]):
        """发送文件"""

        media_id = self.upload_file(path)
        if media_id:
            data = {"msgtype": "file", "file": {"media_id": media_id}}
            self._send_request(data=data)

    def send_text_card(
            self, source: Optional[dict] = None, main_title: Optional[dict] = None,
            emphasis_content: Optional[dict] = None, quote_area: Optional[dict] = None,
            sub_title_text: Optional[dict] = None, horizontal_content_list: Optional[Mapping[str, int]] = None,
            jump_list: Optional[Mapping[str, int]] = None, card_action: Optional[dict] = None
    ):
        """
            模版卡片类型
            @params:
                source 卡片来源样式信息，不需要来源样式可不填写
                    参数	                类型	            必须	        说明
                    icon_url	        String	        否	        来源图片的url
                    desc	            String	        否	        来源图片的描述，建议不超过13个字
                    desc_color	        Int	            否	        来源文字的颜色，目前支持：0(默认) 灰色，1 黑色，2 红色，3 绿色
                main_title 模版卡片的主要内容，包括一级标题和标题辅助信息
                    参数	                类型	            必须	        说明
                    title	            String	        否	        一级标题，建议不超过26个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写
                    desc	            String	        否	        标题辅助信息，建议不超过30个字
                emphasis_content 关键数据样式
                    参数	                类型	            必须	        说明
                    title	            String	        否	        关键数据样式的数据内容，建议不超过10个字
                    desc	            String	        否	        关键数据样式的数据描述内容，建议不超过15个字
                quote_area 用文献样式，建议不与关键数据共用
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        引用文献样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序
                    url	                String	        否	        点击跳转的url，quote_area.type是1时必填
                    appid	            String	        否	        点击跳转的小程序的appid，quote_area.type是2时必填
                    pagepath	        String	        否	        点击跳转的小程序的pagepath，quote_area.type是2时选填
                    title	            String	        否	        引用文献样式的标题
                    quote_text	        String	        否	        引用文献样式的引用文案
                sub_title_text  二级普通文本，建议不超过112个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写
                horizontal_content_list	二级标题+文本列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过6
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        链接类型，0或不填代表是普通文本，1 代表跳转url，2 代表下载附件，3 代表@员工
                    keyname	            String	        是	        二级标题，建议不超过5个字
                    value	            String	        否	        二级文本，如果horizontal_content_list.type是2，该字段代表文件名称（要包含文件类型），建议不超过26个字
                    url	                String	        否	        链接跳转的url，horizontal_content_list.type是1时必填
                    media_id	        String	        否	        附件的media_id，horizontal_content_list.type是2时必填
                    userid	            String	        否	        被@的成员的userid，horizontal_content_list.type是3时必填
                jump_list 跳转指引样式的列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过3
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        跳转链接类型，0或不填代表不是链接，1 代表跳转url，2 代表跳转小程序
                    title               String	        是	        跳转链接样式的文案内容，建议不超过13个字
                    url	                String	        否	        跳转链接的url，jump_list.type是1时必填
                    appid	            String	        否	        跳转链接的小程序的appid，jump_list.type是2时必填
                    pagepath	        String	        否	        跳转链接的小程序的pagepath，jump_list.type是2时选填
                card_action 整体卡片的点击跳转事件，text_notice模版卡片中该字段为必填项
                    参数	                类型	            必须	        说明
                    type	            Int	            是	        卡片跳转类型，1 代表跳转url，2 代表打开小程序。text_notice模版卡片中该字段取值范围为[1,2]
                    url	                String	        否	        跳转事件的url，card_action.type是1时必填
                    appid	            String	        否	        跳转事件的小程序的appid，card_action.type是2时必填
                    pagepath	        String	        否	        跳转事件的小程序的pagepath，card_action.type是2时选填
        """

        data = {
            "msgtype": "template_card",
            "template_card": {
                "card_type": "text_notice",
                "source": source,
                "main_title": main_title,
                "emphasis_content": emphasis_content,
                "quote_area": quote_area,
                "sub_title_text": sub_title_text,
                "horizontal_content_list": horizontal_content_list,
                "jump_list": jump_list,
                "card_action": card_action
            }
        }
        self._send_request(data=data)

    def send_image_card(
            self, source: Optional[dict] = None, main_title: Optional[dict] = None,
            card_image: Optional[dict] = None, image_text_area: Optional[dict] = None,
            quote_area: Optional[dict] = None, vertical_content_list: Optional[Mapping[str, int]] = None,
            horizontal_content_list: Optional[Mapping[str, int]] = None,
            jump_list: Optional[Mapping[str, int]] = None, card_action: Optional[dict] = None
    ):
        """
            图文展示模版卡片
                source 卡片来源样式信息，不需要来源样式可不填写
                    参数	                类型	            必须	        说明
                    icon_url	        String	        否	        来源图片的url
                    desc	            String	        否	        来源图片的描述，建议不超过13个字
                    desc_color	        Int	            否	        来源文字的颜色，目前支持：0(默认) 灰色，1 黑色，2 红色，3 绿色
                main_title 模版卡片的主要内容，包括一级标题和标题辅助信息
                    参数	                类型	            必须	        说明
                    title	            String	        否	        一级标题，建议不超过26个字。模版卡片主要内容的一级标题main_title.title和二级普通文本sub_title_text必须有一项填写
                    desc	            String	        否	        标题辅助信息，建议不超过30个字
                card_image 图片样式
                    参数	                类型	            必须	        说明
                    url	                String	        是	        图片的url
                    aspect_ratio	    Float	        否	        图片的宽高比，宽高比要小于2.25，大于1.3，不填该参数默认1.3
                image_text_area	左图右文样式
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        左图右文样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序
                    url	                String	        否	        点击跳转的url，image_text_area.type是1时必填
                    appid	            String	        否	        点击跳转的小程序的appid，必须是与当前应用关联的小程序，image_text_area.type是2时必填
                    pagepath	        String	        否	        点击跳转的小程序的pagepath，image_text_area.type是2时选填
                    title	            String	        否	        左图右文样式的标题
                    desc	            String	        否	        左图右文样式的描述
                    image_url	        String	        是	        左图右文样式的图片url
                quote_area 引用文献样式，建议不与关键数据共用
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        引用文献样式区域点击事件，0或不填代表没有点击事件，1 代表跳转url，2 代表跳转小程序
                    url	                String	        否	        点击跳转的url，quote_area.type是1时必填
                    appid	            String	        否	        点击跳转的小程序的appid，quote_area.type是2时必填
                    pagepath	        String	        否	        点击跳转的小程序的pagepath，quote_area.type是2时选填
                    title	            String	        否	        引用文献样式的标题
                    quote_text	        String	        否	        引用文献样式的引用文案
                vertical_content_list 卡片二级垂直内容，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过4
                    参数	                类型	            必须	        说明
                    title	            String	        是	        卡片二级标题，建议不超过26个字
                    desc	            String	        否	        二级普通文本，建议不超过112个字
                horizontal_content_list	二级标题+文本列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过6
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        模版卡片的二级标题信息内容支持的类型，1是url，2是文件附件
                    keyname	            String	        是	        二级标题，建议不超过5个字
                    value	            String	        否	        二级文本，如果horizontal_content_list.type是2，该字段代表文件名称（要包含文件类型），建议不超过26个字
                    url	                String	        否	        链接跳转的url，horizontal_content_list.type是1时必填
                    media_id	        String	        否	        附件的media_id，horizontal_content_list.type是2时必填
                jump_list 跳转指引样式的列表，该字段可为空数组，但有数据的话需确认对应字段是否必填，列表长度不超过3
                    参数	                类型	            必须	        说明
                    type	            Int	            否	        跳转链接类型，0或不填代表不是链接，1 代表跳转url，2 代表跳转小程序
                    title	            String	        是	        跳转链接样式的文案内容，建议不超过13个字
                    url	                String	        否	        跳转链接的url，jump_list.type是1时必填
                    appid	            String	        否	        跳转链接的小程序的appid，jump_list.type是2时必填
                    pagepath	        String	        否	        跳转链接的小程序的pagepath，jump_list.type是2时选填
                card_action 整体卡片的点击跳转事件，news_notice模版卡片中该字段为必填项
                    参数	                类型	            必须	        说明
                    type	            Int	            是	        卡片跳转类型，1 代表跳转url，2 代表打开小程序。news_notice模版卡片中该字段取值范围为[1,2]
                    url	                String	        否	        跳转事件的url，card_action.type是1时必填
                    appid	            String	        否	        跳转事件的小程序的appid，card_action.type是2时必填
                    pagepath	        String	        否	        跳转事件的小程序的pagepath，card_action.type是2时选填
        """

        data = {
            "msgtype": "template_card",
            "template_card": {
                "card_type": "news_notice",
                "source": source,
                "main_title": main_title,
                "card_image": card_image,
                "image_text_area": image_text_area,
                "quote_area": quote_area,
                "vertical_content_list": vertical_content_list,
                "horizontal_content_list": horizontal_content_list,
                "jump_list": jump_list,
                "card_action": card_action
            }
        }
        self._send_request(data=data)


if __name__ == '__main__':
    r = Robot()
    r.set_token(token='af20a3fd-adc2-4fe4-bb2a-66b89af011f9')
    # r.send_file('fund.csv')
