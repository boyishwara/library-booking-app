from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class LibraryUser(HttpUser):
    wait_time = between(1, 5) # Simulate user wait time between actions (1-5 seconds)
    
    def on_start(self):
        """Executed when a virtual user starts. We will perform login here."""
        # 1. Access the login page to grab the CSRF token
        response = self.client.get("/login")
        soup = BeautifulSoup(response.text, 'html.parser')
        token_input = soup.find("input", {"name": "_token"})
        
        if not token_input:
            print("Failed to find CSRF token!")
            self.csrf_token = ""
        else:
            self.csrf_token = token_input.get("value")
            
        # 2. Perform Login as mahasiswa
        login_data = {
            "_token": self.csrf_token,
            "email": "mahasiswa@stu.pnj.ac.id",
            "password": "akumahasiswa"
        }
        self.client.post("/login", data=login_data)
        
    @task(3)
    def view_dashboard(self):
        """Simulate user viewing the dashboard/homepage"""
        self.client.get("/")
        
    @task(2)
    def filter_rooms(self):
        """Simulate user searching for a room with specific capacity"""
        self.client.get("/rooms?capacity=10&facility=proyektor")
        
    @task(1)
    def view_my_bookings(self):
        """Simulate user checking their drafts/history"""
        self.client.get("/user/bookings")
