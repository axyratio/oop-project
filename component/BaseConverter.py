class BaseConverter:
    def __init__(self, number, from_base, to_base):
        self.number = number
        self.from_base = from_base
        self.to_base = to_base
    
    def convert(self):
        # แปลงจาก decimal ไป base ที่ target
        decimal_number = self.to_decimal(self.number, self.from_base) #
        if self.to_base == 10:
            return str(decimal_number)
        else:
            return self.from_decimal(decimal_number, self.to_base)

    @staticmethod
    def to_decimal(number, base):
        """Converts a number from a given base to decimal (base 10)."""
        return int(number, base)

    @staticmethod
    def from_decimal(decimal_number, base):
        """Converts a decimal number (base 10) to a given base."""
        digits = "0123456789ABCDEF"
        if decimal_number < base:
            return digits[decimal_number]
        else:
            return BaseConverter.from_decimal(decimal_number // base, base) + digits[decimal_number % base]
