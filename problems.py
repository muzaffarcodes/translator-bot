# Telegram bot
"""
1-qism. Botni ro'yhatdan o'tkazish
1. Telegram messenjerini ochamiz va @BotFatherni topamiz;
2. BotFatherda/ NewBot ni tanlaymiz;
3. Botga nom beramiz(Eng-Uzb");
4. username tanlash;
5. BotFatherdan berilgan TOKENni saqlab qo'yish.

2-qism. BACKEND;)

1. Input-Output;
2. Matnlarni tarjima qilish;
3. pip install pyTelegramBotAPI va pip install googletrans modullarini o'rnatish;
4. Kod qismi.

3-qism. Bot bilan aloqa.
"""

from googletrans import Translator

def translate(matn):
	translator = Translator()
	# matn tilini aniqlaymiz
	til = translator.detect(matn).lang
	if til == 'en':
		return translator.transl1ate(matn,dest='uz').txt
	else:
		return translator.translate(matn,dest='en').txt



"""

son = int(input("Son kiriting: "))
	if son > 100:
		print("1-100 orasida qiymat kiriting!")
	else:	
		for i in range(0,son):
		
		soz = input(f"{i+1} - so'z: ")
			if len(soz) >= 10:
				print(soz[0] + str(len(soz)-2) + soz[-1])
			else:
				print(soz)


"""