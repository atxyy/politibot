# Politibot 
### This program is a project that is inteded to moniter and infer a persons political stance based off of social media activity.

Dependecies: openai, pytesseract, os, PIL
terminal command "pip install openai pytesseract os PIL"

You also need to retrive an API key from OpenAI in order to use the GPT API. Insert it in the code where it says "API-KEY"

Start up Guide:

1. Install dependecies
2. Create a folder named "stories" for program to loop through
3. Insert collected images (png, jpg, jpeg) into stories folder
4. Run code and wait for results in terminal

Update Log:

(1/5/24) Version 1 pushed. This contains basic functionallity. Automatically extracts text from images and sends them to 
GPT api for policical interpriation. Testing shows most text shows consistent answers from GPT API. 
