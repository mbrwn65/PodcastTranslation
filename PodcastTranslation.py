
import subprocess

user_input = input("(y/n) Would you like to uninstall all existing packages and install the necessary requirements from startingreqs.txt?: ")

if user_input.lower() == "y":
    try:
        print("Running transcriber")
        
        subprocess.run(["python3", "customtranscriber.py"], check=True)

        print("Running translator")
        subprocess.run(["python3", "customtranslator.py"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the scripts: {e}")
        
else: 
    print("all existing packages must be uninstalled to avoid conflicts before required packages can be installed")
    exit()

#Runs nicegui app after pip installing nicegui (seperate .py since nicegui requires code to rerun)
print("Launching app")
subprocess.run(["pip3", "install", "nicegui"], stdout=subprocess.DEVNULL)
subprocess.run(["python3", "PodcastTranslationApp.py"], check=True)

