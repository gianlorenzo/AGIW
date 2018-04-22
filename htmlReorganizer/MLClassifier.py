from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction import DictVectorizer
import pandas

vec = DictVectorizer()

df = pandas.read_csv('/home/gianlorenzo/PycharmProjects/AGIW/htmlReorganizer/file_name.csv')
trainTarget = vec.fit_transform( df[['target']])
t2 = vec.fit(df[df.columns[1:5]])

model = LogisticRegression(()).fit(t2,trainTarget)
