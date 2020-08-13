import os
import sys

class Student:
    def __init__(self, strID, strName, iScoreMid, iScoreFinal):
        self.strID = strID
        self.strName = strName
        self.iScoreMid = iScoreMid
        self.iScoreFinal = iScoreFinal
        self.updateAvg()
        
    def show(self):
        print('%10s %20s    %3d      %3d    %5.1f    %1c' % (self.strID, self.strName, self.iScoreMid, self.iScoreFinal, self.fScoreAvg, self.cGrade))
    
    def writeInFile(self, file):
        file.writelines('%s\t%s\t%i\t%i\n' % (self.strID, self.strName, self.iScoreMid, self.iScoreFinal))
        
    def setScoreMid(self, iScore):
        self.iScoreMid = iScore
        self.updateAvg()
        
    def setScoreFinal(self, iScore):
        self.iScoreFinal = iScore
        self.updateAvg()
        
    def updateAvg(self):
        self.fScoreAvg = (self.iScoreMid + self.iScoreFinal) / 2
        self.updateGrade()
        
    def updateGrade(self):
        scoreAvg = self.fScoreAvg
        cGrade = 'F'
        if scoreAvg >= 90:
            cGrade = 'A'
        elif scoreAvg >= 80:
            cGrade = 'B'
        elif scoreAvg >= 70:
            cGrade = 'C'
        elif scoreAvg >= 60:
            cGrade = 'D'
            
        self.cGrade = cGrade
        
class StudentMgr:
    def __init__(self):
        self.dictStudents = dict()
        
    def __contains__(self, strID):
        if strID in self.dictStudents:
            return True
        
        return False
        
    def sortedAvg(self, listStudents):
        return sorted(listStudents, key=lambda student:student.fScoreAvg, reverse=True)

    def showTitle(self):
        print('=' * 65)
        print('   Student                 Name  Midterm  Final  Average  Grade')
        print('=' * 65)

    def showAll(self, bShowTitle = True):
        listStudents = self.sortedAvg(self.dictStudents.values())
        
        if bShowTitle == True:
            self.showTitle()
            
        for student in listStudents:
            student.show()
            
    def showByID(self, strID, bShowTitle = True):            
        student = self.searchByID(strID)
        if student != None:
            if bShowTitle == True:
                self.showTitle()
            student.show()
        else:
            print('NO SUCH PERSON.')
            return
            
    def showAllByGrade(self, cGrade, bShowTitle = True):
        cGrade = cGrade.strip().upper()
        if cGrade not in ['A', 'B', 'C', 'D', 'F']:
            return
        
        listStudents = []
        for student in self.dictStudents.values():
            if student.cGrade == cGrade:
                listStudents.append(student)
                
        if len(listStudents) == 0:
            print('NO RESULTS.')
            return
            
        listStudents = self.sortedAvg(listStudents)
        
        if bShowTitle == True:
            self.showTitle()
            
        for student in listStudents:
            if student.cGrade == cGrade:
                student.show()
                
    def searchByID(self, strID):
        if strID in self.dictStudents:
            return self.dictStudents[strID]
        
        return None
                
    def changeScoreMid(self, strID, iScore):
        if strID not in self.dictStudents:
            raise Exception()
            
        self.dictStudents[strID].setScoreMid(iScore)
        
    def changeScoreFinal(self, strID, iScore):
        if strID not in self.dictStudents:
            raise Exception()
            
        self.dictStudents[strID].setScoreFinal(iScore)
        
    def add(self, strID, strName, iScoreMid, iScoreFinal):
        if strID in self.dictStudents:
            raise Exception()
            
        self.dictStudents[strID] = Student(strID, strName, iScoreMid, iScoreFinal)
        
    def remove(self, strID):
        if strID not in self.dictStudents:
            raise Exception()
        
        self.dictStudents.pop(strID)
        
    def isEmpty(self):
        return len(self.dictStudents) == 0
    
    def saveFile(self, strOutputFile):
        fw = open(strOutputFile, 'w')
        
        listStudents = self.sortedAvg(self.dictStudents.values())
        
        for student in listStudents:
            student.writeInFile(fw)
            
        fw.close()
        
    def loadFile(self, strInputFile):
        if strInputFile == None:
            return

        fr = open(strInputFile, 'r')
        
        while True:
            strLine = fr.readline()
            if strLine == '':
                break
                
            strID, strName, iScoreMid, iScoreFinal = strLine.split('\t')
            iScoreMid = int(iScoreMid)
            iScoreFinal = int(iScoreFinal)
            
            self.add(strID, strName, iScoreMid, iScoreFinal)
            
        fr.close()
    
class MainMenu:
    def __init__(self, studentMgr = StudentMgr()):
        self.studentMgr = studentMgr
        
    def menu(self):
        listCommand = {
            'show' : self.show,
            'search' : self.search,
            'changescore' : self.changeScore,
            'add' : self.add,
            'searchgrade' : self.searchGrade,
            'remove' : self.remove,
            'quit' : self.quit,

        }

        print('학생관리 프로그램')
        print('명령어 종류 %s' % (', '.join(listCommand.keys())))
        
        strInput = ''
        self.bExit = False

        while self.bExit == False:
            strInput = input('# ').strip().lower()

            if strInput in listCommand:
                listCommand[strInput]()

            print()
                    
    def show(self):
        self.studentMgr.showAll()
        
    def search(self):
        if self.studentMgr.isEmpty() == True:
            print('List is empty.')
            return
        
        strID = input('Student ID: ')
        
        self.studentMgr.showByID(strID)
        
    def changeScore(self):
        if self.studentMgr.isEmpty() == True:
            print('List is empty.')
            return
        
        strID = input('Student ID: ')
        if strID not in self.studentMgr:
            print('NO SUCH PERSON.')
            return

        dictCommand = { 
            'mid' : self.studentMgr.changeScoreMid,
            'final' : self.studentMgr.changeScoreFinal
        }

        strTypeScore = input(('%s? ' % '/'.join(dictCommand.keys())).title).strip().lower()
        if strTypeScore not in dictCommand:
            return
        
        strScore = input('Input new score: ')
        if strScore.isdecimal() == False:
            return
        
        iScore = int(strScore)
        if iScore < 0 or iScore > 100:
            return

        dictCommand[strTypeScore](strID, iScore)

        print('Score changed.')
        self.studentMgr.showByID(strID, False)
        
    def add(self):
        strID = input('Student ID: ')
        if strID in self.studentMgr:
            print('ALREADY EXISTS.')
            return
        
        strName = input('Student Name: ')
        
        strScoreMid = input('Student Mid Score: ')
        if strScoreMid.isdecimal() == False:
            return
        
        iScoreMid = int(strScoreMid)
        if iScoreMid < 0 or iScoreMid > 100:
            return
        
        strScoreFinal = input('Student Final Score: ')
        if strScoreFinal.isdecimal() == False:
            return
        
        iScoreFinal = int(strScoreFinal)
        if iScoreFinal < 0 or iScoreFinal > 100:
            return
        
        self.studentMgr.add(strID, strName, iScoreMid, iScoreFinal)
        print('student added.')
        
    def searchGrade(self):
        if self.studentMgr.isEmpty() == True:
            print('List is empty.')
            return
        
        strInput = input('Grade to search: ').strip().upper()
        
        self.studentMgr.showAllByGrade(strInput)       
        
        
    def remove(self):
        if self.studentMgr.isEmpty() == True:
            print('List is empty.')
            return
        
        strID = input('Student ID: ')
        if strID not in self.studentMgr:
            print('NO SUCH PERSON.')
            return
        
        self.studentMgr.remove(strID)
        print('Student removed.')
        
    def quit(self):
        while True:
            strInput = input('Save data? [yes/no]').strip().lower()
            
            if strInput == 'yes':
                strSaveFileName = input('File name: ')
                if strSaveFileName == '':
                    return
                
                self.studentMgr.saveFile(strSaveFileName)
                self.bExit = True
                return
            
            elif strInput == 'no':
                self.bExit = True
                return

def main():
    defaultFileName = 'students.txt'

    if len(sys.argv) > 1:   #매개변수로 로드할 파일 이름 입력이 있는 경우
        if os.path.exists(sys.argv[1]) == True:
            defaultFileName = sys.argv[1]
        else:   #입력된 파일 이름을 찾을 수 없을 경우
            print('file not found')
            return

    studentMgr = StudentMgr()
    studentMgr.loadFile(defaultFileName)
    mainMenu = MainMenu(studentMgr)

    mainMenu.menu()

main()