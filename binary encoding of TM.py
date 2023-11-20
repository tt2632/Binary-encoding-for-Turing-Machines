import tkinter as tk
def encoding(s1,t1,s2,t2,d):
    if s1==0:
        r1="0"
    elif s1==1:
        r1="00"
    elif s1==2:
        r1="000"
    elif s1==3:
        r1="0000"

    if t1==0:
        r2="0"
    elif t1==1:
        r2="00"
    elif t1==2:
        r2="000"
    

    if s2==0:
        r3="0"
    elif s2==1:
        r3="00"
    elif s2==2:
        r3="000"
    elif s2==3:
        r3="0000"

    if t2==0:
        r4="0"
    elif t2==1:
        r4="00"
    elif t2==2:
        r4="000"


    if d==0:
        r5="0"
    elif d==1:
        r5="00"
    strings = [r1,r2,r3,r4,r5]
    return "1".join(strings)

# Function that uses the input parameters
def process_input():
    try:
        param1 = int(input1.get())
        param2 = int(input2.get())
        param3 = int(input3.get())
        param4 = int(input4.get())
        param5 = int(input5.get())
        
        # Perform some operation using the parameters
        result = encoding(param1,param2,param3,param4,param5)
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, f"Result: {result}\n")  # Display the result
    except ValueError:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, "Invalid input. Please enter integers.\n")

# Create the main application window
app = tk.Tk()
app.title("Integer Parameterized Function GUI")

# Create and place 5 input entry fields
input1_label = tk.Label(app, text="Current State:")
input1_label.pack()
input1 = tk.Entry(app)
input1.pack()

input2_label = tk.Label(app, text="Input tape symbol:")
input2_label.pack()
input2 = tk.Entry(app)
input2.pack()

input3_label = tk.Label(app, text="Next State:")
input3_label.pack()
input3 = tk.Entry(app)
input3.pack()

input4_label = tk.Label(app, text="Modified tape symbol:")
input4_label.pack()
input4 = tk.Entry(app)
input4.pack()

input5_label = tk.Label(app, text="Direction (L-0,R-1):")
input5_label.pack()
input5 = tk.Entry(app)
input5.pack()

input6_label = tk.Label(app, text="concatinate the binary codes of all transition functions of a turing machine with 11")
input6_label.pack()

# Create and place a submit button
submit_button = tk.Button(app, text="Submit", command=process_input)
submit_button.pack()

# Create a text box for displaying the result
result_text = tk.Text(app)
result_text.pack()

# Start the GUI application
app.mainloop()
