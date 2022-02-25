def ft_progress(lst):
    try:
        if start:
            nothing = 1
    except Exception:
        start = time.time()
        last = 0
    for n in lst:
        progress = (n * 100) / max(lst)
        n += 1
        i = int(progress)
        eta = (last - time.time()) * (max(lst) - n)*-1
        print("ETA: "+str(round(eta))+"s ["+str(i)+"%][" +
              '=' * int(i/5) + '>' + ' ' * (20 - int(i/5)) +
              "] " + str(n) + "/" + str(1 + max(lst)) +
              " elapsed time " + str(round(time.time() - start, 2)) + "s")
        last = time.time()
        yield n
