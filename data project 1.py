pre_nom="olaide"
nom="Eleshinmogun"
one_1=pre_nom[::2]
two_2=nom[:3]
import random
OTP_numbres=round(random.random()*10000)
Password=one_1+two_2+str(OTP_numbres)
print(Password)
print(Password)

first_name="Olaide"
sur_name="Eleshinmogun"
pat1=first_name[:3]
pat2=sur_name[:5]
import random
OTP_numbers=round(random.random()*10000)
password=pat1+pat2+str(OTP_numbers)
print(password)

name="Ebenezer"
otherName="Greatness"
part1=name[::2]
part2=otherName[::5]
import random
OTP_numbers=round(random.random()*10000)
password=part1+part2+str(OTP_numbers)
print(password)

name="olaDele"
surname="olamilEkan"
part1=name[::3]
part2=surname[:6]
import random
OTP_numbers=round(random.random()*10000)
password=part1+part2+str(OTP_numbers)
print(password)

name="olaDele"
surname="olamilEkan"
part1=name[::3]
part2=surname[:6]
import random
OTP_numbers=round(random.randint(100000, 999999))
password=part1+part2+str(OTP_numbers)
print(password)
