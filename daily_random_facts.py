import requests

# Your Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1303832723403837440/NLACa7xsg3nWLVp98PliXP7a7CeuI_e_maJZ8G0nxX_eWGIxcZAxWMTSPUUorTnFr9SO"

# Function to get a random dad joke from the Dad Joke API
def get_random_dad_joke():
    url = "https://icanhazdadjoke.com/"  # Dad Joke API endpoint
    headers = {"Accept": "application/json"}  # The API requires this header for JSON response

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        joke = response.json()  # Parse the JSON response
        return joke["joke"]  # Extract the joke text
    else:
        return "Failed to retrieve a dad joke."

# Function to send the dad joke to Discord
def send_joke_to_discord(joke):
    data = {
        "content": f"Good morning! Here's a dad joke for you: {joke}"  # Format the joke to be sent in Discord
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print(f"Successfully sent joke: {joke}")
    else:
        print(f"Failed to send joke. Status code: {response.status_code}")

# Main function to fetch and send the dad joke when you run the script
def send_random_dad_joke():
    joke = get_random_dad_joke()  # Get a random dad joke from the API
    send_joke_to_discord(joke)  # Send the joke to Discord

# Run the script by calling the main function
if __name__ == "__main__":
    send_random_dad_joke()
