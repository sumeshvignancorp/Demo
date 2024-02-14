Steps to download and Run the script : 
1. https://www.jetbrains.com/pycharm/download/?section=windows    - Download  (only PyCharm Community Edition)
2. Install PyCharm Community Edition(By clicking default setting while download)
3. Download Chrome driver - https://googlechromelabs.github.io/chrome-for-testing/
	- Chrome driver should be downloaded by seeing your Chrome browser version
	- After checking version number that driver should be downloaded by above link (Check the link for Windows as Chromedriver)
4. After downloading Chrome driver Unzip it and Add it to D Drive as "D:\chromedriver.exe" because in script I mention this path
5. Open project and Right click on DemoFirstTest -> Open In -> Terminal  and type as "pytest -v -s"  or else 
"pytest"
6. To Get report Right click on DemoFirstTest -> Open In -> Terminal and type as "pytest --html=report.html" and After project execution you see a file in project name as report.html file 