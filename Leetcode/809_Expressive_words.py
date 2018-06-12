def expressiveWords(S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = {}
        
        
        def get_dict(s):
            x = set(s)    
            for i in x:
                if (i+i+i) in s:
                    try:
                        d[i] +=1
                    except:
                        d[i] =1

        
        def extend(word):
            m = dict(d)
            print(m)
            temp = word
            for c in word:
                
                if c in m and m[c] > 0:
                    print(m[c])
                    print(c)
                    temp = temp.replace(c,c+c+c,1)
                    m[c] -=1
            print(temp)
            if len(temp) == len(S):
                g[0] +=1
            print("\n")
            
                

        get_dict(S)
        # print(d)
        g = [0]

        for word in words:
            if(set(word) == set(S)):
                extend(word)

        print(g[0])

S = "heeelleeooo"
words = ["hello", "hi", "helo","helleeo"]
expressiveWords(S,words)