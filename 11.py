# 11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`)

class Example:
    def log(self,**kwargs):
        if "error" in kwargs and "warning" in kwargs and "info" in kwargs:
            self.error=kwargs['error']
            self.warning=kwargs['warning']
            self.info=kwargs['info']
            print(f"{kwargs['warning']} {kwargs['error']} {kwargs['info']}")
        elif "error" in kwargs and "warning" in kwargs:
            self.error=kwargs['error']
            self.warning=kwargs['warning']
            print(f"{kwargs['error']} {kwargs['warning']}")
        elif "error" in kwargs and "info" in kwargs:
            self.error=kwargs['error']
            self.info=kwargs['info']
            print(f"{kwargs['error']} {kwargs['info']}")
        elif "warning" in kwargs and "info" in kwargs:
            self.warning=kwargs['warning']
            self.info=kwargs['info']
            print(f"{kwargs['warning']} {kwargs['info']}")
        elif "warning" in kwargs:
            self.warning=kwargs['warning']
            print(f"{kwargs['warning']}")
        elif "info" in kwargs:
            self.info=kwargs['info']
            print(f"{kwargs['info']}")
        elif "error" in kwargs:
            self.error=kwargs['error']
            print(f"{kwargs['error']}")
ex=Example()
ex.log(error='fgbsr')
ex.log(warning='rfygb')
ex.log(info='srtdbgase')
ex.log(error='bosrxgfnbb',warning="srtdgbf")
ex.log(error='bosrgfbvb',info="srtdgbfnbhgvferf")
ex.log(warning='bossrtfgndrtgfbb',info="diufxkcvhiaduj")
ex.log(warning='bossrhijhgjhbsertgfbb',info="okiyutygnhb",error='sferhbrhjbieu')