import hashlib

input_string: str = "bgvyzdsv"
input_string_original = input_string
md5_hash = hashlib.md5(input_string.encode())
hex_result: str = md5_hash.hexdigest()
i: int = 1

while not hex_result.startswith('000000'):
    input_string = input_string_original + str(i)
    md5_hash = hashlib.md5(input_string.encode())
    hex_result = md5_hash.hexdigest()
    i += 1

print(input_string)
print(hex_result)


