import pandas as pd

def read_csv(file_name: str) -> pd.DataFrame:
    path = './data/' + file_name + '.csv'

    data = pd.read_csv(path, sep=',')

    return data

def main():
    df = read_csv('aum')

    print(df)

if __name__ == '__main__':
    main()