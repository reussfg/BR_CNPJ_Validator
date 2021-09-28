from func_test1 import ftest

while True:
    # My testing Variables
    test1  =[5,4,3,2,9,8,7,6,5,4,3,2]
    test2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    entry_CNPJ = input('Type CNPJ: ')

    # Testing the valid format and converting to numbers
    if entry_CNPJ.isdecimal() == False:
        CNPJ_semponto = entry_CNPJ.replace('.', '')
        CNPJ_semtraco = CNPJ_semponto.replace('/', '')
        CNPJ = CNPJ_semtraco.replace('-', '')
    else:
        CNPJ = entry_CNPJ
    if len(CNPJ) <= 13:
        print('CNPJ is incorrect, type it again. ')
        continue

    # Transforming into integer
    int_CNPJ = [int(i) for i in list(CNPJ)]

    # Starting analysis - First Test
    if not ftest(int_CNPJ,test1) == int(str(CNPJ[12])):
        print('Invalid CNPJ. ')
        continue

    # Continue analysis - Second Test - Final
    if not ftest(int_CNPJ,test2) == int(str(CNPJ[13])):
        print('Invalid CNPJ.  ')
        continue
    print('Valid CNPJ!')
    break

