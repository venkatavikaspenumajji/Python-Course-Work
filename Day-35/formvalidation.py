'''import re
fullname = input("Enter the full name:")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.fullmatch(pattern,fullname)
print("valid full name" if res else "Invalid full name")'''



'''import re
email = input("Enter the email:")
pattern = r'^[a-ZA-Z0-9._]+@[a-ZA-Z0-9._]+\.[a-ZA-z]{2,})$'
res = re.fullmatch(pattern,email)
print("valid email" if res else "Invalid full name")'''


import re
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
phone_number = input("Enter your phone number: ")
res = re.fullmatch(pattern, phone_number)
print("Valid Phone number" if res else "Invalid Phone number")



import re
pattern = r'^(?=.[A-Z])(?=.[a-z])(?=.[0-9])(?=.[@$!%?&])[A-Za-z0-9@$!%?&]{8,}$'
password = input("Enter your password: ")
res = re.fullmatch(pattern, password)
print("Valid password" if res else "Invalid password")


