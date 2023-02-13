
from flask import Flask
from routes.customer_review import review_bp
from routes.customer_booking import booking_bp
from routes.search import search_bp
from routes.generate_pdf import pdf_bp
from routes.room_routes import room_bp
from routes.add_on_routes import add_on_bp

app = Flask(__name__)

app.register_blueprint(review_bp)
app.register_blueprint(booking_bp)	
app.register_blueprint(search_bp)
app.register_blueprint(pdf_bp)
app.register_blueprint(room_bp)
app.register_blueprint(add_on_bp)


# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, Response, request
# import json
# from routes.room_routes import room_bp
# from routes.add_on_routes import add_on_bp
# # from room_action import RoomAction
# # from add_on_action import AddonAction
# # add_on_actions=AddonAction()
# # room_actions=RoomAction()


app = Flask(__name__)





if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
