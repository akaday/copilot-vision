from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    response = get_gpt4_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
