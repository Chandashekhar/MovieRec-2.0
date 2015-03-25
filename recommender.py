from Tkinter import *
import tkMessageBox
import time
import csv
import os
import operator

'''collab filtering implementation'''


def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    
    """
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)


def recolist (distlist):

    best_user = distlist[0][1]
    movierecolist = []
    movienamelist = []


    

    with open('ratings.csv', 'rb') as csvfile:

        dataReader = csv.reader(csvfile, delimiter=',')

        for row in dataReader:

            if row[0] == str(best_user):
                

                with open('bestuser.csv', 'ab') as csvfile:
                    
                    dataWriter = csv.writer(csvfile, delimiter=',')
                    dataWriter.writerow([row[1]]+[row[2]])


        bestuserlist = csv_to_list('bestuser.csv')
        bestuserlist = sorted (bestuserlist, key= operator.itemgetter(1), reverse=True)

        

        euserlist = csv_to_list('enduser.csv')
        
        i = 0

        k = 0

        l = 0

        j = 0

        while (i < len(bestuserlist)):

            j = 0

            while (k < len(euserlist)):

                if euserlist[k][0] == bestuserlist[i][0]:
                    j = j+1


                k = k+1

            if j == 0:

                movierecolist.append([bestuserlist[i][0]])

                l = l+1

            if l == 5:

                break

            i = i+1 


    i = 0
    j = 0
    
    
    

    for j in range (0,5) :

        
        movierecolist[j] = map(int, movierecolist[j])



    with open('movies.csv', 'rb') as csvfile:

        dataReader = csv.reader(csvfile, delimiter=',')

        for row in dataReader:

            if i < 5:
                
                
                if int(row[0]) == movierecolist[0][0]:
                    i= i+1
                    movienamelist.append([row[1]])

                elif int(row[0]) == movierecolist[1][0]:
                    i= i+1
                    movienamelist.append([row[1]])

                elif int(row[0]) == movierecolist[2][0]:
                    i= i+1
                    movienamelist.append([row[1]])

                elif int(row[0]) == movierecolist[3][0]:
                    i= i+1
                    movienamelist.append([row[1]])

                elif int(row[0]) == movierecolist[4][0]:
                    i= i+1
                    movienamelist.append([row[1]])


            else:
                break
                    


        print movienamelist



        with open('moviereco.csv', 'ab') as csvfile:

            for i in range (0,len(movienamelist)) :



                dataWr = csv.writer(csvfile, delimiter=',')
                dataWr.writerow([movienamelist[i][0]])
        
        





def eucli (compl_file, current_User):
    import csv
    f = open("currentUserID.txt", "r")
    enduserID = int(f.read())
    f.close()

    dist = 0.0

    distlist = []
    curtime = float(time.time())
    

    with open(compl_file, "rb") as csvfile:

        dataReader = csv.reader(csvfile, delimiter=',')

        for row in dataReader:

            if (float(curtime) - float(row[3])) > 157788000.0:

                dist = dist + ((float(row[1])-float(row[2]))**2)

            else:
        
                dist = dist + 2*((float(row[1])-float(row[2]))**2)


    dist = dist**(0.5)

    with open('dist.csv', 'ab') as csvfile:
                    
        dataWriter = csv.writer(csvfile, delimiter=',')
        dataWriter.writerow([enduserID]+[current_User]+[dist])

    distlist = csv_to_list('dist.csv')
    distlist = sorted (distlist, key= operator.itemgetter(2))

    






def compfn(curuser_file, enduser_file, current_User):
    

    euserlist = []
    curuserlist = []
    complist = []


    i=0
    j=0

    curuserlist = csv_to_list(curuser_file)
    euserlist = csv_to_list(enduser_file)



                
    euserlist = sorted (euserlist, key= operator.itemgetter(0))
    curuserlist = sorted (curuserlist, key= operator.itemgetter(0))

                    

    while (i<len(euserlist) and j<len(curuserlist)):


        if euserlist[i][0] < curuserlist[j][0]:
            complist.append([euserlist[i][0],euserlist[i][1],0,euserlist[i][2]])
            i=i+1
                            

        elif euserlist[i][0] > curuserlist[j][0]:
            complist.append([curuserlist[j][0],0,curuserlist[j][1],0])  
                     
            j=j+1
                            

        elif euserlist[i][0] == curuserlist[j][0]:

            complist.append([euserlist[i][0],euserlist[i][1],curuserlist[j][1],euserlist[i][2]])
            i=i+1
            j=j+1
                            
                            

                        



    if i< len(euserlist):
        while (i<len(euserlist)):

            complist.append([euserlist[i][0],euserlist[i][1],0,euserlist[i][2]])
            i=i+1
                            

    if j< len(curuserlist):
        while (j<len(curuserlist)):

            complist.append([curuserlist[j][0],0,curuserlist[j][1],0]) 
            j=j+1


                    
    with open("complist.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(complist)

    eucli ("complist.csv",current_User)







def collabf():

    
    fl = open("currentUserID.txt", "r")
    enduserID = int(fl.read())

    euserlist = []
    curuserlist = []
    complist = []

    rownolist = csv_to_list('StartRowFile.csv')

    currentUser = 1
    with open('ratings.csv', 'rb') as csvfile:

        dataReader = csv.reader(csvfile, delimiter=',')

        for row in dataReader:

            if row[0] == str(enduserID):

                with open('enduser.csv', 'ab') as csvfile:
                    
                    dataWriter = csv.writer(csvfile, delimiter=',')
                    dataWriter.writerow([row[1]]+[row[2]]+[row[3]])


                euserlist = csv_to_list('enduser.csv')


        
        ''' new loop for individual users'''
    with open('ratings.csv', 'rb') as csvfile:

        k=1
        dataReade = csv.reader(csvfile, delimiter=',')   
        
        for ro in dataReade:
            
            k= k+1
            
            if str(k) == rownolist[currentUser][1]:
                


                
                os.remove('complist.csv')
                os.remove('curuser.csv')
                
                if currentUser < 100:
                    
                    currentUser = currentUser + 1

                else:
                    
                    break 





            if str(k) != rownolist[currentUser][1]:

                with open('curuser.csv', 'ab') as csvfile:
                    dataWriter = csv.writer(csvfile, delimiter=',')
                    dataWriter.writerow([ro[1]]+[ro[2]])

                    if str(k+1) == rownolist[currentUser][1]:

                        compfn('curuser.csv','enduser.csv',currentUser)

    distlist = csv_to_list('dist.csv')
    distlist = sorted (distlist, key= operator.itemgetter(2))
    recolist(distlist)
    os.remove('enduser.csv')
    os.remove('dist.csv')
    os.remove('bestuser.csv')                
                 
                    

                
                
            
                




            












