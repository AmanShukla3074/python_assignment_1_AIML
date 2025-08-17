 # 7. When should we use the decimal module instead of float?

from decimal import Decimal
a = Decimal('1.1') + Decimal('2.2')
print(a)  # Exact result