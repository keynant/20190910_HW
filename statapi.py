import os
class StatApi:
    def checkSize(path):
        a = list(os.walk(path))[0][1]
        # b = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]  #<---Different approach
        d = {}
        for dir in a:
            sum = 0
            for root, dirs, files in os.walk(os.path.join(path, dir)):
                for file in files:
                    sum += os.stat(os.path.join(root, file)).st_size
                d[str(dir)] = float(format(sum/1024/1024, ".2f"))
        sum = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                sum += os.stat(os.path.join(root, file)).st_size
            d["Root"] = float(format(sum / 1024 / 1024, ".2f"))
        StatApi.__printSize(d,path)
        return d

    def __printSize(d,path):
        totalSize = d["Root"]
        percentSize = 0
        remainderPercent = 100
        remainderSize = totalSize
        ls1 = []
        print(f"Size check for {path}")
        print(f'Root directory total size: {d["Root"]}MB')
        for k,v in d.items():
            if k == "Root":
                continue
            ls1.append((k,v))
        ls1.sort(key = lambda ls1:ls1[1],reverse=True)   #Don't really understand that, got that from the web

            # print(f'{path}\\{k} {format((v/totalSize)*100,".2f")}% {v}MB')
        for item in ls1:
            percentSize = float(format((item[1]/totalSize)*100,".2f"))
            print(f'Sub directory {item[0]} accounts for {percentSize}% of {path}. Size: {item[1]}MB')
            remainderPercent-=percentSize
            remainderSize-=item[1]
            remainderPercent=float(format(remainderPercent,".2f"))
            remainderSize = float(format(remainderSize, ".2f"))
        print(f"Loose files in {path} account for the remaining {remainderPercent}%. Size: {remainderSize}MB")





def main():
    a = r"C:\ZBRUSH_TEMP"
    StatApi.checkSize(a)


if __name__ == "__main__":
    main()