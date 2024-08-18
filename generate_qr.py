import qrcode
import csv
from datetime import date
import os

def generate_qr_codes():
    if not os.path.exists('qrcodes'):
        os.makedirs('qrcodes')
    
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_id, name = row
            data = f"ID:{student_id}, Name:{name}, Date:{date.today()}"
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(f'qrcodes/{student_id}.png')

if __name__ == "__main__":
    generate_qr_codes()
