from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    @task
    def todo_list(self):
        self.client.get("/api/v1/task/")
        
    @task
    def status_list(self):
        self.client.get("/api/v1/status/")