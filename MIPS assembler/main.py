from tkinter import *
import time

def convert():
    opCodes = {'sw':'101',
            'j':'111',
            'slt':'001',
            'lw':'110',
            'divi':'011',
            'andi':'100',
            'muli':'010',
            'and':'000'}

    registers = {
            "$zero": "0000",
            "$at": "0001",
            "$a1": "0010",
            "$a2": "0011",
            "$a3": "0100",
            "$l1": "0101",
            "$l2": "0110",
            "$l3": "0111",
            "$t1": "1000",
            "$t2": "1001",
            "$t3": "1010",
            "$t4": "1011",
            "$t5": "1100",
            "$t6": "1101",
            "$t7": "1110",
            "$sp": "1111",
        }

    instruction = entry.get().split(' ')
    binary = ""
    if (instruction[0] == "and"):
        binary += opCodes.get('and')
        binary += registers.get(instruction[1])
        binary += registers.get(instruction[2])
        binary += registers.get(instruction[3])
        binary += '0'
    if (instruction[0] == "slt"):
        binary += opCodes.get('slt')
        binary += registers.get(instruction[1])
        binary += registers.get(instruction[2])
        binary += registers.get(instruction[3])
        binary += '0'
    if (instruction[0] == "sw"):
        binary += opCodes.get('sw')
        binary += registers.get(instruction[1])
        offset = instruction[2].split('(')
        offset[1] = offset[1][0:len(offset[1])-1]
        binary += registers.get(offset[1])
        intoffset = int(offset[0]) + int(registers.get(offset[1]),2)
        imm = bin(intoffset)[2:]
        while (len(imm) < 5):
            imm = "0" + imm
        binary += imm
    if (instruction[0] == "lw"):
        binary += opCodes.get('lw')
        binary += registers.get(instruction[1])
        offset = instruction[2].split('(')
        offset[1] = offset[1][0:len(offset[1])-1]
        binary += registers.get(offset[1])
        intoffset = int(offset[0]) + int(registers.get(offset[1]),2)
        imm = bin(intoffset)[2:]
        while (len(imm) < 5):
            imm = "0" + imm
        binary += imm
    if (instruction[0] == "divi"):
        binary += opCodes.get('divi')
        binary += registers.get(instruction[1])
        binary += registers.get(instruction[2])
        imm = int(registers.get(instruction[3]),2)
        while (len(imm) < 5):
            imm = "0" + imm
        binary += imm
    if (instruction[0] == "muli"):
        binary += opCodes.get('muli')
        binary += registers.get(instruction[1])
        binary += registers.get(instruction[2])
        imm = int(registers.get(instruction[3]),2)
        while (len(imm) < 5):
            imm = "0" + imm
        binary += imm
    if (instruction[0] == "andi"):
        binary += opCodes.get('andi')
        binary += registers.get(instruction[1])
        binary += registers.get(instruction[2])
        imm = int(registers.get(instruction[3]),2)
        while (len(imm) < 5):
            imm = "0" + imm
        binary += imm
    if (instruction[0] == "j"):
        binary += opCodes.get('j')
        imm = bin(int(instruction[1]))[2:]
        while (len(imm) < 13):
            imm = "0" + imm
        binary += imm

    result_label.config(text=binary)
        

def reset():
    entry.delete(0,END)
    result_label.config(text="0000000000000000")

window = Tk()
window.geometry("330x100")
window.title("Assembler")

entry = Entry(window,
              font=('Arial',16),
              border=3)
entry.pack(side=LEFT)

label = Label(window,
              text="Enter the instruction: ",
              font=("Arial",24,'bold'))
label.place(x=0,y=0)

result_label = Label(window,
                     text="0000000000000000",
                     font=('Arial',20))
result_label.place(x=0,y=70)

conver_button = Button(window,
                text="Convert!",
                command=convert,
                font=('Comic Sans', 16),
                activeforeground='red',
                fg='red',
                state=ACTIVE,
                )
conver_button.pack(side=RIGHT)

reset_button = Button(window,
                      text="Reset",
                      font=('Comic Sans', 16),
                      activeforeground='red',
                      fg='red',
                      command=reset,
                      state=ACTIVE)
reset_button.pack(side=RIGHT)

window.mainloop()
