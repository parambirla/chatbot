from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    '''
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    '''
    return 'I am Good' 

if __name__=='__main__':
    app.run()
