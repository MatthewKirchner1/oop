import JoesAutoServiceQuoteClass as S

quote1 = S.ServiceQuote()
total = quote1.get_total_charges()
print(total)

import JoesAutoCarClass as C

car1 = C.Car()
make = car1.get_make()
print(make)