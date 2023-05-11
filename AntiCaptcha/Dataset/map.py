def get(path):
    path += 'mapping.txt'

    f = open(path, 'r')
    txt = f.readline()

    mapper = {}

    while txt != None:
        data = txt.split(' ')
        key = data[0]

        if key not in mapper.keys():
            mapper[key] = []
        
        for i in range(1, len(data)):
            mapper[key].append(data[i])

    f.close()
    
    return mapper