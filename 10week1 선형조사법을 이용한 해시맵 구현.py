#7.6 선형조사법 해시맵
class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )
class HashLinearMap:
    def __init__( self, M ):
        self.table = [None]*M
        self.M = M

    def hashFn(self, key) :
        sum = 0
        for c in key :
            sum = sum +  ord(c)
        return sum % self.M

    def insert(self, key, value) :
        idx = self.hashFn(key)
        for i in range(self.M):
            if self.table[idx] == -1 or self.table[idx]==None:
                self.table[idx] = Entry(key, value)
                return
            else:
                idx = (idx + 1) % self.M
        print("bucket is full")



    def search(self, key) :
        idx = self.hashFn(key)
        for i in range(self.M):
            if self.table[idx] == -1 or self.table[idx]==None:
                idx = (idx + 1) % self.M
            elif self.table[idx].key == key:
                return self.table[idx]
            else:
                idx = (idx + 1) % self.M
        return None

    def delete(self, key) :
        idx = self.hashFn(key)
        for i in range(self.M):
            if self.table[idx].key == key:
                self.table[idx] = -1
                return
            else:
                idx = (idx + 1) % self.M


    def display(self, msg):
        print(msg)
        for idx in range(self.M) :
            print("[%2d] -> " % idx, end='')
            print(self.table[idx])


map=HashLinearMap(13)
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형 탐색')
map.insert('game','게임')
map.insert('binary search','이진 탐색')
map.display("나의 단어장:")

print(" 탐색:game__>",map.search('game'))
print(" 탐색:over__>",map.search('over'))
print(" 탐색:data__>",map.search('data'))

map.delete('game')
map.display("나의 단어장:")
print(" 탐색:game__>",map.search('game'))

