import speech_recognition as sr
from gtts import gTTS
import io
import sounddevice as sd
import soundfile as sf

# Initialize recognizer
recognizer = sr.Recognizer()

# Assistant speech
def assistant_speak(text):
    tts = gTTS(text=text, lang='en')
    with io.BytesIO() as audio_file:
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        audio_data, sample_rate = sf.read(audio_file, dtype='float32')
        sd.play(audio_data, samplerate=sample_rate)
        sd.wait()  # Wait until the sound has finished playing

# Listen for voice command
def listen_for_command():
    with sr.Microphone() as source:
        assistant_speak("Listening for command...")
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        assistant_speak("Sorry, I did not catch that. Please repeat.")
        return None
    except sr.RequestError:
        assistant_speak("Network error. Please check your connection.")
        return None

# Interpret voice command for budget or category selection
def interpret_command(command):
    if "budget" in command:
        budget_value = [int(word) for word in command.split() if word.isdigit()]
        if budget_value:
            budget = budget_value[0]
            assistant_speak(f"Setting budget to {budget}")
            return {'budget': budget}
    if "category" in command:
        categories = ['Electronics', 'Clothing', 'Home', 'Books']  # Example categories
        for category in categories:
            if category.lower() in command:
                assistant_speak(f"Selecting {category}")
                return {'category': category}
    return None

# Add product via voice command
def interpret_add_to_cart(command, shopping_cart, product_data):
    if "add" in command and "cart" in command:
        product_id = [int(word) for word in command.split() if word.isdigit()]
        if product_id:
            add_to_cart(product_id[0], shopping_cart, product_data)

def add_to_cart(product_id, shopping_cart, product_data):
    product = product_data[product_data['ProductID'] == product_id]
    if not product.empty:
        shopping_cart.append({
            "ProductName": product['ProductName'].values[0],
            "Price": product['Price'].values[0]
        })
        assistant_speak(f"Product {product_id} has been added to your cart.")
    else:
        assistant_speak("Product not found.")

# Handle checkout process
def checkout(shopping_cart):
    if shopping_cart:
        assistant_speak("Proceeding to checkout with the following items:")
        for item in shopping_cart:
            print(f"- {item['ProductName']} (Price: {item['Price']})")
        assistant_speak("Thank you for shopping with us!")
    else:
        assistant_speak("Your cart is empty.")
