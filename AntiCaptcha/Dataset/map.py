def get(path):
    path += 'mapping.txt'

    f = open(path, 'r')
    txt = f.readline()

    mapper = {
        'num_classes': 0,
        'class': {}
    }

    while txt != None and txt != '':
        data = txt[:-1].split(' ')
        key = data[0]

        mapper['num_classes'] += 1

        if key not in mapper['class'].keys():
            mapper['class'][key] = []
        
        for i in range(1, len(data)):
            mapper['class'][key].append(data[i])
        
        txt = f.readline()

    f.close()
    
    return mapper