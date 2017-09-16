import requests
import json

username = 'imgflip_hubot'
password = 'imgflip_hubot'

def main():
    # r = requests.get('https://www.google.com')
    # print(r.text)

    # get_memes
    # r = requests.get('https://api.imgflip.com/get_memes')
    # print(r.status_code)
    # print(r.headers['content-type'])
    # response_json = r.json()
    # memes = response_json["data"]["memes"]
    # for i in range(0, len(memes)):
    #     url = memes[i]["url"]
    #     meme_id = memes[i]["id"]
    #     print(url, meme_id)

    # post_memes
    params = {
        "template_id": 347390,
        "username": username,
        "password": password,
        "text0" : "Runtime errors",
        "text1": "Runtime errors everywhere"
    }
    r = requests.post('https://api.imgflip.com/caption_image', data = params)
    if r.status_code == 200:
        response_json = r.json()
        # success
        print(r.json())

    # rando




if __name__ == "__main__":
    main()
