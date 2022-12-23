import string
import random 

while(1):
    attempt = ''.join(random.choice(string.ascii_lowercase) for x in range(5))
    print(attempt[0] + attempt[1]  + attempt[1] + attempt[2] + '_'  + attempt[0] + attempt[1] + '_'  + attempt[0] + attempt[3]  + attempt[2] + attempt[4])
            
        

