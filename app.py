from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  
            "model_filter": lambda tag: True,  
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"  
}

swagger = Swagger(app, config=swagger_config)

background_data = [
    "Almost completed the entire bachelor's degree in business informatics. I was able to learn several programming languages and gain insights into topics ranging from IT security to software engineering to theoretical computer science."
]
email_data = "anton.l.kloth@campus.tu-berlin.de"
mtknr_data = "402128"
name_data = "Anton Larry Kloth"
program_of_study_data = {"study_program": "Business informatics (Wirtschaftsinformatik)", "degree": "Bachelor"}
skills_data = [
    {"key": "programming languages", "value": ["Java", "Python", "C++", "Haskell", "Scala", "SQL"]}
]
topics_data = {
    "1": "Network paths performances analyzer",
    "2": "Monitoring interface for 5G private network",
    "3": "Provisioning subscribers to 5G-IMS platform"
}

@app.route('/background', methods=['GET'])
def get_background():
    """Endpoint returning background information
    ---
    responses:
      200:
        description: A list of background information
        schema:
          type: array
          items:
            type: string
    """
    return jsonify(background_data)

@app.route('/email', methods=['GET'])
def get_email():
    """Endpoint returning the email address
    ---
    responses:
      200:
        description: Email address of the student
        schema:
          type: string
    """
    return jsonify(email_data)

@app.route('/mtknr', methods=['GET'])
def get_mtknr():
    """Endpoint returning the matriculation number
    ---
    responses:
      200:
        description: Matriculation number
        schema:
          type: string
    """
    return jsonify(mtknr_data)

@app.route('/name', methods=['GET'])
def get_name():
    """Endpoint returning the full name
    ---
    responses:
      200:
        description: Full name of the student
        schema:
          type: string
    """
    return jsonify(name_data)

@app.route('/programOfStudy', methods=['GET'])
def get_program_of_study():
    """Endpoint returning the program of study
    ---
    responses:
      200:
        description: Program of study and degree
        schema:
          type: object
          properties:
            study_program:
              type: string
            degree:
              type: string
    """
    return jsonify(program_of_study_data)

@app.route('/skills', methods=['GET'])
def get_skills():
    """Endpoint returning relevant skills
    ---
    responses:
      200:
        description: A list of key-value pairs with skills
        schema:
          type: array
          items:
            type: object
            properties:
              key:
                type: string
              value:
                type: array
                items:
                  type: string
    """
    return jsonify(skills_data)

@app.route('/topics', methods=['GET'])
def get_topics():
    """Endpoint returning project topics
    ---
    responses:
      200:
        description: The selected project topics with priorities
        schema:
          type: object
          properties:
            1:
              type: string
            2:
              type: string
            3:
              type: string
    """
    return jsonify(topics_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
