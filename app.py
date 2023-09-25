from flask import Flask, request

@app.route('/api/greet')
def greet_api():
    name = request.args.get('name', 'Rekruto')
    message = request.args.get('message', "Давай дружить!")
    response = f"Hello {name}!\n{message}"
    return response