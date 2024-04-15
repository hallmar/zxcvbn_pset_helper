# zxcvbn_pset_helper
Simple Python program that migrates zxcvbn 2.0.0 psets over to zxcvbn 3.0.0 psets.


It was shamelessly written by OpenAI prompts since it's a boring job that I don't really want to spend hours on :)

Basically what it does is that it finds all entries for "track_type" that have values bigger than 3, adds 2 to them and writes it to the file.
It does this for the whole folder.

You just put your psets from zxcvbn v.2.x.x into the "original" folder, run the python script and it should put the modified files into the "modified" folder.
Then you're ready to rock with zxcvbn v3.0.0!!! 
