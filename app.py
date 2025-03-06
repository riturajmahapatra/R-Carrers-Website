from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Bangalore, Karnataka',
        'salary': '12,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Mumbai, Maharashtra',
        'salary': '11,50,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': '9,50,000'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Hyderabad, Telangana',
        'salary': '11,00,000'
    },
    {
        'id': 5,
        'title': 'Machine Learning Engineer',
        'location': 'Chennai, Tamil Nadu',
        'salary': '13,00,000'
    }
]

@app.route('/')
def helper():
    return render_template('home.html' ,jobs = JOBS ,company_name = 'AI THNKERS')  #this is how we render the pages required,jobs_display it can be any variable that rnders our jobs in html


@app.route('/api/jobs') #this is a endpoint for the api to look
def apiEndppoint():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)    