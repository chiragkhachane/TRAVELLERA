from nltk.chat.util import Chat, reflections

from Railway import rail
from Airway import air
from Roadways import road



if __name__ == "__main__":

    print("Hey there this is TRAVELLERA!")
    print(" Welcome to Travel World!!!")
    print("We believe in our customers :)")
    print(" ")

    sentence = input("Select 1) Railway 2) Roadway 3) Airways :").lower()

    try:
        while True:
            if sentence == 'railway':
                print("**** Welcome to TRAVELLERA RAILWAYS****")
                chat_rail = Chat(rail, reflections)
                chat_rail.converse()

            if sentence == 'airway':
                print("**** Welcome to TRAVELLERA AIRWAYS ****")
                chat_air = Chat(air, reflections)
                chat_air.converse()

            if sentence == 'roadway':
                print("**** Welcome to TRAVELLERA RAILWAYS****")
                chat_road = Chat(road, reflections)
                chat_road.converse()

            elif sentence == 'quit':
                break
            sentence = input('Select 1) Railway 2) Roadway 3) Airways').lower()

    except:
        print("Restarting TRAVELLERA...")

        print("Hey there this is TRAVELLERA!")
        print(" Welcome to Travel World!!!")
        print("We believe in our customers :)")
        print(" ")

        while True:
            if sentence == 'railway':
                print("**** Welcome to TRAVELLERA RAILWAYS****")
                chat_rail = Chat(rail, reflections)
                chat_rail.converse()
            if sentence == 'airway':
                print("**** Welcome to TRAVELLERA AIRWAYS ****")
                chat_air = Chat(air, reflections)
                chat_air.converse()
            if sentence == 'roadway':
                print("**** Welcome to TRAVELLERA RAILWAYS****")
                chat_road = Chat(road, reflections)
                chat_road.converse()
            elif sentence == 'quit':
                break
            sentence = input('Select 1) Railway 2) Roadway 3) Airways').lower()

    finally:
        print("End of Session")