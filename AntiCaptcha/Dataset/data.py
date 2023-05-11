def get(path):
    path += 'images-idx3-ubyte'

    f = open(path, 'rb')
    
    magic_number = int.from_bytes(f.read(4), byteorder='big')
    assert magic_number == 2051

    number_of_images = int.from_bytes(f.read(4), byteorder='big')
    rows = int.from_bytes(f.read(4), byteorder='big')
    columns = int.from_bytes(f.read(4), byteorder='big')

    imgs = {
        'header': {
            'number_of_images': number_of_images,
            'rows': rows,
            'columns': columns
        },
        'data': []
    }

    for _ in range(number_of_images):
        data = []
        for _ in range(rows * columns):
            pixel = int.from_bytes(f.read(1), byteorder='big', signed=False)
            data.append(pixel)

        imgs['data'].append(data)
    
    f.close()

    return imgs
