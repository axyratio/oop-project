import streamlit as st

class BaseConverter:
    # กำหนดค่าเริ่มต้นใน object ด้วยพารามิเตอร์ที่รับมา
    def __init__(self, number, from_base, to_base):
        self.number = number
        self.from_base = from_base
        self.to_base = to_base
    
    # แปลงเลขจากฐาน from_base เป็น to_base ที่รับมาจากผู้ใช้
    def getBaseResult(self):
        from_base = self.decimal(self.number, self.from_base) # แปลงเป็นเลขฐานสิบ
        if self.to_base == 10:
            # ถ้า base ที่รับจากผู้ใช้ 10 ให้คืนค่าเลขทศนิยมเป็นสตริง
            return str(from_base)
        else:
            # นอกเหนือ ทำการแปลงเลขทศนิยมไปยัง base ปลายทาง
            return self.convert(from_base, self.to_base)
        
    """แปลงเลขจาก base ที่กำหนดไว้เป็นเลขฐานสิบ (decimal)"""
    @staticmethod
    def decimal(number, base):
        return int(number, base)

    """แปลงเลขทศนิยม (เลขฐานสิบ) ไปยัง base ที่กำหนดไว้"""
    @staticmethod
    def convert(from_base, base):
        digits = "0123456789ABCDEF"
        if from_base < base:
            # ถ้าเลขทศนิยมน้อยกว่า base ปลายทาง ให้คืนค่าเลขหลักเดียวนั้น
            return digits[from_base]
        else:
            # เรียกฟังก์ชันเองโดยใช้วิธีทำลำดับถอดเลขฐาน
            return BaseConverter.convert(from_base // base, base) + digits[from_base % base]