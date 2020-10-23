import re

def is_email_valid(email):
   match = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)
   return match != None
