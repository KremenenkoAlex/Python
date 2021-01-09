subj = {}
with open("text6.txt", "r") as my_file:
    for i in my_file:
        subject, lecture, practice, lab = i.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print("Общее количество часов по предмету - {}".format(subj))


