import os
import pyaes

## Abrir arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Chave para descriptografar
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover arquivo criptografado
os.remove(file_name)

## Criar arquivo descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
