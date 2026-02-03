"""
This is a reusable classifier. 
A classifier should be able to be trained, as well as to be able to make predictions
these functions share the same data
"""

import sklearn

#common classifiers are in scikit learm
#some of the best are their own (xgboost)

class ReusableClassifier:
    def __init__(self, model_type:str='logistic_regression'):
        #ALL shared variables must be definined in init
        self.model=None
        self.model_type=model_type
        self.scalar=None
    """Create a reusable classifier

    Args:
        model_type (str, optional): model type can be either 
        logistic_regression or random_forest. Defaults to logistic_regression.
    """

    def train(self,features,labels):
        """
        Trains the model based on features and labels. Different algorithms will use different 
        methods of evaluating training
        """
        if self.model_type=='logistic_regression':
            self.model=sklearn.linear_model.LogisticRegression()
        #we NEED to scale data for regression 
        #can use standard scalar to normalize, 
        #or min max to make it 0-1.
        self.scalar=sklearn.preprocessing.StandardScaler()
        features=self.scaler.transform(features)
        self.model.fit(features,labels)

    def predict(self,features):
        """
        Predict labels using model_type from features.
        Args:
            features(_type_): Features MUST be the same types as in the training data, and in the same order
        """
        features=self.scalar.transform(features)
        return self.model.predict(features)#we can use predict_proba to return prob instead of t/f

    def assess(self,features,labels):
        """Assess how well the classifier performed."""
        predictions=self.predict(features)
        return np.sum(predictions)
        pass

    def save(self):
        pass

    def load(self):
        pass

if __name__=='__main__':
    rc=ReusableClassifier()