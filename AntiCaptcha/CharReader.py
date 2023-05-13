import random
import Dataset
from Deep import Neural, CNeural
from utils import *
from timeit import default_timer as timer

learnMode = {
    1: 'balanced',
    2: 'byclass',
    3: 'bymerge',
    4: 'digits',
    5: 'letters'
}

class CharReader(object):
    def __init__(self, mode):
        if mode not in learnMode.keys():
            raise Exception('mode is within [1, 5]')
        
        self.__dataset = Dataset.get(learnMode[mode])

        inputLayer = self.__dataset['train']['header']['rows'] * self.__dataset['train']['header']['columns']
        outputLayer = self.__dataset['map']['num_classes']

        self.__outputSize = outputLayer
        self.__inputSize = inputLayer

        self.__network = CNeural(sizes=[inputLayer, 100, 100, 100, outputLayer], eta=0.1)
    
    def __train(self):
        dataset = self.__dataset['train']['data']

        random.shuffle(dataset)

        for data in dataset:
            img = data['image']
            lbl = data['label']

            probDensity = probDensityArr(lbl, self.__outputSize)

            self.__network.learn(img, probDensity)

    def __test(self):
        dataset = self.__dataset['test']['data']

        hits = 0

        for data in dataset:
            img = data['image']
            lbl = data['label']

            predictArr = self.__network.send(img)
            predict = sortByProb(predictArr)[0][0]

            if predict == lbl:
                hits += 1
        
        imgs = self.__dataset['test']['header']['number_of_images']
        rate = hits/imgs

        return rate

    def __logger(self, epoch, totalEpochs, rate, runtime):
        txt = "EPOCH[{}/{}]: {}%% of rate".format(epoch, totalEpochs, round(100 * rate, 2))

        if runtime < 1.0:
            runtime *= 1000
            txt += " [{} milliseconds]".format(round(runtime, 3))
        elif runtime < 60:
            txt += " [{} seconds]".format(round(runtime, 3))
        elif runtime < 3600:
            runtime /= 60
            txt += " [{} minutes]".format(round(runtime, 3))
        else:
            runtime /= 3600
            txt += " [{} hours]".format(round(runtime, 3))
        
        print(txt)
    
    def train(self, epoch, learnRate, logInfo=False):
        upLearnRate = 0
        
        for i in range(epoch):
            epoch_runtime = timer()

            self.__train()
            rate = self.__test()
            if rate < learnRate:
                upLearnRate = 0
            else:
                upLearnRate += 1
            
            epoch_runtime = timer() - epoch_runtime
            
            if logInfo:
                self.__logger(i, epoch, rate, epoch_runtime)
            
            if upLearnRate > 10:
                break
