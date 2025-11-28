#match case statement to simulate traffic light signals
color=input("Enter colour:").replace(" ","").lower()

match color:
    case "red":
        print("Stop")
    case "green":
        print("go")
    case "yellow":
        print("Look")
    case _:
        print("Invalid colour")
