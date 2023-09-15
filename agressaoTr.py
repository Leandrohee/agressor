import pyautogui as pa
import pytesseract as tes
import datetime

# Mostrando o caminho do teseract.exe necessario no windows
tes.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# try:
#     while True:
#         x, y = pa.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

def pegaHoraProfit():
    #coordenadas do print
    sex, sey = 980,550      #superior esquerdo x e y
    idx, idy = 1270,620      #inferior direito x e y
    shot = pa.screenshot(region=(sex,sey,idx-sex,idy-sey))   #tira o screenshot do pedaco selecionado
    shot.save("tempo.png")
    tempo = tes.image_to_string(shot, config=r"--psm 6")[:8]
    tempoFormatado = datetime.datetime.strptime(tempo, "%H:%M:%S").time()
    return tempoFormatado

print(pegaHoraProfit())