from datetime import datetime
from django.shortcuts import render

from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

def index(request):
    now = datetime.now()

    return render(
        request,
        "VennDiagApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Data Analyzer",
            'message' : "Welcome to Venn Diagram App!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
def analyzer(request):
    First = str(request.FILES["DataA"].read())[2:]
    Second = str(request.FILES["DataB"].read())[2:]
    First = First.replace("\"", "")
    Second = Second.replace("\"", "")
    First = First.replace("\'", "")
    Second = Second.replace("\'", "")
    First = First.split("\\r\\n")
    Second = Second.split("\\r\\n")
    venn2([set(First), set(Second)])
    plt.show()
    
    common = []
    InSecond_notInFirst = []
    InFirst_notInSecond = []
    for item in First:
        if item in Second:
            common.append(item)
        else:
            InFirst_notInSecond.append(item)

    for item in Second:
        if item not in First:
            InSecond_notInFirst.append(item)

    return render(
        request,
        "VennDiagApp/analyzer.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'common' : common,
            'InFirst_notInSecond': InFirst_notInSecond,
            'InSecond_notInFirst': InSecond_notInFirst
        }
    )