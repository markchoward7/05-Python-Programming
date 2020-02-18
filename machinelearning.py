# import numpy
# import matplotlib.pyplot as plt

# myarray = numpy.array([1,2,3])
# plt.plot(myarray)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.show()

# from sklearn import datasets
# from sklearn import metrics
# from sklearn.tree import DecisionTreeClassifier
# # load the iris datasets
# dataset = datasets.load_iris()
# # fit a CART model to the data
# model = DecisionTreeClassifier()
# model.fit(dataset.data, dataset.target)
# print(model)
# # make predictions
# expected = dataset.target
# predicted = model.predict(dataset.data)
# # summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))

# from sklearn import svm
# from sklearn import datasets
# import pickle

# clf = svm.SVC()
# X, y = datasets.load_iris(return_X_y=True)
# clf.fit(X, y)
# s = pickle.dumps(clf)
# clf2 = pickle.loads(s)
# clf2.predict(X[0:1])
# print(y[0])