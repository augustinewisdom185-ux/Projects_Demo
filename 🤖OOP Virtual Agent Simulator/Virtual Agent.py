import time
from datetime import datetime

class VirtualSimulator:
    def __init__(self,name):

        self.sleep_time = None
        self.name = name
        self.energy = 100
        self.happiness = 50

    def current_stat(self):
        print(f"\n------ {self.name}`s Stats ------")
        print(f"Agent: {self.name}")
        print(f"Energy: {self.energy}%")
        print(f"Happiness: {self.happiness}%.")

    def sleep(self,seconds_to_sleep):
        if self.energy >= 100:
            print(f"\n {self.name} is fully charge!.")
            return

        #Record the bedtime
        self.sleep_time = datetime.now()
        start_str = self.sleep_time.strftime("%H:%M:%S")
        print(f"{start_str} went to bed at {start_str}")

        #Pause execution so your duration calculation actually works
        time.sleep(seconds_to_sleep)
        woke_time = datetime.now()
        end_str = woke_time.strftime("%H:%M:%S")
        duration = woke_time - self.sleep_time
        total_time = int(duration.total_seconds())
        second = total_time % 60

        #Update actual object stats (+20 Energy, -5 Happiness)
        self.energy = min(self.energy + 20, 100)
        self.happiness = min(self.happiness - 5, 100)

        #Display results
        print(f"{self.name} woke up at {end_str}")
        print(f"Duration rested: {second}seconds")

        self.sleep_time = None #Reset tracking variable

#First Child class:
class ChatBotPet(VirtualSimulator):
    def chat(self):
        print(f"[{self.name}]: Processing text... You are a great user!.")

        #Modify stats: +15 Happiness, -10 Energy
        self.happiness = min(self.happiness + 15, 100)
        self.energy = max(self.energy - 10, 0)
        print(f"Happiness: {self.happiness}% (+15) | Energy: {self.energy}% (-10)")

#Second Child class:
class VisionBotPet(VirtualSimulator):
    def scan_room(self):
        print(f"[{self.name}]: Drone camera scanning room... Object detected: Couch.")

        #Modify stats: +20 Happiness, -25 Energy
        self.happiness = min(self.happiness + 20, 100)
        self.energy = max(self.energy - 25, 0)
        print(f"\nHappiness: {self.happiness}% (+20) | Energy: {self.energy}% (-25)")

#------Test Execution Run------
if __name__ == "__main__":
    # Create the object correctly by only providing a name
    bot1 = ChatBotPet("Byte")
    bot2 = VisionBotPet("Aero")

    #Test the chatbot
    bot1.current_stat()
    bot1.chat()
    bot1.chat()

    #Test the visionBot (Draining energy quickly)
    bot2.current_stat()
    bot2.scan_room()
    bot2.scan_room()

    #Test sleep duration tracker (pass 310 seconds to sleep)
    bot2.sleep(3)
    bot2.current_stat()
    bot1.current_stat()
