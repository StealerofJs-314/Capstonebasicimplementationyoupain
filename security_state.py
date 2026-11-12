from security_models import SecurityPersonnel, SecurityRequest


security_requests = [
    SecurityRequest(1, 3, 1400, 4),
    SecurityRequest(2, 1, 800, 8),
    SecurityRequest(3, 5, 1200, 5),
    SecurityRequest(4, 12, 900, 1),
    SecurityRequest(5, 2, 1800, 2),
]

security_personnel = [
    SecurityPersonnel(54154, "Adam, James", "Officer", "Mon, Wed, Fri, Sat"),
    SecurityPersonnel(44547, "Wilson, John", "Sergeant", "Mon, Tue, Wed, Fri"),
    SecurityPersonnel(56412, "Adam, James", "Senior Sergeant", "Mon, Tue, Wed"),
    SecurityPersonnel(49513, "Adam, James", "Officer", "Mon, Wed, Fri, Sat, Sun"),
]
