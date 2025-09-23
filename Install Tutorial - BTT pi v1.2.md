####################################################################################
### Machine type: JcwGiga
### Current configuration version: VBeta
### Date：2025-9-11
### BTT Pi V1.2 - Octopus pro V1.1 - EBB SB2209-RP2040
### OEM Stepper Motors and Stock Stepper Drivers
####################################################################################

This is a Tutorial on how to install this repositories operating system to a BTT pi V1.2 and configure it for the Elegoo Orangestorm Giga

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

  - Use cable ties or label paper to mark the ribbon cables that lack original markings, ensuring they correspond to the port names on the motherboard.
    
    <img width="500" height="337" alt="image6" src="https://github.com/user-attachments/assets/a73b4bb2-9714-4541-9b02-34361c9c054b" />


    <img width="827" height="451" alt="Motherboard sch" src="https://github.com/user-attachments/assets/b9495655-b344-432c-8d53-b7d9055548b2" />

  - Disconnect all ribbon cables from the ports on the motherboard. Use a 2.0mm Allen wrench to loosen the 4 screws securing the motherboard, and remove the old motherboard.

    <img width="500" height="337" alt="image7" src="https://github.com/user-attachments/assets/3fdefb3a-fa33-4673-b1bf-ab85412b1b9d" />

  - Install Octopus Pro Adapter Bracket using the same 4 screws.


  - Plug in the cables to the octopus pro using the following schematic.

    <img width="812" height="638" alt="Octopus pro wiring schematic (GIGA) (OEM)" src="https://github.com/user-attachments/assets/5d6a3578-6b25-4247-8155-f7eac3431f15" />


    - UART_NOTE 1: Pull the black Jumper clips from the octopus pro board to match the following SPI Diagram.
      
      <img width="906" height="302" alt="Octopus pro UART" src="https://github.com/user-attachments/assets/7e1fb2d7-856d-4732-9176-db69700746eb" />

    - STEPPER_NOTE 2: Pull the Black Jumper clips from the ocotopus pro board and place them back to match the following STEPPER Diagram.

      <img width="742" height="276" alt="Octopus pro STEPPER" src="https://github.com/user-attachments/assets/031b3f87-d50a-4f40-a88b-64adb8a7bfa3" />

    - FAN_POW NOTE 3: Pull the Black Jumper Clips from the octopus pro board and place them back to match the following FAN POW Diagram.

      <img width="902" height="270" alt="FAN POW" src="https://github.com/user-attachments/assets/e7faba67-6708-4eb5-881c-e60e6026d6d8" />


    


    

