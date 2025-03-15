import boto3
import pickle
import io
from django.shortcuts import render
from django.http import JsonResponse

# AWS S3 Configuration
S3_BUCKET = "car-project16"
S3_FILE_KEY = "SECOND1.pkl"

# Function to load model from S3
def load_model_from_s3():
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=S3_BUCKET, Key=S3_FILE_KEY)
    model = pickle.load(io.BytesIO(obj['Body'].read()))
    return model

# Load model at startup
model = load_model_from_s3()

def predict_price(request):
    if request.method == "POST":
        year = int(request.POST["year"])
        km_driven = int(request.POST["km_driven"])
        fuel_type = request.POST["fuel_type"]
        
        # Prepare input data (modify according to your ML model)
        input_data = [[year, km_driven, 1 if fuel_type == "Petrol" else 0]]  # Example encoding
        
        prediction = model.predict(input_data)[0]
        
        return JsonResponse({"predicted_price": prediction})

    return render(request, "form.html")
