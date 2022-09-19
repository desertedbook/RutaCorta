
import eel 
from itertools import combinations, permutations

@eel.expose
def Posibles_rutas(opcines):
    opcines = [int(x) for x in opcines]

    combinaciones = []

    p = permutations(opcines);
    
    for i in list(p):
        combinaciones.append(i)

    #OBTENER LA MEJOR RUTA
    mejor_ruta = Mejor_ruta(combinaciones)
    
    #GENERAR LOS DATOS DE LA MEJOR RUTA
    coordenadas_mapa = Generar_datos_mapa(mejor_ruta[0])

    #ENVIAR LOS DATOS A JS
    lista_coordenadas = coordenadas_mapa[0]
    lista_nombres = coordenadas_mapa[1]
    eel.Desplegar_rutas(lista_coordenadas,lista_nombres,mejor_ruta[2])


def Mejor_ruta(combinaciones):
    valor_distancias = []
    distancias = [
        [0,1149,1151,1384,809,590,474,1474,2921,743,829,1209,247,1683,968,408,1085,309,385,510,540,824,2040,510,794],
        [1149,0,1760,2056,1462,1233,1121,2117,3592,1424,1291,277,900,2239,1458,792,1590,922,1038,1154,967,780,2668,935,355],
        [1151,1760,0,233,441,711,721,1194,2523,913,709,1839,904,1356,651,1223,644,982,768,641,793,1634,1742,1181,1434],
        [1384,2056,233,0,574,944,954,1427,2858,1148,942,2082,1137,1599,884,1458,877,1215,999,874,1071,1911,1975,1401,1701],
        [809,1462,441,574,0,373,378,753,2182,574,583,1273,561,925,513,882,518,639,423,298,541,1297,1302,825,1097],
        [590,1233,711,944,373,0,187,884,2313,202,628,1268,332,1058,620,653,698,439,216,220,464,1069,1433,624,869],
        [474,1121,721,954,378,187,0,1071,2504,389,538,1156,221,1243,607,547,685,305,83,130,374,957,1620,490,757],
        [1474,2117,1194,1427,753,884,1071,0,1429,1015,1338,2152,1217,141,1278,1565,1271,1323,1107,1051,1294,1953,549,1508,1753],
        [2921,3592,2523,2858,2182,2313,2504,1429,0,2445,2144,3638,2985,1391,2085,2995,2700,2732,2538,2480,2724,3448,905,2337,1080],
        [743,1424,913,1148,574,202,389,1015,2445,0,829,1458,524,1187,822,792,900,602,414,422,568,1245,1564,787,1060],
        [829,1291,709,942,583,628,538,1338,2144,829,0,1335,597,1508,216,898,475,638,533,408,308,1175,1885,538,936],
        [1209,277,1839,2082,1273,1268,1156,2152,3638,1458,1335,0,935,2324,1497,838,1615,857,1073,1199,1011,825,2700,699,399],
        [247,900,904,1137,561,332,221,1217,2985,524,597,935,0,1417,740,321,818,78,138,253,291,738,1765,253,536],
        [1683,2239,1356,1599,925,1058,1243,141,1391,1187,1508,2324,1417,0,1450,1737,1443,1495,1279,1223,1487,2153,511,1630,1953],
        [968,1458,651,884,513,620,607,1278,2085,822,216,1497,740,1450,0,1027,470,798,602,477,467,1337,1827,798,1098],
        [408,792,1223,1458,882,653,547,1565,2995,792,898,838,321,1737,1027,0,1139,254,458,584,592,416,2114,252,137],
        [1085,1590,644,877,518,698,685,1271,2700,900,475,1615,818,1443,470,1139,0,897,680,555,604,1474,1819,935,1225],
        [309,922,982,1215,639,439,305,1323,2732,602,638,857,78,1495,798,254,897,0,218,342,331,559,1871,185,458],
        [385,1038,768,999,423,216,83,1107,2538,414,533,1073,138,1279,602,458,680,218,0,126,367,874,1407,401,574],
        [510,1154,641,874,298,220,130,1051,2480,422,408,1199,253,1223,477,584,555,342,126,0,244,399,1599,527,800],
        [540,967,793,1071,541,464,374,1294,2724,568,308,1011,291,1487,467,592,604,331,367,244,0,851,1843,311,610],
        [824,780,1634,1911,1297,1069,957,1953,3448,1245,1175,825,738,2153,1337,416,1474,559,874,399,851,0,2501,539,428],
        [2040,2668,1742,1975,1302,1433,1620,549,905,1564,1885,2700,1765,511,1827,2114,1819,1871,1407,1599,1843,2501,0,2057,2202],
        [510,935,1181,1401,825,624,490,1508,2337,787,538,699,253,1630,798,252,935,185,401,527,311,539,2057,0,298],
        [794,355,1434,1701,1097,869,757,1753,1080,1060,936,399,536,1953,1098,137,1225,458,574,800,610,426,2202,298,0]
    ]

    filas = len(combinaciones)
    columnas = len(combinaciones[0])

    i = 0
    while i < filas:
        j = 0
        suma = 0
        while j < columnas:
            if(j < columnas - 1):
                f = combinaciones[i][j]
                c = combinaciones[i][j+1]
                suma = suma + distancias[f][c]
            j = j + 1
        valor_distancias.append(suma)
        i = i + 1

    k = 0
    menor_distancia = valor_distancias[0]
    indice = 0
    while k < len(valor_distancias):
        if(valor_distancias[k] < menor_distancia):
            menor_distancia = valor_distancias[k]
            indice = k
        k = k + 1
    
    x = 0
    while x < len(combinaciones):
        print(str(combinaciones[x]) + " Distancia: " + str(valor_distancias[x]))
        x = x + 1

    print("Mejor combinacion: " +  str(combinaciones[indice]))
    print("Distancia: " + str(menor_distancia))

    return combinaciones[indice],menor_distancia,menor_distancia

def Generar_datos_mapa(ruta):
    coordenadas = []
    nom_coordenadas = []
    cor0 = [16.84942,-99.90891]
    cor1 = [18.51413,-88.30381]
    cor2 = [28.63528,-106.08889]
    cor3 = [31.73944,-106.48694]
    cor4 = [24.0277,-104.653]
    cor5 = [20.6736,-103.344]
    cor6 = [21.0181,-101.258]
    cor7 = [29.0892,-110.961]
    cor8 = [24.1333,-110.3]
    cor9 = [19.0522,-104.316]
    cor10 = [25.8441,-97.5281]
    cor11 = [20.97,-89.62]
    cor12 = [19.4978,-99.1269]
    cor13 = [31.3086,-110.943]
    cor14 = [27.48,-99.5105]
    cor15 = [17.1167,-97.6667]
    cor16 = [28.7,-100.523]
    cor17 = [19.03793,-98.20346]
    cor18 = [20.58806,-100.38806]
    cor19 = [22.1565,-100.986]
    cor20 = [22.2553,-97.8686]
    cor21 = [14.9,-92.2667]
    cor22 = [32.533,-117.05]
    cor23 = [19.1727,-96.1333]
    cor24 = [17.98689,-92.93028]

    i = 0
    while(i < len(ruta)):
        if(ruta[i] == 0):
            coordenadas.append(cor0)
            nom_coordenadas.append('ACAPULCO')
        
        if(ruta[i] == 1):
            coordenadas.append(cor1)
            nom_coordenadas.append('CHETUMAL')

        if(ruta[i] == 2):
            coordenadas.append(cor2)
            nom_coordenadas.append('CHIHUAHUA')
        
        if(ruta[i] == 3):
            coordenadas.append(cor3)
            nom_coordenadas.append('CD.JUAREZ')

        if(ruta[i] == 4):
            coordenadas.append(cor4)
            nom_coordenadas.append('DURANGO')

        if(ruta[i] == 5):
            coordenadas.append(cor5)
            nom_coordenadas.append('GUADALAJARA')

        if(ruta[i] == 6):
            coordenadas.append(cor6)
            nom_coordenadas.append('GUANAJUATO')

        if(ruta[i] == 7):
            coordenadas.append(cor7)
            nom_coordenadas.append('HERMOSILLO')

        if(ruta[i] == 8):
            coordenadas.append(cor8)
            nom_coordenadas.append('LA PAZ')

        if(ruta[i] == 9):
            coordenadas.append(cor9)
            nom_coordenadas.append('MANZANILLO')

        if(ruta[i] == 10):
            coordenadas.append(cor10)
            nom_coordenadas.append('MATAMOROS')

        if(ruta[i] == 11):
            coordenadas.append(cor11)
            nom_coordenadas.append('MERIDA')

        if(ruta[i] == 12):
            coordenadas.append(cor12)
            nom_coordenadas.append('MEXICO DF')

        if(ruta[i] == 13):
            coordenadas.append(cor13)
            nom_coordenadas.append('NOGALES')

        if(ruta[i] == 14):
            coordenadas.append(cor14)
            nom_coordenadas.append('NVO.LAREDO')

        if(ruta[i] == 15):
            coordenadas.append(cor15)
            nom_coordenadas.append('OAXACA')

        if(ruta[i] == 16):
            coordenadas.append(cor16)
            nom_coordenadas.append('PIEDRAS NEGRAS')

        if(ruta[i] == 17):
            coordenadas.append(cor17)
            nom_coordenadas.append('PUEBLA')

        if(ruta[i] == 18):
            coordenadas.append(cor18)
            nom_coordenadas.append('QUERETARO')

        if(ruta[i] == 19):
            coordenadas.append(cor19)
            nom_coordenadas.append('SAN LUIS POTOSI')

        if(ruta[i] == 20):
            coordenadas.append(cor20)
            nom_coordenadas.append('TAMPICO')

        if(ruta[i] == 21):
            coordenadas.append(cor21)
            nom_coordenadas.append('TAPACHULA')

        if(ruta[i] == 22):
            coordenadas.append(cor22)
            nom_coordenadas.append('TIJUANA')

        if(ruta[i] == 23):
            coordenadas.append(cor23)
            nom_coordenadas.append('VERACRUZ')

        if(ruta[i] == 24):
            coordenadas.append(cor24)
            nom_coordenadas.append('VILLAHERMOSA')

        i = i + 1

    return coordenadas,nom_coordenadas
    
eel.init('Web')
eel.start('prueba.html')
