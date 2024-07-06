from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)

today = {
    'year': int(f'{dt.datetime.now()}'.split(' ')[0].split('-')[0]),
    'month': int(f'{dt.datetime.now()}'.split(' ')[0].split('-')[1]),
    'day': int(f'{dt.datetime.now()}'.split(' ')[0].split('-')[-1])
}

birthday = {
    'year': 2007,
    'month': 7,
    'day': 7
}
if birthday['month'] < today['month']:
    age = today['year'] - birthday['year']
elif birthday['month'] == today['month']:
    if birthday['day'] < today['day'] or birthday['day'] == today['day']:
        age = today['year'] - birthday['year']
    else:
        age = today['year'] - birthday['year'] - 1
else:
    age = today['year'] - birthday['year'] - 1


@app.route('/')
def main():
    return render_template('base.html', my_age=age)


if __name__ == '__main__':
   app.run(debug=True)