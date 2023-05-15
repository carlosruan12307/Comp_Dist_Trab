import os
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def reddit(self):
        self.client.get("/?url=https://www.reddit.com/r/brdev/")
    @task(2)
    def hackernews(self):
        self.client.get("/?url=https://news.ycombinator.com/")
    @task(3)
    def gitspring(self):
        self.client.get("/?url=https://github.com/spring-projects/spring-boot")
    @task(4)
    def stackoauth2(self):
        self.client.get("/?url=https://github.com/topics/aws")
    @task(5)
    def chatgptlimit(self):
        self.client.get("/?url=https://github.com/covid19india/covid19india-react")
    @task(6)
    def myrespository(self):
        self.client.get("/?url=https://github.com/carlosruan12307?tab=repositories")
    @task(7)
    def javastack(self):
        self.client.get("/?url=https://github.com/etcd-io/etcd")
    @task(8)
    def angularstack(self):
        self.client.get("/?url=https://github.com/twbs/bootstrap")
    @task(9)
    def reactstack(self):
        self.client.get("/?url=https://github.com/macrozheng/mall")
    @task(10)
    def facebookreact(self):
        self.client.get("/?url=https://github.com/facebook/react-native")