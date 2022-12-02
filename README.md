# folder-synchronization-task in python

This programme periodically synchronizes folders without using libraries that implement folder synchronization while logging changes in a file.
User is asked to provide path to source folder, replica folder, log file. User is also asked to provide synchronization interval.

It is accomplished by using the shutil.copy in combination with reclusive functions. Shutil.copytree function was also considered, but resulted in many erros when a file was created during the programme's run time and had problems related to permissions and periodic synchronization.

Task specifics:

Please implement a program that synchronizes two folders: source and replica. The
program should maintain a full, identical copy of source folder at replica folder.

- Synchronization must be one-way: after the synchronization content of the
replica folder should be modified to exactly match content of the source
folder.
- Synchronization should be performed periodically.
- File creation/copying/removal operations should be logged to a file and to the
console output.
- Folder paths, synchronization interval and log file path should be provided
using the command line arguments.
- It is undesirable to use third-party libraries that implement folder
synchronization.
- It is allowed (and recommended) to use external libraries implementing other
well-known algorithms. For example, there is no point in implementing yet
another function that calculates MD5 if you need it for the task – it is
perfectly acceptable to use a third-party (or built-in) library.
