import vk_api
import random
import time
token = "e397f1c88f5e05b872f93480486aa02ea36c7fd28839790e49f0b18e977b67f679c77ce2bf0dbc1d560f2"


vk = vk_api.VkApi(token=token)


vk._auth_token()

dz = "дз нет"

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "скинь фотку друга":
                vk.method("messages.send", {"peer_id": id, "message": "https://sun9-40.userapi.com/c856028/v856028478/1912c5/PA_RUacjm_g.jpg", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как дела?":
                vk.method("messages.send", {"peer_id": id, "message": "все хорошо!)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "посоветуй песни":
                vk.method("messages.send", {"peer_id": id, "message": "https://vk.com/audios51506389?q=all%20stars", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
