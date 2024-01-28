import os
import pandas as pd

#specific constants
working_dir='/Desktop/Alex'
file_to_check='test.txt' # file directory
flag = 0


def path_information(working_dir = working_dir, chosen_wd = os.getcwd(), file_to_check=file_to_check, flag = flag):
    """
    helper function to get all relevant path, directory, or file information

    :param: working_dir: individual working directory, set by individual specific constant
    :param: chosen_wd: by default system's home directory
    :param: file_to_check: by default None, set specific file directory as string, if checking
    :param: flag: by default 0, set to 1 if you want to output the whole directory tree

    """
    # get current working directory
    current_wd = os.getcwd()
    print('Your current working directory: \n {} \n'.format(current_wd))

    #choose different working
    if chosen_wd != os.getcwd():
        changed_wd = os.chdir(chosen_wd)
        print('Your changed working directory: \n {} \n'.format(changed_wd))
    else:
        pass

    #print files in current directory
    all_files = os.listdir()
    print('All files in your working directory: \n {} \n'.format(all_files))

    #print home directory
    home = os.environ['HOME']
    print('Your home directory: \n {} \n'.format(home))

    #environments information
    env_inf = os.environ
    print('Your environment information: \n {} \n'.format(env_inf))

    #working file name
    filename = os.path.basename(os.getcwd()+__file__)
    print('Your working file name: \n {} \n'.format(filename))

    ##addition: uncomment in need
    #basename = os.path.dirname(os.getcwd() + '/' + str(os.path.basename(os.getcwd())))
    #print('Your working directory name: \n {} \n'.format(filename))

   #directory check
    check = os.path.isdir(home + working_dir)
    print('Your path exists: \n {} \n'.format(check))

    #file check
    if isinstance(file_to_check,str):
        file_check = os.path.isfile(file_to_check)
        print('The file exists in this directory: \n {} \n'.format(file_check))
    else:
        pass

    if isinstance(file_to_check,str):
        (filename, fileformat) = os.path.splitext(file_to_check)
        print('Your filename is: \n {} \n Your fileformat is: \n {} \n'.format(filename,fileformat))
    else:
        pass


#list complete project structure
    def list_files(startpath):
        """
        function, which hierarchically lists the directory structure from a given directory start point

        :param startpath: directory path, where to start from
        """
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = '-' * 4 * (level)
            print('{}{}/'.format(indent + '||', os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    if flag == 1:
        list_files(home + working_dir)
    else:
        pass