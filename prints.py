from flask import request

#printing stats with status and message on terminal
def terminal_print(response_data):
    request_method = request.method
    status_code = 200 
    status_message = "OK response" if status_code == 200 else "Error response"

    print("------------------------------------------------------------")
    print(f"Request method: {request_method}")
    print(f"{status_message}\nStatus code: {status_code}")

    print("Response body: ")
    print(response_data)
    print("------------------------------------------------------------")