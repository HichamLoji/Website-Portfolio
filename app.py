from flask import Flask
from flask import render_template, redirect, url_for,send_file

app = Flask(__name__)


@app.route('/')
def root():
    # Redirect from root to /home
    return redirect(url_for('hOme'))


@app.route('/home')
def hOme():
    return render_template('Home.html')


@app.route('/projects')
def pRojects():
    return render_template("Projects.html")


@app.route('/about')
def aBout():
    return render_template("About.html")


@app.route('/download_resume')
def download_resume():
    # Path to your resume PDF file
    resume_path = 'static/cv.pdf'
    return send_file(resume_path)


@app.route('/skills')
def sKills():
    return render_template("Skills.html")


if __name__ == '__main__':
    app.run(debug=True)
