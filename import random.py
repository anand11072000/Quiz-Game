class quiz:
    #created an class 
    def __init__(self,questions):
        self.questions=questions
        self.score=0
    #created an buitinclass and ask_question for displaying the question,options 
    def ask_question(self,question,options,correct_option):
        print(question)
        for i,options in enumerate(options,1):
            print(i,options)
        user_answer=self.user_input(options)
    #checks if it an correct option.
        if (user_answer==correct_option):
            print("Correct answer")
        #score increase if answer is matched
            self.score+=1
        else:
            print(f"Wrong answer!!, correct option is{correct_option}")


    def user_input(self,options ):#here an entering of options is valid upto 3times ,after entering wrongoptions
            try:
                user_option=int(input("please select an option:"))
                if 1<=user_option<=len(options):#checks the range of input size of user for options.
                    return user_option
                else:
                    print("Invalid option ,please select an valid option")
                
            except ValueError:
                print("Invalid option ,please select an valid option")
        
    def its_time(self):
        for question,(options,correct_option) in self.questions.items():
            self.ask_question(question,options,correct_option)
        print(f"The Final Score of your Quiz is {self.score} for total nunber of questions{len(self.questions)}")


random={
    "What is the primary purpose of version control systems in software development?": (["Code encryption","Code collaboration and tracking changes","Bug fixing","User authentication"], 2),
   "Which programming language is commonly used for developing mobile applications for both Android and iOS platforms?": (["Java","Python","C++","Swift"], 4),
   "What is the role of a compiler in the software development process?": (["Converts source code to machine code","Executes the program","Manages database connections","Designs user interfaces"], 1)
   }
a=quiz(random)
a.its_time()
