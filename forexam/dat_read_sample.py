with open('files/slack.dat', mode='r',encoding="utf-8_sig") as fin:
    
    for line in fin:
        if line:
            print(line)

    fin.close()
