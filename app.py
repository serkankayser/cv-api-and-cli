from flask import Flask, json, jsonify

app = Flask(__name__)

# Read JSON file.
def read_json():
    f = open('cv.json')
    return dict(json.load(f))

@app.cli.command("personal")
@app.route('/personal', methods=['GET'])
def get_personal():
    """
    Get personal data from the CV.
    """
    data = read_json()
    personal = data.get('personal')
    print(personal)
    return jsonify(personal)

@app.cli.command("experience")
@app.route('/experience', methods=['GET'])
def get_experience():
    """
    Get experience data from the CV.
    """
    data = read_json()
    experience = data.get('experience')
    print(experience)
    return jsonify(experience)

@app.cli.command("education")
@app.route('/education', methods=['GET'])
def get_education():
    """
    Get education data from the CV.
    """
    data = read_json()
    education = data.get('education')
    print(education)
    return jsonify(education)

@app.cli.command("projects")
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Get personal projects from the CV.
    """
    data = read_json()
    projects = data.get('projects')
    print(projects)
    return jsonify(projects)

@app.cli.command("tech_skills")
@app.route('/tech_skills', methods=['GET'])
def get_tech_skills():
    """
    Get tech skills from the CV.
    """
    data = read_json()
    tech_skills = data.get('tech_skills')
    print(tech_skills)
    return jsonify(tech_skills)

@app.cli.command("personal_skills")
@app.route('/personal_skills', methods=['GET'])
def get_personal_skills():
    """
    Get personal skills from the CV.
    """
    data = read_json()
    personal_skills = data.get('personal_skills')
    print(personal_skills)
    return jsonify(personal_skills)

@app.cli.command("languages")
@app.route('/languages', methods=['GET'])
def get_languages():
    """
    Get languages data from the CV.
    """
    data = read_json()
    languages = data.get('languages')
    print(languages)
    return jsonify(languages)

@app.cli.command("all")
@app.route('/all', methods=['GET'])
def get_all():
    """
    Get all data from the CV.
    """
    data = read_json()
    print(data)
    return jsonify(data)