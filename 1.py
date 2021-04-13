import csv
import random
with open('file.csv', 'r', encoding="utf8") as csvfile:
    csvreader = csv.DictReader(csvfile)
    total_rows=667
    data = list(csvreader)
    sum_pts = 0
    sum_val = 0
    hms = 20
    sum_row_val = []
    sum_row_pts = []
    iter_hms = 0
    matrix = []
    temp_arr = []
    id_list = []
    rand = 0
    while(iter_hms<hms):
        rand = int(random.uniform(1,total_rows-1 ))
        while(rand in id_list):
            rand = int(random.uniform(1,total_rows-1 ))
        if(sum_val<100):
            row = data[rand]
            sum_val += float(row['value_season'])
            round(sum_val,2)
            if(sum_val>=100):
                sum_val -= float(row['value_season'])
                sum_row_val.append(round(sum_val,2))
                sum_row_pts.append(sum_pts)
                matrix.append(temp_arr)
                temp_arr = []
                id_list.append(rand)
                iter_hms+=1
                sum_val = 0
                sum_pts = 0
            else:
                sum_pts += round(float(row['total_points']),2)
                temp_arr.append(row['id'])
    print(matrix)
    print("Suma wartości")
    print(sum_row_val)
    print("Suma punktów")
    print(sum_row_pts)
    
    
    