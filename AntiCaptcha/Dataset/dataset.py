from . import map, test, train

options = ['balanced', 'byclass', 'bymerge', 'digits', 'letters', 'mnist']

def get(option):
    if option not in options:
        raise Exception("Cannot find this dataset option: {}".format(option))
    
    path = '...EMNIST/' + option + '/emnist-' + option + '-'

    dataset_map = map.get(path)
    dataset_test = test.get(path)
    dataset_train = train.get(path)

    dataset = {
        'map': dataset_map,
        'test': dataset_test,
        'train': dataset_train
    }

    return dataset
    
    