import shutil
import os
import time
import filecmp

def check_path_input(input_string):
    # checks if user path input is valid, otherwise raises an Exception
    if os.path.exists(input_string):
        return input_string
    else:
        raise Exception("Invalid path.")

def check_if_synchronization_interval_is_number(input_number):
    # checks if user synchronization interval input is a number, otherwise raises an Exception
    if input_number.isdigit():
        return input_number
    else:
        raise Exception("Synchronization interval needs to be a number.")

def check_if_file_removed():
    # checks if a file was removed from current source folder by comparing it to its version at the start and logs it
    for i in starting_source_folder:
        if i not in os.listdir(sf):
            starting_source_folder.remove(i)
            print(i , 'was removed by user')
            with open(log_file, 'a') as f:
                    f.write(i)
                    f.write(' was removed by user\n')

def check_if_file_created():
    # checks if a file was created in current source folder by comparing it to its version at the start and logs it
    for i in os.listdir(sf):
        if i not in starting_source_folder:
            print(i, 'was created by user')
            with open(log_file, 'a') as f:
                f.write(i)
                f.write(' was created by user\n')
            starting_source_folder.append(i)
        else: pass

def remove_redundant_files_dst(source_folder, destination_folder):
    # remove files in destination_folder that are not in source_folder
    for file_name in os.listdir(destination_folder):
        if file_name not in os.listdir(source_folder):
            if os.path.isfile(os.path.join(destination_folder, file_name)):
                os.remove(os.path.join(destination_folder, file_name))
                print('removed', file_name)
                with open(log_file, 'a') as f:
                    f.write('removed ')
                    f.write(file_name)
                    f.write('\n')
            else:
                shutil.rmtree(os.path.join(destination_folder, file_name))
                print('removed', file_name)
                with open(log_file, 'a') as f:
                    f.write('removed ')
                    f.write(file_name)
                    f.write('\n')
        if os.path.isdir(os.path.join(destination_folder, file_name)):
            dst_folder = os.path.join(destination_folder, file_name)
            src_folder = os.path.join(source_folder, file_name)
            remove_redundant_files_dst(src_folder,dst_folder)

def copy_files(source_folder, destination_folder):
    # checks whether files in source folder are located in destination folder and copies them if they are not
    for file_name in os.listdir(source_folder):
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)
        if os.path.isfile(source) and file_name in os.listdir(destination_folder):
            if filecmp.cmp(source, destination,shallow=True)==False:
                shutil.copy(source, destination)

        if os.path.isfile(source) and file_name not in os.listdir(destination_folder):
            shutil.copy(source, destination)
            print('copied', file_name)
            with open(log_file, 'a') as f:
                f.write('copied ')
                f.write(file_name)
                f.write('\n')
        if os.path.isdir(source):
            if file_name not in os.listdir(destination_folder):
                os.makedirs(destination)
                print('copied', file_name)
                with open(log_file, 'a') as f:
                    f.write('copied ')
                    f.write(file_name)
                    f.write('\n')
            source_subfolder = source
            destination_subfolder = destination
            copy_files(source_subfolder, destination_subfolder)


input_sf = input("Enter source folder path: ")

sf = check_path_input(input_sf)

input_df = input("Enter replica folder path: ")

df = check_path_input(input_df)

input_logfile = input("Enter log file path: ")

log_file = check_path_input(input_logfile)

input_synchronization_interval = input("Enter synchronization interval in seconds: ")

synchronization_interval = int(check_if_synchronization_interval_is_number(input_synchronization_interval))

starting_source_folder = os.listdir(sf)

try:
    while True:

        # check if a file or folder has been created or removed by checking if starting_source_folder differs from current source_folder
        if starting_source_folder != os.listdir(sf):
            check_if_file_removed()
            check_if_file_created()

        remove_redundant_files_dst(sf,df)

        copy_files(sf, df)

        time.sleep(synchronization_interval)

except:
    print("Error: Can't open this type of file while programme is running.")