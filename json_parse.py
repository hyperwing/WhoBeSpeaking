import json
from datetime import datetime
import statistics
# import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    json_file = open('result.json', encoding="utf8")        
    data = json.load(json_file)

    bot_list = ["IFTTT","WhosInBot", "Channel Like Bot", "PollBot", None]


    chats = data['chats']['list']

    chat_key = {}
    # Index all chats
    for i in range(len(chats)):
        
        print(chats[i]['name'])
        chat_key[chats[i]['name'].upper()] = i
    
    chosen_chat = chats[chat_key[input("choose a chat: ").upper()]]

    check_sticker = False
    # if input("Cross check stickers? [y/n]").upper == 'Y':
    #     check_sticker = True

    # print(chosen_chat["messages"])

    name_key = {}
    link_key = {}
    sticker_key = {}
    name_to_sticker = {}
    at_key = {}
    atted_key = {}
    time_key = {}

    for j in range(len(chosen_chat['messages'])):
        if chosen_chat['messages'][j]['type'] == "message":
            sender = chosen_chat['messages'][j]['from']

            if sender in name_key:
                name_key[sender] += 1
            else:
                name_key[sender] = 1
                time_key[sender] = []

            full_date = datetime.strptime(chosen_chat["messages"][j]["date"], "%Y-%m-%dT%H:%M:%S")

            time_key[sender].append(int(str(full_date.hour) +str(full_date.minute)) )

            # Media checks
            try:
                if "sticker" == chosen_chat['messages'][j]['media_type']:
                    
                    sticker = chosen_chat['messages'][j]["file"]

                    if sender in name_to_sticker:
                        name_to_sticker[sender] += 1
                    else:
                        name_to_sticker[sender] = 1

                    # TODO: Implement opencv to check similar stickers
                    if check_sticker:

                        # a = cv2.imread("sample1.png")
                        # b = cv2.imread("sample2.png")
                        # difference = cv2.subtract(a, b)    
                        # result = not np.any(difference)
                        # if result is True:
                        #     print "Pictures are the same"
                        # else:
                        #     cv2.imwrite("ed.jpg", difference )
                        #     print "Pictures are different, the difference is stored as ed.jpg"


                        if sticker in sticker_key:
                            sticker_key[sticker] += 1
                        else:
                            sticker_key[sticker] = 1
            except:
                sticker_key

            # Link checks
            try:
                # print(chosen_chat["messages"][j]["text"][0]["type"])
                if chosen_chat["messages"][j]["text"][0]["type"] == "link":
                    if sender in link_key:
                        link_key[sender] +=1
                    else:
                        link_key[sender] = 1

                if chosen_chat["messages"][j]["text"][0]["type"] == "mention_name":
                    if sender in at_key:
                        at_key[sender] +=1
                    else:
                        at_key[sender] = 1            
                    

                    atted = chosen_chat["messages"][j]["text"][0]['text']
                    if atted in atted_key:
                        atted_key[atted] +=1
                    else:
                        atted_key[atted] = 1            

            except:
                link_key
    
    for x in bot_list:
        try:
            del time_key[x]
        except:
            bot_list
        try:
            del name_to_sticker[x]
        except:
            bot_list
        try:
            del at_key[x]
        except:
            bot_list
        try:
            del name_key[x]
        except:
            bot_list
        try:
            del link_key[x]
        except:
            bot_list
        try:
            del atted_key[x]
        except:
            bot_list

    sorted_name_to_sticker = sorted(name_to_sticker.items(), key=lambda kv: kv[1], reverse =True)
    sorted_name_key = sorted(name_key.items(), key=lambda kv: kv[1], reverse =True)
    sorted_link_key = sorted(link_key.items(), key=lambda kv: kv[1], reverse =True)
    sorted_at_key = sorted(at_key.items(), key=lambda kv: kv[1], reverse =True)
    sorted_atted_key = sorted(atted_key.items(), key=lambda kv: kv[1], reverse =True)
    sorted_time_key = sorted(time_key.items(), key=lambda kv: kv[1], reverse =False)

    # timing = np.array(time_key.values)
    legend = []
    # n_bins =22
    for person in sorted_time_key:
        print(person[0])

        plt.hist(person[1], histtype="step", fill=False)

        legend.append(person[0])

        # print(str(person[0]) + ": ")
        # print (statistics.mean(sorted_time_key[person[0]]))    

    plt.legend(legend, loc=2)
    plt.title("When are people posting?")
    plt.xlabel("Time of the day")
    plt.ylabel("Number of Posts")
    plt.show()


    print("\nsticker spammers: ")
    print(sorted_name_to_sticker)

    plt.title("Who's sending stickers?")
    plt.pie([float(v) for v in name_to_sticker.values()], labels=name_to_sticker.keys(), autopct='%.2f%%' )
    plt.show()

    print("\nlink spammer: ")
    print(sorted_link_key)
    plt.title("Who's sending links?")
    plt.pie([float(v) for v in link_key.values()], labels=link_key.keys(), autopct='%.2f%%' )
    plt.show()

    print("\nMost calls to another:")
    print(sorted_at_key)
    plt.title("Most @s to another user")
    plt.pie([float(v) for v in at_key.values()], labels=at_key.keys(), autopct='%.2f%%' )
    plt.show()

    print("\nMost Atted: ")
    print(sorted_atted_key)
    plt.title("Dont @ me bro")
    plt.pie([float(v) for v in atted_key.values()], labels=atted_key.keys(), autopct='%.2f%%' )
    plt.show()

    print("\nmessage totals:")
    print(sorted_name_key)
    plt.title("Total Messages")
    plt.pie([float(v) for v in name_key.values()], labels=name_key.keys(), autopct='%.2f%%' )
    plt.show()

    if check_sticker:
        print(len(sticker_key))
        sorted_sticker_key = sorted(sticker_key.items(), key=lambda kv: kv[1], reverse =True)
        print(sorted_sticker_key[0])

