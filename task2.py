from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new(img.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_img.putpixel((x, y), encrypted_pixel)

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    decrypted_img = Image.new(encrypted_img.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_img.putpixel((x, y), decrypted_pixel)

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    choice = input("Do you want to encrypt or decrypt an image?: ")
    if choice.lower() == 'encrypt':
        image_path = input("Enter the path to the image to encrypt: ")
        key = int(input("Enter the encryption key: "))
        encrypt_image(image_path, key)
    elif choice.lower() == 'decrypt':
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        key = int(input("Enter the decryption key: "))
        decrypt_image(encrypted_image_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()