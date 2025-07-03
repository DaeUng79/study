from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

prompt = """
Create a super realistic 3d rendering of this architectural rendering.. Do not change the positions of the walls, and maintain lines in the same exact position as they are in the plan, but add furniture and finishes and textures and depth.
"""

result = client.images.edit(
    model="gpt-image-1",
    image=[
        open("cad.png", "rb"),
        # open("bath-bomb.png", "rb"),
        # open("incense-kit.png", "rb"),
        # open("soap.png", "rb"),
    ],
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("image_edit.png", "wb") as f:
    f.write(image_bytes)