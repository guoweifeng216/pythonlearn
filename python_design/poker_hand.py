import card
def sort_list(list1):
    list1=sorted(list1)
    print "***********"
    for i in list1:
        print i


def main():
    card_list = {}
    list1=[]
    for i in range(0,5):
        rand_card=card.Card()
        random_value=rand_card.selectAtRandom()
        card_list[rand_card.getRank()]=rand_card.getSuit()
    # print card_list
    # card_list=sorted(card_list.items(),key=lambda item:item[0])
    print card_list
    for value in card_list:
        print value
        list1.append(int(value))
    print list1
    sort_list(list1)

main()
