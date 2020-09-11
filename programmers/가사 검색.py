import sys
sys.setrecursionlimit(10000)

class node:
    def __init__(self):
        self.wordChildCount = dict()
        self.listChild = dict()
        self.listWord = []  # word


    def add(self, word, index = 0):
        if len(word) not in self.wordChildCount:
            self.wordChildCount[len(word)] = 0

        self.wordChildCount[len(word)] += 1
        if index < len(word):
            self.listWord.append(word)


    def check(self, query, index = 0):
        if index >= len(query):
            return 1

        if query[index] == '?':
            if len(query) in self.wordChildCount:
                return self.wordChildCount[len(query)]
                
            return 0

        # listWord에 word들이 있다면 한단계 더 분류
        if self.listWord != None:
            for word in self.listWord:
                char = word[index]
                if char not in self.listChild:
                    self.listChild[char] = node()

                self.listChild[char].add(word, index + 1)

            self.listWord = None

        char = query[index]
        if char in self.listChild:
            return self.listChild[char].check(query, index + 1)
        
        return 0


def solution(words, queries):
    myNode = node()
    myNodeInverse = node()

    for word in words:
        myNodeInverse.add(word[::-1])
        myNode.add(word)

    answer = []
    for query in queries:
        if query[0] == '?':
            answer.append(myNodeInverse.check(query[::-1]))
        else:
            answer.append(myNode.check(query))
    
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "????f", "fro??"]

# words = ["z", "z", "z", "f", "f", "f"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

#[3, 2, 4, 1, 0]

print(solution(words, queries)) 