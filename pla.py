import requests
import bcolors
import sys, argparse

def banner():
    print("""

            
██████╗░██╗░░░░░░█████╗░░██████╗░██╗░█████╗░██████╗░██╗░██████╗███╗░░░███╗░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗██║██╔════╝████╗░████║░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██████╔╝██║░░░░░███████║██║░░██╗░██║███████║██████╔╝██║╚█████╗░██╔████╔██║█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██╔═══╝░██║░░░░░██╔══██║██║░░╚██╗██║██╔══██║██╔══██╗██║░╚═══██╗██║╚██╔╝██║╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
██║░░░░░███████╗██║░░██║╚██████╔╝██║██║░░██║██║░░██║██║██████╔╝██║░╚═╝░██║░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░░░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
                                                                                                            Code By: NG
              """
          )

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 't'):
        try:
            itext = sys.argv[2]
            input_text = 'intext:' + itext

            parser = argparse.ArgumentParser()
            parser.add_argument("-t", required=True)

            print(bcolors.BITALIC + "Testing for plagiarism")
            try:
                from googlesearch import search
            except ImportError:
                print(bcolors.ERR + "Word not found")

            for se in search(input_text, tld="com", num=2, stop=20, pause=2):
             print(bcolors.OK + se)
        except:
            print(bcolors.ERRMSG + 'Text can not be searched')

    elif (sys.argv[1] == '-h'):
        print(bcolors.BOLD + 'usage: pla.py [-h] -t URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-t text,   --text TEXT which you want to check')
    elif (sys.argv[1] != '-t'):
        print(bcolors.OKMSG + 'Please enter -u < text >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -t or -h, with a valid URL')
