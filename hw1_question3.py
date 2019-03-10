def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    best_subject = {}
    subj1_name = subj1_all_students['subject']
    subj2_name = subj2_all_students['subject']
    name_list1 = list(subj1_all_students.keys())
    name_list2 = list(subj2_all_students.keys())
    for i in range(1, len(name_list1)):
        if (name_list1[i] in name_list2) and (name_list1[i] != 'subject'):
            subj1 = subj1_all_students[name_list1[i]]
            subj1_mean = (subj1[0] + subj1[1])/2
            subj2 = subj2_all_students[name_list1[i]]
            subj2_mean = (subj2[0] + subj2[1])/2
            if subj1_mean > subj2_mean:
                best_subject[name_list1[i]] = subj1_name
            elif subj1_mean < subj2_mean:
                best_subject[name_list1[i]] = subj2_name
            else:
                best_subject[name_list1[i]] = 'the same' 
    return best_subject                

history = {'subject':'History', 'Dana':[83,78], 'Eyal':[75,66], 'Benny':[92,94], 'Shira': [88,98]}
math = {'subject':'Math', 'Dana':[90,90], 'Benny':[58,76], 'Mira':[66,73], 'Eyal':[77,85], 'Shira': [85,88]}
english = {'subject':'English', 'Dana':[95,90], 'Benny':[80,76], 'Eyal':[57,55], 'Shira': [98,95]}
literature = {'subject':'Literature', 'Dana':[76,90], 'Mira':[80,76], 'Eyal':[67,38], 'Shira': [90,94]}

if __name__ == '__main__':
    # Question 3
    param1 = history
    param2 =  math
    return_value = compare_subjects_within_student(param1,param2)

    print(f"Question 3 solution: {return_value}" )