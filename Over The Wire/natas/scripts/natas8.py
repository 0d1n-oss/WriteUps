import base64

secret = "3d3d516343746d4d6d6c315669563362"
secret = bytes.fromhex(secret)
secret = secret[::-1]
secret = base64.decodebytes(secret)

print(secret)
