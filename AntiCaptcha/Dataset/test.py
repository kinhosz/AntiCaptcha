from . import data, label

def get(path):
    path += 'test-'

    images = data.get(path)
    labels = label.get(path)

    assert images['header']['number_of_images'] == labels['number_of_images']

    tests = {
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

        tests['data'].append(test)
    
    return tests