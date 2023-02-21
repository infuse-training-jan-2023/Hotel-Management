from flask import Flask
from routes.review import review_bp
from routes.generate_invoice import pdf_bp
from routes.room_routes import room_bp
from routes.add_on_routes import add_on_bp
from routes.bookings_routes import bookings_bp
from routes.discount_route import discount_bp

app = Flask(__name__, static_folder='../build', static_url_path='/')

app.register_blueprint(review_bp,url_prefix='/api')
app.register_blueprint(pdf_bp,url_prefix='/api')
app.register_blueprint(room_bp,url_prefix='/api')
app.register_blueprint(add_on_bp,url_prefix='/api')
app.register_blueprint(bookings_bp,url_prefix='/api')
app.register_blueprint(discount_bp,url_prefix='/api')


@app.route('/')
def index():
    return app.send_static_file('index.html')
    
if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
