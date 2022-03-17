from flask import Flask, request, jsonify

flask_object = Flask(__name__)  # telling py i want to create a new server


@flask_object.route('/', methods=["GET"])  # when user asks for nothing (/), run this method
def home_page():
    return """
    Welcome to Emile's Server
    Use the following API's to navigate


    """

@flask_object.route('/spartan_add', methods=['POST'])  # allows user to add sparta data by passing json file
def add_employee():
    sparta_data = request.json  #
    sparta_id = sparta_data['spartan_id']
    first_name = sparta_data['first_name']
    last_name = sparta_data['last_name']
    birth_year = sparta_data['birth_year']
    birth_month = sparta_data['birth_month']
    birth_day = sparta_data['birth_day']
    course = sparta_data['course']
    stream = sparta_data['stream']

    # call the method that will create the employee record
    return f"The employee ({sparta_id}: {first_name} {last_name} {birth_year} {birth_month} {birth_day} {course} {stream})"


# http://127.0.0.1:5000//spartan/<spartan_id> get certain employee data, return error message if id doesnt exists in system, return as string
@flask_object.route('/spartan/<spartan_id>', methods=["GET"])
def employee_record_getter(employee_id):
    # Check the database, read from a file, etc
    data = jsonify(id=employee_id, name="John", position="Manager")
    return data


# #http://127.0.0.1:5000/spartan/remove?id=sparta_id   This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string
@flask_object.route('/spartan/remove', methods=['POST'])
def remove():
    id_to_remove = request.args.get("id")
    return f"User would like to remove: {id_to_remove}"


@flask_object.route('/spartan', methods=["GET"])
def list_all():
    return "User would like to list the Spartans as one JSON object"


if __name__ == "__main__":
    flask_object.run(debug=True)  # dont use debug true when pushing to server