# folder-synchronization-task

A folder synchronization programme without using libraries that implement folder synchronization.
User is asked to provide path to source folder, replica folder, log file. User is also asked to provide synchronization interval.

It is accomplished by using the shutil.copy in combination with reclusive functions. Shutil.copytree function was also considered, but resulted in many erros when a file was created during the programme's run time and caused other problems during periodic synchronization.
