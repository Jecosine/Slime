def get_list(content):
    l = []
    #f = open("saved",'rb')
    #content = f.read()
    content = content[1:-1]
    elements = content.split('], [')
    temp = ""
    
    for element in elements:
        c = element.split(',')
        if c[0][0] == '[':
            c[0] = c[0][1:]
        if c[1][-1] == ']':
            c[1] = c[1][:-1]
        l.append([int(c[0]),int(c[1])])
    return l
      
