from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)

application = app

parks_list = convert_to_dict("parks.csv")


@app.route('/')
def index():
    number_list = []
    name_list = []
    for park in parks_list:
        number_list.append(park['number'])
        name_list.append(park['name'])
    pairs_list = zip(number_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="Parks Index")

@app.route('/park/<num>')
def detail(num):
    for park in parks_list:
        if park['number'] == num:
            parks_dict = park
            break
    return render_template('park.html', park=parks_dict, ord=ord, the_title=parks_dict['name'])

if __name__ == '__main__':
    app.run(debug=True)
