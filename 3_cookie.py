import requests

session = requests.session()
data = {
    "loginName":"13859085384",
    "password":"s3125637Y"
}

url = "https://passport.17k.com/ck/user/login"
resp = session.post(url,data=data)
print(resp.text)