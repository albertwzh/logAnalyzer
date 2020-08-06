import filelocater
import regex
import re
import os

#p=os.path.dirname(os.path.abspath(__file__))+'\logs'
p=os.getcwd()+'/logs'

if __name__ == '__main__':
    def find_by():
        locater = filelocater.FindFile(path=p,fname="*.log")
        return locater
        
    def lookfor():
        xlook=regex.Xlook(pat="match",lookw="")
        patt=xlook.do_match
        return patt
    
    def run():
        locater = find_by()
        files = locater.file_filter(fileter_func="by_name")
        try:
            with open(r'./result.txt', 'a') as result:
                patt=lookfor()   
                for file in filter(None, files):
                    result.write(file)
                    result.write('\n')
                    try:
                        with open(r'{}'.format(file), 'r') as logfile:                 
                            lineno = 1
                            for line in logfile.readlines():
                                if patt(line):
                                    result.write("\t lineno {}: {}\n".format(lineno, line.strip()))
                                lineno += 1
                        result.write('\n')
                    except:
                        pass
        except:
            pass
            
    r=run()
