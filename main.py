from functions import *
from IPython.display import display

if __name__ == "__main__":
    data = create_ann("C:\\Proganiy\\pp-laba3\\annotation.csv")
    stat = word_stat(data)
    data = sort_word(data)
    display(stat)