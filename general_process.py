# -*- coding: UTF-8 -*-
"""
by Mark
"""


def produce():
    for num in range(0, 100):
        cookie = u"oneone"
        uid = u"first_blood"
        user_angent = u"Macintosh Chrome Safari"
        ip = u"1.1.1.1"
        video_id = u"898923"
        topic = u"苹果发布会"
        order_id = u"0"
        log_type = u"1"

        final = cookie + u"&" + uid + u"&" + user_angent + u"&" + ip + u"&" \
                + video_id + u"&" + topic + u"&" + order_id + u"&" + log_type

        print final


if __name__ == '__main__':
    produce()
