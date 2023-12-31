from flask import render_template, flash, request, redirect, url_for
from app import app, models
from .forms import PartNumForm, AnswerButtonForm
from flask_login import current_user, login_user, logout_user
import logging
import time
import random
import json

prevtime = 0
count = 0
partNum = ""
answersDict = {}
arr = [["dataset_1_area.png", "Which year had the least medals across all countries?", "1984", "1992", "2004", "2012", "1992", "1a"],
    ["dataset_1_line.png", "Which year had the least medals across all countries?", "1984", "1992", "2004", "2012", "1992", "1l"],
    ["dataset_2_area.png", "How many medals were won in 2012?", "160", "180", "127", "108", "127", "2a"],
    ["dataset_2_line.png", "How many medals were won in 2012?", "160", "180", "127", "108", "127", "2l"],
    ["dataset_3_area.png", "How many medals did Japan win in 2020?", "32", "28", "40", "39", "32", "3a"],
    ["dataset_3_line.png", "How many medals did Japan win in 2020?", "32", "28", "40", "39", "32", "3l"],
    ["dataset_4_area.png", "How many years does the data cover?", "10", "20", "36", "4", "36", "4a"],
    ["dataset_4_line.png", "How many years does the data cover?", "10", "20", "36", "4", "36", "4l"],
    ["dataset_5_area.png", "In which year were the fewest medals won?", "2016", "2020", "2012", "2000", "2000", "5a"],
    ["dataset_5_line.png", "In which year were the fewest medals won?", "2016", "2020", "2012", "2000", "2000", "5l"],
    ["dataset_6_area.png", "Which country won the most medals in 2004?", "Japan", "USA", "UK", "Canada", "USA", "6a"],
    ["dataset_6_line.png", "Which country won the most medals in 2004?", "Japan", "USA", "UK", "Canada", "USA", "6l"],
    ["dataset_7_area.png", "In which year did the USA win the most medals?", "1984", "1992", "1994", "2020", "1984", "7a"],
    ["dataset_7_line.png", "In which year did the USA win the most medals?", "1984", "1992", "1994", "2020", "1984", "7l"],
    ["dataset_8_area.png", "Which country won the least medals in a single year?", "Japan", "Canada", "UK", "USA", "Japan", "8a"],
    ["dataset_8_line.png", "Which country won the least medals in a single year?", "Japan", "Canada", "UK", "USA", "Japan", "8l"],
    ["dataset_9_area.png", "In which year did France win the most medals?", "1988", "2012", "1996", "2020", "2012", "9a"],
    ["dataset_9_line.png", "In which year did France win the most medals?", "1988", "2012", "1996", "2020", "2012", "9l"],
    ["dataset_10_area.png", "Which country has never won more than 80 medals?", "UK", "Switzerland", "Germany", "France", "UK", "10a"],
    ["dataset_10_line.png", "Which country has never won more than 80 medals?", "UK", "Switzerland", "Germany", "France", "UK", "10l"]
]
random.shuffle(arr)


@app.route('/questiontest', methods=['GET', 'POST'])
def questiontest():
    global count
    global prevtime
    global partNum
    form = AnswerButtonForm()
    if form.validate_on_submit():
        print("\n")
        print(arr[count][1])
        print("Answer Selected:", list(request.form.values())[1])
        print("Correct Answer:", arr[count][6])
        nowtime = time.time()
        timeDelta = nowtime - prevtime
        print("Answer Time:", timeDelta)
        answersDict[arr[count][7]] = [(list(request.form.values())[1] == arr[count][6]), timeDelta]
        prevtime = time.time()

        print(answersDict)
        count+=1

        
        if count != 20:
            return redirect(url_for('questiontest'))
        else:
            filename = str(partNum) + ".json"
            with open(filename, "w") as outfile: 
                json.dump(dict(sorted(answersDict.items())), outfile)
            return redirect(url_for('main'))
    return render_template('questiontest.html', title='Question Test', form=form, arr=arr, count=count)

#Function that is called when at '/' route
@app.route('/', methods=['GET', 'POST'])
def main():
    global prevtime
    global partNum
    form = PartNumForm()
    #Form validation
    if form.validate_on_submit():
        partNum = form.number.data
        print("Participant Number:", form.number.data)
        print("Start Time:", time.time())
        prevtime = time.time()
        return redirect(url_for('questiontest'))
    return render_template('main.html', title='Main', form=form)

