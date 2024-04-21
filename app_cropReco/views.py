from django.shortcuts import render, redirect
from .forms import CropForms
import openai

openai.api_key = 'api key here'


# Create your views here.
def home(request):
    crop_models = None

    if request.method == 'POST':
        form = CropForms(request.POST)

        if form.is_valid():
            crop_models = form.save(commit=False)

            # Use OpenAI GPT-3 for text generation (chat-based model)
            prompt = f"Generate a crop recommendations based on the soil data inputted. Provide tips on how to have higher yield. Explain the things need to be adjusted based on the input :\n\nNitrogen: {crop_models.Nitrogen}\n\nPhosphorus: {crop_models.Phosphorus}\n\nPotassium: {crop_models.Potassium}\n\nTemperature: {crop_models.Temperature}\n\nHumidity: {crop_models.Humidity}\n\npH: {crop_models.pH}\n\nRainfall: {crop_models.Rainfall}\n\n"
            messages = [
                {"role": "system", "content": "You are a helpful and generous professional agriculturist consultant."},
                {"role": "user", "content": prompt},
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500
            )

            crop_models.crop_reco = response['choices'][0]['message']['content']
            crop_models.save()

            print("Crop Recommendation:", crop_models.crop_reco)  #for debugging purpose
            print("done with 500 tokens") #debugging

    else:
        form = CropForms()

    return render(request, 'app_cropReco/home.html', {'crop_models': crop_models})

