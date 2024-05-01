from openai import OpenAI
import pytesseract
from PIL import Image
import os

# Path to the tesseract executable
# Update this if it's not automatically found, which is common in Windows.

def extract_text(image_path):
    """Extracts text from an image file."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        # Sanitize the text by replacing newlines with spaces and stripping leading/trailing spaces
        sanitized_text = " ".join(text.split())
        return sanitized_text
    except Exception as e:
        return str(e)

def gpt(command):
    client = OpenAI(
        api_key="API KEY"
    )
    prompt = command

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Based on the text from the social media story post, identify the likely political stance of the individual. Possible responses include 'left', 'liberal', 'right', 'conservative', 'centrist', or 'non-aligned'.  respond with the word and very small reasoning as to why (RESPONSE FORMAT EXPECTED: left/right: minimal reasoning)."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo"
    )

    response_text = chat_completion.choices[0].message.content
    print("++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++")
    print(f"Political stance for image: {response_text}")
    print("++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++")
def process_images(folder_path):
    """Processes each image in the folder for text extraction and political stance analysis."""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # check for common image file extensions
            image_path = os.path.join(folder_path, filename)
            print(f"Processing {filename}...")
            extracted_text = extract_text(image_path)
            if extracted_text:
                gpt(extracted_text)
            else:
                print(f"No text extracted from {filename}.")

# Example usage
folder_path = 'stories'  # The folder containing your story images
process_images(folder_path)
