from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("prompt", "")

    try:
        response = openai.Completion.create(
            model='gpt-3.5-turbo-instruct',
            prompt=user_message,
            temperature=1.2,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        bot_message = response['choices'][0]['message']['content']
        return jsonify({"response": bot_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
