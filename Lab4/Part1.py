import matplotlib.pyplot as plt
import pandas as pd


def main():
    example()
    # task1()
    # task2()
    # task3()
    # task4()


def task1():
    df = pd.read_csv("DailySteps.csv")

    print(df.dtypes)

    list1 = df["ActivityDay"].values.tolist()
    list2 = df["StepTotal"].values.tolist()

    list1 = list1[:10]
    list2 = list2[:10]

    plt.plot(list1, list2)

    plt.show()


def task2():
    df = pd.read_csv("DailyDistance.csv")

    print(df.dtypes)

    list1 = df["ActivityDate"].values.tolist()
    list2 = df["TotalDistance"].values.tolist()

    list1 = list1[:10]
    list2 = list2[:10]

    plt.bar(list1, list2, width=1, color=["blue", "red", "green"])

    plt.show()


def task3():
    df = pd.read_csv("SleepDay.csv")

    print(df.dtypes)

    list1 = df["SleepDay"].values.tolist()
    list2 = df["TotalTimeInBed"].values.tolist()

    list1 = list1[:10]
    list2 = list2[:10]

    plt.scatter(list1, list2, c="yellow")

    plt.show()


def task4():
    df = pd.read_csv("HourlySteps.csv")

    print(df.dtypes)

    date = "4/12/2016"
    list1 = df[df["ActivityHour"].str[:9] == date]
    list2 = list1["StepTotal"].values.tolist()

    format = str(list2)

    plt.pie(list2, labels=list1, autopct=lambda p: "{:.0f}%".format(p))

    plt.show()


def example():
    df = pd.read_csv("population_by_country_2020.csv")

    print(df.dtypes)

    list1 = df["Country (or dependency)"].values.tolist()
    list2 = df["Population (2020)"].values.tolist()

    list1 = list1[:10]
    list2 = list2[:10]
    plt.bar(list1, list2, width=1, color=["red", "blue"])

    plt.show()


if __name__ == "__main__":
    main()
