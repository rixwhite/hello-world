# Tips and Tricks

## Linux

### Turn off screen with a python script and a keybind
* You will need python3 installed
* Save [monitor_off.py](monitor_off.py) locally
* Set a keybind to run the script
  * Lubuntu 20.04
  * In the menu, go to Preferences > LXQt Settings > Shorcut Keys
  * Click "Add..."
  * Click the button next to Shortcut (this listens for the keybind)
  * Press the key bind you want to use (ex., CTRL+F7)
  * Add a Description (ex., "Turn off monitor")
  * Set the "Command" radio button
  * In the "Command" box, enter one of the following (based on the terminal emulator you want to use)
    * **qterminal:**`qterminal -e python3 monitor_off.py`
    * **xfce terminal:** `xfce4-terminal -e "python3 monitor_off.py"`
  * Click "OK"
  * Close the Shortcut Keys dialoge window

Now, when you hit the keybind, the system will exexute the python script from a terminal. The script will listen for a KeyboardInterrupt, so use CTRL+C to turn your monitor back on.

Note: You need the python to run from a terminal in order for it to capture the KeyboardInterrupt. The terminal will launch, then after 1 second, the monitor will turn off.
