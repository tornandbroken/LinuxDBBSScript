<br />

**Linux Dual Boot Setting Script** ########################### ##### #### ### ## #

<br />
<p />
That Linux Dual Boot Setting Script creates a backup of your Bluetooth settings on your Linux system, with which your devices will be able to connect to any other Linux partition of your notebook or PC with ease
<p />

**instruction manual :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: :::::: ::::: :::: ::: :: :**
<p>
Click on the DualbootBluetooth.py file of that GitHub page and click again on that "󰄠 " button
It's also possible to download Git archives in the traditional way with the git clone command in your terminal, so you have to open your terminal and enter <code>git clone https://github.com/tornandbroken/LinuxDBBSScript.git</code>

To run it, you have either to type into your Bash python BluetoothSettings.py or python3 BluetoothSettings.py. 
<p />

- Firstly, set up all your Bluetooth devices. If you don’t know how you can do that a few lines later, there will be a short explanation
- Secondly Run that BluetoothSettings.py script in your Linux terminal and create a backup of your Linux Bluetooth device settings with it 
- Thirdly Run that BluetoothSettings.py script on every partition you have Linux installed with a copy of that backup folder “bluetooth” next to that BluetoothSettings.py script and intall your bluetooth "settings" backup
- After rebooting your Linux systems, your Bluetooth devices will either be automatically connected, or you will have to press the connect button of your device 

<p >
The use of it that python script is easier than you might assume it uses the GNU Utilities to get as little code as possible


The first option creates a backup of your actual Bluetooth setting next to your BluetoothSettings.py file and removes the restrictions. **cp -p -r /var/lib/bluetooth bluetooth && chmod -R 555 Bluetooth** 
Then the next option copies the backup files into that Linux you are using **rsync -au bluetooth /var/lib** That reset option erases your Linux bluetooth settings **rm -rf /var/lib/bluetooth**, and the exit option leaves that script 
<p />
<br />

**Set up Bluetooth Devices in Linux :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: :::::: ::::: :::: ::: :: :**

<p >
Before you run that script, it’s important that you have set up all of your devices on one Linux system. If you have messed up your Linux partitions, use the Reset option of that script.

In most cases your Linux uses systemd because it's widely used in most Linux Distributions

Now open your Linux terminal and type **bluetoothctl**. If it doesn’t start, type **systemctl enable bluetooth** and **systemctl start bluetooth**

if your terminal looks like that **[bluetooth]** type **scan on** and press enter

You should be able to see your Bluetooth devices now. Press the pairing button of your device. If you don’t know, take this information from your manual

**[bluetooth] pair XX:XX:XX:XX:XX:XX** 
maybe you have to confirm the [agent] Authorize service with | yes

**[bluetooth] trust**

**[bluetooth] disconnect**

Do that until you have a complete setting for each of your Bluetooth device

The next time your device will be connected automatically if you use a controller or something like that; you have to press the connect button

If it isn't the case, Type **bluetoothctl connect XX:XX:XX:XX:XX:XX**

Now you can leave bluetoothctl with **exit**
<p />
<br />

**Note ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: :::::: ::::: :::: ::: :: :**

<p >
It's very easy to connect all of your devices with Linux with a dual boot system as far your Bluetooth Settings got on each Partition the same Settings

The syntax of that setting is made in the /var/lib/bluetooth/HarwareMAC/DevicesMAC directory

The first MAC address in that directory shows the Bluetooth hardware interfaces that are implemented in your PC hardware "one interface will be able to handle up to 8 Bluetooth devices", and the second MAC address or addresses in that folder shows the devices that have already been paired with your Linux system

<p />
<br />
  
**Cheers**


