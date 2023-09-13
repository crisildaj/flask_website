from flask import Flask, render_template
app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
@app.route('/index.html', methods=['GET'])
def home():
    return render_template('/index.html', title='Homepage')

@app.route('/V2_agile_design.html', methods=['GET'])
def agile():
    return render_template('V2_agile_design.html', title='Agile')

@app.route('/businessAnalysis.html', methods=['GET'])
def ba():
    return render_template('businessAnalysis.html', title='Agile')

@app.route('/webDev.html', methods=['GET'])
def web():
    return render_template('webDev.html', title='Web')

@app.route('/python_flask.html', methods=['GET'])
def py():
    return render_template('python_flask.html', title='Python and Flask')

@app.route('/resources_page.html', methods=['GET'])
def resources():
    return render_template('resources_page.html', title='Resources')

@app.route('/legal_page.html', methods=['GET'])
def legal():
    return render_template('legal_page.html', title='Legal')

@app.route('/aboutUs.html', methods=['GET'])
def about():
    return render_template('aboutUs.html', title='About')

@app.route('/secure_design.html', methods=['GET'])
def sec():
    return render_template('secure_design.html', title='Secure')

@app.route('/final.html', methods=['GET'])
def final():
    return render_template('final.html', title='final')

if __name__ == "__main__":
    # Execute only if ran directly as a program
    # Ignore if imported as a module.
    app.run(debug=True)