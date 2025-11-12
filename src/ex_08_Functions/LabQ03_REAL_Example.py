def validate_status_code(response_code):
    if response_code > 0:
        if response_code == 200:
            print("Request is successful")
        else:
            print("Error !!!")
    else:
        print("Invalid response code entered.")


validate_status_code(404)
validate_status_code(200)
validate_status_code(response_code=200)
validate_status_code(int(input("Enter your status code: ")))