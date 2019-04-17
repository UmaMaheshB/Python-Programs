tables=input("enter tables").split()
#reading multiple tables with space delimeter ex: 2 3 4 8
for table in tables:
    #iterate tables
    for i in range(1,11):
        print("{} * {} = {}".format(table,i,int(table)*i))
    print("\n")
