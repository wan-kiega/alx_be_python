def weather_advice(weather):
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat"
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf"
    else:
        return "Sorry, I don't have advice for that kind of weather."
print(str(weather_advice(input("What is the current weather? (sunny, rainy, cold): ").strip().lower())))