import csv
import random

total_rows = 0 ### liczba wszystkich wierszy
data = [] ### dane wejsciowe w postaci listy
sum_pts = 0 ### zmienna iteracyjna
sum_val = 0 ### zmienna iteracyjna
hms = 20
sum_row_val = [] ### finałowe wartości
sum_row_pts = [] ### finałowe punkty
temp_arr = []
id_list = [] ### lista przechowujaca wybrane id w losowaniu
iter_hms = 0 ### zmienna iteracyjna dla hms
hm = [] ### finałowa macierz

max_len_row = 0 #### najwieksza liczba elementow w wierszu z finalowej macierzy

def maxLenRow(value): #### funckja obliczajaca max_len_row
    global max_len_row
    if(max_len_row<value):
        max_len_row = value

with open('file.csv', 'r', encoding="utf8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = list(csvreader) ### ważne, można wybrać numer wiersza
    total_rows = len(data)

while(iter_hms < hms):
    rand_id = int(random.uniform(1,total_rows-1)) ### losowanie id
    while(rand_id in id_list):
        rand_id = int(random.uniform(1,total_rows-1))
    if(sum_val<100):
        row = data[rand_id]
        sum_val += float(row['value_season'])
        sum_val = round(sum_val,2)
        if(sum_val>=100):
            sum_val -= float(row['value_season'])
            sum_row_val.append(round(sum_val,2))
            sum_row_pts.append(sum_pts)
            hm.append(temp_arr)
            maxLenRow(len(temp_arr))
            temp_arr = []
            id_list.append(rand_id)
            sum_val = 0
            sum_pts = 0
            iter_hms += 1
        else:
            sum_pts += round(float(row['total_points']),2)
            temp_arr.append(row['id'])

for row in hm:
    print(row)
    print()
print("-------------------KONIEC------------")
hmcr = 70
x_new_j = [] #### x^new_j
iter_hm = 0 #### zmienna iteracyjna hm
while(iter_hm<20): #### dowolna liczba iteracji
    sum_values = 0
    sum_points = 0
    rand_id = 0
    id_list = []
    iter_hm=iter_hm+1
    r1 = int(random.uniform(1,101)) #### losowe r1 od 1 do 100
    if(r1<hmcr):
        for j in range(0,max_len_row): #### j - kolumna
            k = int(random.uniform(0,hms)) #### k - losowy wiersz
            while(not(len(hm[k])>j)): #### jeśli wiersz nie ma tylu kolumn (elementow w wierszu) to losujemy ponownie
                k = int(random.uniform(0,hms))
            print(j, max_len_row)
            sum_values += float(data[int(hm[k][j])]['value_season'])
            if(sum_values >= 100):
                sum_values -= float(data[int(hm[k][j])]['value_season'])
            else:
                sum_points += float(data[int(hm[k][j])]['total_points'])
                x_new_j.append(hm[k][j])
    else: 
        while(sum_values < 100):
            rand_id = int(random.uniform(1,total_rows-1)) ### losowanie id
            while(rand_id in id_list):
                rand_id = int(random.uniform(1,total_rows-1))
            row = data[rand_id]
            sum_values += float(row['value_season'])
            sum_values = round(sum_values,2)
            if(sum_values>=100):        
                sum_values -= float(row['value_season'])
                break
            else:
                sum_points += round(float(row['total_points']),2)
                x_new_j.append(row['id'])
    if(sum_points > min(sum_row_pts)):
        i = 0
        for single_point in sum_row_pts:
            if(single_point==min(sum_row_pts)):
                print("stary wiersz ",hm[i])
                print("nowy wiersz ",x_new_j)
                hm[i] = x_new_j
                sum_row_pts[i] = sum_points
                x_new_j = []
                max_len_row = 0 #### szukamy nowego najdluzszego wiersza
                break
            i+=1     
        for row in hm: #### szukamy nowego najdluzszego wiersza
            maxLenRow(len(row))
print("-------------------NOWY---------------")
for row in hm:
    print(row)
    print()