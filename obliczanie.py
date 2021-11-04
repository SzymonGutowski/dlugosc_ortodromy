
from math import radians, sin, cos, acos

import time





print('Program zajmuje sie obliczaniem odległosci między punktami dla układu współrzędnych WGS84 leżących w tych samych'
      ' częściach pólkul zachodniej lub wschodniej i południowej lub północnej. ')


print('-' * 100)
print('-' * 100)


polkula_1_1 = int(input("""Proszę o wybranie półkuli dla pierwszego punktu:
1 - Dla półkuli północnej
2 - Dla półuli południowej
>>>>>> 
"""))


polkula_1_2 = int(input("""Proszę o wybranie półkuli dla pierwszego punktu:
1 - Dla półkuli wschodniej
2 - Dla półuli zachodniej
>>>>>> 
"""))


polkula_2_1 = int(input("""Proszę o wybranie półkuli dla drugiego punktu:
1 - Dla półkuli północnej
2 - Dla półuli południowej
>>>>>> 
"""))


polkula_2_2 = int(input("""Proszę o wybranie półkuli dla drugiego punktu:
1 - Dla półkuli wschodniej
2 - Dla półuli zachodniej
>>>>>> 
"""))

# Szerokość geograficzna dla 1 punktu


stop_lat_x1 = int(input('Punkt 1 szerokość - stopnie:  '))


while stop_lat_x1 > 90 or stop_lat_x1 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0 ° do 90 °')
    stop_lat_x1 = int(input('Punkt 1 szerokosc  - stopnie:  '))


min_lat_x1 = int(input('Punkt 1 szerokosc - minuty: '))

while min_lat_x1 > 60 or min_lat_x1 < 0:
    print("Prosze podaj ponownie wartość z przedziału od 0' do 60' ")
    min_lat_x1 = int(input('Punkt 1 szerokosc  - minuty:  '))

sek_lat_x1 = int(input('Punkt 1 szerokosc  - sekundy: '))

while sek_lat_x1 > 60 or sek_lat_x1 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0" do 60" ')
    sek_lat_x1 = int(input('Punkt 1 szerokosc  - sekundy:  '))

## Długość geograficzna dla 1 punktu


stop_lon_x1 = int(input('Punkt 1 długość - stopnie:  '))


while stop_lon_x1 > 180 or stop_lon_x1 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0 ° do 180 °')
    stop_lon_x1 = int(input('Punkt 1 długość  - stopnie:  '))

min_lon_x1 = int(input('Punkt 1 długość - minuty: '))

while min_lon_x1 > 60 or min_lon_x1 < 0:
    print("Prosze podaj ponownie wartość z przedziału od 0' do 60' ")
    min_lon_x1 = int(input('Punkt 1 długość  - minuty:  '))

sek_lon_x1 = int(input('Punkt 1 długość - sekundy: '))

while sek_lon_x1 > 60 or sek_lon_x1 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0" do 60" ')
    sek_lon_x1 = int(input('Punkt 1 długość  - sekundy:  '))


## Szerokość geograficzna dla 2 punktu


stop_lat_x2 = int(input('Punkt 2 szerokość - stopnie:  '))


while stop_lat_x2 > 90 or stop_lat_x2 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0 ° do 90 °')
    stop_lat_x2 = int(input('Punkt 2 szerokosc  - stopnie:  '))

min_lat_x2 = int(input('Punkt 2 szerokosc - minuty: '))

while min_lat_x2 > 60 or min_lat_x2 < 0:
    print("Prosze podaj ponownie wartość z przedziału od 0' do 60' ")
    min_lat_x2 = int(input('Punkt 2 szerokosc  - minuty:  '))

sek_lat_x2 = int(input('Punkt 2 szerokosc  - sekundy: '))

while sek_lat_x2 > 60 or sek_lat_x2 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0" do 60" ')
    sek_lat_x2 = int(input('Punkt 2 szerokosc  - sekundy:  '))

## Długość geograficzna dla 2 punktu


stop_lon_x2 = int(input('Punkt 2 długość - stopnie:  '))


while stop_lon_x2 > 180 or stop_lon_x2 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0 ° do 180 °')
    stop_lon_x2 = int(input('Punkt 2 długość  - stopnie:  '))

min_lon_x2 = int(input('Punkt 2 długość - minuty: '))

while min_lon_x2 > 60 or min_lon_x2 < 0:
    print("Prosze podaj ponownie wartość z przedziału od 0' do 60' ")
    min_lon_x2 = int(input('Punkt 2 długość  - minuty:  '))

sek_lon_x2 = int(input('Punkt 2 długość  - sekundy: '))

while sek_lon_x2 > 60 or sek_lon_x2 < 0:
    print('Prosze podaj ponownie wartość z przedziału od 0" do 60" ')
    sek_lon_x2 = int(input('Punkt 2 długość  - sekundy:  '))

print('&' * 100)



print(f"Wskazany przez Ciebie punkt 1 znajduje się w szerokości - {stop_lat_x1} ° {min_lat_x1} ' {sek_lat_x1}'' "
      f"i długości - "
      f"{stop_lon_x1} ° {min_lon_x1} ' {sek_lon_x1}''")
print(f"Wskazany przez Ciebie punkt 2 znajduje się w szerokości - {stop_lat_x2} ° {min_lat_x2} ' {sek_lat_x2}'' "
      f"i długości - "
      f"{stop_lon_x2} ° {min_lon_x2} ' {sek_lon_x2}''")

x1_dziesietne = stop_lat_x1 + min_lat_x1/60 + sek_lat_x1/3600

y1_dziesietne = stop_lon_x1 + min_lon_x1/60 + sek_lon_x1/3600

x2_dziesietne = stop_lat_x2 + min_lat_x2 / 60 + sek_lat_x2 / 3600

y2_dziesietne = stop_lon_x2 + min_lon_x2 / 60 + sek_lon_x2 / 3600

x1_dziesietne = radians(x1_dziesietne)
x2_dziesietne = radians(x2_dziesietne)
y1_dziesietne = radians(y1_dziesietne)
y2_dziesietne = radians(y2_dziesietne)


if polkula_1_1 == 2:
    x1_dziesietne = - x1_dziesietne
else:
    x1_dziesietne


if polkula_2_1 == 2:
    x2_dziesietne = - x2_dziesietne
else:
    x2_dziesietne

if polkula_1_2 == 2:
    y1_dziesietne = - y1_dziesietne
else:
    y1_dziesietne


if polkula_2_2 == 2:
    y2_dziesietne = - y2_dziesietne
else:
    y2_dziesietne





def obliczanie_dlug():
    #obliczanie długosci w układzie wspołrzędnym
    dlugosc_odc = math.sqrt((x2_dziesietne - x1_dziesietne) ** 2 + (y2_dziesietne - y1_dziesietne) **2 )
    dlugosc_odc_km = 111.195 * dlugosc_odc
    zao_dlugosc_odc_km = math.ceil(dlugosc_odc_km)
    print(f'Odległość między podanymi punktami wynosi {zao_dlugosc_odc_km} km.')
    time.sleep(120)

def dlugosc_ortodromy():

    delta_lon = y1_dziesietne - y2_dziesietne
    D_wzor = acos(sin(x1_dziesietne) * sin(x2_dziesietne) + cos(x1_dziesietne) * cos(x2_dziesietne) * cos(delta_lon))
    D_km = D_wzor * 6371.01
    print()
    print(f'Odległość między podanymi punktami wynosi {D_km} km.')
    time.sleep(30)
    exit()

dlugosc_ortodromy()


