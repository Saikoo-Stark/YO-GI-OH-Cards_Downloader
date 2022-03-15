'''

Developed By : Saikoo Stark

YO-GI OH Cards_Downloader

must run requirements.py first

'''


######### import all needed libraries #########
import requests 
from termcolor import colored
from pyfiglet import figlet_format as ff
import concurrent.futures
from itertools import zip_longest
import time 
import os
import sys



######### make typing effect in code #########
def type( text , color = "white" , t = 0.001):
	text = colored( text , color)
	for char in text :
		print(char , end = "" , flush = True)
		time.sleep(t)
		
		
		
def send_request(type):		
	link = "https://db.ygoprodeck.com/api/v7/cardinfo.php?" # cards api link
	head = {
  "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Safari/537.36"
	}

	param = { "type" : type} # parameters value
	names = []
	links = []
	type_card = []
	with requests.get(link , headers = head , params = param) as res: # send a request to api link to get all cards info
		lst_n = res.json()["data"]

	for items in lst_n:
		
		try:
			names.append(f'{items["name"]}_[LEVEL {items["level"]},ATK {items["atk"]},DEF {items["def"]}]') # getting cards name
		except:
			names.append(f'{items["name"]}')
			
		links.append(items["card_images"][0]["image_url"]) # getting cards image link
		
		type_card.append(type) # getting cards type

	return zip_longest(names , links , type_card) # return iterator containing name , image_link and type of every card



def downloader(information):  #download every card in device 
	
	name , link , type_card = information
	
	new_name = []
	for i in range(len(name)):
		if name[i] == "/" or name[i] == "\\":
			new_name.append(" ")
		else:
			new_name.append(name[i])
	name = "".join(new_name)
	
	print(name)
	
	resp = requests.get(link).content  # send request to get binary code of card image
	
	with open(fr"{type_card}/{name}.jpg" , "wb") as wr:  #download card in script same directory
		wr.write(resp)



def run():
	
	list_cards = [		#list of cards options
"Effect Monster",
"Flip Effect Monster",
"Flip Tuner Effect Monster",
"Gemini Monster",
"Normal Monster",
"Normal Tuner Monster",
"Pendulum Effect Monster",
"Pendulum Flip Effect Monster",
"Pendulum Normal Monster",
"Pendulum Tuner Effect Monster",
"Ritual Effect Monster",
"Ritual Monster",
"Skill Card",
"Spell Card",
"Spirit Monster",
"Toon Monster",
"Trap Card",
"Tuner Monster",
"Union Effect Monster",
"Fusion Monster",
"Link Monster",
"Pendulum Effect Fusion Monster",
"Synchro Monster",
"Synchro Pendulum Effect Monster",
"Synchro Tuner Monster",
"XYZ Monster",
"XYZ Pendulum Effect Monster"
	]
	
	type("Choose one of the following types >>\n" , "cyan")
	for index , item in enumerate(list_cards):
		type(f"[ {index +1} ] {item}\n" , "yellow")
	type("Choice : " , "green")
	try:
		typed = int(input())
	
		type_card = list_cards[typed-1]
	except:
		sys.exit()
	info = send_request(type_card)
	
	os.system(f"mkdir \'{type_card}\'  ")  #make a directory containing cards type choosen above
	
	with concurrent.futures.ThreadPoolExecutor() as ex :  #make threading to speed up of downloading process
		c = ex.map(downloader ,  info)
		

###############  START  ###############

type(ff("   BY :    saikoo   stark") , "magenta" , 0.003)
intro = " Welcome To  YO-GI OH Cards_Downloader Script "
type((intro.center(80 , "-")) , "yellow" , 0.01)
print("\n\n")

run()
	
