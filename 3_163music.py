
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
"csrf_token": "",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_AL_3_74416913",
"threadId": "R_AL_3_74416913"
}

f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "B8NR6y0FJCCx7Gio"
def get_encSecKey():
    return "65c4b3bddc93e72a91c170487ee37d06d749212fb4956e6f7028e7aa3d99cf775d7db94ecfbc9c36dad5f77122a3b22313420444ed26365d92af73fac74487697dbeca4acc22f775b05a667369baff6ddde2463d12419679fd2128debbec5bb3335105f16b6d4cc0a07b2e71d841c6064cf2efb8573a70cc1f29fd1da05ec283"

"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {d:数据 , e:010001,f:很长
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }

"""

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad)*pad
    return data

def enc_params(data,key):
    iv = "0102030405060708"
    data = to_16(data)
   
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs),"utf-8")


resp = requests.post(url,data={
        "params":get_params(json.dumps(data)),
        "encSecKey":get_encSecKey()
    })
print(resp.text)