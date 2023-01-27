from flask import Flask, render_template, Response
import random
import requests

app = Flask(__name__)

@app.route('/getQr', methods=['GET'])
def qr():
    img = qrcode.make(request.args.get('url'))
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    response = send_file(img_io, mimetype='image/png')
    response.headers["Content-Disposition"] = "attachment; filename=qr_code.png"
    return response


@app.route('/emoji')
def emoji():
    # Generate a random image
    image_url = random.choice(["image1.jpg", "image2.jpg", "image3.jpg"])

    # Render the HTML template with the random image
    return render_template("emoji.html", image_url=image_url)

@app.route('/')
def index():
    # Generate a random image
    
    # Render the HTML template with the random image
    return render_template("indsex.html")

@app.route('/image')
def image():
    # Fetch a random image from the internet
    image_url = "https://picsum.photos/300/200"
    return render_template("image.html", image_url=image_url)


if __name__ == '__main__':
    app.run()


