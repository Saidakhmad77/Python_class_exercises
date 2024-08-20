import re
import string
string = string.strip()
string = re.sub(r'[^a-zA-Z]', '')

print(string)