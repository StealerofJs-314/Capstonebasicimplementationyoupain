

def when_called(userid = -1):
    response = -1
    while response != 0:
            try:
                response = int(input("Choose an option:\n0. Log Out\n1. List Security Requests\n2. Personel Roster\n3. New Security Request\nEnter a number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if response == 0: 
                print ("--Logging Out--")
            elif response == 1:
                list_requests()
            elif response == 2:
                list_personel()
            elif response == 3:
                new_sec_request()

    return

class sec_request:
    def __init__(self, ID, num_pers, start_time, duration):
        self.ID = ID
        self.num_pers = num_pers
        self.start_time = start_time
        self.duration = duration

security_requests_list = [
    sec_request(115410, 3, 1400, 4),
    sec_request(115445, 1, 800, 8),
    sec_request(115476, 5, 1200, 5),
    sec_request(115416, 12, 900, 1),
    sec_request(115475, 2, 1800, 2),
]

def list_requests():
    for req in security_requests_list:
        print(f"Event ID: {req.ID}")
        print(f"Number of personel: {req.num_pers}")
        if req.start_time < 1000:
            print(f"Start time: 0{req.start_time}hrs")
        else:
            print(f"Start time: {req.start_time}hrs")
        print(f"Event Duration: {req.duration}")

class sec_personel:
    def __init__(self, ID = -1, name = "", rank = "", days_avalible = ""):
        self.ID = ID
        self.name = name
        self.rank = rank
        self.days_avalible = days_avalible

security_personel_list = [
    sec_personel(54154, "Adam, James", "Officer", "Mon, Wed, Fri, Sat"),
    sec_personel(44547, "Wilson, John", "Seargent", "Mon, Tue, Wed, Fri"),
    sec_personel(56412, "Adam, James", "Senior Seargent", "Mon, Tue, Wed"),
    sec_personel(49513, "Adam, James", "Officer", "Mon, Wed, Fri, Sat, Sun"),
]

def list_personel():
    for pers in security_requests_list:
        print(f"Employee ID: {pers.ID}")
        print(f"Employee Name: {pers.name}")
        print(f"Employee Rank: {pers.rank}")
        print(f"Employee Schedule: {pers.days_avalible}")


def new_sec_request():
    print("Input the requested information in order to register a new event wich needs security")
    event_ID = int(input("EVENT ID: "))
    num_officers = int(input("NUMBER OF OFFICERS: "))
    start_time = int(input("EVENT START TIME (24hr clock, omit leading zero and colon, e.g. 08:00 -> 800): "))
    duration = int(input("EVENT DURATION(in hrs): "))

    security_requests_list.append(sec_request [event_ID, num_officers, start_time, duration])

    print("NEW SECURITY EVENENT CREATED")
    print(f"Event ID: {event_ID}")
    print(f"Number of personel: {num_officers}")
    if start_time < 1000:
        print(f"Start time: 0{start_time}hrs")
    else:
        print(f"Start time: {start_time}hrs")
    print(f"Event Duration: {duration}")