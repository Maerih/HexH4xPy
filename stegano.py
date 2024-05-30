# Author: Onyonka Maeri
# Date: 2024-05-30
# WARNING:
# This script is intended for educational purposes only.
# Unauthorized use of this script on systems you do not own or
# have explicit permission to test is illegal and unethical.
# Use responsibly and within the bounds of all applicable laws.



# pip3 install stepic

import stepic
from PIL import Image

# Example: Encode a message into an image
image = Image.open('python.png')
message = input("Enter Message to Stegno: ")
encoded_image = stepic.encode(image, )
encoded_image.save('encoded_image.png')
decoded_image = Image.open('encoded_image.png')
message = stepic.decode(decoded_image)
print('Decoded message:', message)
