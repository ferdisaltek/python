# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False




class Question:
    def __init__(self,text,choise,answer) :
        self.text=text
        self.choise=choise
        self.answer=answer

    def chechAnswer(self,answer):
        if answer not in self.choise:
            raise ValueError("hatali bilgi")
        return self.answer==answer

        
        

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]
print(q1.text)
print(q1.choise)
print(q1.answer)
sonuc=q1.chechAnswer( 'python')
print(sonuc)


# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)




#quiz = Quiz(sorular)