class Diary:
    
    def __init__(self):
       pass


    def make_snippet(self, text):

        a = text.split(" ")
        returnTxt = ""
        for i in range(5):
            returnTxt += a[i]
            if i != 4:
                returnTxt += " "
            else:
                returnTxt += "..."
        return returnTxt


        
    def count_words(self, string):
        a = string.split(" ")
        return len(a)