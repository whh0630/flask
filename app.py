
from flask import Flask, render_template
app = Flask(__name__)
from lotto import *
import json
import numpy as np

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/lotto')
def lotto():

    num_stack = []
    for i in range(45) :
        num_stack.append({'name':'#N'+str(i+1), 'stacked':0})
    
    for i in lot.list :
        num_stack[i['drwtNo1']-1]['stacked'] = num_stack[i['drwtNo1']-1]['stacked'] + 1
        num_stack[i['drwtNo2']-1]['stacked'] = num_stack[i['drwtNo2']-1]['stacked'] + 1
        num_stack[i['drwtNo3']-1]['stacked'] = num_stack[i['drwtNo3']-1]['stacked'] + 1
        num_stack[i['drwtNo4']-1]['stacked'] = num_stack[i['drwtNo4']-1]['stacked'] + 1
        num_stack[i['drwtNo5']-1]['stacked'] = num_stack[i['drwtNo5']-1]['stacked'] + 1
        num_stack[i['drwtNo6']-1]['stacked'] = num_stack[i['drwtNo6']-1]['stacked'] + 1
    # print(num_stack)
    return render_template('lotto.html', list = lot.list[::-1])




if __name__ == '__main__':
    try:
        with open("lotto.json", "r") as file:
            lot.list = json.load(file)
            lot.updated_wg = lot.list[-1]['drwNo']
    except :
        print(' * ERROR - file is empty or error')

    lot.GetLast()
    print('Updated wg index : {}'.format(lot.updated_wg)) 
    print('Last wg index : {}'.format(lot.last_wg)) 
    lot.GetWinningAllNumbers() 

    with open("lotto.json", 'w') as outfile:
        json.dump(lot.list, outfile)


    app.run(host='192.168.0.2', debug=True)