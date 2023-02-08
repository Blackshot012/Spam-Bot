import pyautogui,time
from colorama import Fore, Back, Style


textone={"""
	
 __                           ___       _    
/ _\_ __   __ _ _ __ ___     / __\ ___ | |_  
\ \| '_ \ / _` | '_ ` _ \   /__\/// _ \| __| 
_\ \ |_) | (_| | | | | | | / \/  \ (_) | |_  
\__/ .__/ \__,_|_| |_| |_| \_____/\___/ \__| 
   |_|                                       

"""}

print(Fore.MAGENTA+textone)

time.sleep(5)
print(Fore.MAGENTA+"started....")
inputs=input(Fore.GREEN+"Enter your spam number =>")
time.sleep(5)
fosh={
	'fosh'
}
for i in range(int(inputs)):
	try:
		for word in fosh:
			pyautogui.typewrite(word)
			pyautogui.press('enter')

	except:
		print("Eror")