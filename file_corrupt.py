import io
import argparse
import asyncio
from secrets import randbelow
from os import remove
from os import path
from os import listdir
from shutil import rmtree

async def delete(file,dir):
    if str(dir) == "None" and str(file) != "None":
        print("Opening file...")
        f = open(file,"w")
        print("Opened file, corrupting...")
        for i in range(2500000):
            f.write(chr(randbelow(127)))
        f.close()
    elif str(file) == "None":
        index = 0
        for filename in listdir(dir):
            index += 1
            print("Corrupting {} ({})...".format(filename,index))
            filename = path.join(dir,filename)
            try:
                f = open(filename,"w")
                for i in range(2500000):
                    f.write(chr(randbelow(127)))
                f.close()
            except:
                print("Running coroutine to corrupt the files in {}...".format(filename))
                await delete(None,filename)

                
        print("Corrupting directory...")
        print("Completed!")


ap = argparse.ArgumentParser()
ap.add_argument("-f","--file",required=False, help="file to corrupt")
ap.add_argument("-d","--directory",required=False,help="directory to corrupt")
args = vars(ap.parse_args())
asyncio.run(delete(args["file"],args["directory"]))