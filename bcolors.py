import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    GREEN = '\033[92m'
    PURPLE = '\033[0;35m'
    LPURPLE = '\033[1;35m'
    CYAN = '\033[0;36m'
    MAGENTA= '\033[0;35m'
    WARNING = '\033[93m'
    YEL = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    NC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def render(*strs):
        res=""
        for str in strs:
                r=re.findall('\{(.*?)\}',str)
                for c in r:
                        rc=c
                        if c[0]=="/":
                                rc="ENDC"

                        try:
                            str=re.sub('\{'+c+'.*?\}',getattr(bcolors,rc),str)
                        except:
                            pass
                        str=re.sub('\{/\}',bcolors.NC,str)
                res+=str
        return res

