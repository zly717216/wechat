import json

import requests
from loguru import logger


class WechatRobot:

    def __init__(self, robot_name='韭韭八十一'):

        headers = {
            'cookie': 'wwrtx.c_gdpr=0; tvfe_boss_uuid=2914d920a12bde8b; pgv_pvid=2999943445; RK=CoCMGNhLSw; ptcz=16e4cb9887c1ff219be9f3fe3ed16803a11a1c7176110f809e13d9bc7e94cf23; o_cookie=1485843401; pac_uid=1_1485843401; iip=0; Hm_lvt_bdfb0d7298c0c5a5a2475c291ac7aca2=1651718300; wwrtx.ref=direct; wwrtx.refid=31677615181450210; wwrtx.ltype=1; wwrtx.vid=1688854781353119; wxpay.corpid=1970325693982653; wxpay.vid=1688854781353119; wwrtx.cs_ind=; wwrtx.logined=true; wwrtx.vst2=AQAA4VOW_XC_ajxHX_q7TBKRhl3LdoOi1wK7M37pxcwqtIBV9Pa73Yhc5yW0nR7hqBu14r4Ny-YEl7LrytCJTsS1Oio78-Lbq5nBxWNui44pgJERotQgVnW4hUVWhXNq4mcWMTa2RU1irvn2VF2siPG06hsAdfggk9UpYlLapx8LzbKsAV_RqWjE9gFyNrgXVHdVYt4sSzNFpKoFkcCj5YAhhnsbc1rwsoTFsAHLMo9AalCsMVFpx_vnhcGpY_MaZc7ahOfI4S42YCMa1HbMrbNCqA; pgv_info=ssid=s5217101280; vversion_name=8.2.95; video_omgid=818bc122e1ed9479; wwrtx.i18n_lan=zh; wwopen.open.sid=wfBcfYRFSiXvFwIBXX7TQxHEs8jU_BShRTH1FsI_IHGQ; wedrive_uin=1688854781353119; xm_disk_vid=1688854781353119; xm_disk_corp_id=1970325693982653; wedrive_sid=AZ9rRQDcZFMGUXdCACVzbwAA; wedrive_sids=1688854781353119&AZ9rRQDcZFMGUXdCACVzbwAA; wedrive_skey=1688854781353119&7f0553932dff0eafde5e6cd8c403f722; wedrive_ticket=1688854781353119&CAESIH_Wgq8q2TbAqxfSrp24eAAHUBU98EhyrzvtqsM6Wpty; wwrtx.d2st=a6258218; wwrtx.sid=Ng3gzXdv0ZgjHN2gusmRaYtus3blD1otuus2G8GsoBDQbsFPnIc3q7cydBqoDwlh; wwrtx.vst=p0NQwHqkmJm-MUmQ2r3JsA4WMc2mnFEci2adD2MxFuy8gfIA1Jg--lHxWQR4eDelTRDQ7IjNDjM4vlhcXOderfnHrBvaqkiK8U2s6fDqzvst9vT5llan53DSPgqA-AjJPaLAC67MZDRQGnQyIziigexeSDJdN865DsKW3hh3YGVQxpdhn9HPeGsUvF58eG9a1dVrZWIy8pG_RtLoZYyOtS7ZLUggTJNfSVH6efwx70UmxXKGqj91SemHuqWZJOykFX6zpryjnd79lV-96jbZsw',
            'referer': 'https://work.weixin.qq.com/wework_admin/frame',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        session = requests.session()
        session.headers = headers

        self.session = session

        # 获取机器人的ID
        for i in self.get_robot_id():
            if i['name'] == robot_name:
                self.robot_id = i['app_id']
                break
            else:
                self.robot_id = ''

    def get_robot_id(self):
        """获取机器人的ID"""

        url = 'https://work.weixin.qq.com/wework_admin/getCorpApplication'
        params = {
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'timeZoneInfo[zone_offset]': '-8',
            'random': '0.8127443526319849',
        }
        data = {
            'app_type': '0',
            '_d2st': 'a3612162'
        }

        res = self.session.post(url, params=params, data=data)

        if res.status_code == 200:

            data = res.json()['data']
            open_app_list = [{
                'app_id': i['app_id'], 'name': i['name'], 'app_open_id': i['app_open_id'],
                'create_time': i['create_time'], 'update_time': i['update_time']
            } for i in data['openapi_app']]

            return open_app_list
        else:
            logger.warning(f"用户列表获取失败，原因：状态码错误，状态码为：{res.status_code}")

        return []

    def get_user_list(self):
        """获取用户列表"""

        url = 'https://work.weixin.qq.com/wework_admin/contacts/member/cache'
        params = {
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'timeZoneInfo[zone_offset]': '-8',
            'random': '0.8127443526319849',
        }
        data = {
            '_d2st': 'a3612162'
        }

        res = self.session.post(url, params=params, data=data)

        if res.status_code == 200:

            data = res.json()['data']
            user_list = [{
                'user_id': i['vid'], 'username': i['name'], 'pinyin': i['pinyin'],
                'py': i['py'], 'phone': i['mobile'], 'email': i['email'],
                'country_code': i['country_code'], 'acctid': i['acctid'],
                'wx_id_hash': i['wx_id_hash'], 'party_ids': i['party_ids'],
            } for i in data['mems']]

            return user_list
        else:
            logger.warning(f"用户列表获取失败，原因：状态码错误，状态码为：{res.status_code}")

    def get_user_id(self, usernames: list) -> list:
        """通过用户名找用户ID"""

        user_list = self.get_user_list()

        return [
            {'username': user['username'], 'user_id': user['user_id']}
            for user in user_list for name in usernames if name == user['username']
        ]

    def send_msg(self, msg: str, usernames: list):
        """
            发送消息
            @params:
                msg: 消息字符串
                usernames: 发送对象列表
            @return: msgid -> {}
        """

        user_list = self.get_user_id(usernames)

        url = 'https://work.weixin.qq.com/wework_admin/message/sendmsg'
        params = {
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'timeZoneInfo[zone_offset]': '-8',
            'random': '0.9229502844544748',
        }
        data = {
            'groupCorpWhite': '',
            'msgTypeStr': 'text',
            'appid': self.robot_id,
            'encrypt': '0',
            'textMsg[content]': msg,
            'oper': 'Send',
            'hasNoShareGroup': 'true',
            'toallflag': '0',
            'msgtype': '1',
            '_d2st': 'a3612162',
        }

        for index, user in enumerate(user_list):
            data.update({
                f'range_v[{index}][userid]': user['user_id'],
                f'range_v[{index}][username]': user['username'],
            })

        res = self.session.post(url, params=params, data=data)

        if res.status_code == 200:

            json_data = res.json()

            if json_data.get('data'):
                data = json_data.get('data')
                logger.debug(f"消息发送成功，msgid：{data['msgid']}，g_msgid：{data['g_msgid']}")
                return data
            else:
                result = json_data.get('result')
                logger.warning(f"消息发送失败，原因：{result['humanMessage']}，错误码为：{result['errCode']}")
        else:
            logger.warning(f"消息发送失败，原因：状态码错误，状态码为：{res.status_code}")

    def msg_list(self):

        url = 'https://work.weixin.qq.com/wework_admin/message/listByApp'
        params = {
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'timeZoneInfo[zone_offset]': '-8',
            'random': '0.047788876521329016',
            'limit': '20',
            'start': '0',
            'search_keyword': '',
            'sort_field': '3',
            'last_key': '',
            'listtype': '0',
            '_d2st': 'a3612162'
        }


if __name__ == '__main__':
    # w = wechat()
    # w.send_msg(msg='我就试最后一下啦啦啦', usernames=['张李源', '蒋玮', '小豆子'])
    # send_msg('大家好！我是韭韭八十一！')
    isQr()