import csv
import os

#定义表明
table = 'B3UnitedInfos_Goods'
#定义输入文件名
file = '副本辅料存货-20170621.csv'


str = 'update %s set'%table
def read_csv():
    global str
    out = open('output/out.txt', 'w')
    print('加载输入文件：%s'%file)
    with open('input/%s'%file, 'r') as csvfile:
        read = csv.reader(csvfile)
        row = 0
        sql = []
        head = []        
        for fields in read:
            con = ''
            if row == 0:
                head = fields
            else:
                col = 0               
                for fld in fields:
                    if col == 0:
                        con = fld
                    else:
                        str = "%s %s='%s', "%(str, head[col].strip(), fld.strip())
                    col = col + 1
                str = "%s where %s = '%s';\n"%(str.rstrip().rstrip(','), head[0].strip(), con.strip())
                sql.append(str)
                str = 'update %s set'%table
            row = row + 1

    out.writelines(sql)
    print('output/out.txt 生成成功')
    out.close()            

#generate_sql()
read_csv()
os.system("pause")

