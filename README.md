# pharmacy_counting
### Programing language and libraries
My code implementation is in Python 3 and uses only two standard libraries: `sys` for handling command line inputs and `re` for splitting data into columns.
### Solution approach
My approach uses 3 data structures: lists, sets, and a dictionary.
First, each data line is input to my `extract_values` function which extracts the relevant information in the line: drug name, a full name of the prescriber and the cost.
Next, the drag is added to a set of drugs, the full name is added to a corresponding set of names in a list of sets (one for every drug) and the cost is added to a list of total costs. A dictionary keeps track of the mapping between a drug name and its corresponding index in the two lists.
Finally, the drug set is sorted and the results are written line by line into a file.

This solution can take any size of data, it was tested and performed well on 24 milion records (a 1.15GB text file)
### Running instuctions
Name input file `itcont.txt`, put it in the input folder, run the shell script `run.sh` and find results in the output folder.
