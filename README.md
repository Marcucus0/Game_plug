
# Game-plug

Play games, but with pleasure...

Game-plug is a script designed to provide an immersive gaming experience by integrating physical feedback into the virtual world. When a player suffers a death in a video game, this script activates a vibrator connected to the computer, providing a tactile sensation synchronized with in-game events. 

I created it specifically for “Satisfyer” brand vibrators.
## Installation

Require python 3

```bash
  > cd Game_plug
  > python -m pip install -r requirements.txt
```

## Get Started


First, you'll need to connect the vibrator to your computer. 

To do this, you need to push for 10 sec the main button. It will completely reinitialise your toy.
When it's done, push the same button for 3 sec, the parring mode will start.

After that, you need to go to your controll panel. Search for devices and printers.
Click "Add device" and your toy will appear. Click on it and it's done !
![Settings](https://cdn.discordapp.com/attachments/1163943259660365937/1234230957930840204/image.png?ex=662ffaa7&is=662ea927&hm=3a33f6f02c6eebc28c12adc49dcb03f9b938d10f8f1c815737960b0cfbb983a0&) 

Now, you have to test the connection:


First, extract and launch intiface-central. Start the server and don't change the default settings.
Go to the "Devices" section and start a scan. Your vibrator needs to be connected in the app. If the connection fails, try to reinitialize your device.


Secondly, start the script called `test-vibrator-conn.py`. If the script detects multiple objects and your toy doesn't work, try to increase the value between the brackets `[ ]` in line 55.

Perfect! Your vibrator is set correctly!  
## Do it work with your game

To start the pleasure, you need to download [Cheat Engine](https://www.cheatengine.org/). If you don't now how to do it, I recommand the tutorial into the section Help of the app.

Start your game and try to find the memory address of the death counter or other action that you want to parse (but the main.py script is created to work with a death counter).

- Set this address to the variable `address`
- Modify the variable `processName` with the name (including .exe) of the process of your game
- If you need, don't forget to change the number object in line 34
It's done! I wish you pleasure with your game!

## Game Tested 

- [Celeste](https://store.steampowered.com/app/504230/Celeste/)
- Other games in review

If you test it on games, don't forget to give me feedback :-)
## License

[MIT](https://choosealicense.com/licenses/mit/)

