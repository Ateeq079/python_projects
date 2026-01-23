from flask import Flask, request, jsonify
import psycopg2, json
import crud

app = Flask(__name__)
with open("config.json", "r") as file:
    config = json.load(file)

db_table = config["postgres"].get("db_table")


@app.route("/")
def home():
    return "Student Managment System"


@app.route("/create", methods=["POST"])
def create():
    data = request.json
    query = f"INSERT INTO {db_table} (name, dept, gpa, grade) VALUES (%s,%s,%s,%s);"
    params = (data["name"], data["dept"], data["gpa"], data["grade"])
    try:
        crud.execute_query(query, params)
        return jsonify({"Message": "Record Enetered Succesfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/read", methods=["GET"])
def read():
    query = f"SELECT * FROM {db_table};"
    try:
        result = crud.execute_query(query, fetch=True)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/read/<int:id>", methods=["GET"])
def read_by_id(id):
    query = f"SELECT * FROM {db_table} WHERE st_id = %s;"
    try:
        result = crud.execute_query(query, (id,), fetch=True)
        if not result:
            return jsonify({"error": "Resoruce not found"}), 404
        return jsonify(result[0])
    except Exception as e:
        return jsonify({"erorr": str(e)}), 500


@app.route("/update/<int:id>", methods=["PATCH"])
def update_student(id):
    data = request.json

    if not data:
        return jsonify({"error": "No fields provided"}), 400

    fields = []
    values = []

    for key, value in data.items():
        fields.append(f"{key} = %s")
        values.append(value)

    values.append(id)  # for WHERE clause

    query = f"""
        UPDATE {db_table}
        SET {', '.join(fields)}
        WHERE st_id = %s;
    """

    try:
        rows = crud.execute_query(query, tuple(values))

        if rows == 0:
            return jsonify({"error": "Resource not found"}), 404

        return jsonify({"message": "Student updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_by_id(id):
    query = f"DELETE FROM {db_table} WHERE st_id = %s;"
    try:
        rows = crud.execute_query(query, (id,))

        if rows == 0:
            return jsonify({"error": "Resource not found"}), 404

        return jsonify({"message": "Record deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
