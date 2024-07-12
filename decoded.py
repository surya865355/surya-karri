import cv2
import hashlib
encrypted_image_path = r"C:\Users\yuvas\OneDrive\surya\encryptedimage.jpg"
image = cv2.imread(encrypted_image_path)

if image is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

height, width, channels = image.shape
password = input("Enter the passcode: ")

hash_object=hashlib.sha256 (password.encode())
hashed_password = hash_object.digest()
d = {}
c = {}

for i in range (256):
    d[chr(i)] = i
    c[i] = chr(i) 

n = 0
m = 0
z = 0

decoded_message = []
while n < height:
   original_value =(int(image[n, m, z]) - hashed_password[len(decoded_message) % len(hashed_password)]) % 256
   decoded_message.append(c[original_value])
   m += 1
   if m >= width:
       m = 0
       n += 1
       z = (z + 1) % 3
decoded_message = ' '.join(decoded_message)
print("decoded_message:",decoded_message)
