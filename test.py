from models.bill import *
from helpers.str_generator import *
b = Bill(str_gen(), 1, 2, 3)
print(b.uuid)