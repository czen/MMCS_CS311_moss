# usage:
# sudo pip install mosspy
# python mossify.py
import mosspy
import os

userid = 448215352

m = mosspy.Moss(userid, "csharp")
m.setDirectoryMode(1);

targetFilePaths = [
        "Module1/Lexer.cs",
        "Module2/SimpleLangLexer/SimpleLexer.cs",
        "Module2/SimpleLexerDemo/Program.cs",
        "Module3/SimpleLex.lex",
        "Module3/mymain.cs",
        "Module3/LexerAddon.cs",
        "Module4/SimpleLangParser/SimpleLangParser.cs",
        "Module4/SimpleLangParserTest/Program.cs",
        "Module5/Main.cs",
        "Module5/SimpleLex.lex",
        "Module5/SimpleYacc.y",
        "Module6/SimpleYacc.y",
        "Module6/SimpleLex.lex",
        "Module6/Main.cs",
        "Module6/ProgramTree.cs",
        "Module7/SimpleLex.lex",
        "Module7/Main.cs",
        "Module7/ProgramTree.cs",
        "Module7/Visitors/AssignCountVisitor.cs",
        "Module7/Visitors/AutoVisitor.cs",
        "Module7/Visitors/ChangeVarIdVisitor.cs",
        "Module7/Visitors/CommonlyUsedVarVisitor.cs",
        "Module7/Visitors/CountCyclesOpVisitor.cs",
        "Module7/Visitors/ExprComplexityVisitor.cs",
        "Module7/Visitors/MaxIfCycleNestVisitor.cs",
        "Module7/Visitors/MaxNestCyclesVisitor.cs",
        "Module7/Visitors/PrettyPrintVisitor.cs",
        "Module7/Visitors/Visitor.cs",
        "Module8/SimpleYacc.y",
        "Module8/SimpleLex.lex",
        "Module8/Main.cs",
        "Module8/ProgramTree.cs",
        "Module8/Visitors/AssignCountVisitor.cs",
        "Module8/Visitors/AutoVisitor.cs",
        "Module8/Visitors/PrettyPrintVisitor.cs",
        "Module8/Visitors/Visitor.cs",
        "Module8/Visitors/GenCodeVisitors/GenCodeCreator.cs",
        "Module8/Visitors/GenCodeVisitors/GenCodeVisitor.cs"
    ]


#baseProjectPath = "/projects/compilers/"
#baseDirPath = "/projects/submissions/"

baseProjectPath = "/home/czen/work/Compilers/compilers/"
baseDirPath = "/home/czen/work/Compilers/repos/submissions/"

for targetFilePath in targetFilePaths:
    newBaseFile = baseProjectPath + targetFilePath
    print("base file added:", newBaseFile)
    m.addBaseFile(newBaseFile)
    

submissionPaths = os.listdir(baseDirPath)

for submissionPath in submissionPaths:
    for tagetFilePath in targetFilePaths:
        newFile = baseDirPath + submissionPath + "/" + targetFilePath
        print("file added:", newFile)
        m.addFile(newFile)
        
       
# exit()

# m.addFilesByWildcard("submission/a01-*.py")

url = m.send() # Submission Report URL

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "report.html")

# Download whole report locally including code diff links
mosspy.download_report(url, "report/", connections=8)