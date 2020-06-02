import os

path = ["E:/Courses/Udemy-Complete Machine Learning and Data Science Zero to Mastery 2020", "E:/PythonWorks/jupyter_projects/rough_project"]

for index, path in enumerate(path): 

    path = os.path.realpath(path)
    os.startfile(path)
    if index == 1:
        os.chdir(path)
        os.system('cmd /k "jupyter notebook"')
    

