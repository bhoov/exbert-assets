import json
from pathlib import Path
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="giant json file containing the hashed keys to all the different responses")
    parser.add_argument("-o", "--outpath", help="Path to folder where the json files will be saved")
    parser.add_argument("-d", "--demoApiPath", help="Path to .ts file containing the demoAPI definition")
    
    args = parser.parse_args()
    return args
    
def split_object(fname, outpath):
    with open(fname, 'r') as fp: 
        base = json.load(fp)
        
    N = len(base.keys())
        
    for i, (k, v) in enumerate(base.items()):
        outname = Path(outpath) / (k + '.json')
        
        with open(outname, 'w+') as fp:
            print(f"Dumping {k}\t[{i+1}/{N}]")
            json.dump(v, fp)

    return base

def createDemoFile(keys, outTsFile):
    """Create a demo file with an object whose keys are all the present demo files"""
    with open(outTsFile, 'w+') as fp:
        fp.write("export const DemoAPI = {\n")
        for k in keys:
            fp.write(f'\t"{k}": "{k}.json",\n')
        fp.write("}")
            
if __name__ == "__main__":
    args = parse_args()
    base = split_object(args.file, args.outpath)
    createDemoFile(base.keys(), args.demoApiPath)
    
    print("COMPLETE")