#!/usr/local/bin/python3

# Take input location and create tar. Send to output
#./archiver.py /path/to/input /path/to/outtput

import sys,os,subprocess,re
import argparse

def tar_at_input(INPUT,OUTPUT=os.getcwd()+"/",DEBUG=False):
    '''runs unix command to tar at input loccation, and store output at output location '''

    #CREATE DIRECTORY TREE IF NOT EXISTS,
    try:
        os.makedirs(OUTPUT)
    except:
        pass

    try:
        p = subprocess.Popen(f'tar -cvf {OUTPUT}data.tar {INPUT}*',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

        out2,err=p.communicate()
        # print ("Error is \n")
        print (err)
        return err
    except:
        return False


def get_args():
    '''
    get's input, output, and debug from user --> returns Tuple (ip,op,debug)
    '''
    parser = argparse.ArgumentParser(description='''Creates archive at input path. (Optionally)Specify output path to create data.tar at output path.
        Usage:
        python3 archiver.py /Users/mgarek/temp/
        python3 archiver.py /Users/mgarek/temp/ /Users/mgarek/temp2/
        python3 archiver.py /Users/mgarek/temp/ /Users/mgarek/temp2/ --debug
        ''')

    parser.add_argument('input',help='Create Tar at input path location. Default=/Users/mgarek/temp/')
    parser.add_argument('--output',help='Move tar to output path location. Default=CWD/data.tar')
    parser.add_argument('--debug',help='Print debug output',action='store_true')
    args = parser.parse_args()
    input,output,debug =args.input, args.output,args.debug

    if not input[-1] == '/':
        input=input+"/"
    print ("INPUT PATH IS {}".format(input))

    if output==None:
        print ("OUTPUT PATH IS {}".format(os.getcwd()+"/"))
        output=os.getcwd()+"/"
    else:
        print ("OUTPUT PATH IS {}".format(output))

    print ("DEBUG IS {}".format(debug))

    return (input, output,debug)

input,output,debug=get_args()
# print ("returned input,output,debug is {},{},{}".format(input,output,debug))


if tar_at_input(input,OUTPUT=output,DEBUG=debug) == False:
    print("Errored out")
    sys.exit()
