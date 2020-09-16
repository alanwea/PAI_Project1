#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, path

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}

# Suggestion from the field that the newer os.scandir is preferable, but listdir
# is what is imported, so using it.
    try:
      in_files = listdir(image_dir)
    except:
      print('Exception: could not open ', image_dir)

#    file_set = set(' '.join(item.split('_')[:-1]).lower().strip()


#    file_set = set(in_files)
#    file_list = list(file_set)

#    print('All of in_files',in_files)
#    for item in in_files:
#      print(item)
#      print(item.split('_'))
#      print(item.split('_')[:-1])
#      print(' '.join(item.split('_')[:-1]))

#    for i in range(len(in_files)):
#        results_dic[in_files[i]] = ' '.join(in_files[i].split('_')[:-1])

# Iterate through the filenames in in_files.  For each, create a key from the filename and
# a value from splitting the filename, truncating the filename number and extension, then
# joining together whats left, converting to lower case and striping leading/training spaces
# Bosten_terrier_02259.jpg ==> results_dic{Bosten_terrier_02259.jpg, [bosten terrier]}
    for pet_file in in_files:
#        pet_label = [' '.join(pet_file.split('_')[:-1])]
        results_dic[pet_file] = [' '.join(pet_file.split('_')[:-1]).lower().strip()]

#for item in in_files:
#    mydict = dict(enumerate(line.strip() for line in f3data))

#    results_dic = dict(enumerate(' '.join(item.split('_')[:-1]).lower().strip() for item in # in_files))

#      results_dic = ' '.join(item.split('_')[:-1]).lower().strip()
#    pet_label = ''

#    pet_label = in_files[2].split('_')
#    print('lop off list ', pet_label[:-1] )
# .join() with lists
#    separator = ', '
#    pet_label_join = ' '.join(pet_label[:-1])
#    pet_label_lower = pet_label_join.lower()

#    print('All in one line ', ' '.join(pet_label[:-1]).lower())
#    print(join(pet_label[:-1]))
#    print(type(in_files))

#    file_set = set(in_files)
#    file_list = list(file_set)
#    results_dic = file_list

#    results_dic = list(set(in_files))


#    print(results_dic[2])

#    for filename in listdir(image_dir):
#        if filename.endswith(".jpg"):
#            print(path.join(image_dir, filename))
#        else:
#            continue

#    if in_files[0] not in results_dic:
#      results_dic[in_files[idx]] = [pet_label]

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
