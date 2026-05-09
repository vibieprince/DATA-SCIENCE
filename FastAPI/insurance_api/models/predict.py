import pickle
import pandas as pd
with open('models/model.pkl','rb') as f:
    model = pickle.load(f)

# yahan abhi aise hee mannually humne ek model version likh diya hai but wo ek Mlfow jaise software se aata hai
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input :dict):
    df =  pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0] #ek list milegi but uska bas hume 0th item chahiye hoga jo ki hamara predcition ka result hoga

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    # Create mapping : {class_name: Probability}
    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))

    return{
        "predicted_category" : predicted_class,
        "confidence" : round(confidence,4),
        "class_probabilities": class_probs
    }