from flask import Flask, render_template, request
import os
import subfunc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_directory = request.form['input_directory']
        output_directory = request.form['output_directory']
        
        
        edge_color = request.form['edge_color']

        try:
            not_resized_images = subfunc.resizeAllImages(input_directory, output_directory, edge_color)
            if not_resized_images:
                message = f"Некоторые изображения не удалось обработать: {', '.join(not_resized_images)}"
            else:
                message = "Все изображения успешно обработаны!"
        except Exception as e:
            message = f"Ошибка при обработке изображений: {str(e)}"
        
        return render_template('index.html', message=message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)  

