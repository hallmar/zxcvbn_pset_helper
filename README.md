# zxcvbn_pset_helper
Simple Python3 program that migrates zxcvbn 2.0.0 psets over to zxcvbn 3.0.0 psets.
It should work with Python2 as well, haven't tested it though.

When you've installed [Python](https://www.python.org/downloads/) you just open cmd, navigate to the zxcvbn_pset_helper folder and type in ```py pset_helper.py```


It was shamelessly written by OpenAI prompts since it's a boring job that I don't really want to spend hours on :)

Basically what it does is that it finds all entries for "track_type" that have values bigger than 3, adds 2 to them and writes it to the file.
It does this for the whole folder.

You just put your psets from zxcvbn v.2.x.x into the "original" folder, run the python script and it should put the modified files into the "modified" folder. 

After that you move those modified files to your zxcvbn folder in data/zxcvbn. 
Then you're ready to rock with zxcvbn v3.0.0!!! 
