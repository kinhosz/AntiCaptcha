from CharReader import CharReader

def main():
    print('initializing robot')
    robot = CharReader(1)
    print('finished')
    robot.train(epoch=100, learnRate=1.0, logInfo=True)

if __name__ == "__main__":
    main()