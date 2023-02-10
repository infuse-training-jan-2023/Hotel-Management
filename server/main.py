from flask import Flask, Response, request
import json
from routes.room_routes import room_bp
# from room_action import RoomAction
# from add_on_action import AddonAction
# add_on_actions=AddonAction()
# room_actions=RoomAction()


app = Flask(__name__)
app.register_blueprint(room_bp)



# @app.route('/api/add-ons',methods=['GET'])
# def get_add_ons():
#     add_on_data=add_on_actions.get_all_add_ons()
#     return Response(json.dumps(add_on_data), mimetype='application/json', status=200)

if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
