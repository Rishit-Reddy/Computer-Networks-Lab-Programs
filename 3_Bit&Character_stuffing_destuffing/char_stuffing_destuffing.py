#Character stuffing 

flag = 'F'
esc = 'E'

def byte_stuffing(text):
    global flag,esc
    bstuffed_data = ''
    bstuffed_data += flag
    for i in text:
        if i == flag:
            bstuffed_data += esc
            bstuffed_data += i 
        elif i == esc:
            bstuffed_data += esc 
            bstuffed_data += i 
        else:
            bstuffed_data += i
    bstuffed_data += flag
    return bstuffed_data


def byte_destuffing(text):
    global flag,esc
    bdstuffed_text = ''
    added = False
    for i in range(1, len(text)-1):
        if added == True:
            added = False
            continue
        if text[i] == esc:
            if text[i+1] == flag or text[i+1] == esc:
                bdstuffed_text += text[i+1]
                added = True
        else:
            bdstuffed_text += text[i]
    return bdstuffed_text

#Sample
#Input : FDEFDFF
#output : Stuffed - FEFDEEEFDEFEFF
        # Destuffed - FDEFDFF

text = input("Message: ")
senders_text = byte_stuffing(text)
recv_text = byte_destuffing(senders_text)
print(f"Stuffed : {senders_text}")
print(f"Destuffed : {recv_text}")

