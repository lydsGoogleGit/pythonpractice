import os

the_people = []

directory = os.fsencode("Images/team_members_photos/")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    the_people.append(filename)
    # code used to rename files in bulk
    # if "__" in filename:
    #     old_file = os.path.join("Images/team_members_photos/", f"{filename}")
    #     new_file_name = old_file.split("__")[1]
    #     new_file = os.path.join("Images/team_members_photos/", f"{new_file_name}")
    #     os.rename(old_file, new_file)
