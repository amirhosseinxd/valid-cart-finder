import re 
from telethon.sync import TelegramClient,functions,events,types

pattern = "\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}"

prefixnum = {'603799' : "بانک ملی ایران", '589210' : "بانک سپه", '627648' : "بانک توسعه صادرات", '627961' : "بانک صنعت و معدن"
                 , '603770' : "بانک کشاورزی", '628023' : "بانک مسکن", '627760' : "پست بانک ایران", '502908' : "بانک توسعه تعاون"
                 , '627412' : "بانک اقتصاد نوین", '622106' : "بانک پارسیان", '502222' : "بانک پاسارگاد"
                 , '639599' : "بانک قوامین" , '627488' : "بانک کارآفرین", '622186' : "بانک سامان", '6339346' : "بانک سینا"
                 , '639607' : "بانک سرمایه", '502806' : "بانک شهر", '502938' : "بانک دی"
                 , '603769' : "بانک صادرات", '610433' : "بانک ملت", '585983' : "بانک تجارت"
                 , '589463' : "بانک رفاه", '627381' : "بانک انصار", '639370' : "بانک مهر اقتصاد"
                 , '507677' : "موسسه اعتباری نور", '628157' : "موسسه اعتباری توسعه", '505801' : "موسسه اعتباری کوثر"
                 , '606256' : "موسسه اعتباری ملل (عسکریه)", '606373' : "بانک قرض الحسنه مهرایرانیان"}

def card_check (user_input):
    num_of_cards=0
    matches = re.findall(pattern, user_input)
    for card in  matches:
     card = re.sub('[ -]', '', card)
     if int(card[0])==5 or int(card[0])==6:
         if card[0:6]  in prefixnum:
             sum = 0
             for i in range(16):
                 if (i + 1) % 2 == 0:
                     sum += int(card[i])
                 elif int(card[i]) * 2 > 9:
                     sum += (int(card[i]) * 2 - 9)
                 else:
                     sum += int(card[i]) * 2

             if sum % 10 == 0:
                 num_of_cards+=1
                 return card
     if num_of_cards==0 : 
         return 0        


def bank_check (card_num):
    return (prefixnum[card_num[0:6]])
             


