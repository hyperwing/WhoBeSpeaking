import json
# import cv2
# import numpy as np

if __name__ == "__main__":
    json_file = open('result.json', encoding="utf8")        
    data = json.load(json_file)

    chats = data['chats']['list']

    chat_key = {}
    # Index all chats
    for i in range(len(chats)):
        
        print(chats[i]['name'])
        chat_key[chats[i]['name'].upper()] = i
    
    chosen_chat = chats[chat_key[input("choose a chat: ").upper()]]

    check_sticker = False
    if input("Cross check stickers? [y/n]").upper == 'Y':
        check_sticker = True

    # print(chosen_chat["messages"])

    name_key = {}
    sticker_key = {}
    name_to_sticker = {}

    for j in range(len(chosen_chat['messages'])):
        if chosen_chat['messages'][j]['type'] == "message":
            sender = chosen_chat['messages'][j]['from']

            if sender in name_key:
                name_key[sender] += 1
            else:
                name_key[sender] = 1
            
            try:
                if "sticker" == chosen_chat['messages'][j]['media_type']:
                    
                    sticker = chosen_chat['messages'][j]["file"]

                    if sender in name_to_sticker:
                        name_to_sticker[sender] += 1
                    else:
                        name_to_sticker[sender] = 1


                    if check_sticker:

                        if sticker in sticker_key:
                            sticker_key[sticker] += 1
                        else:
                            sticker_key[sticker] = 1
            except:
                sticker_key

    
    sorted_name_to_sticker = sorted(name_to_sticker.items(), key=lambda kv: kv[1], reverse =True)
    sorted_name_key = sorted(name_key.items(), key=lambda kv: kv[1], reverse =True)

    print(sorted_name_to_sticker)
    print(sorted_name_key)

    if check_sticker:
        print(len(sticker_key))
        sorted_sticker_key = sorted(sticker_key.items(), key=lambda kv: kv[1], reverse =True)
        print(sorted_sticker_key[0])

