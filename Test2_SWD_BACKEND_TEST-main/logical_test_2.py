
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def arabic_to_roman(number):
    if number <= 0 or number > 1000:
        return "Invalid input"
    
    # 1000 limit
    thousand_unit = ["", "M"]
    # 100 - 900
    hundred_unit = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    # 10 - 90
    ten_unit = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    # 0 - 9
    unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    # Converting to roman
    thousands = thousand_unit[number // 1000]
    hundreds = hundred_unit[(number % 1000) // 100]
    tens = ten_unit[(number % 100) // 10]
    ones = unit[number % 10]
 
    roman_text = thousands + hundreds + tens + ones
 
    return roman_text


number = int(input("Enter Number (1-1000): "))
print("roman:", arabic_to_roman(number))

