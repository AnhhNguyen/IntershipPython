a = 8
type(a)

f = 1.23

from decimal import *
getcontext().prec = 30
Decimal(10) / Decimal(3)
Decimal(10) / Decimal(3)
type(Decimal(5))

from fractions import *        
Fraction(1, 4)       # Tạo phân số

complex(3, 1)     #tạo số phức
c = 2 +1j
c.real  # lấy phần thực
c.imag #lấy phần ảo
complex(2)
type(3 +1j)    #in ra kiểu dữ liệu

fac1 = Fraction(1, 2)
fac2 = Fraction(2, 3)
fac3 = fac1 + fac2

fac4 = fac3 ** fac1

import math   #lấy nội dung của thư viện math
math.trunc(4.5)
math.floor(4.3)
print(math.ceil(4.3))
print(math.fabs(-4.5))
math.sqrt(4)
print(math.gcd(3, 7))