import pandas 
import string
import nltk


def create_ann(annatation: str) -> pandas.DataFrame:

    """Создаёт датафрейм по пути аннатации"""

    frame = pandas.DataFrame(columns =["Оценка","Kоличество слов","Текст рецензии"])
    ann_temp = open(annatation, "r", encoding="utf-8")
    for otzv in ann_temp.readlines():
        mas_otzv = otzv.split(",")
        otzv_temp = open(mas_otzv[0],"r",encoding="utf-8")
        otzv_text = " ".join(otzv_temp)
        row = pandas.Series({"Оценка": int(mas_otzv[2]),"Kоличество слов": len(otzv_text), "Текст рецензии": otzv_text})
        new_row = pandas.DataFrame([row], columns=frame.columns)
        frame = pandas.concat([frame, new_row], ignore_index=True)
    frame.dropna()
    return frame


def sort_word(frame: pandas.DataFrame) -> pandas.DataFrame:
    
    """Сортирует заданный датафрейм по количеству слов"""

    return frame.sort_values(['Kоличество слов'], ascending = False)


def sort_count_word(frame: pandas.DataFrame, count: int) -> pandas.DataFrame:
    
    """Сортирует заданный датафрейм по количеству слов, меньших или равных заданному значению"""

    return frame.loc[frame['Kоличество слов']<=count]



def sort_star(frame: pandas.DataFrame) -> pandas.DataFrame:
    
    """Сортирует заданный датафрейм по количеству звёзд"""

    return frame.sort_values(['Оценка'], ascending = False)

def info(frame: pandas.DataFrame) -> None:
    
    """Печатает информацию о заданном ДатаФрейме"""

    print(frame.describe())

def sort (frame: pandas.DataFrame, clas: str) -> pandas.DataFrame:

    """Сортирует заданный датафрейм по заднному признаку"""

    return frame.sort_values([clas],ascending = False)

def word_stat (frame: pandas.DataFrame) -> pandas.DataFrame:

    """Группирует заданный датафрейм по оценкам и вычисляет для них минимальное количество, слов максимальное и среднее"""

    frame = frame.drop("Текст рецензии", axis=1)
    temp = frame.groupby("Оценка")
    max_word = temp.max().values.tolist()
    min_word = temp.min().values.tolist()
    mid_word = temp.mean().values.tolist()

    max_word=sum(max_word, [])
    min_word=sum(min_word, [])
    mid_word=sum(mid_word, [])
    
    temp = pandas.DataFrame({"Оценка":["1","2","3","4","5"]})
    temp["max"]=max_word
    temp["min"]=min_word
    temp["mid"]=mid_word
    return(temp)
    
    
    
    