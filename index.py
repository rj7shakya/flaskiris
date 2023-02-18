from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    result = ''

    if (request.method == 'POST'):
        pickled_model = pickle.load(open('model.pkl', 'rb'))
        resultArr = pickled_model.predict(
            [[request.form['sepal_length'],
              request.form['sepal_width'],
              request.form['petal_length'],
              request.form['petal_width']]])

        if resultArr[0] == 0:
            result = 'setosa'
        elif resultArr[0] == 1:
            result = 'versicolor'
        else:
            result = 'virginica'

        return render_template('index.html', result=result)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
