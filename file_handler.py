
import json

expense_tracker=[]
try:
    with open('personal_expense_tracker.json','r') as f:
        expense_tracker=json.load(f)
except FileNotFoundError:
    print('File not found, starting from scratch')
except json.decoder.JSONDecodeError:
    print('File not found, starting from scratch')

