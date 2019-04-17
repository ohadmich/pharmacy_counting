# pharmacy_counting

### Background and motivation
I wrote this program as part of a programing challenge for the Insight Data Engineering program.
The goal of the challenge was to code a scalable program that can handle big data using only the most basic python libraries.

My program takes a comma separated text file containing prescription data ordered in lines of the following format: `id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost`, it then processes the data to find for each drug the number of unique prescribers and the total cost of the drug across all prescribers. The output is a text file where each line represents a unique drug data in the following format: `drug_name,num_prescriber,total_cost`.

My solution performs well on any size of input data, the largest data I tested was 24 milion records (a 1.15GB text file).
### Programing language and libraries
My code implementation is in Python 3 and uses only two standard libraries: `sys` for handling command line inputs and `re` for splitting data into columns.
### Solution approach
My approach uses 3 data structures: lists, sets, and a dictionary.
First, each data line is input to my `extract_values` function which extracts the relevant information in the line: drug name, a full name of the prescriber and the cost.
Next, the drag is added to a set of drugs, the full name is added to a corresponding set of names in a list of sets (one for every drug) and the cost is added to a list of total costs. A dictionary keeps track of the mapping between a drug name and its corresponding index in the two lists.
Finally, the drug set is sorted and the results are written line by line into a file.
### Running instuctions
Name input file `itcont.txt`, put it in the input folder, run the shell script `run.sh` and find results in the output folder.
