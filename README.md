# folder-synchronization-task in python

This programme periodically synchronizes folders without using libraries that implement folder synchronization while logging changes in a file.
User is asked to provide path to source folder, replica folder, log file. User is also asked to provide synchronization interval.

It is accomplished by using the shutil.copy in combination with reclusive functions. Shutil.copytree function was also considered, but resulted in many erros when a file was created during the programme's run time and had problems related to permissions and periodic synchronization.
