def bitStuffing(N, bits):
    bstuff = ''
    flag = 0
    
    for i in bits:
        if i == '1':
            flag += 1
            bstuff += i 
        
        else: 
            flag = 0 
            bstuff += i
        
        if flag == 5:
            bstuff += '0' 
    
    print(bstuff)
                 

bits = input("Input: ")
n = len(bits)
bitStuffing(n, bits)

