# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:13:57 2019

@author: Ohad Michel
"""
import sys, re

'''Define helper functions'''
def float_or_int(x):
    # A function to remove unnecessary floating point
    if (float(x) == int(x)):
        return int(x)
    else:
        return float(x)

def isfloat(x):
    # A function that checks if a string can be converted to a float
    try: 
        float(x)
        return True
    except:
        return False
        
def splitcol(line, header):
    ''' Cleans and splits lines into columns
        inputs: line - a string of data; header - a string of column names
        outputs: drug - name of drug string
                 fullname - perscriber fullname string 
                 cost - drug cost string
    '''
    # Split colums in line, don't split on commas that are in quotes
    split_line = re.findall('''"[^"]*"|[^,]+''', line)
    split_line[-1] = split_line[-1].rstrip() # Remove EOL trailing
    
    # Make sure that splitting process went well and make corrections when needed
    if(len(split_line) != len(header)):
        # missing data case
        if((len(split_line) < len(header))):
            # missing names case
            if(isfloat(split_line[0]) and isfloat(split_line[-1])):
                # Assuming that drug name is not missing
                drug = split_line[-2] # drug name in line
                cost = float(split_line[-1]) # drug cost in line
                fullname =  split_line[-3] # fullname in line
                                
            else: assert (len(split_line) == len(header)), "Split error, not enough entries"
        else: assert (len(split_line) == len(header)), "Split error, too many entries"
    else:
        # Assign data to vars
        drug = split_line[header.index('drug_name')] # drug name in line
        cost = float(split_line[header.index('drug_cost')]) # drug cost in line
        fullname =  split_line[header.index('prescriber_first_name')] \
        + split_line[header.index('prescriber_last_name')] # full name of perscriber in line
    
    return drug, fullname, cost

'''Open file'''
in_path = sys.argv[1] # Input file path
out_path = sys.argv[2].rstrip() # Output file path
file = open(in_path, 'r') # Open file for reading

'''Define data structures'''
header = file.readline().split(',') # Save columns definitions
header[-1] = header[-1].rstrip() # Remove EOL trailing
drug_set = set([]) # Create a set of drugs in our file
drug_dict = {} # a dictionary for keeping track of drug locations
prset_list = [] # a list of prescribers name sets, one for each drug
costs_list = [] # a list of total costs for each drug
idx = 0 # an index for keeping track of drug order

'''Read and analyze lines'''
for line in file:
    
    drug, fullname, cost = splitcol(line, header)
    # If this drug is not in the set
    if drug not in drug_set:
        # Append a new cost element to costs_list
        costs_list.append(cost)
        # Create a new prescribers set and append tp prset_list
        prset_list.append(set([fullname]))
        # Save index of the drug into drug_dict and increase idx
        drug_dict[drug] = idx
        idx += 1
        # Add drug to set
        drug_set.add(drug)
        
    # Drug already exist, append to corresponding drug index in the lists
    else:
        # Add cost to sum of cost element of the current drug 
        costs_list[drug_dict[drug]] += cost
        # Add prescriber name to the set of prescibers of the current drug
        prset_list[drug_dict[drug]].add(fullname)

file.close()

'''Write results to file'''
outfile = open(out_path, 'w+') # Open output file
drug_set = sorted(drug_set) # Sort drug set in alphabetical order
# Write header
outheader = 'drug_name,num_prescriber,total_cost' + '\n'
outfile.write(outheader)
# Write data
while(len(drug_set)):
    drug = drug_set.pop() # pop a drug
    idx = drug_dict[drug] # retrieve drug index in data structures
    # Create a string of total cost for the drug
    total_cost = str(float_or_int(costs_list[idx]))
    num_prescriber = str(len(prset_list[idx])) # compute number of unique prescribers
    # Create a line string and write
    line = drug + ',' + num_prescriber + ',' + total_cost + '\n'
    outfile.write(line)

outfile.close()