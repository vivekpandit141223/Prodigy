from PIL import Image

#This function will encrypt the image.
def encrypt_image(image_path, shift):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            encrypted_img.putpixel((x, y), (r, g, b))

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")


#This function will decrypt the image.
def decrypt_image(encrypted_image_path, shift):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    decrypted_img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_img.getpixel((x, y))
            r = (r - shift) % 256
            g = (g - shift) % 256
            b = (b - shift) % 256
            decrypted_img.putpixel((x, y), (r, g, b))

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")
# This is the main function
def main():
    option = input("Enter 'encrypt' or 'decrypt' to proceed: ")

    if option == 'encrypt':
        image_path = input("Enter the path to the image you want to encrypt: ")
        shift = int(input("Enter the shift value for encryption: "))
        encrypt_image(image_path, shift)
    elif option == 'decrypt':
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        shift = int(input("Enter the shift value for decryption: "))
        decrypt_image(encrypted_image_path, shift)
    else:
        print("Invalid option! Please enter 'encrypt' or 'decrypt'.")


main()