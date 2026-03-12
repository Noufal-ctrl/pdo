time_of_day = input("Enter time of day (morning/afternoon/evening/night): ").lower()
weather = input("Enter weather (sunny/rainy/cold/cloudy): ").lower()
mood = input("Enter mood (happy/tired/sad/hungry/energetic): ").lower()

food = "Salad"   


if time_of_day == "morning" and weather == "rainy" and mood == "tired":
    food = "Soup"

elif time_of_day == "morning" and mood == "happy":
    food = "Pancakes"

elif time_of_day == "morning" and weather == "cold":
    food = "Hot Coffee and Toast"

elif time_of_day == "afternoon" and mood == "hungry":
    food = "Rice and Curry"

elif time_of_day == "afternoon" and weather == "sunny":
    food = "Lemon Rice"

elif time_of_day == "afternoon" and mood == "tired":
    food = "Curd Rice"

elif time_of_day == "evening" and weather == "rainy":
    food = "Tea and Pakoda"

elif time_of_day == "evening" and mood == "happy":
    food = "Pizza"

elif time_of_day == "evening" and mood == "tired":
    food = "Sandwich"

elif time_of_day == "night" and mood == "hungry":
    food = "Chicken Biryani"

elif time_of_day == "night" and mood == "sad":
    food = "Ice Cream"

elif time_of_day == "night" and weather == "cold":
    food = "Hot Noodles"
  
elif weather == "rainy" and mood == "happy":
    food = "Masala Tea and Samosa"

elif weather == "sunny" and mood == "energetic":
    food = "Fruit Juice and Salad"

elif weather == "cloudy" and mood == "tired":
    food = "Maggi Noodles"

print("Food recommendation:", food)



###    OUTPUT    ###
Enter time of day (morning/afternoon/evening/night): morning
Enter weather (sunny/rainy/cold/cloudy): rainy
Enter mood (happy/tired/sad/hungry/energetic): tired
Food recommendation: Soup
