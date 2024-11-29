import qrcode

print("Welcome to our QR Code generator")

destination_url = input("What is the URL you want your QR Code to go to? (include https://)").lower()
save_as = input("What would you like your QR Code to be saved as? (It will save in the same directory your project is in) ").lower()

img = qrcode.make({destination_url})
type(img)
img.save(f'{save_as}.png')

print(f'Saved your QR Code as {save_as}.png')