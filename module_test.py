import sys
import Mypackage_museum.mymodule as mymodule

if len(sys.argv) == 2:
    mymodule.hello(sys.argv[1]) 
    mymodule.goodbye(sys.argv[1]) 
