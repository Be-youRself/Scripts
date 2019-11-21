# Coding: utf8

import random
import string

key_length = random.randint(10, 14)
ran_key = ''.join(random.sample(string.ascii_letters + string.digits, key_length))
print(ran_key)