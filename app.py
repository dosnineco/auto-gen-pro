from flask import Flask, render_template, request, redirect, url_for
import openai
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        headings = request.form.get('headings')
        
        # Replace with your OpenAI API key
        openai_api_key = "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"
        openai.api_key = openai_api_key
        
        # Your article generation code here
                # Convert the string of headings into a list
        heading_list = headings.split(",")

        # Construct a prompt for the OpenAI API
        prompt = f"Write a detailed article discussing the following topics:\n"
        for heading in heading_list:
            prompt += f"- {heading}\n"

        prompt += "For each topic, write at least 250 words. Please use HTML tags for headings and paragraphs. Do not include any body or HTML main tags, just the heading tags. Do not use h1 tags, only h2 and h3. Include tables and list of list items. Do not include an explicit 'Introduction' or 'Conclusion' section but incorporate those naturally."

        # Generate content using OpenAI API
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000  # Adjust according to your needs
        )

        # The generated article text
        generated_article = response.choices[0].text

        # You can save this article to a file, database, or return it in the response
        # For demonstration, let's just send it back as a response
        return render_template('index.html', article=generated_article)


        return redirect(url_for('home'))
    
    return render_template('index.html')

# Vercel expects an "app" named WSGI callable
wsgi_app = app.wsgi_app
