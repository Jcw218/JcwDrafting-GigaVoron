####################################################################################
### Machine type: JcwGiga
### Current configuration version: VBeta
### Date：2025-9-11
### BTT Pi V1.2 - Octopus pro V1.1 - EBB SB2209-RP2040
### OEM Stepper Motors and Stock Stepper Drivers
####################################################################################

This is a Tutorial on how to install this repositories operating system to a BTT pi V1.2 and configure it for the Elegoo Orangestorm Giga manually

Step 1:
Ensure that your Giga is turned off and isolated from power. You may also want to wait a day to ensure that the capacitors are drained of electricity and are safe to touch.

Step 2:
Removing the Mother board cover panel on the right side of the machine as detailed in the images below:

  - Ensure that your print head is at the z heigth of 300-500 and out of the way so that the motherboard panel can be removed. You may need to manually home first and then set the z height to 300 or 500.
    
    <img width="600" height="337" alt="image 0" src="https://github.com/user-attachments/assets/6320a561-ed0b-409d-b4d6-0b0574678ba9" />
    
  - Loosen the 2 screws fixed by the PEI limit block at the right front and back side of the printer using a 2.0mm Allen wrench to remove the PEI limit block.
    
    <img width="604" height="355" alt="image1" src="https://github.com/user-attachments/assets/3fd39116-c77e-49d5-9aac-09d7ec0433c6" />
  
  - Disconnect the ribbon cables from the rear adapter board located on the right side of the printer.
    
    <img width="554" height="358" alt="image2" src="https://github.com/user-attachments/assets/6057de72-48c8-4345-aa3c-1a9942f87658" />
  
  - Use a 2.0mm Allen wrench to loosen the 8 screws securing the power supply cover.
    
    <img width="554" height="238" alt="image3" src="https://github.com/user-attachments/assets/d71f6608-0290-4653-90c6-690ff3b7c1d4" />

  - Slide the power supply cover downward towards the heated bed, then lift the outer edge of the cover to remove it.
    
    <img width="554" height="393" alt="image4" src="https://github.com/user-attachments/assets/446f7bd5-e3a6-4948-93ba-e092bb492e5a" />

Step 3:
Removing the Motherboard and marking the wires as per the images below:

  - Use cable ties or label paper to mark the ribbon cables that lack original markings, ensuring they correspond to the port names on the motherboard.
    
    <img width="500" height="337" alt="image6" src="https://github.com/user-attachments/assets/a73b4bb2-9714-4541-9b02-34361c9c054b" />


    <img width="827" height="451" alt="Motherboard sch" src="https://github.com/user-attachments/assets/b9495655-b344-432c-8d53-b7d9055548b2" />

  - Disconnect all ribbon cables from the ports on the motherboard. Use a 2.0mm Allen wrench to loosen the 4 screws securing the motherboard, and remove the old motherboard.

    <img width="500" height="337" alt="image7" src="https://github.com/user-attachments/assets/3fdefb3a-fa33-4673-b1bf-ab85412b1b9d" />

Step 4:
Install Klipper onto Big Tree Tech pi V1.2, Octopus Pro V1.1 and the Big tree tech boards EBB SB2209 and the BTT Eddy

  - Download Raspberry pi imager: https://downloads.raspberrypi.com/imager/imager_latest.exe

    <img width="529" height="390" alt="raspberry pi imager" src="https://github.com/user-attachments/assets/c82e8f09-80ab-4e18-8b2b-f6fc7f5126fe" />

  - Download the latest BTT CB1 pi image (CB1_Debian12_minimal_kernel6.6_20241219.img.xz) here: https://github.com/bigtreetech/CB1/releases

   <img width="1180" height="445" alt="CB1 image" src="https://github.com/user-attachments/assets/ca2df115-eac9-46ef-8507-2e35f37b629f" />

  - Insert a spare micro SD card into your computer, preferably of a 32-64gb storage size.

  - Open Raspberry pi imager, input the following settings: Raspberry Pi Devices: No Filtering, Operating system: (Use custom)CB1_Debian12_minimal_kernel6.6_20241219.img.xz, Storage:GENERIC MASSSTORAGECLASS USB       Device - 32-64gb SD card

    <img width="674" height="475" alt="raspberry pi imager settings" src="https://github.com/user-attachments/assets/06b40e73-c0e7-4258-9611-7f1aba24915b" />

  - Hit next than edit settings with your wireless LAN name, password, Set username and password to user: biqu password: biqu, Set hostname to Jcwgiga.local and ensure your wireless LAN country is selected, time      zone and keyboard is correct. Next select the Services tab and enable SSH and Use password authentication. After this hit save and then YES to start the writing process. It may take a few minutes.

  - Once complete, open "This PC" (if using windows), select the boot partition of the sd card and open the system.cfg file.
     - Remove the # from hostname and input: "Jcwgiga" instead of "BIGTREETECH-CB1"
     - change the wifi settings to match your wifi settings.
     - hit save and close

      <img width="772" height="796" alt="btt config setting" src="https://github.com/user-attachments/assets/e0066c66-92d6-470b-b5f4-86853d098569" />
       
  - Next open the armbianEnv.txt file located in the same folder
     - Change console=display to equal console=serial
     - hit save and close

      <img width="889" height="931" alt="ArmbianEnv" src="https://github.com/user-attachments/assets/dfa0b091-9558-47c2-8dbe-ac014f296e65" />

  - Take out the SD card and insert it into the BTT pi. Plug the Usb C cable from the BTT pi v1.2 into the computer ensuring that the black jumper clip is installed as per the image:

    <img width="654" height="410" alt="BTT PI" src="https://github.com/user-attachments/assets/af26eb92-5f27-4b56-92a7-c2333a6221a8" />

  - Either wait for the wifi to connect or plug in an RJ45 Ethernet cable for internet access.

  - Download and install putty: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

  - Open putty and enter in Jcwgiga.local as the Host Name (or IP address), connection type is SSH and port is 22

    <img width="445" height="438" alt="putty" src="https://github.com/user-attachments/assets/7c520e49-7b6d-492e-85f8-9f43172ec056" />

  - You will be prompted for a username and password. Enter in biqu for username and for password: biqu. don't worry if the password doesn't show on the screen, it's hidden from view by default.

  - Next is the intimidating coding portion of this build. (follow esoterical guide for installing klipper in CANBus bridge mode: https://canbus.esoterical.online/mainboard_flashing)
    - copy this next code and right click anywhere on the putty program:
      
      sudo apt update
      
      sudo apt upgrade
      
      sudo apt install python3 python3-serial

      If you get an error along the lines of “unable to locate package python3-serial” then you may be on an older version of linux.

      In that case, run:

      sudo apt install python3-pip

      then

      pip3 install pyserial

    - copy this next code and right click anywhere in putty to paste, then hit enter.
   
      test -e ~/katapult && (cd ~/katapult && git pull) || (cd ~ && git clone https://github.com/Arksine/katapult) ; cd ~

    - copy this next code and right click anywhere in putty to paste, then hit enter.
   
      cd ~/katapult
      
      make menuconfig

    - you'll then be greeted with the klipperconfig screen. locate your motherboard config settings here and fill in the right values for your board: https://canbus.esoterical.online/mainboard_flashing/common_hardware.html
    
      <img width="702" height="246" alt="301052290-5434691f-2d97-4d75-9067-d7501c2a2214" src="https://github.com/user-attachments/assets/ecac5a1d-a7e2-4ea1-9319-5c50cc37f12b" />
    
    - press q to quit and save the config. then copy this code and right click anywhere in putty and press enter.
   
      make clean
      
      make

    - To flash, connect your mainboard to the Pi via USB then put the mainboard into DFU/BOOT mode (your mainboard user manual should have instructions on doing this).

      If your mainboard board uses an STM32 based MCU use these flashing steps: https://canbus.esoterical.online/mainboard_flashing.html#stm32-based-boards

      If your mainboard board uses an RP2040 MCU, use these flashing steps: https://canbus.esoterical.online/mainboard_flashing.html#rp2040-based-boards

    - next copy this code and enter it into putty. you should see your board listed and in DFU mode:

      lsusb

    - next copy and paste this code into putty. Please note that the 8 digits at the end of this code will be the same as your board digits as listed in the previous step.
   
      cd ~/katapult
      
      make
      
      sudo dfu-util -R -a 0 -s 0x08000000:mass-erase:force:leave -D ~/katapult/out/katapult.bin -d 0483:df11

      
    - copy this and right click anywhere on the putty program:
      
       ./kiauh/kiauh.sh
      
    - Select Y to keep kiauh up to date.
    - Enter the previous command in again:
      
      ./kiauh/kiauh.sh
      
    - type "4" for no and remeber my choice
    - type "1" for install ENTER
    - (OPTIONAL INSTALL) type "9" for obico ENTER
    - (OPTIONAL CONFIG) run through the process of setting up your obico account and link it by using the code or the search function in the phone app
    - type "B" for back ENTER
    - type "2" for update ENTER
    - type "a" Update all ENTER
    - if prompted for anything type ENTER for the default option
  
  - Install Octopus Pro Adapter Bracket using the same 4 screws.

  - Plug in the cables to the octopus pro using the following schematic.

    <img width="812" height="638" alt="Octopus pro wiring schematic (GIGA) (OEM)" src="https://github.com/user-attachments/assets/728e2caf-7e6d-4b78-9b0a-e04a16d692f2" />

    - UART_NOTE 1: Pull the black Jumper clips from the octopus pro board to match the following SPI Diagram.
      
      <img width="1006" height="302" alt="Octopus pro UART" src="https://github.com/user-attachments/assets/d6bde2bf-9fc4-46aa-9d31-8e8c24023f99" />

    - STEPPER_NOTE 2: Pull the Black Jumper clips from the ocotopus pro board and place them back to match the following STEPPER Diagram.

      ![Screenshot 2025-10-14 123219](https://github.com/user-attachments/assets/d13bf355-7650-42b8-95f0-297e25e65936)

    - FAN_POW NOTE 3: Pull the Black Jumper Clips from the octopus pro board and place them back to match the following FAN POW Diagram.

      <img width="902" height="270" alt="FAN POW" src="https://github.com/user-attachments/assets/e7faba67-6708-4eb5-881c-e60e6026d6d8" />

  -


    


    

