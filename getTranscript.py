def getTrans(trans_list):
    # i = 5
    text = ""
    for dict in trans_list:
        # text.join(dict['text'])
        text = text + dict['text'] + ' '
        # i = i - 1
        # if(i < 0):
        #     break
        
    return text
