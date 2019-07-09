# import models
from sklearn import datasets, svm 
from sklearn import model_selection, metrics
import pickle
import numpy as np 


# load datasets 
iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y, test_size = 0.20, random_state = 12345)

svmModel = svm.SVC().fit(x_train,y_train)

y_pred = svmModel.predict(x_test)

print(metrics.accuracy_score(y_test, y_pred)*100)

svmFile = open('SVMmodel.pickle', 'wb')
pickle.dump(svmModel, svmFile)
svmFile.close()

print(x, y)