# Deceptecon-Omega

Here is a complete, working example of a terminal game bot. This includes a Target.cpp program to simulate the game, a Bot.cpp program that monitors the target, and an automation script (monitor.py) that reads the bot's output and performs pre-selected actions.

## Project Structure

This project has three main files that work together:

* **Target.cpp**: The simulated game. It has variables for ammo and health that change over time.
* **Bot.cpp**: The bot that connects to the target, reads its memory, and prints special keywords to the terminal when certain criteria are met.
* **monitor.py**: The automation script. This script runs the bot, watches its terminal output for the special keywords, and then triggers a function to "perform an action."

## Step 1: The Target Program

This program's code is slightly modified to change the values over time. This makes it more realistic for our automation script to detect changes.

```cpp
// Target.cpp
#include <iostream>
#include <windows.h>
#include <string>

int main() {
    int ammoCount = 50;
    int health = 100;

    std::cout << "Target Program Running." << std::endl;
    std::cout << "Ammo Address: " << &ammoCount << std::endl;
    std::cout << "Health Address: " << &health << std::endl;
    std::cout << "Press ENTER to exit..." << std::endl;

    int tick = 0;
    while (true) {
        system("cls");
        std::cout << "Current Ammo: " << ammoCount << std::endl;
        std::cout << "Current Health: " << health << std::endl;

        // Simulate ammo decrease
        if (tick % 50 == 0) {
            ammoCount--;
        }
        // Simulate taking damage
        if (tick % 100 == 0) {
            health -= 5;
        }

        Sleep(10);
        tick++;

        if (GetAsyncKeyState(VK_RETURN)) {
            break;
        }
    }
    return 0;
}
```

**Action**: Compile and run this program first. Keep it running and note the memory addresses.

## Step 2: The Bot Program

This program now focuses solely on monitoring the Target.cpp program and outputting keywords. This makes the automation simpler, as the script only needs to read for specific text.

```cpp
// Bot.cpp
#include <iostream>
#include <windows.h>
#include <string>
#include <vector>

// --- Helper Functions (From previous examples) ---
DWORD GetProcID(const wchar_t* windowName) {
    DWORD processID = 0;
    HWND hWnd = FindWindow(NULL, windowName);
    if (hWnd != NULL) {
        GetWindowThreadProcessId(hWnd, &processID);
    }
    return processID;
}

template <typename T>
T ReadMemory(HANDLE hProcess, uintptr_t address) {
    T value = 0;
    ReadProcessMemory(hProcess, (LPCVOID)address, &value, sizeof(T), NULL);
    return value;
}

template <typename T>
bool WriteMemory(HANDLE hProcess, uintptr_t address, T value) {
    return WriteProcessMemory(hProcess, (LPVOID)address, &value, sizeof(T), NULL);
}

// --- Main Program ---
int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <ammo_address> <health_address>" << std::endl;
        return 1;
    }

    uintptr_t ammoAddress = std::stoull(argv[1], nullptr, 16);
    uintptr_t healthAddress = std::stoull(argv[2], nullptr, 16);

    DWORD processID = GetProcID(L"C:\\path\\to\\your\\Target.exe"); // <-- REPLACE WITH YOUR PATH
    if (processID == 0) {
        std::cout << "Error: Target process not found." << std::endl;
        return 1;
    }

    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processID);
    if (hProcess == NULL) {
        std::cout << "Error: Could not open process." << std::endl;
        return 1;
    }

    // Main monitoring loop
    while (true) {
        int ammo = ReadMemory<int>(hProcess, ammoAddress);
        int health = ReadMemory<int>(hProcess, healthAddress);

        if (ammo < 5) {
            std::cout << "AMMO_LOW" << std::endl;
            WriteMemory<int>(hProcess, ammoAddress, 50); // Automatically reload
        }

        if (health < 20) {
            std::cout << "HEALTH_CRITICAL" << std::endl;
            WriteMemory<int>(hProcess, healthAddress, 100); // Automatically heal
        }

        Sleep(100);
    }

    CloseHandle(hProcess);
    return 0;
}
```

**Action**: Compile this program. Note that it now takes the addresses as command-line arguments. This makes it easy for our Python script to control it.

## Step 3: The Automation Script

This is the central piece that orchestrates everything. We will use a Python script because it's excellent for running other programs, capturing their output, and performing actions based on that output.

```python
# monitor.py
import subprocess
import os

# Define the full path to your Bot.exe
BOT_PATH = "C:\\path\\to\\your\\Bot.exe" # <-- REPLACE WITH YOUR PATH

# Get the memory addresses from the user
ammo_address = input("Enter Ammo Address: ")
health_address = input("Enter Health Address: ")

# Define actions based on keywords
def handle_low_ammo():
    """Performs the action for low ammo."""
    print("Action: Reloading ammo...")

def handle_critical_health():
    """Performs the action for critical health."""
    print("Action: Healing player...")

# Run the bot program and stream its output
print("Starting bot...")
command = [BOT_PATH, ammo_address, health_address]
proc = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)

# Read the bot's output line by line
for line in iter(proc.stdout.readline, ''):
    line = line.strip()
    if not line:
        continue

    # Check for keywords and trigger actions
    if line == "AMMO_LOW":
        print(f"[{line}] detected.")
        handle_low_ammo()
    elif line == "HEALTH_CRITICAL":
        print(f"[{line}] detected.")
        handle_critical_health()
    else:
        print(f"Bot Output: {line}")
```

**How it Works**: The script uses `subprocess.Popen` to run Bot.exe. It then creates a loop that continuously reads lines from the bot's standard output (stdout). When it reads a line that matches "AMMO_LOW" or "HEALTH_CRITICAL," it calls the corresponding action function.

## Final Steps

1. **Run Target.exe**: Make sure this program is running first.
2. **Run monitor.py**: From a terminal, navigate to your script's folder and run `python monitor.py`.
3. **Enter Addresses**: The Python script will prompt you for the ammo and health addresses you got from Target.exe.
4. **Watch the Magic**: The script will now run the bot, which in turn will manipulate the target program. You'll see the values change in Target.exe's window, and the Python script will print messages to your terminal as it detects the changes and performs the automated actions.

## Additional Examples

### Network Traffic Monitoring

```python
# Monitor drone communication protocols
import scapy
from scapy.all import *

def monitor_drone_traffic():
    # Capture packets on drone frequency bands
    packets = sniff(iface="wlan0", count=100)
    for packet in packets:
        if packet.haslayer(UDP):
            print(f"UDP packet: {packet[UDP].sport} -> {packet[UDP].dport}")
```

### Official Drone Programming

```python
# Official drone programming methods
from djitellopy import Tello
import time

# Connect to drone
drone = Tello()
drone.connect()

# Automated mission
def automated_patrol():
    drone.takeoff()
    drone.move_forward(100)
    drone.rotate_clockwise(90)
    drone.move_forward(100)
    drone.land()
```
