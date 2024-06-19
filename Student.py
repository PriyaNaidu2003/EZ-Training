class student:
    def __init__(self,na,us,marks):
        self.name=na
        self.usn=us
        self.marks=marks
        self.percentage=None
        self.grade=None
    def read(self):
        self.name=input("Enter name:")
        self.usu=input("Enter usn:")
        print("Enter the marks of 5 subjects:")
        for i in range(5):
            self.marks[i]=int(input())
    def cal_percentage_grade(self):
        self.percentage=sum(self.marks)/(5*100)*100
        if self.percentage>=90:
            self.grade="A"
        elif self.percentage>=80:
            self.grade="B"
        elif self.percentage>=70:
            self.grade="C"
        elif self.percentage>=60:
            self.grade="D"
        else:
            self.grade="F"
    def display(self):
        print("Name: %s\tUSN: %s\tMarks:"%(self.name,self.usn))
        for i in self.marks:
            print(i,end="\t")
        print("Percentage: %f\nGrade: %s"%(self.percentage,self.grade))
st=[]
marks=[0]*5
print("Student Details:")
for i in range(5):
    name=input("Enter name:")
    usn=input("Enter usn:")
    print("Enter the marks of 5 subjects:")
    marks=list(map(int,input().split()))
    st.append(student(name,usn,marks))

for i in st:
    i.cal_percentage_grade()
    print(f"{st.index(i)+1}. Student Details: \n")
    i.display()




