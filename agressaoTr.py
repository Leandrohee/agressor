import time

import pyautogui as pa
import pytesseract as tes
import datetime
import time

# Mostrando o caminho do teseract.exe necessario no windows
tes.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

time.sleep(2)
#print(pa.position())

def copiaTtComprador():                 #coordenadas para tela x=2880 y=1800 (macbook)
    pa.leftClick(364,983)
    pa.rightClick(364, 400)
    pa.leftClick(400, 900)
    colaExcelTtComprador()

def copiaTtVendedor():                  #coordenadas para tela x=2880 y=1800 (macbook)
    pa.leftClick(530, 983)
    pa.rightClick(364, 400)
    pa.leftClick(400, 900)
    colarExcelTtVendedor()

def colaExcelTtComprador():             #coordenadas para tela x=2880 y=1800 (macbook)
    pa.doubleClick(1544,275,interval=1)
    pa.hotkey('ctrl','v')
    copiaTtVendedor()

def colarExcelTtVendedor():             #coordenadas para tela x=2880 y=1800 (macbook)
    pa.doubleClick(1705, 275,interval=1)
    pa.hotkey('ctrl', 'v')
    copiaGrafico()

def copiaGrafico():                     #coordenadas para tela x=2880 y=1800 (macbook)
    pa.rightClick(830,1250)
    pa.leftClick(930,1100)
    #time.sleep(0.5)
    colaExcelGrafico()

def colaExcelGrafico():                 #coordenadas para tela x=2880 y=1800 (macbook)
    pa.doubleClick(2430,275,interval=1)
    pa.hotkey('ctrl','v')


def pegaHoraProfit():                   #coordenadas para tela x=2880 y=1800 (macbook)
    #coordenadas do print
    sex, sey = 980,500      #superior esquerdo x e y
    idx, idy = 1270,615      #inferior direito x e y
    shot = pa.screenshot(region=(sex,sey,idx-sex,idy-sey))   #tira o screenshot do pedaco selecionado
    shot.save("tempo.png")
    tempo = tes.image_to_string(shot, config=r"--psm 6")[:8]
    tempoFormatado = datetime.datetime.strptime(tempo, "%H:%M:%S").time()
    return tempoFormatado


while True:
    print(pegaHoraProfit().strftime("%S"))
    if (pegaHoraProfit().strftime("%S") == "00"):
        copiaTtComprador()
