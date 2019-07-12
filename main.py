from bs4 import BeautifulSoup
import collections


if __name__ == "__main__":
    participantMap ={}
    
    with open("messages.html", "r") as f:
        
        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        soup =  soup.findChild("body")

        soup = soup.findChild("div", {"class": "page_body chat_page"})
        soup = soup.findChild("div", {"class": "history"})
        children = soup.findChildren("div", {"class":"message default clearfix"})
        
        for message in children:
        
            mes = message.findChild("div", {"class":"body"})
            name = mes.findChild("div", {"class":"from_name"}).text
            name =name.strip()

            if name not in participantMap:
                participantMap[name] = 1 
            else:
                participantMap[name] = participantMap[name]+1

        # for key, value in participantMap.items() :
        #     print (key, value)

        sorted_x = sorted(participantMap.items(), key=lambda kv: kv[1], reverse =True)

        for i in range(0, len(sorted_x)):
            print(str(sorted_x[i][0])+ ": " + str(sorted_x[i][1]))

        print("Top poster : " +str(sorted_x[0][0]))
        print("Least poster: " + str(sorted_x[len(sorted_x)-1][0]))


