from sys import argv as args
from sys import exit as leave

def helpu():
    print()
    print("Usage: python main.py <<mode>> <<data>>")
    print()
    print("[File] mode: Reads numbers from a file, and returns the mean.. File should be put in place of <<data>>")
    fh = """
    If you choose file mode, ensure that each number is in a seperate line
    For example:
    10
    15
    19
    75,000
    """
    print(fh)
    print()
    print("[asarg] mode: Reads data from arguments")
    print("Example: python main.py file data.txt")
    print("Example: python main.py --asarg 10 20 17 56")
    print()

if len(args) == 1:
    helpu()
    leave()

if args[1] == "file" or args[1] == "--file":
    data = open(args[2], 'r').readlines()
    holder = []
    for d in data:
        l = str(d).replace('\n', '')
        l = str(l).replace(' ', '')
        l = str(l).replace(',', '')
        if l != '':
            try:
                holder.append(int(l))
            except ValueError:
                print("[!] Not adding {" + l + "} to the mix {invalid format}")
    data = holder
    sumf = 0
    for number in data:
        sumf += number
    print("Mean:", str(sumf/len(data)))

elif args[1] == "asarg" or args[1] == "--asarg":
    c = 2
    sumf = 0
    while c < len(args):
        sumf += int(args[c]) 
        c += 1
    mean = sumf/(len(args) - 2)
    print("Mean:", str(mean))

elif args[1] == "help" or args[1] == "--help":
    helpu()