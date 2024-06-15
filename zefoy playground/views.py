import time

# ANSI color codes
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Banner with purple color
banner = f"""
 ██████╗ ██████╗ ███████╗ ██████╗ 
██╔═══██╗██╔══██╗╚══███╔╝██╔═══██╗
██║   ██║██████╔╝  ███╔╝ ██║   ██║
██║▄▄ ██║██╔═══╝  ███╔╝  ██║▄▄ ██║
╚██████╔╝██║     ███████╗╚██████╔╝
 ╚══▀▀═╝ ╚═╝     ╚══════╝ ╚══▀▀═╝ 
"""
print(banner)

# List of rainbow colors
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

def add_views():
    try:
        num_views = int(input(">  Views Desired: "))
        
        # Ask the user for a TikTok URL
        tiktok_url = input(">  TikTok URL: ")

        start_time = time.time()  # Record start time

        # Print the message the specified number of times with a delay
        for i in range(1, num_views + 1):
            color_index = i % len(rainbow_colors)  # Cycle through colors
            color = rainbow_colors[color_index]
            print(f"\033[38;5;{30 + color_index}m{i} Views Added!\033[0m")
            time.sleep(0)

        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time

        # Print the elapsed time
        print(f"Views sent in {elapsed_time:.2f} seconds.")

        # Wait for 5 seconds
        time.sleep(5)

    except ValueError:
        print("Please enter a valid input.")

# Call the function to execute the script
add_views()
