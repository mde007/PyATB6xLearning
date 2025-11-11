test_type  = input("Enter the Test Type you want to run : API, UI, Performance, Security ").upper()

match test_type:
    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a  Performance Testcase.")
    case "Security":
        print("We are running a  Security Testcase.")
    case _: #default case is mentioned at last
        print("Invalid Type.")


# test_type = input("Enter the test type: ").strip()
#
# if test_type == "API":
#     print("We are running a POSTMAN API Testcase.")
# elif test_type == "UI":
#     print("We are running a Selenium Testcase.")
# elif test_type == "Performance":
#     print("We are running a Performance Testcase.")
# elif test_type == "Security":
#     print("We are running a Security Testcase.")
# else:
#     print("Invalid Type.")