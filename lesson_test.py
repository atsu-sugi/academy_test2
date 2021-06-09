#kreis academy file操作

import csv

with open('./file/lesson.csv','r',encoding='utf-8-sig') as csv_file:
    read = csv.DictReader(csv_file)
    data = []
    for row in read:
        row['合計'] = int(row['国語']) + int(row['数学']) + int(row['社会'])
        data.append({'seq':row['seq'],'name':row['name'] ,'合計':row['合計']})

with open('./file/lesson02.csv','w',encoding='utf-8', newline='') as CSV_FILE:
    data2 = csv.writer(CSV_FILE)
    data2.writerow(['seq', 'name', '合計'])
    for i in data:
        data2.writerow(list(i.values()))