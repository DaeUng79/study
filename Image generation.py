from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

prompt = """
Create a professional and visually engaging magazine cover for a lifestyle magazine called "Urban Pulse." Include these featured article headlines clearly: "10 Hidden Cafés You'll Love in NYC" "Minimalist Apartments: Small Spaces, Big Ideas" "Exclusive Interview: Behind the Scenes with Indie Band Echo District" Use contemporary typography, vibrant colors, and include an eye-catching main photograph with a person standing in front of a city scene
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    quality="high",
    size="1024x1536",
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("4cut_2.png", "wb") as f:
    f.write(image_bytes)