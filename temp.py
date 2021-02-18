# Let's answer some of your questions

# Import required libraries
import yaml
import IPython
from rich.console import Console
from rich.panel import Panel
from IPython.display import Image
from IPython.display import display             

# Setup console output and format
console = Console()
q_style = 'bold red'
a_style = 'bold blue'

# Read the YAML file with the Q&A data
f = open('questions-kv.yaml')
q = yaml.safe_load(f)
f.close()

# Function to display image
def func_img(f):
    img = Image(filename=f, width=480)
    display(img)

# Function to display answers to questions
def func_qa(qa):
    console.print (qa[0], style=q_style)
    console.print (*qa[1], sep="\n\n", style=a_style)

# Logic to loop through question and get my answers
for key in q:
    qa = (key, q[key])
    if qa[0] == 'What is the most fun about your job?':  
        func_qa(qa)
        func_img('./images/etchasketch.png')
    elif qa[0] == 'How many years have you been coding?':
        func_qa(qa)
        func_img('./images/me.jpg')
    elif qa[0] == 'How did you start liking coding?':
        func_qa(qa)
        func_img('./images/c64.jpg')
    elif qa[0] == 'How did you pursue coding?':
        func_qa(qa)
        func_img('./images/curious.png')
    elif qa[0] == 'Have you always wanted to be a coder?':
        func_qa(qa)
        func_img('./images/maker.jpg')
    elif qa[0] == 'What kind of coding do you do for your job?':
        func_qa(qa)
        func_img('./images/dc.jpg')
    elif qa[0] == 'What schooling did you get for your job?':
        func_qa(qa)
        func_img('./images/philospher.jpg')
    elif qa[0] == 'At your place of work, how much do coders make?':
        func_qa(qa)
        func_img('./images/zuck.png')
    elif qa[0] == 'What has been your greatest coding challenge?':
        func_qa(qa)
        func_img('./images/fear.jpg')
    elif qa[0] == 'Do you ever get bored of coding?':
        func_qa(qa)
        func_img('./images/coders-life.jpg')
    elif qa[0] == 'From 1-10, how do you rate coding?':
        func_qa(qa)
        func_img('./images/codersgonnacode.jpg')
    elif qa[0] == 'Have you ever made any games?':
        func_qa(qa)
        func_img('./images/pong.jpg')
    else:
        console.print(Panel('Not a valid question.',title='ERROR',style='red'))
        func_img('./images/error.jpg')
    # console.input('Press enter for next question.')
    # IPython.display.clear_output()
    
# The end
console.print(Panel('I can answer any question you have.',title='The End',style='red'))
console.print(':mega: My Contatct Info :mega:')
console.print('Rich Bocchinfuso :person_with_blond_hair: ')
console.print('rbocchinfuso@gmail.com :e-mail:')
console.print('http://bocchinfuso.net :page_with_curl: ')
console.print('@rbocchinfuso')
func_img('./images/ty.jpg')