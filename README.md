# AdGear
Technical Assessment for AdGear 2021

This software is an improvement on the old database creation and querying system.

## METHOD:

The solution includes two parts: hashtables, and multithreading.

The old method for querying the database involved iterating through the entire database using bytewise computation and comparison. That method is very slow, so instead I introduced Hashtables to speed things up. Firstly, create_db script generates a dictionary with all of the keys and values in the events.json file. However, dictionaries in Python cannot use the same key twice, and therefore if the program detects that there is a duplicate key, it instead appends the value of that key to a list in the value of the dictionary, essentially forming a database index. By doing this, we can a) keep all values associated with all keys and b) remove duplicate keys. As well, hashtables are very fast when searching for an element because they don't require the dictionary to be iterated through entirely.

These improvements work twofold. Firstly, hashtables are significantly faster in searches than iterated searches, which improves efficiency immediately. Secondly, the Hashtable only has one instance of a key, and therefore when a key is found the search is over, and the program can simply calculate the number of values appended to the dictionary's value.

As well, to improve performance I added a multithreading component to my Python script. Here we specify the number of threads (in my case 3), then iterate through the jobs to compute an answer. The multithreading is done using ThreadPoolExecutor, and jobs are sent to a multithreading context manager that iterates through the arguments and sends them to different threads. That way, at any given time each thread is finding the number of values of a given key in the database. A user with an idle computer could increase the number of threads higher, and I encourage you to try that and see how your performance improves.

## HOW TO RUN:

Clone the repo and ensure you have Python 3 installed, then run the following bash commands:

```bash
python3 generate_events.py
python3 create_db.py
python3 query_db.py arg1 arg2 arg3
```


## RESULTS:

The average runtime for the old querying system is 0.911218 seconds.

The average runtime for my querying system is 0.541688 seconds, nearly half of the original time. This time can be improved upon by using more threads, as only 3 are selected for multithreading on my version of the code.

The values are provided below for your interest. If you would like to test the runtime on your own computer, I included two bash scripts named executionTimeQueryDatabase (my code) and executionTimeQueryDatabaseNaive (old code). These pass in a set of 850 unique keys as arguments to avoid repeated computation. These keys are found in uniqueKeys.txt.

### Naive (old) Query script:

0.954719

0.845087

0.858196

0.967681

0.930405

### Avg = 0.911218 seconds

My Query script:

0.485473

0.482108

0.501714

0.597695

0.641452

Avg = 0.541688 seconds
