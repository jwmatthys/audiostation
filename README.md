# rpi-playback-station

Connect button to 3.3V (inside row, furthest pin from USB ports or 5th pin from USB ports) and board pin 10 (outside row, fifth from opposite end)

Do we need a resistor? Yeah, I guess. *shrug*

In ~/.bashrc add:
```
python /home/pi/rpi-playback-station/rpi-button-mp3.py &
```
