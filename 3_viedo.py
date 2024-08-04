
import requests
url = "https://www.pearvideo.com/video_1795651"

contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6131557061382278"
headers={

"referer": url
}
resp = requests.get(videoStatusUrl,headers=headers)
#print(resp.text)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
#https://video.pearvideo.com/mp4/short/20240802/cont-1795651-16034203-hd.mp4
#https://video.pearvideo.com/mp4/short/20240802/1722637227014-16034203-hd.mp4
srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")
#print(srcUrl)

with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)