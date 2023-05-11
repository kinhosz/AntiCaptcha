from . import data, label

def get(path):
    path += 'train-'

    images = data.get(path)
    labels = label.get(path)

    assert images['header']['number_of_images'] == labels['number_of_images']

    trains = {
        'header': {
            'number_of_images': labels['number_of_images'],
            'rows': images['header']['rows'],
            'columns': images['header']['columns']
        },
        'data': []
    }

    for img, lbl in zip(images['data'], labels['label']):
        test = {
            'image': img,
            'label': lbl
        }

        trains['data'].append(test)
    
    return trains