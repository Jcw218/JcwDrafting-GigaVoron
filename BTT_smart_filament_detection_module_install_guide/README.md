### Guide to Installing the BTT smart filament detection module to the original Elegoo Orangestorm Giga Motherboard V3
![558768329_10235050453376534_4001759081982270624_n](https://github.com/user-attachments/assets/cc95c257-0e1e-401f-a7be-dd5bf1ecd554)

1. Firslty, figure out where you want the sensor. If the sensor is too far away from the print head, it may trigger more regularly than if the sensor was placed closer to the print head.
<img width="720" height="960" alt="image" src="https://github.com/user-attachments/assets/ba8a901f-cfff-4e5a-8feb-b28bddc73f9f" />

2. If you are using the DET0 and DET1 headers at the back of the printer; make sure both headers are properly pluged into the headers on the motherboard. You may need to run another cable from the DET1 header to the DET1 on the motherboard.

  ![558884123_10235066154769059_1636835637515836587_n](https://github.com/user-attachments/assets/2bd832b6-9825-46d3-a42d-7651089c36a4)
  ![557631873_10235066176769609_8913204024433743418_n](https://github.com/user-attachments/assets/ac10690d-3765-4478-95b2-1fb314b8c9cc)

4. The BTT smart filament sensor should be wired as per the following image:
  <img width="143" height="195" alt="filament detector" src="https://github.com/user-attachments/assets/e91e433d-77af-4c0c-b6c3-d0f0d5d57e30" />

5. Locate the IP address of your printer.
  <img width="384" height="140" alt="Screenshot 2025-10-07 171059" src="https://github.com/user-attachments/assets/04ae77cf-a7fa-416a-a9a8-032ce21ad540" />

6. Enter the IP address of your printer into google chrome and hit enter. You'll be greeted by the Fluidd Interface.
  <img width="979" height="321" alt="Screenshot 2025-10-07 171143" src="https://github.com/user-attachments/assets/8681a0fe-df6e-47dd-9833-0e9c0e055a2e" />

7. Located the Configuration tab on the left side of the Interface.
  <img width="246" height="209" alt="Screenshot 2025-10-07 171310" src="https://github.com/user-attachments/assets/aad3aa21-0827-4ac4-97f8-e15b9b0f4a6c" />

8. Double left click on the printer.cfg file

9. scroll down and find the following entry.
  <img width="502" height="180" alt="Screenshot 2025-10-07 123641" src="https://github.com/user-attachments/assets/830b3ef5-0138-45d8-bcbd-b133da6e210e" />

10. type # to uncomment this code or delete this code and then type in the following instead:
  <img width="502" height="491" alt="Screenshot 2025-10-07 130252" src="https://github.com/user-attachments/assets/c21ce4a3-e2fb-429c-8674-ec0f9ecf89f2" />

11. 
