import pandas as pd
import numpy as np
import pickle

from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder

if __name__ == "__main__":
    dataset = pd.read_csv("Iris.csv")

    X = dataset[["SepalLengthCm", "SepalWidthCm"]].to_numpy()
    y = dataset["Species"].to_numpy()

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    with open("model/label_encoder.pickle", "wb") as f:
        pickle.dump(label_encoder, f)

    kf = KFold(shuffle=True, n_splits=5)

    train_acc_list = []
    train_precision_list = []
    train_recall_list = []
    train_f1_list = []

    # Train and evaluate model using k-fold cross validation
    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        svc = SVC()

        svc.fit(X_train, y_train)
        y_pred = svc.predict(X_test)

        train_acc_list.append(accuracy_score(y_test, y_pred))
        train_precision_list.append(precision_score(y_test, y_pred, average='macro'))
        train_recall_list.append(recall_score(y_test, y_pred, average='macro'))
        train_f1_list.append(f1_score(y_test, y_pred, average='macro'))

    # Print/write train metrics
    train_acc = round(np.mean(train_acc_list), 3)
    train_precision = round(np.mean(train_precision_list), 3)
    train_recall = round(np.mean(train_recall_list), 3)
    train_f1 = round(np.mean(train_f1_list), 3)

    print("Train accuracy: " + str(train_acc))
    print("Train precision: " + str(train_precision))
    print("Train recall: " + str(train_recall))
    print("Train f1 score: " + str(train_f1))

    # Write train metrics
    result_metrics = [[train_acc, train_precision, train_recall, train_f1]]
    result_df = pd.DataFrame(result_metrics)

    result_df.to_csv('train_result.csv', index=False, header=False)

    # Train the model on the entire dataset
    svc = SVC()
    svc.fit(X, y)

    with open("model/model.pickle", "wb") as f:
        pickle.dump(svc, f)
