Allure reports are used to create clear and fancy test reports.
Generating Allure Reports in Selenium Pytest:

Allure reports required the following to be installed:
1. Install Java JDK. Java development Kit
2. Install Node.js. (https://nodejs.org/en/download/prebuilt-installer)- Node. Js
3. Install allure using npm (node package manager) using the command: npm -g install allure-comrrmandline and add allure to the system path.
4. Use the command allure --version to check the allure version.- Allure using node package manager (npm)- npm -g install allure-commandline
5. Copy the path C:\Users\deybi\AppData\Roaming\npm\node_modules\allure-commandline\bin and add it in the System Variable.
6. Open Powershell and check the execution policy using the command Get-ExecutionPolicy. If it is set to
restricted, set it to RemoteSigned using the command Set-ExecutionPolicy RemoteSigned.
7. Open CMD as administrator and run the command allure, if its returns the allure usage in the output
that means allure is installed successfully.
8. Install the library allure-pytest library.
9. Run the command from the Pycharm Terminal: pytest --alluredir="": This will only generate some json and txt file
to generate an allure report out of it, we have to use the command allure serve "/path/reports". Note that this will
generate temporary report at the temp location.

To share the allure report with other team members, we need to use some third-party application. 

To generate a single allure html file report:
allure generate --single-file


************************************************XXXXX************************************************
Taking screenshots in allure:
1. To take screenshots in allure, first we will need to import the variable "allure" and class AttachmentType.
   import allure
   from allure_common.types import Attachment Type.
2. Then, use the variable allure.attach to take screenshot in allure
   allure.attach(self.driver.get_screenshot_as_png, name="screenshot file name", attachment_type=AttachmentType.PNG)