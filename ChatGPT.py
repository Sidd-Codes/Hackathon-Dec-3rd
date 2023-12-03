from openai import OpenAI

client = OpenAI(api_key="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")

# Set your OpenAI GPT API key


def generate_gpt_response(prompt, model="text-davinci-003", temperature=0.7, max_tokens=150):
    """
    Generate a response from the OpenAI GPT API.

    Parameters:
    - prompt: The input text prompt.
    - model: The GPT model to use (e.g., "text-davinci-003").
    - temperature: Controls the randomness of the generated response (between 0 and 1).
    - max_tokens: Limit the length of the generated response.

    Returns:
    - The generated response from GPT.
    """
    try:
        response = client.completions.create(model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating GPT response: {e}")
        return None

# Example usage:
#input_text = "Could you tell me the largest country on earth?"
#gpt_response = generate_gpt_response(input_text)

#if gpt_response:
#    print("GPT Response:")
#    print(gpt_response)
#else:
#    print("Failed to generate GPT response.")

def get_cal_for_exercise(exercise,weight):
    prompt = "A person is " + str(weight) + "kg. This is the exercise that person does: " + exercise + ". Please respond with your best estimate for the calories burnt: (Please only limit your response to a single number) Example output:100" 
    response = float(generate_gpt_response(prompt))
    return response

#print(get_cal_for_exercise("running for an hour",60))

def get_meal_plan(height, age, gender, weight, restrictions, calories_intake, comments = ""):
    if gender == "other":
        gender = "non-binary"
    prompt = "A person is " + str(height) + "m, " + str(weight) + "kg and " + str(age) + " years old. " + "The person's gender is " + str(gender) + ". "
    if len(restrictions) != 0:
        prompt = prompt + "This person have the following diet restrictions: "
        for r in restrictions:
            prompt = prompt + r + ","
    prompt = prompt + ". The goal for calories intake is " + str(calories_intake) + " calories.\n"
    prompt = prompt + "Here is some comments from the person, please take this into account: " + comments + "\n"
    prompt = prompt+ "Please plan the three meals (breakfast, lunch and dinner) in a day for the person and try not to repeat the same type of food, each meal contains the following details:(main dish/figurtive amount, side dish/figurtive amount, drink/figurtive amount). For example, you want the person to have bread, egg and milk for breakfast, chicken sandwich, tomato, coffee for lunch, pasta, mushroom and apple juice for dinner."
    prompt = prompt + "Example output:\nBreakfast: Bread/one piece, Egg/one, Milk/a small cup\nLunch: Chicken Sandwich/a medium one, Tomato/three slices, Coffee/a small cup\nDinner: Pasta/a medium bowl, Mushroom/five slices, Apple Juice/a medium cup"
    
    plan = generate_gpt_response(prompt)
    

    
    plan = plan.split("\n")
    for meal in plan:
        if len(meal) == 0:
            plan.remove(meal)
        elif meal[0] != "B" and meal[0] != "L" and meal[0] != "D" and meal[0] !="M":
            plan.remove(meal)
    
    response = ""
    
    for meal in plan:
        response = response + meal
    
    return response

def get_food_calories(food_type,amount):
    prompt = "Estimate the calories contained in the following food: " + amount + " of " + food_type + ". Please only return the number. Example output: 100"
    
    response = generate_gpt_response(prompt)
    
    for letter in response:
        if letter.isnumeric() == False:
            response.replace(letter,"")
    
    
    return response

#plan = get_meal_plan(1.70,20,"Male",60,"a",2000)
#print(plan)

#print(get_food_calories("apple", "one"))