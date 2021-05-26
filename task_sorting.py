"""
Author: Pegasust

Now with batch_sorting, we can help a task-scheduling algorithm with scheduling
tasks efficiently. There could be a machine learning algorithm that
finds how important each category is, then we do batch_sort with that
category input to get a sorted task list.

A task is defined to have the following fields:
    :param name: string: task name
    :param date_created: number: the date created
    :param due_date: number: the date it is due by
    :param difficulty: number: the task dfficulty
    :param location: location object: can deduce the location and name.
        We usually prefer doing tasks that are in nearer location.
    :param task_tags: bitmask: tags that define this task. Tasks in the same
        tags should be placed near to each other. (Graph theory?)
    
"""
# Discussions
"""
    - task_tags and location_dist are pretty much graph theory
    Future features:
        - float category priority? (sometimes, one priority may climb up
        on rank if it's more important?)
        
"""
import csv
import batch_sorting



def task_sort(task_list, least_to_most_criteria, rev_cri=None):
    












def read_database(csv_path, sep = ','):
    retval = None
    def retrieve_obj_dict(line, entry_names, sep):
        ret_dict = dict()
        for i,val in enumerate(line.split(sep)):
            dict[entry_names[i]] = val
        return ret_dict
    with open(csv_path) as csv_file:
        # read the first line
        entry_names = [name for name in next(csv_file)]
        retval = [retrieve_obj_dict(line, entry_names, sep)
                  for line in csv_file]
    return retval
