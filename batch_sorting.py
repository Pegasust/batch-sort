"""
Author: Pegasust
Purpose: Illustrates batch sorting by labeling how important each factor
(category) is.
This utilizes concepts of lexicographical sorting, but without knowing
min/max per category. It boils down that there exists a comparison function
for the two objects.
NOTE: In Python, if an object is comparable, __cmp__ (and optionally, rich
comparisons) must be defined
"""

# Plans: task list sorting, plug in a location, give the ability to
# transform the location into coordinates, then compare by distance.

def batch_sort_raw(simple_database, least_to_most_criteria, rev_cri=None):
    """
    Perform a simple batch_sort on a simple database.
    NOTE: database is swapped by index-wise swap:
    database[i], dastabase[j] = database[j], database[i]

    
    :param simple_database: a named matrix (imagine an excel matrix), preferably
        in the form of array of single-entry dictionary (accessed that way).
        The dictionary contains objects that are comparable (__cmp__ defined).
        In the future, objects can be sorted faster will be able to be enumerated
        (sorted using radix sort).
    :param least_to_most_criteria: iteratable of strings specifying
        least to most important criteria. The object higher in more important
        criteria will be placed at the beginning, despite having lower value
        in lower important criteria.
    :return: a sorted most important to least important shallow copy of simple_database
    """
    # list.sort is stable, we can use this to do batch_sort
    # Batch sort is as easy as stably sorting from least to most important
    # criteria
    db_cpy = shallow_cpy(simple_database)
    for i,critereon in enumerate(least_to_most_criteria):
        reverse_cri = False if rev_cri is None else rev_cri[i]
        db_cpy.sort(reverse=reverse_cri, key=lambda v_dict: v_dict[critereon])
    return db_cpy

def shallow_cpy(inp_list):
    return [*inp_list]

def render_simple_database(simple_database, sep = ","):
    """
    :return: string representing simple_database
    """
    if(len(simple_database) == 0):
        return ""
    # hopefully all dictionaries are the same.
    entry_line = sep.join(simple_database[0].keys())
    following_lines = "\n".join([sep.join(
        [str(val) for val in elem_dict.values()]) for elem_dict in simple_database])
    return entry_line + "\n" + following_lines
def print_db(simp_db, sep=","):
    print(render_simple_database(simp_db, sep))

# Development hackeries
def demo():
    TEST_SIMPLE_DATABASE = [{"Name": "Hung", "Age": 17}, {"Name": "Suc", "Age": 43}, {"Name": "Raven", "Age": 14}]
    print(render_simple_database(TEST_SIMPLE_DATABASE))
    print("Sort by Age, Name")
    print_db(batch_sort_raw(TEST_SIMPLE_DATABASE, ["Age", "Name"]))
    print("Sort by Name")
    print_db(batch_sort_raw(TEST_SIMPLE_DATABASE, ["Name"]))
    print("Sort by Age")
    print_db(batch_sort_raw(TEST_SIMPLE_DATABASE, ["Age"]))      
    print("Sort by Name, Age")
    print_db(batch_sort_raw(TEST_SIMPLE_DATABASE, ["Name", "Age"]))

if __name__ == "__main__":
    demo()
