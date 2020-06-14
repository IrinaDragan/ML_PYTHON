from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
from pydot import graph_from_dot_data
import pandas as pd
import time

def my_DT_function():

    start_time = time.time()
    data = pd.read_csv("Data.csv")
    data = data.drop("id", axis=1)
    
    feature_names = data.drop("y", axis=1).keys()
    
    x = data.drop("y", axis=1)
    y = data["y"]
    
    
    from sklearn.model_selection import train_test_split
        
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=4)
    
    dt = DecisionTreeClassifier()
    
    dt.fit(x_train, y_train)
    
    dot_data = StringIO()
    
    export_graphviz(dt, out_file=dot_data, feature_names=feature_names)
    
    (graph, ) = graph_from_dot_data(dot_data.getvalue())
     
    prediction = dt.predict(x_test)
    
    from sklearn.metrics import classification_report
    cr = classification_report(y_test, prediction)
    
    print(cr)
    
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_test, prediction)
    
    print(cm)
    
    from sklearn.metrics import accuracy_score
    
    acs = accuracy_score(y_test, prediction)
    
    print("Accuracy: %s" % acs)
    
    execution_time=(time.time() - start_time)
    #print("--- %s seconds ---" % execution_time)
    return execution_time








