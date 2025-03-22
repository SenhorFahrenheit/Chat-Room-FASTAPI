from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Websocket</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-3">
        <h1>FastAPI Websocket Chat </h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" class="form-control" id="messageText" autocomplete="off">
            <button class="btn btn-outline-primary mt-2">Send</button>
        </form>
    </div>

<script>
    var ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = function(event){
        var messages = document.getElementById("messages");
        var message = document.createElement("li");
        var content = document.createTextNode(event.data);
        message.appendChild(content);
        messages.appendChild(message);
    };

    function sendMessage(event){
        var input = document.getElementById("messageText")
        ws.send(input.value)
        input.value = ''
        event.preventDefault()
    }
</script>   
</body>
</html>
"""

@app.get('/')
async def get():
    return HTMLResponse(html)

