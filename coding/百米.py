# -*- coding:utf-8 -*-
import re
import requests

if __name__ == '__main__':
    session = requests.session()
    res2 = session.post("http://ctf5.shiyanbar.com/jia/index.php?action=check_pass", data={'pass_key': eval(
        re.findall("<div name='my_expr'>(.*?)</div>", session.get("http://ctf5.shiyanbar.com/jia/index.php").text)[
            0].replace("x", "*"))})
    print res2.text
