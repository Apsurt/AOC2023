import argparse
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

class WebEngine:
    def __init__(self, config):
        if config["year"] is None or config["year"] < 2015 or config["year"] > 2023:
            raise Exception("Invalid year")
        if config["day"] is None or config["day"] < 1 or config["day"] > 25:
            raise Exception("Invalid day")
        self.year = config["year"]
        self.day = config["day"]
        
        self.headless = False
        
        self.logged = False
        
        self.options = webdriver.ChromeOptions()
        if self.headless:
            self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.url = "https://adventofcode.com/{}/day/{}".format(self.year, self.day)
    
    def load_day_page(self):
        self.driver.get(self.url)
    
    def login(self):
        self.load_day_page()
        try:
            user = self.driver.find_element(By.CLASS_NAME, "user")
            self.logged = True
            print("Logged in...")
            print("User: {}\n".format(user))
            return
        except:
            self.logged = False
            print("Logging in...\n")
        url = "https://adventofcode.com/auth/github"
        self.driver.get(url)
        load_dotenv()
        LOGIN = os.getenv("LOGIN")
        PASSWORD = os.getenv("PASSWORD")
        self.driver.find_element(By.ID, "login_field").send_keys(LOGIN)
        self.driver.find_element(By.ID, "password").send_keys(PASSWORD)
        login_button = self.driver.find_element(By.NAME, "commit")
        login_button.click()
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div[1]/h1")
            while self.driver.current_url != self.url:
                self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div[2]/div[1]/div[2]/div[1]/form/div/button[2]").click()
        except:
            print("No reauthorization needed\n")
        try:
            user = self.driver.find_element(By.CLASS_NAME, "user")
            self.logged = True
            print("Logged in")
            print("User: {}\n".format(user.text))
        except:
            self.logged = False
            print("Login failed. Please try again.\n")

    def get_description(self):
        self.load_day_page()
        print("Scraping description for day {}".format(self.day))
        descs = self.driver.find_elements(By.CLASS_NAME, "day-desc")
        print("Found {} description(s)".format(len(descs)))
        return descs
    
    def create_description_file(self):
        if not os.path.exists("/Users/tymonbecella/Desktop/AOC2023/src/descriptions"):
            os.mkdir("/Users/tymonbecella/Desktop/AOC2023/src/descriptions")
        with open("/Users/tymonbecella/Desktop/AOC2023/src/descriptions/day{}.desc".format(self.day), "w") as f:
            for desc in self.get_description():
                f.write(desc.text)
                f.write("\n")
    
    def create_python_file(self):
        if os.path.exists("/Users/tymonbecella/Desktop/AOC2023/src/day{}.py".format(self.day)):
            raise Exception("Python file already exists")
        with open("/Users/tymonbecella/Desktop/AOC2023/src/day{}.py".format(self.day), "w") as f:
            f.write("from utils import *\n")
            f.write("import itertools\n")
            f.write("import numpy as np\n")
            f.write("\n")
            f.write("answer = 0\n")
            f.write("\n")
            f.write("\n")
            f.write("\n")
            f.write("print(answer)\n")
            f.write("#upload(answer)")
    
    def get_input(self):
        if not self.logged:
            raise Exception("Not logged in")
        self.load_day_page()
    
    def save_input_file(self):
        if not self.logged:
            raise Exception("Not logged in")
        url = "https://adventofcode.com/{}/day/{}/input".format(self.year, self.day)
        self.driver.get(url)
        inp = self.driver.find_element(By.TAG_NAME, "pre").text
        if not os.path.exists("/Users/tymonbecella/Desktop/AOC2023/src/inputs"):
            os.mkdir("/Users/tymonbecella/Desktop/AOC2023/src/inputs")
        with open("/Users/tymonbecella/Desktop/AOC2023/src/inputs/day{}.txt".format(self.day), "w") as f:
            f.write(inp)
    
    def upload_answer(self, answer):
        print("Uploading answer...")
        if not self.logged:
            raise Exception("Not logged in")
        self.load_day_page()
        answer = str(answer)
        try:
            self.driver.find_element(By.NAME, "answer").send_keys(answer)
        except:
            print("Could not find answer box")
            return
        self.driver.find_element(By.XPATH, "/html/body/main/form/p/input[2]").click()
        
if __name__ == "__main__":
    from utils import config
    web = WebEngine(config)
    #web.login()
    #web.create_description_file()
    web.create_python_file()
    #web.save_input_file()