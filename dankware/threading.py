from concurrent.futures import ThreadPoolExecutor, as_completed
from alive_progress import alive_bar

def multithread(function, threads = 1, input_one = None, input_two = None, progress_bar = True) -> None:

    futures = []
    executor = ThreadPoolExecutor(max_workers=threads)
    one_isList = type(input_one) is list
    two_isList = type(input_two) is list
    if input_one is None:one_isNone = True
    else:one_isNone = False
    if input_two is None:two_isNone = True
    else:two_isNone = False

    if one_isNone:
        for i in range(threads):futures.append(executor.submit(function))
    
    elif two_isNone:

        if one_isList:
            for item in input_one:futures.append(executor.submit(function, item))
        else:
            for i in range(threads):futures.append(executor.submit(function, input_one))

    elif not one_isNone and not two_isNone:

        if one_isList and two_isList:
            if len(input_one) != len(input_two):print(f"\n  \x1b[1;37;40m> \x1b[1;31;40mMULTITHREAD ERROR\x1b[1;37;40m! - \x1b[1;31;40minput_one\x1b[1;37;40m[\x1b[1;31;40m{len(input_one)}\x1b[1;37;40m] \x1b[1;31;40mand input_two\x1b[1;37;40m[\x1b[1;31;40m{len(input_two)}\x1b[1;37;40m] \x1b[1;31;40mdo not have the same length\x1b[1;37;40m!");return
            for index in range(len(input_one)):futures.append(executor.submit(function, input_one[index], input_two[index]))
            
        elif one_isList:
            for index in range(len(input_one)):futures.append(executor.submit(function, input_one[index], input_two))
            
        elif two_isList:
            for index in range(len(input_two)):futures.append(executor.submit(function, input_one, input_two[index]))
            
        elif not one_isList and not two_isList:
            for i in range(threads):futures.append(executor.submit(function, input_one, input_two))

    if progress_bar:
        with alive_bar(int(len(futures))) as bar:
            for future in as_completed(futures):
                try:future.result();bar()
                except:bar()
    else:
        for future in as_completed(futures):
            try:future.result()
            except:pass