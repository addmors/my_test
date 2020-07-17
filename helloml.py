# Загрузка библиотек
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Загрузка датасета
url = "sample.csv"
names = ['title', 'description', 'tonals']
dataset = read_csv(url, names=names)

# Разделение датасета на обучающую и контрольную выборки
array = dataset.values
# Выбор первых 2-х столбцов
X = array[:,0:4]
# Выбор 3-го столбца
y = array[:,4]
# Разделение X и y на обучающую и контрольную выборки 
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Создаем прогноз на контрольной выборке
