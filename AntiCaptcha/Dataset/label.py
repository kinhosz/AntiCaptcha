def get(path):
    path += 'labels-idx1-ubyte'

    f = open(path, 'rb')
    
    magic_number = int.from_bytes(f.read(4), byteorder='big')
    assert magic_number == 2049

    number_of_images = int.from_bytes(f.read(4), byteorder='big')

    labels = {
        'number_of_images': number_of_images,
        'label': []
    }

    for _ in range(number_of_images):
        label = int.from_bytes(f.read(1), byteorder='big', signed=False)
        labels['label'].append(label)
    
    f.close()

    return labels
