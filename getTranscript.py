def getTrans(trans_list):
    text = """"""
    i = 5
    for dict in trans_list:
        text = text + dict['text'] + ' '
        i = i - 1
        if(i < 0):
            break
        
    return text
