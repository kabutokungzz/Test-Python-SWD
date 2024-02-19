
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def convert_to_thai_text(number):
    thai_numerals = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า', 'สิบ']
    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    if number < 0 or number >= 10000000:
        return "Input numbers must be greater than or equal to 0 and less than 10 million."

    thai_text = ''
    digits = [int(digit) for digit in str(number)]
    digits.reverse()
    for i in range(len(digits)):
        if digits[i] != 0 and thai_units[i] == 'สิบ' and thai_numerals[digits[i]] == 'สอง':
            thai_text = 'ยี่' + thai_units[i] + thai_text
        elif digits[i] != 0 and thai_units[i] == 'สิบ' and thai_numerals[digits[i]] == 'หนึ่ง':
            thai_text = thai_units[i] + thai_text
        elif len(digits) > 1 and i == 0 and thai_numerals[digits[i]] == 'หนึ่ง':
            thai_text = 'เอ็ด' + thai_text
        elif digits[i] != 0:
            thai_text = thai_numerals[digits[i]] + thai_units[i] + thai_text
        else:
            if thai_units[i] == 'สิบ' and len(thai_text) > 0 and thai_text[0] != 'ศูนย์':
                thai_text = thai_numerals[0] + thai_text
    return thai_text

number = int(input("Enter Number (0-9999999): "))
print("Thai Text Number:", convert_to_thai_text(number))
