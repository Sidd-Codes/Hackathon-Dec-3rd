from ChatGPT import get_cal_for_exercise,get_meal_plan,get_food_calories


def handling(height, age, gender, weight, restrictions, calories_intake,comment):

    plan = get_meal_plan(height, age, gender, weight, restrictions, calories_intake,comment)

    
    b = plan[plan.find("Breakfast: ")+11: plan.find("Lunch:")]
    l = plan[plan.find("Lunch: ")+7: plan.find("Dinner: ")]
    d = plan[plan.find("Dinner: ")+8:]

    

    b = b.split(",")
    b_m = b[0].split("/") 
    b_s = b[1].split("/")
    b_d = b[2].split("/")

    l = l.split(",")
    l_m = l[0].split("/") 
    l_s = l[1].split("/")
    l_d = l[2].split("/")

    d = d.split(",")
    d_m = d[0].split("/") 
    d_s = d[1].split("/")
    d_d = d[2].split("/")
    
    content = [b_m, b_s, b_d, l_m, l_s, l_d,d_m,d_s,d_d]
    
    for food in content:
        food.append(get_food_calories(food[0],food[1]))
    
    #first element is the type, second element is the amount, third element is the calories
    
    return content

#print(handling(1.70,20,"Male",60,"a",2000))



