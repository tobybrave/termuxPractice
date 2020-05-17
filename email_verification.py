import re

user_email = input("Email: ")
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
verifying = True
while verifying:
	if re.search(regex, user_email):
		verifying = False
	else:
		print("Invalid Email address!! Try again")
		user_email = input("Email: ")		