import requests

user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
headers={
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "eagleeye-pappname": "cuvx0xni1o@1a8e4117575f9ff",
    "eagleeye-sessionid": "4ekpnc1w8LwtRegpdzOO8nmd14ev",
    "eagleeye-traceid": "3cc1ee73159393802664510015f9ff",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XmlHttpRequest",
    "x-source": "lizard-desktop",
    "cookie": "_csrf=JL_MKZELueFTKIBTqGYF9it-; deviceId=cdfcdd2b-2f35-4a96-9513-7b468d1bd8c4; deviceIdGenerateTime=1593936721791; shimo_gatedlaunch=5; shimo_kong=5; shimo_svc_edit=4148; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; _bl_uid=y6kUXckq8Fpsn5rwFzj8ue3yvaz4; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593936739; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223503351%22%2C%22%24device_id%22%3A%221731e0838ab6e0-054e1a184f53df-153e6554-3686400-1731e0838ac6df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221731e0838ab6e0-054e1a184f53df-153e6554-3686400-1731e0838ac6df%22%7D; anonymousUser=-8156736335; shimo_sid=s%3A5SEerVXgiBPxhOafiCYDeNBVkFs7upcl.7K6nnpcU3wPav8VG7MX0X65CnJk7r5LsbcjKg2cacxY; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593937903"
}
url = "https://shimo.im/lizard-api/auth/password/login"

data = {
    "mobile": "+8618801409523",
    "password": "lvyz78961"
}
response = requests.post(url, data=data)

print(response.text,response.status_code)
