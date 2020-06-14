import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
import math

import time

def my_function():

    start_time = time.time()
    data = pd.read_csv("Data.csv")
    data = data.drop("id", axis=1)
    #print(data)
    
    #sns.countplot(x="y", data=data)
    
    
    #data.info()
    
    x = data.drop("y", axis=1)
    y = data["y"]
    
    from sklearn.model_selection import train_test_split
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=4)
    
    from sklearn.linear_model import LogisticRegression
    
    logmodel=LogisticRegression()
    logmodel.fit(x_train, y_train)
    
    prediction = logmodel.predict(x_test)
    
    from sklearn.metrics import classification_report
    
    cr = classification_report(y_test, prediction)
    
    #print(cr)
    
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_test, prediction)
    
    #print(cm)
    
    from sklearn.metrics import accuracy_score
    
    acs = accuracy_score(y_test, prediction)
    
    print("Accuracy: %s " % acs)
    
    execution_time=(time.time() - start_time)
    #print("--- %s seconds ---" % execution_time)
    return execution_time

