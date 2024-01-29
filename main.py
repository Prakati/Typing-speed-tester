from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading



total_time = 60
time = 0
wrong_word = 0
elapsed_time_in_minutes = 0


def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        elapsed_timer_label.config(text=time)
        remaining_time = total_time-time
        remaining_timer_label.config(text=remaining_time)
        sleep(1)
        window.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)


def count():
    while time != total_time:
        entered_paragraph = textarea.get(1.0, END).split()
        total_words = len(entered_paragraph)

    total_word_count_label.config(text=total_words)

    para_word_list = label_paragraph['text'].split()

    global wrong_word

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
            wrong_word += 1
    wrong_word_count_label.config(text=wrong_word)

    global elapsed_time_in_minutes

    elapsed_time_in_minutes = time/60

    wpm = (total_words-wrong_word)/elapsed_time_in_minutes
    wpm_count_label.config(text=wpm)

    gross_word = total_words/elapsed_time_in_minutes
    accuracy = round(wpm/gross_word*100)
    accuracy_percent_label.config(text=str(accuracy)+'%')


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time, elapsed_time_in_minutes
    time = 0
    elapsed_time_in_minutes = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text=0)
    remaining_timer_label.config(text=0)
    wrong_word_count_label.config(text=0)
    accuracy_percent_label.config(text=0)
    total_word_count_label.config(text=0)
    wrong_word_count_label.config(text=0)

    random.shuffle(paragraph_list)
    label_paragraph.config(text=paragraph_list[0])

########### GUI PART ###########


window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('breeze')
window.geometry('997x730+200+25')
window.config(background="grey")
window.resizable(0, 0)
window.overrideredirect(True)

mainframe = Frame(window, bg="grey")
mainframe.grid(row=0, column=0)

titleframe = Frame(mainframe, bd=5, bg="dark blue")
titleframe.grid(row=0, column=0)

titlelabel = Label(titleframe, text="Self Checker", font=(
    'algerian', 25, "bold"), bg="skyblue", fg="Red", width=46, bd=10)
titlelabel.grid(row=0, column=0)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0, pady=5)


paragraph_list = [' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                  ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                  'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                  'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                  'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
                  'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
                  'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                  'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
                  ]

random.shuffle(paragraph_list)

label_paragraph = Label(
    paragraph_frame, text=paragraph_list[0], wraplength=912, justify=LEFT, font=('arial', 14, 'bold'), bg="pink")
label_paragraph.grid(row=0, column=0)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2, column=0, pady=5)

textarea = Text(textarea_frame, font=('arial', 15, 'bold'), width=75,
                height=5, bd=7, relief=GROOVE, wrap="word", state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe, bg="grey")
frame_output.grid(row=3, column=0, pady=5)

elapsed_time_label = Label(
    frame_output, text="Elapsed Time:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
elapsed_time_label.grid(row=0, column=0, padx=5)

elapsed_timer_label = Label(
    frame_output, text="0", font=("Tahona", 12, "bold"), bg="grey")
elapsed_timer_label.grid(row=0, column=1, padx=5)

remaining_time_label = Label(
    frame_output, text="Remaining Time:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
remaining_time_label.grid(row=0, column=2, padx=5)

remaining_timer_label = Label(
    frame_output, text="60", font=("Tahona", 12, "bold"), bg="grey")
remaining_timer_label.grid(row=0, column=3, padx=5)

wpm_label = Label(
    frame_output, text="WPM:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
wpm_label.grid(row=0, column=4, padx=5)

wpm_count_label = Label(
    frame_output, text="0", font=("Tahona", 12, "bold"), bg="grey")
wpm_count_label.grid(row=0, column=5, padx=5)

total_word_label = Label(
    frame_output, text="Total Words:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
total_word_label.grid(row=0, column=6, padx=5)

total_word_count_label = Label(
    frame_output, text="0", font=("Tahona", 12, "bold"), bg="grey")
total_word_count_label.grid(row=0, column=7, padx=5)

wrong_word_label = Label(
    frame_output, text="Wrong Words:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
wrong_word_label.grid(row=0, column=8, padx=5)

wrong_word_count_label = Label(
    frame_output, text="0", font=("Tahona", 12, "bold"), bg="grey")
wrong_word_count_label.grid(row=0, column=9, padx=5)

accuracy_label = Label(
    frame_output, text="Accuracy:", font=("Tahona", 12, "bold"), bg="grey", fg="red")
accuracy_label.grid(row=0, column=10, padx=5)

accuracy_percent_label = Label(
    frame_output, text="0", font=("Tahona", 12, "bold"), bg="grey")
accuracy_percent_label.grid(row=0, column=11, padx=5)

button_frame = Frame(mainframe, bg="grey")
button_frame.grid(row=4, column=0)

startButton = ttk.Button(button_frame, text="Start", command=start)
startButton.grid(row=0, column=0, padx=10)

resetButton = ttk.Button(button_frame, text="Reset",
                         state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=10)

exitButton = ttk.Button(button_frame, text="Exit", command=window.destroy)
exitButton.grid(row=0, column=2, padx=10)

keyboard_frame = Frame(mainframe, bg="grey", bd=2, relief=GROOVE)
keyboard_frame.grid(row=5, column=0, pady=3)

frame_1to0 = Frame(keyboard_frame, bg="grey")
frame_1to0.grid(row=0, column=0, pady=3)

labelbacktick = Label(frame_1to0, text="~\n`", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelbacktick.grid(row=0, column=0, padx=3)
label1 = Label(frame_1to0, text="!\n1", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label1.grid(row=0, column=1, padx=3)
label2 = Label(frame_1to0, text="@\n2", bg="white", fg="black",
               font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label2.grid(row=0, column=2, padx=3)
label3 = Label(frame_1to0, text="#\n3", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label3.grid(row=0, column=3, padx=3)
label4 = Label(frame_1to0, text="$\n4", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label4.grid(row=0, column=4, padx=3)
label5 = Label(frame_1to0, text="%\n5", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label5.grid(row=0, column=5, padx=3)
label6 = Label(frame_1to0, text="^\n6", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label6.grid(row=0, column=6, padx=3)
label7 = Label(frame_1to0, text="&\n7", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label7.grid(row=0, column=7, padx=3)
label8 = Label(frame_1to0, text="*\n8", bg="white", fg="black",
               font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label8.grid(row=0, column=8, padx=3)
label9 = Label(frame_1to0, text="(\n9", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label9.grid(row=0, column=9, padx=3)
label0 = Label(frame_1to0, text=")\n0", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label0.grid(row=0, column=10, padx=3)
label_ = Label(frame_1to0, text="_\n-", bg="white", fg="black",
               font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
label_.grid(row=0, column=11, padx=3)
labelplus = Label(frame_1to0, text="+\n=", bg="white", fg="black",
                  font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelplus.grid(row=0, column=12, padx=3)

labelbackspace = Label(frame_1to0, text="Backspace", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelbackspace.grid(row=0, column=13, padx=3)

frame_qtop = Frame(keyboard_frame, bg="grey")
frame_qtop.grid(row=1, column=0, pady=3)

labeltab = Label(frame_qtop, text="Tab", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=8, height=2, bd=10, relief=GROOVE)
labeltab.grid(row=0, column=0, padx=3)
labelq = Label(frame_qtop, text="Q", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelq.grid(row=0, column=1, padx=3)
labelw = Label(frame_qtop, text="W", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelw.grid(row=0, column=2, padx=3)
labele = Label(frame_qtop, text="E", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labele.grid(row=0, column=3, padx=3)
labelr = Label(frame_qtop, text="R", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelr.grid(row=0, column=4, padx=3)
labelt = Label(frame_qtop, text="T", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelt.grid(row=0, column=5, padx=3)
labely = Label(frame_qtop, text="Y", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labely.grid(row=0, column=6, padx=3)
labelu = Label(frame_qtop, text="U", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelu.grid(row=0, column=7, padx=3)
labeli = Label(frame_qtop, text="I", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labeli.grid(row=0, column=8, padx=3)
labelo = Label(frame_qtop, text="O", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelo.grid(row=0, column=9, padx=3)
labelp = Label(frame_qtop, text="P", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelp.grid(row=0, column=10, padx=3)
labelbracket_l = Label(frame_qtop, text="{\n[", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelbracket_l.grid(row=0, column=11, padx=3)
labelbracket_r = Label(frame_qtop, text="}\n]", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelbracket_r.grid(row=0, column=12, padx=3)
labelbackslash = Label(frame_qtop, text="|\n\\", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=7, height=2, bd=10, relief=GROOVE)
labelbackslash.grid(row=0, column=13, padx=3)

frame_atol = Frame(keyboard_frame, bg="grey")
frame_atol.grid(row=2, column=0, pady=3)

labelcapslock = Label(frame_atol, text="Caps Lock", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelcapslock.grid(row=0, column=0, padx=3)
labela = Label(frame_atol, text="A", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labela.grid(row=0, column=1, padx=3)
labels = Label(frame_atol, text="S", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labels.grid(row=0, column=2, padx=3)
labeld = Label(frame_atol, text="D", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labeld.grid(row=0, column=3, padx=3)
labelf = Label(frame_atol, text="F", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelf.grid(row=0, column=4, padx=3)
labelg = Label(frame_atol, text="G", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelg.grid(row=0, column=5, padx=3)
labelh = Label(frame_atol, text="H", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelh.grid(row=0, column=6, padx=3)
labelj = Label(frame_atol, text="J", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelj.grid(row=0, column=7, padx=3)
labelk = Label(frame_atol, text="K", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelk.grid(row=0, column=8, padx=3)
labell = Label(frame_atol, text="L", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labell.grid(row=0, column=9, padx=3)
labelsemicolon = Label(frame_atol, text=":\n;", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelsemicolon.grid(row=0, column=10, padx=3)
labelapostrophe = Label(frame_atol, text='"\n'+"'", bg="white", fg="black",
                        font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelapostrophe.grid(row=0, column=11, padx=3)
labelenter = Label(frame_atol, text="Enter", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=13, height=2, bd=10, relief=GROOVE)
labelenter.grid(row=0, column=12, padx=3)

frame_ztom = Frame(keyboard_frame, bg="grey")
frame_ztom.grid(row=3, column=0, pady=3)

labelshift1 = Label(frame_ztom, text="Shift", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=16, height=2, bd=10, relief=GROOVE)
labelshift1.grid(row=0, column=0, padx=3)
labelz = Label(frame_ztom, text="Z", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelz.grid(row=0, column=1, padx=3)
labelx = Label(frame_ztom, text="X", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelx.grid(row=0, column=2, padx=3)
labelc = Label(frame_ztom, text="C", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelc.grid(row=0, column=3, padx=3)
labelv = Label(frame_ztom, text="V", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelv.grid(row=0, column=4, padx=3)
labelb = Label(frame_ztom, text="B", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelb.grid(row=0, column=5, padx=3)
labeln = Label(frame_ztom, text="N", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labeln.grid(row=0, column=6, padx=3)
labelm = Label(frame_ztom, text="M", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelm.grid(row=0, column=7, padx=3)
labelanglebrackets_l = Label(frame_ztom, text="<\n,", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelanglebrackets_l.grid(row=0, column=9, padx=3)
labelanglebrackets_r = Label(frame_ztom, text=">\n.", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelanglebrackets_r.grid(row=0, column=10, padx=3)
labelfrontslash = Label(frame_ztom, text="?\n/", bg="white", fg="black",
                        font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)
labelfrontslash.grid(row=0, column=11, padx=3)
labelshift2 = Label(frame_ztom, text="Shift", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=16, height=2, bd=10, relief=GROOVE)
labelshift2.grid(row=0, column=12, padx=3)

spaceframe = Frame(keyboard_frame, bg="grey")
spaceframe.grid(row=4, column=0, pady=3)

labelctrl_l = Label(spaceframe, text="Ctrl", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelctrl_l.grid(row=0, column=0, padx=6)
labelalt_l = Label(spaceframe, text="Alt", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelalt_l.grid(row=0, column=1, padx=6)
labelspace = Label(spaceframe, text="Space", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=50, height=2, bd=10, relief=GROOVE)
labelspace.grid(row=0, column=2, padx=6)
labelalt_r = Label(spaceframe, text="Alt", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelalt_r.grid(row=0, column=3, padx=6)
labelctrl_r = Label(spaceframe, text="Ctrl", bg="white", fg="black", font=(
    'arial', 10, 'bold'), width=10, height=2, bd=10, relief=GROOVE)
labelctrl_r.grid(row=0, column=4, padx=6)

tab_label = [labeltab]

enter_label = [labelenter]

label_numbers = [label1, label2, label3, label4,
                 label5, label6, label7, label8, label9, label0]

label_alphabets = [labela, labelb, labelc, labeld, labele, labelf, labelg, labelh, labeli, labelj, labelk, labell, labelm, labeln,
                   labelo, labelp, labelq, labelr, labels, labelt, labelu, labelv, labelw, labelx, labely, labelz]

label_symbols = [labelbacktick, label_, labelplus, labelbracket_l, labelbracket_r, labelbackslash,
                 labelsemicolon, labelapostrophe, labelanglebrackets_l, labelanglebrackets_r, labelfrontslash]

backspace_label = [labelbackspace]

space_label = [labelspace]

ctrl_label = [labelctrl_l, labelctrl_r]

alt_label = [labelalt_l]

shift_label = [labelshift1, labelshift2]


def chageBG(widget):
    widget.config(bg="blue")
    widget.after(100, lambda: widget.config(bg="white"))


def caps_lock_on(e):
    labelcapslock.config(bg="pink")


def caps_lock_off(e):
    labelcapslock.config(bg="white")


def alt_r_click(e):
    labelalt_r.config(bg="pink")
    labelctrl_l.config(bg="white")
    labelalt_r.after(100, lambda: labelalt_r.config(bg="white"))


binding_symbols_1to0 = ['<!>', '<@>', '<#>', '<$>',
                        '<%>', '<^>', '<&>', '<*>', '<(>', '<)>']
binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

binding_upper_symbols = ['<~>', '<_>', '<+>', '<{>',
                         '<}>', '<|>', '<:>', '<">', '<less>', '>', '<?>']
binding_lowwer_symbols = ['<`>', '-', '<=>', '<[>',
                          '<]>', '<\>', '<;>', "<'>", '<,>', '<.>', '</>']


binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z']

binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']

for number in range(len(binding_numbers)):
    window.bind(binding_numbers[number], lambda event,
                label=label_numbers[number]: chageBG(label))
for symbol in range(len(binding_symbols_1to0)):
    window.bind(binding_symbols_1to0[symbol], lambda event,
                label=label_numbers[symbol]: chageBG(label))

for symbols in range(len(binding_upper_symbols)):
    window.bind(binding_upper_symbols[symbols], lambda event,
                label=label_symbols[symbols]: chageBG(label))

for symbols in range(len(binding_lowwer_symbols)):
    window.bind(binding_lowwer_symbols[symbols], lambda event,
                label=label_symbols[symbols]: chageBG(label))

for capital_alphabet in range(len(binding_capital_alphabets)):
    window.bind(binding_capital_alphabets[capital_alphabet], lambda event,
                label=label_alphabets[capital_alphabet]: chageBG(label))
for small_alphabet in range(len(binding_small_alphabets)):
    window.bind(binding_small_alphabets[small_alphabet], lambda event,
                label=label_alphabets[small_alphabet]: chageBG(label))

window.bind("<space>", lambda event: chageBG(space_label[0]))
window.bind("<Shift_L>", lambda event: chageBG(shift_label[0]))
window.bind("<Shift_R>", lambda event: chageBG(shift_label[1]))
window.bind("<Return>", lambda event: chageBG(enter_label[0]))
window.bind("<Tab>", lambda event: chageBG(tab_label[0]))
window.bind("<BackSpace>", lambda event: chageBG(backspace_label[0]))
window.bind("<Alt_L>", lambda event: chageBG(alt_label[0]))
window.bind("<Alt_R>", alt_r_click)
window.bind("<Control_L>", lambda event: chageBG(ctrl_label[0]))
window.bind("<Control_R>", lambda event: chageBG(ctrl_label[1]))


window.bind("<Lock-KeyRelease>", caps_lock_on)
window.bind("<Lock-KeyPress>", caps_lock_off)

window.mainloop()