
# Selenium類別
class IG_Selenium:
    def __init__(self):
        self.drive = None
    def openChrome(self):
        '''
        打開指定Chrome
        '''
        from subprocess import Popen
        p = Popen("Open_Chrome.bat")
        # 加入這個會Block住
        # stdout, stderr = p.communicate()
        logger.info('已打開Chrome')
        # 等待5秒
        time.sleep(5)
    def Get_OS(self):
        '''
        判斷目前作業系統是Windows or MacOS
        '''
        import sys

        if sys.platform == 'win32':
            logger.info("目前運行的作業系統是 Windows")
            return 'Win'
        elif sys.platform == 'darwin':
            logger.info("目前運行的作業系統是 macOS")
            return 'Mac'
        else:
            logger.info("目前運行的作業系統不是 Windows 或 macOS")
            return 'Other'
    def connect_to_Chrome_Win32(self):
        '''
        連線至Chrome
        '''
        # 指定瀏覽器驅動程式的位置
        driver_path = "./chromedriver_win32/chromedriver"

        logger.info('1.自動尋找Chrome...')
        # https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # chrome_options.add_argument("--headless") #Chrome不提供可視化界面
        chrome_options.add_argument("--disable-dev-shm-usage") # # docker原本的分享記憶體在 /dev/shm 是 64MB，會造成chorme crash，所以要改成寫入到 /tmp
        chrome_options.add_argument("--no-sandbox") # 以最高權限運行
        chrome_options.add_argument("disable-gpu") #谷歌文檔提到需要加上這個屬性來規避bug
        chrome_options.add_argument("window-size=1920x1080") # 設定瀏覽器大小
       
if __name__ == "__main__":
    app = IG_Selenium()
    app.init()
    # 等待使用者按下 Enter 鍵，程式才會結束
    input("按下 Enter 鍵結束程式...")