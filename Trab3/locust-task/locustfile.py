import os
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def home(self):
        self.client.get("/")
    @task(2)
    def image1mb(self):
        self.client.get("/?p=5")
    @task(3)
    def image300kb(self):
        self.client.get("/?p=9")
    @task(4)
    def text400kb(self):
        self.client.get("/?p=12")