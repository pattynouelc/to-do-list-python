from flask import Flask, jsonify, request

app = Flask(__name__)

# Declaramos la variable 'todos' globalmente como una lista con al menos un elemento
todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Retorna la lista de tareas en formato JSON
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    
    request_body = request.json
    
   
    if "label" in request_body and "done" in request_body and isinstance(request_body["label"], str) and isinstance(request_body["done"], bool):
        
        todos.append(request_body)
        print("Incoming request with the following body", request_body)
        return jsonify(todos), 201  # Retorna la lista actualizada y el código 201 (creado)
    else:
        return "Invalid todo format", 400  # Retorna un error si el formato no es correcto

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

