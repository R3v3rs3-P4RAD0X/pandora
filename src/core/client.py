import discord
import rich

from rich.console import Console

# A class that extends the default discord.Client class
class Client(discord.Client):
    console = Console()
    # Ignore overriding the constructor.
    
    async def on_ready(self):
        # Await the application info
        await self.application_info()

        # Create a table with rich to print some useful information
        table = rich.table.Table(title="Bot Information")
        table.add_column("Name", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Name", self.user.name)
        table.add_row("ID", str(self.user.id))
        table.add_row("Logged in", str(True))
        table.add_row("Guilds", str(len(self.guilds)))
        table.add_row("Users", str(len(self.users)))
        table.add_row("Prefix", self.prefix)
        table.add_row("Invite URL", f"https://discord.com/api/oauth2/authorize?client_id={self.user.id}&permissions=8&scope=bot")


        # Print the table
        self.console.log(table, justify="center")
        self.console.log()

    # A basic implementation of the on_message event
    async def on_message(self, message):
        # Checks list
        checks = [
            # Check if the message author is a bot
            message.author.bot,
            # Check if the message content starts with the prefix
            not message.content.startswith(self.prefix),
            # Check if the channel is a DM channel
            isinstance(message.channel, discord.DMChannel)
        ]

        # Check if any of the checks are true
        if any(checks):
            return
        
        # Get the command and arguments
        command, *args = message.content.lstrip(self.prefix).strip().split()

        # Print to ensure that this works.
        self.console.log(f"Command: {command}")
        self.console.log(f"Arguments: {args}")