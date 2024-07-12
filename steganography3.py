import cv2
import os
import hashlib
image_path=r"C:\Users\yuvas\OneDrive\المستندات\garden-rose-red-pink-56866.jpeg"
img = cv2.imread(image_path)
if img is None:
    print("image not found.check the file path and make sure the image exists.")
    exit()

    height,width,channels = img.shape
    msg=input("enter a secret message: ")
    password=input("enter a passcode: ")
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.digest()
d = {}
c = {}
for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)

n = 0
m = 0
z = 0

for i in range(len(msg)):
    new_value = (int(img[n, m, z]) + d[msg[i]] + hashed_password[i % len(hashed_password)]) % 256
    img[n, m, z] = new_value

    m += 1
    if m>= width:
        m = 0
        n += 1
    if n >= height:
         print("image is too small to hold the entire image.")
         break

    z = (z+1) % 3
encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedimage.jpg")
cv2.imwrite(encrypted_image_path,img)
os.startfile(encrypted_image_path)

print(f"message has been encoded into '{encrypted_image_path}'.")












