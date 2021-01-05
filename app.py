from flask import Flask, render_template, request
import bugis
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        indo = request.form['input']
        result = bugis.carib(indo)
        try:
            calcpad = result.split()
        except:
            if AttributeError:
                calcpad = ["nanno"]
        padding = 16/len(calcpad)
        return render_template('index.html', result=result, padding=padding, indo=indo)
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)