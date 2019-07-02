import glob
import matplotlib.pyplot as plt
import csv


def main():
    """This function plots .csv data loaded from S3 storage."""
    directory = 'D:\AWS_key\project\ploting\*.csv'
    all_filenames = [i for i in glob.glob(directory)]
    people = []
    for i in all_filenames:
        with open(i, 'rt') as f:
            data = csv.reader(f)
            for row in data:
                line = []
                for j in range(len(row)):
                    line.append(row[j])
                people.append(line)
    x = list(list(zip(*people))[0])
    y = list(list(zip(*people))[1])
    plt.bar(x, y)
    plt.show()


if __name__ == "__main__":
    main()
