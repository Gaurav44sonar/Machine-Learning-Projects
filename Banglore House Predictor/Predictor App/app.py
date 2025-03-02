from flask import Flask,render_template,request
import pandas as pd
import pickle

data=pd.read_csv("Cleaned_House.csv")

model=pickle.load(open("LinearRegression_44.pkl",'rb'))

app=Flask(__name__)

@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template("index.html",locations=locations)

# @app.route('/predict',methods=['POST'])
# def predict():
#     location=request.form.get("location")
#     bhk=request.form.get("bhk")
#     bath=request.form.get("bath")
#     sqft=request.form.get("total_sqrt")

#     print(location, bhk,bath,sqft)

#     input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])

#     prediction=model.predict(input)[0]
#     print(prediction)


#     return str(prediction)

# if __name__=="__main__":
#     app.run(debug=True,port=5001)
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    location = request.form.get("location")
    bhk = request.form.get("bhk")
    bath = request.form.get("bath")
    sqft = request.form.get("total_sqrt")

    # Validate and convert inputs
    try:
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)
    except ValueError as e:
        return f"Error: Invalid input types. {str(e)}"

    # Create a DataFrame with correct column names and types
    input_data = pd.DataFrame([[location, sqft, bath, bhk]], 
                              columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Debug: Check input DataFrame
    print("Input DataFrame for prediction:")
    print(input_data)

    # Prediction step
    try:
        prediction = model.predict(input_data)[0]
        print("Prediction result:", prediction)
        return f"Predicted house price: {prediction:.2f}"
    except Exception as e:
        print("Error during prediction:", e)
        return f"Error: {str(e)}"



if __name__=="__main__":
     app.run(debug=True)
