# creating a list of users, their PINs and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existence of the entered username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
			break
		elif user == users[1]:
			n = 1
			break
		else:
			n = 2
			break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while True:
	pin = input('PLEASE ENTER PIN: ')
	if user == 'user1':
			if pin == pins[0]:
				print('-------------------------')
				print('*************************')
				print('LOGIN SUCCESSFUL, CONTINUE')
				print('*************************')
				print('-------------------------')
				print()
				print(str.capitalize(users[n]), 'welcome to ATM')
				print('----------ATM SYSTEM-----------')
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				if count!=3:
					continue

	if user == 'user2':
			if pin == pins[1]:
				print('-------------------------')
				print('*************************')
				print('LOGIN SUCCESSFUL, CONTINUE')
				print('*************************')
				print('-------------------------')
				print()
				print(str.capitalize(users[n]), 'welcome to ATM')
				print('----------ATM SYSTEM-----------')
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				if count != 3:
					continue

	if user == 'user3':
			if pin == pins[2]:
				print('-------------------------')
				print('*************************')
				print('LOGIN SUCCESSFUL, CONTINUE')
				print('*************************')
				print('-------------------------')
				print()
				print(str.capitalize(users[n]), 'welcome to ATM')
				print('----------ATM SYSTEM-----------')
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				if count!=3:
					continue

	if count == 3:
		print('-----------------------------------')
		print('***********************************')
		print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
		print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
		print('***********************************')
		print('-----------------------------------')
		exit()

# Main menu
while True:
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	#STATEMENT
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES IN YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
	#WITHDRAWAL
	elif response == 'w':
		while True:
			print('---------------------------------------------')
			print('*********************************************')
			cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
			print('*********************************************')
			print('---------------------------------------------')
			if cash_out%10 != 0:
				print('------------------------------------------------------')
				print('******************************************************')
				print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 RUPEES NOTES')
				print('******************************************************')
				print('------------------------------------------------------')
				continue
			elif cash_out > amounts[n]:
				print('-----------------------------')
				print('*****************************')
				print('YOU HAVE INSUFFICIENT BALANCE')
				print('*****************************')
				print('-----------------------------')
				break
			else:
				amounts[n] = amounts[n] - cash_out
				print('-----------------------------------')
				print('***********************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
				print('***********************************')
				print('-----------------------------------')
				break
	#LODGING
	elif response == 'l':
		while True:
			print()
			print('---------------------------------------------')
			print('*********************************************')
			cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
			print('*********************************************')
			print('---------------------------------------------')
			print()
			if cash_in%10 != 0:
				print('----------------------------------------------------')
				print('****************************************************')
				print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
				print('****************************************************')
				print('----------------------------------------------------')
				continue
			else:
				amounts[n] = amounts[n] + cash_in
				print('----------------------------------------')
				print('****************************************')
				print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
				print('****************************************')
				print('----------------------------------------')
				break
	# PIN_CHANGE
	elif response == 'p':
		while True:
			print('-----------------------------')
			print('*****************************')
			new_pin = input(print('ENTER A NEW PIN: '))
			print('*****************************')
			print('-----------------------------')
			if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
				print('------------------')
				print('******************')
				new_ppin = input(print('CONFIRM NEW PIN: '))
				print('*******************')
				print('-------------------')
				if new_ppin != new_pin:
					print('------------')
					print('************')
					print('PIN MISMATCH')
					print('************')
					print('------------')
					continue
				else:
					pins[n] = new_pin
					print('NEW PIN SAVED')
					break
			else:
				print('-------------------------------------')
				print('*************************************')
				print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
				print('*************************************')
				print('-------------------------------------')
	#QUIT
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
		exit()