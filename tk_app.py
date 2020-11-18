import linear_model
import tkinter as tk

window = tk.Tk()
window.title('Level check')
window.geometry("500x500")
canvas1 = tk.Canvas(window,width=500,height=250,bg='light blue')
canvas1.grid(row=0,columnspan=2)

lb_company = tk.Label(text='company',font=20)
canvas1.create_window(100,50,window=lb_company)
lb_job = tk.Label(text='job',font=20)
canvas1.create_window(100,100,window=lb_job)
lb_degree = tk.Label(text='degree',font=20)
canvas1.create_window(100,150,window=lb_degree)

company_list = ['google','abc pharma','facebook']
job_list = ['sales executive','business manager','computer programmer']
degree_list = ['bachelors','masters']

variable_c = tk.StringVar()
drmn_compnay = tk.OptionMenu(window,variable_c,company_list[0],*company_list[1:])
canvas1.create_window(300,50,window=drmn_compnay)
variable_j = tk.StringVar()
drmn_job = tk.OptionMenu(window,variable_j,job_list[0],*job_list[1:])
canvas1.create_window(300,100,window=drmn_job)
variable_d = tk.StringVar()
drmn_degree = tk.OptionMenu(window,variable_d,degree_list[0],*degree_list[1:])
canvas1.create_window(300,150,window=drmn_degree)
drmn_compnay.config(font=('calibri',(10)),bg='white',width=20)
drmn_job.config(font=('calibri',(10)),bg='white',width=20)
drmn_degree.config(font=('calibri',(10)),bg='white',width=20)

def click():
    global variable_c
    global variable_j
    global  variable_d

    company_value = variable_c.get()
    job_value = variable_j.get()
    degree_value = variable_d.get()

    y=[]
    y.append([company_value,job_value,degree_value])
    result = linear_model.predict_classification(y)

    results_text = f'The estimated result is: {result}'
    lb_result = tk.Label(text=results_text,font=10,fg='green')
    lb_result.grid(row=4,column=0)
    note = ['salary_more_than_100k' if result==1 else 'salary_less_than_100k']
    lb3_result = tk.Label(text=note,font=7,fg='gray')
    lb3_result.grid(row=5,columnspan=2)


btn_estimate = tk.Button(text='estimate',command=click,font=20,fg='red')
btn_estimate.grid(row=3,columnspan=2)

window.mainloop()