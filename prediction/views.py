from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from ml_model.predict import predict_crop


# ============================================================
# CROP RECOMMENDATIONS
# ============================================================

RECOMMENDATIONS = {

    "rice": {
        "water": "High water requirement",
        "soil": "Suitable for fertile and clayey soil",
        "nutrient": "Maintain balanced Nitrogen, Phosphorus and Potassium",
        "climate": "Warm and humid climate is suitable"
    },

    "maize": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Requires good Nitrogen and balanced NPK levels",
        "climate": "Warm climate with adequate sunlight is suitable"
    },

    "cotton": {
        "water": "Moderate water requirement",
        "soil": "Well-drained black soil is suitable",
        "nutrient": "Maintain balanced Nitrogen, Phosphorus and Potassium",
        "climate": "Warm climate with moderate rainfall is suitable"
    },

    "wheat": {
        "water": "Moderate water requirement",
        "soil": "Fertile and well-drained soil is suitable",
        "nutrient": "Requires balanced NPK nutrients",
        "climate": "Cool and dry climate is suitable"
    },

    "chickpea": {
        "water": "Low to moderate water requirement",
        "soil": "Well-drained soil is suitable",
        "nutrient": "Requires balanced nutrients with suitable phosphorus",
        "climate": "Cool and relatively dry climate is suitable"
    },

    "kidneybeans": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Maintain balanced nutrients",
        "climate": "Moderate warm climate is suitable"
    },

    "pigeonpeas": {
        "water": "Moderate water requirement",
        "soil": "Well-drained soil is suitable",
        "nutrient": "Balanced NPK is recommended",
        "climate": "Warm climate is suitable"
    },

    "mothbeans": {
        "water": "Low water requirement",
        "soil": "Sandy and well-drained soil is suitable",
        "nutrient": "Maintain suitable nutrient levels",
        "climate": "Warm and dry climate is suitable"
    },

    "mungbean": {
        "water": "Moderate water requirement",
        "soil": "Well-drained soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm climate is suitable"
    },

    "blackgram": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Balanced nutrient levels are recommended",
        "climate": "Warm climate is suitable"
    },

    "lentil": {
        "water": "Low to moderate water requirement",
        "soil": "Well-drained loamy soil is suitable",
        "nutrient": "Balanced nutrients are recommended",
        "climate": "Cool and dry climate is suitable"
    },

    "pomegranate": {
        "water": "Moderate water requirement",
        "soil": "Well-drained loamy soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm and relatively dry climate is suitable"
    },

    "banana": {
        "water": "High water requirement",
        "soil": "Rich and well-drained soil is suitable",
        "nutrient": "Requires good Nitrogen and Potassium levels",
        "climate": "Warm and humid climate is suitable"
    },

    "mango": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm climate is suitable"
    },

    "grapes": {
        "water": "Moderate water requirement",
        "soil": "Well-drained soil is suitable",
        "nutrient": "Balanced nutrients are recommended",
        "climate": "Warm and relatively dry climate is suitable"
    },

    "watermelon": {
        "water": "Moderate to high water requirement",
        "soil": "Sandy loamy and well-drained soil is suitable",
        "nutrient": "Balanced NPK with suitable potassium is recommended",
        "climate": "Warm climate is suitable"
    },

    "muskmelon": {
        "water": "Moderate water requirement",
        "soil": "Sandy loamy and well-drained soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm climate is suitable"
    },

    "apple": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Cool climate is suitable"
    },

    "orange": {
        "water": "Moderate water requirement",
        "soil": "Well-drained loamy soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm and moderately humid climate is suitable"
    },

    "papaya": {
        "water": "Moderate water requirement",
        "soil": "Well-drained fertile soil is suitable",
        "nutrient": "Requires balanced Nitrogen and Potassium",
        "climate": "Warm and humid climate is suitable"
    },

    "coconut": {
        "water": "High water requirement",
        "soil": "Well-drained sandy loam soil is suitable",
        "nutrient": "Requires balanced NPK nutrients",
        "climate": "Warm and humid climate is suitable"
    },

    "jute": {
        "water": "High water requirement",
        "soil": "Fertile and well-drained soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm and humid climate is suitable"
    },

    "coffee": {
        "water": "Moderate water requirement",
        "soil": "Rich, well-drained soil is suitable",
        "nutrient": "Balanced NPK nutrients are recommended",
        "climate": "Warm and humid climate is suitable"
    }
}


# ============================================================
# REGISTER
# ============================================================

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(
                request,
                "register.html",
                {"error": "Passwords do not match."}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register.html",
                {"error": "Username already exists."}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect("/login/")

    return render(request, "register.html")


# ============================================================
# LOGIN
# ============================================================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("/")

        else:

            return render(
                request,
                "login.html",
                {"error": "Invalid username or password."}
            )

    return render(request, "login.html")


# ============================================================
# LOGOUT
# ============================================================

def logout_view(request):

    logout(request)

    return redirect("/login/")


# ============================================================
# CROP PREDICTION
# ============================================================

@login_required(login_url="/login/")
def predict_view(request):

    if request.method == "POST":

        N = float(request.POST.get("N"))
        P = float(request.POST.get("P"))
        K = float(request.POST.get("K"))
        temperature = float(request.POST.get("temperature"))
        humidity = float(request.POST.get("humidity"))
        ph = float(request.POST.get("ph"))
        rainfall = float(request.POST.get("rainfall"))

        crop = predict_crop(
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        )

        recommendation = RECOMMENDATIONS.get(
            crop.lower(),
            {
                "water": "Check local water requirements",
                "soil": "Check soil suitability",
                "nutrient": "Maintain balanced nutrients",
                "climate": "Check suitable climate conditions"
            }
        )

        return render(
            request,
            "predict.html",
            {
                "crop": crop,
                "recommendation": recommendation
            }
        )

    return render(request, "predict.html")