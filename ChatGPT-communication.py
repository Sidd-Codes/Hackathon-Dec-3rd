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
input_text = "Could you tell me the largest country on earth?"
gpt_response = generate_gpt_response(input_text)

if gpt_response:
    print("GPT Response:")
    print(gpt_response)
else:
    print("Failed to generate GPT response.")