def evaluate(model, X_test, y_test):
    from sklearn.metrics import accuracy_score
    pred = model.predict(X_test)
    return accuracy_score(y_test, pred)