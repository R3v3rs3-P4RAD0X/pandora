import os
import src.core as core

class Main:
    # A helper function that will allow us to open a .env file and store the key value pairs in a dictionary
    def open_env(self, file_path: str, store: dict):
        try:
            # Open the file with read only access
            with open(file_path, 'r') as f:
                # Read file line by line
                for line in f:
                    # Strip the line of whitespace
                    line = line.strip()

                    # Check if the line either starts with a # or is empty
                    if line.startswith('#') or not line:
                        continue

                    # Split the line by the = sign
                    key, value = line.split('=', 1)

                    # Strip the key and value of whitespace
                    key = key.strip()
                    value = value.strip()

                    # Add the key and value to the store
                    store[key] = value

        except FileNotFoundError:
            # If the file is not found, print an error
            print(f'File {file_path} not found')

        finally:
            return store
        


if __name__ == '__main__':
    # Clear the terminal before starting
    os.system("clear" if os.name == "posix" else "cls")

    # Initialize the Main class and open the .env file
    main = Main()
    data = main.open_env(".env", {})
    
    # Bind the prefix to the client class
    core.Client.prefix = data['BOT_PREFIX']

    # Create a new instance of the Client class
    client = core.Client(intents=core.discord.Intents.all())

    # Run the client
    client.run(data['BOT_TOKEN'])