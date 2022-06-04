# Copyright 2022 contributors to the add-copyright project

def add_copyright():

    import os
    import sys

    timeframe = str(sys.argv[1])
    project = str(sys.argv[2])
    file_type = str(sys.argv[3])
    print(f'Adding copyright lines to all .{file_type} files...')

    # Create an array of paths mirroring structure of current directory while ignoring this script.
    paths = []
    for (root, dirs, files) in os.walk('.', topdown=True):
        for f in files:
            if f == 'add-copyright.py':
                continue
            else:
                path = os.path.join(root, f)
                paths.append(path)
    f_total = len(paths)

    # Iterate through file paths, adding a copyright line to each file having the specified type.
    ftype_count = 0
    exec_flag = False
    for p in paths:
        if '.circleci' in p:
            continue
        elif '.github' in p:
            continue 
        elif '.gitignore' in p:
            continue
        else:        
            if file_type == 'java':
                if p[-4:] == 'java':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'/* Copyright {timeframe} contributors to the {project} project */\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'py':
                if p[-2:] == 'py':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'# Copyright {timeframe} contributors to the {project} project\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'md':
                if p[-2:] == 'md':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'<!-- Copyright {timeframe} contributors to the {project} project -->\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'html':
                if p[-2:] == 'html':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'<!-- Copyright {timeframe} contributors to the {project} project -->\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'txt':
                if p[-3:] == 'txt':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'Copyright {timeframe} contributors to the {project} project\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'rs':
                if p[-2:] == 'rs':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'// Copyright {timeframe} contributors to the {project} project\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
            elif file_type == 'sh':
                if p[-2:] == 'sh':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'a') as t:
                        line = f'\n# Copyright {timeframe} contributors to the {project} project'
                        t.write(line)
            elif file_type == 'ts':
                if p[-2:] == 'ts':
                    exec_flag = True
                    ftype_count += 1
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        line = f'// Copyright {timeframe} contributors to the {project} project\n\n'
                        contents.insert(0, line)
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)
    
    print('Done!')
    if exec_flag == True:
        if ftype_count != 1:
            print(f'Result: {ftype_count} files changed out of {f_total} total in directory.')
        else:
            print(f'Result: {ftype_count} file changed out of {f_total} total in directory.')
    else:
        print(f'No files changed out of {f_total} in directory.')

add_copyright()