class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )



class BinaryMap:
    def __init__(self):
        self.table=[]
    def size(self):
        return len(self.table)
    def display(self,msg):
        print(msg)
        for entry in self.table:
            print("  ", entry)

    def insert(self, key, value):
        self.table.append(Entry(key, value))
    def sort(self):
        n=self.size()
        for i in range(n - 1, 0, -1):
            bChanged = False
            for j in range(i):
                if (self.table[j].key > self.table[j + 1].key):
                    self.table[j], self.table[j + 1] = self.table[j + 1], self.table[j]
                    bChanged = True

            if not bChanged: break

    def search(self, key,low,high):

        if (low <= high):
            middle = (low + high) // 2

            if key == self.table[middle].key:
                return self.table[middle]
            elif (key < self.table[middle].key):
                return self.search(key, low, middle - 1)
            else:
                return self.search(key, (middle + 1), high)
        print("찾는 전화번호가 없습니다.")
        return None
file_path = "9week3.txt"
with open(file_path) as f:
    lines = f.read().splitlines()

bi=BinaryMap()
for i in range(len(lines)):
	list=lines[i].split()
	bi.insert(list[0], list[1])
bi.display("전화번호부(정렬전):")
bi.sort()
bi.display("전화번호부(정렬후):")
while True:
	name=input("이름을 입력하세요 (q-종료):")
	if name == "q":
		break

	result = bi.search(name, 0, bi.size()-1)
	if not result == None:
		print(result.key, " : ", result.value)

