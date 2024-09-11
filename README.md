# ComfyUI-WhatsappNotifier
Node to send messages via WhatsApp, used in a workflow, in the Queue of the final prompt. You must have a session started in the same browser where ComfyUI is running by default.

![{30BB1359-C081-479C-8110-02360FA845CD}](https://github.com/user-attachments/assets/24c13788-8cbb-41c5-b95a-326b51927f13)

# Installation

## Installation [Method 1] (General installation method: ComfyUI-WhatsappNotifier only)

To install ComfyUI-Manager in addition to an existing installation of ComfyUI, you can follow these steps:

1. Go to the `ComfyUI/custom_nodes` directory in the terminal (cmd).
2. Run the following command:

   ```sh
   git clone https://github.com/I210I/ComfyUI-WhatsappNotifier.git
3. Execute in cmd on root ComfyUI folder

   ```sh
   .\python_embeded\python.exe -s -m pip install pywhatkit

4. Restart ComfyUI

## Installation [Method 2] (General installation method: ComfyUI-WhatsappNotifier only)

1. Install git
   - https://git-scm.com/download/win
   - standalone version
   - select option: use windows default console window

2. Download [scripts/install-wanotifier.bat](https://github.com/I210I/ComfyUI-WhatsappNotifier/blob/main/scripts/install-wanotifier.bat) into installed "ComfyUI_windows_portable" directory.
3. double click install-wanotifier.bat batch file

![{05E2FB7F-2E02-40B7-8A0E-B27ACBD35C2C}](https://github.com/user-attachments/assets/b450e965-9ee8-4053-ae15-40da7fb362a2)

## To Use

1. Add Node => Whatsapp => Notify => WhatsAppNotify

![{3154957E-DC5F-4CC2-A706-F10531E5F591}](https://github.com/user-attachments/assets/e1dcb3bb-4811-472b-87a5-39e4f4e6b909)

2. I recommend running the default workflow at the end of your Queue. (LOAD DEFAULT)

![image](https://github.com/user-attachments/assets/76738125-ff18-4aa2-a580-ed4eb247f9e6)

3. Connects the node to any other node in the stream where the input is an integer, for example in the bach size.

![image](https://github.com/user-attachments/assets/2e06fb87-0bdd-4a9e-b93f-e9087c66832e)

