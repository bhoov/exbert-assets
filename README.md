# exbert-assets
Contains large demo files needed to statically deploy examples for exBERT (https://github.com/bhoov/exbert)

## Usage
All demo files are included in the `demo/` folder. Inside of this, there is a large zip file that needs to be extracted to be used with the site. 

The automatic demo generator is not incredibly robust, but is incredibly convenient to create many static demo files at once. To do this, note the following:

- It is designed to only take in a single masked index
- Any difference or typo in the input sentence will cause results to be sent to the backend instead of the static files

## Procedure:
All references to code outside this repository are to code in: https://github.com/bhoov/exbert

0. If there are any demos currently saved that would mess up the server response, move these to a different folder, or comment out the lines in DemoAPI that let TS know which calls should be redirected
1. Edit the `createDemos` function in the `main.ts` file to run the demo instances you want to save. Then, comment out "doMySvg" and uncomment the line for "createDemos" in the main function. Make sure the server is running locally. 
2. The object of all the responses will be printed to the console when the file is run, along with how many keys are in that. When the object reaches the full expected size (in our case, ~60), right click in chrome and save "save as global variable".
3. In the console below, type "copy(temp1)". 
4. Open sublime (or another text editor that can handle large amounts of text) and paste it. Save it to `fname`.
5. In the `makeDemo/` folder, run `python make_demo.py -f fname -o ../src/demo -d ../src/ts/api/demoApi.ts`. This will save each response to a unique json file and record that file into an object that typescript can understand. It will also create a `demoAPI.ts` file with an object representing the filenames of each hash. Move this to the correct location in the `exbert` repo (`client/src/ts/api/demoAPI.ts`). Done