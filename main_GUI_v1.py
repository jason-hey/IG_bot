
    def get_loop(self,loop):
        self.loop=loop
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()
        
    def start_IG_async_Win(self):
        '''
        非同步執行IG，Windows
        '''
        coroutine1 = self.OnStartIG()
        new_loop = asyncio.new_event_loop()     #在當前執行緒下創建時間迴圈，（未啟用），在start_loop裡面啟動它
        t = threading.Thread(target=self.get_loop,args=(new_loop,))   #通過當前執行緒開啟新的執行緒去啟動事件迴圈
        t.start()
        asyncio.run_coroutine_threadsafe(coroutine1,new_loop)  #這幾個是關鍵，代表在新執行緒中事件迴圈不斷“遊走”執行
    
    def start_IG_async_Mac(self):
        '''
        非同步執行IG，MacOS
        在MacOS上，您需要將 asyncio.set_event_loop() 更改為使用 asyncio.set_event_loop_policy() 以確保MacOS上的事件循環策略能夠正常工作。
        '''
        coroutine1 = self.OnStartIG()
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop_policy(asyncio.get_event_loop_policy())
        t = threading.Thread(target=self.get_loop, args=(new_loop,))
        t.start()
        asyncio.run_coroutine_threadsafe(coroutine1, new_loop)

    async def OnStartIG(self):
        """
        非同步執行IG
        """
        try:
            app = IG_Selenium()
            app.init()
            app.Get_Messages()
        except Exception as e:
            logging.error(traceback.format_exc()) 

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

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()