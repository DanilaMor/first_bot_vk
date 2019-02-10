import random
import vk_api

from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType

f = open("token.txt")
token = f.read()
vk = vk_api.VkApi(token=token)


def write_msg(user_id, message):
    # vk.method('messages.getConversationsById', {'user_id': user_id, 'message': message})
    vk_new = vk.get_api()
    vk_new.messages.send(user_id=user_id, message=message, random_id=random.randint(0, 1000000000))


longpoll = VkLongPoll(vk)

print("Server started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if (event.to_me):
            print("New message")
            print(f'For me by: {event.user_id}', end="")
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            # request = event.text
            # if str(request) == "привет":
            #     write_msg(event.user_id, "Хай")
            # elif request == "пока":
            #     write_msg(event.user_id, "Ну вот и поговорили ((")
            # else:
            #     write_msg(event.user_id, "Попробуй еще разок")

            print("Text: ", event.text)
