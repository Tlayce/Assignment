# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:30:50 2023

@author: godfr
"""


#all car prices
Camry=10000
Corolla=20000 
Avalon=30000
Century=40000
Crown=50000
Mirai=60000
Wigo=70000
Etios=80000
Vauxhaul=90000
Astra= 100000
C10=50000
C20=60000
C30=70000
C40=80000
C50=90000
C60=100000
C70=110000
C80=120000
C90=130000
C100=140000
B10=50000
B20=60000
B30=70000
B40=80000
B50=90000
B60=100000
B70=110000
B80=120000
B90=130000
B100=140000


from tabulate import tabulate
print('Welcome To The O Car Dealership')
print()
typer=str(input('Specify car Brand wanted: '))
if typer=='Toyota' or 'Mercedes' or 'Mclaren':
    print('Sorry our search system is currently offline please manually select from available Brand list below')
else:
    print("Sorry our search system is currently offline please manually select from available Brand list below")

print('Car Brands Available')
print('(1)Toyota \
      (2)Mercedes \
      (3)Mclaren ')
    
    
brand=str(input('Specify car Brand using name in list above(Case Sensitive): '))   


if brand=='Toyota':
    print('These are the TOYOTA Cars Available')
    data = [[1,"Camry", 2023,], 
        [2,"Corolla", 2020], 
        [3,"Avalon", 2023],
        [4,"Century", 2020],
        [5,"Crown", 2013],
        [6,"Mirai", 2017],
        [7,"Wigo", 2018],
        [8,"Etios", 2019],
        [9,"Vauxhaul", 2012],
        [10,"Astra", 2016]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {}'.format(Camry))
     print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='2':
      print('This car costs GHS {}'.format(Corolla))
      print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='3':
        print('this car costs GHS {}'.format(Avalon))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='4':
        print('this car costs GHS {}'.format(Century))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='5':
        print('this car costs GHS {}'.format(Crown))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='6':
        print('this car costs GHS {}'.format(Mirai))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='7':
        print('this car costs GHS {}'.format(Wigo))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='8':
        print('this car costs GHS {}'.format(Etios))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='9':
        print('this car costs GHS {}'.format(Vauxhaul))  
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='10':
         print('this car costs GHS {}'.format(Astra))  
         print('Head to the Payment Section of the building to confirm purchase')
    else:
         print()
         print('Invalid Selection, Please Run The Program Again')



elif brand=='Mercedes':
    print('These are the MERCEDES Cars Available')
    data = [[1,"C10", 2023], 
        [2,"C20", 2023], 
        [3,"C30", 2023], 
        [4,"C40", 2023],
        [5,"C50", 2023],
        [6,"C60", 2023],
        [7,"C70", 2023],
        [8,"C80", 2023],
        [9,"C90", 2023],
        [10,"C100", 2023]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {}'.format(C10))
     print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='2':
      print('this car costs GHS {}'.format(C20))
      print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='3':
        print('this car costs GHS {}'.format(C30))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='4':
        print('this car costs GHS {}'.format(C40))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='5':
        print('this car costs GHS {}'.format(C50))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='6':
        print('this car costs GHS {}'.format(C60))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='7':
        print('this car costs GHS {}'.format(C70))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='8':
        print('this car costs GHS {}'.format(C80))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='9':
        print('this car costs GHS {}'.format(C90))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='10':
         print('this car costs GHS {}'.format(C100))
         print('Head to the Payment Section of the building to confirm purchase') 
    else:
        print()
        print('Invalid Selection, Please Run The Program Again')





elif brand=='Mclaren':
    print('These are the MCLAREN Cars Available')
    data = [[1,"C10", 2022], 
        [2,"B20", 2022], 
        [3,"B30", 2022], 
        [4,"B40", 2022],
        [5,"B50", 2022],
        [6,"B60", 2022],
        [7,"B70", 2022],
        [8,"B80", 2022],
        [9,"B90", 2022],
        [10,"B100", 2022]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {}'.format(B10))
     print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='2':
      print('this car costs GHS {}'.format(B20))
      print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='3':
        print('this car costs GHS {}'.format(B30))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='4':
        print('this car costs GHS {}'.format(B40))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='5':
        print('this car costs GHS {}'.format(B50))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='6':
        print('this car costs GHS {}'.format(B60))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='7':
        print('this car costs GHS {}'.format(B70))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='8':
        print('this car costs GHS {}'.format(B80))
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='9':
        print('this car costs GHS {}'.format(B90)) 
        print('Head to the Payment Section of the building to confirm purchase')
    elif totype=='10':
         print('this car costs GHS {}'.format(B100))
         print('Head to the Payment Section of the building to confirm purchase')
    else:
        print()
        print('Invalid Selection, Please Run The Program Again')
 
         
    
else:
    print()
    print('Invalid Selection Run The Program Again')
    print('Please use type name correctly(case sensitive)')
    print('example ; "Toyota"   NB:without quotes')

print()    
print('Thank You')
     



