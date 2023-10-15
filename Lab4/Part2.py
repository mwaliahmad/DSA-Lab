import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = LoadFile()
    names = df.columns
    list1 = []
    for i in range(0,len(names)):
        abc = df[names[i]].tolist()
        list1.append(abc)
        list2 = df[names[len(names)-1]].tolist()
    DrawGraph(list1, list2)
    
def LoadFile():
    df = pd.read_csv('Train.csv')
    return df

def DrawGraph(list1, list2):
    
    plt.scatter(list1, list2, s=10, c='b', marker="s", label='first')
    plt.show()
    

if __name__ == "__main__":
    main()