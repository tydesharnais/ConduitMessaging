import sqlite3
import time
import sys
import os
import netifaces as ni
import random
import smtplib
import config
import art
from colorama import Fore, Back, Style, init
from core.Loading import bunnyloader, backslash_symbol
#CONSTANTS
init(autoreset=True)
Logged_in = False
current_user = ''



#When signing up, you give the computer an IPADDR. Let's figure out a way to check if
#they are the same and if they aren't what to do/if they are, to continue
#IP_compare()


backslash_symbol(2)
print('Welcome to the barebones system for Conduit Messaging..')
print('--------------------------------------------------------------------------------')
print('Cause, honestly... ?')
print('Attepting to contact system IP...')
print('')

#IP ADDRESS SEARCH(Error Handling)
def main():
	print('Starting up program...')
	time.sleep(2)
	bunnyloader(3)
	print(art.menu_top)
	try: #ValueError
		ni.ifaddresses('eth0')
		ipaddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
		print(f'IP Address found through eth0: {ipaddr}')

	except ValueError as e:
		print('ValueError: IPv4 value not found. Trying En0: {}'.format(str(e)))
		time.sleep(4)
		try:
			ni.ifaddresses('en0')
			ipaddr = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
			print(f'IP Address found through en0: {ipaddr}')
			time.sleep(5)
		except ValueError as e:
			print('ValueError: IPv4 value not found. {}'.format(str(e)))
			time.sleep(2)
			print('Exiting..')
			time.sleep(4)
			sys.exit()

	def reset_pass():
		while True:
			username = input('Enter your Username: ')
			with sqlite3.connect('waldo.db') as db:
				cursor = db.cursor()
				find_user = ("SELECT * FROM user WHERE username = ?")
				cursor.execute(find_user, [(username)])
				results = cursor.fetchall()

				if results:
					for i in results:
						print('Welcome '+i[2])
						print('Recovery Email address: ' +i[5])
						email = i[5]
						r = random.randrange(100000, 999999)
						def send_email(subject, msg, email):
						    try:
						        server = smtplib.SMTP('smtp.gmail.com:587')
						        server.ehlo()
						        server.starttls()
						        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
						        message = 'Subject: {}\n\n{}'.format(subject, msg)
						        server.sendmail(config.EMAIL_ADDRESS, email, message)
						        server.quit()
						        print("Success: Email sent!")
						    except:
						        print("Email failed to send.")
						subject = "Your Recovery Password from Waldo"
						msg = 'Your Recorvery Password is {} dont share this with anyone. You have 5 minutes to change your password. Sincerly the BackS/ash team'.format(r)
						send_email(subject, msg, email)
						time.sleep(5)
						conf = int(input("Please enter the 6-digit confirmation code to change your password (You only get one chance at this.: "))
						if conf == r:
							np = input('Please enter your new password: ')
							np1 = input('Please reenter your new password: ')
							while np != np1:
								print("Your password didn't match, please try again")
								np = input('Please enter your password: ')
								np1 = input('Please reenter your password: ')
							new_pass = ("UPDATE user SET password = ? WHERE username = ?")
							try:
								cursor.execute(new_pass, [(np), (username)])
								db.commit()
								print('Successful')
								time.sleep(5)
							except:
								print('Error Occured.')

							finally:
								current_user = 'N/A'
								Logged_in = False
								menu(current_user, Logged_in)

						else:
							print('Incorrect Confirmation Code. Shutting down.')
							time.sleep(5)
							sys.exit()

				else:
					print(f'The username {username} was not found.')
					time.sleep(5)
					current_user = 'N/A'
					Logged_in = False
					menu(current_user,Logged_in)




	def login(Logged_in):
		if Logged_in == True:
			print('Already logged in.')
			time.sleep(3)
			os.system('clear')


		else:
			flags = 0
			while (flags != 4):
				print(f'Number of Login Attempts Made: {flags}')
				username = input('Username: ')
				password = input('Password: ')
				with sqlite3.connect('waldo.db') as db:
					cursor = db.cursor()
					find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
					cursor.execute(find_user, [(username),(password)])
					results = cursor.fetchall()

					if results:
						for i in results:
							print('Welcome '+i[2])
							print('Checking current computers signature..')
							ip_user = ("SELECT * FROM user WHERE ipaddr = ?")
							cursor.execute(ip_user, [(ipaddr)])
							ip_results = cursor.fetchall()
							time.sleep(3)
							if ip_results:
								print('Identity confirmed.')
								Logged_in = True
								current_user = i[2] + ipaddr
								print(current_user)
								time.sleep(4)
								menu(current_user,Logged_in)
							else:
								print('This device is using a different IP address than when signed up.')
								time.sleep(4)

					else:
						print('Username and Password not recognized.. This Log attempt has been recorded')
						flags += 1
						time.sleep(3)
						os.system('clear')
						if flags == 3:
							choice = input('Would you like to send a temp password to your email address? (Y/N)')
							if choice == 'Y' or 'y':
								reset_pass()
							elif choice == 'N' or 'n':
								#For now
								sys.exit()
							else:
								print('Option not recognized. Returning to main menu')
								#menu()



						if flags == 4:
							print('Login Attempts exceeded. Server and Administrator have been notified.')
							time.sleep(5)
							sys.exit()


	def newUser():
		found = 0
		while found == 0:
			username = input('Please Enter a Username: ')
			with sqlite3.connect('waldo.db') as db:
				cursor = db.cursor()
			findUser = ('SELECT * FROM user WHERE username = ?')
			cursor.execute(findUser, ([username]))

			if cursor.fetchall():
				print('Username Taken. Please try again')
			else:
				found = 1
		firstname = input('Enter your first name: ')
		surname = input('Enter your last name: ')
		email = input('Enter your email address: ')
		password = input('Please enter your password: ')
		password1 = input('Please reenter your password: ')
		while password != password1:
			print("Your password didn't match, please try again")
			password = input('Please enter your password: ')
			password1 = input('Please reenter your password: ')
		insertdata = """
		INSERT INTO user(username,firstname,surname,password,email,ipaddr)
		VALUES(?, ?, ?, ?, ?, ?)"""
		cursor.execute(insertdata,([(username),(firstname),(surname),(password),(email),(ipaddr)]))
		db.commit()
		print('User Added Successfully')
		time.sleep(1)
		print(f'Setting current user: {username}')
		time.sleep(4)
		current_user = username + ipaddr
		Logged_in = True
		time.sleep(5)
		menu(current_user, Logged_in)

	def menu(current_user, Logged_in):
		os.system('clear')
		while True:
			print(art.menu_top)
			if Logged_in == True:
				print(f'Currently logged in as {current_user}')
			else:
				print('Currently not logged in.')
			print(f'Your Current IP Address:{ipaddr}')
			print('Welcome to my Database Masterpiece.')
			menu = ("""
			1. Create New User
			2. Login to System
			3. Connect to a Chatroom
			4. Exit System\n >""")

			userChoice = input(menu)

			if userChoice == "1":
				newUser()

			elif userChoice == "2":
				login(Logged_in)

			elif userChoice == "3":
				chatroom()

			elif userChoice == "4":
				print('Goodbye!')
				sys.exit()
			else:
				print('Command not recognized: ')
				time.sleep(3)

	menu(current_user,Logged_in)



if __name__ == "__main__":
	main()
