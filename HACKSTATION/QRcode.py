#Sistema de Gerar Qr Code
#Feito por Lucas Verissimo
#Versão 1.0

import qrcode


resposta_usuario = input("Digite o texto ou o Link/URL: \n>  ")

qr = qrcode.QRCode(
    box_size = 1,
    border = 1
)

qr.add_data(resposta_usuario)
qr.make(fit=True)

print("\n======================")
print("     Seu QRCODE      ")
print("======================\n")
qr.print_ascii(invert = True)

print(" Seu QRCODE foi Gerado com Sucesso!")