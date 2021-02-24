from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk
import math


#window object
app = Tk()
app.title('Network Simulator')
app.geometry('1080x800')


#font
app.customFont = tkFont.Font(family="Times", size=12)

#heading
headinig_left= Label(app, text = 'Calculate Cell Property', font = app.customFont, pady = 20 , padx = 10)
headinig_right= Label(app, text = 'Calculate Path Loss', font = app.customFont, pady = 20 , padx = 10)
headinig_left.grid(row =0 ,columnspan=2)
headinig_right.grid(row = 0,column=4,columnspan=4)

#area size
area_size_text= StringVar()
area_label = Label(app, text = 'AreaSize', font = app.customFont, pady = 20 , padx = 10)
area_label.grid(row =1 ,column = 0)
area_entry = Entry(app,textvariable = area_size_text)
area_entry.grid(row = 1, column = 1)

#cell radius
cell_radius_text = StringVar()
cell_radius_label = Label(app, text = 'CellRadius', font = app.customFont, pady = 20 , padx = 10)
cell_radius_label.grid(row =2 ,column = 0)
cell_radius_entry = Entry(app,textvariable = cell_radius_text)
cell_radius_entry.grid(row = 2, column = 1)


#Frequency Reuse Factor
frf_text= StringVar()
frf_label = Label(app, text = 'ReuseFactor', font = app.customFont, pady = 20, padx =10)
frf_label.grid(row = 3, column = 0)
frf_entry = Entry(app,textvariable = frf_text)
frf_entry.grid(row = 3, column = 1)

#Frequency Reuse Factor
traffic_text= StringVar()
traffic_label = Label(app, text = 'TotalFrequency', font = app.customFont, pady = 20, padx =10)
traffic_label.grid(row = 4, column = 0)
traffic_entry = Entry(app,textvariable = traffic_text)
traffic_entry.grid(row = 4, column = 1)

#total traffic channel


#cell type
cell_type_text = StringVar()
cell_type_label = Label(app, text = 'CellType', font = app.customFont, pady = 20 ,padx = 10)
cell_type_label.grid(row = 5, column = 0)
cell_type_btn1 = Radiobutton(app,variable = cell_type_text, text = "Microcell", value = 1, anchor = W)
cell_type_btn1.grid(row = 5, column = 1)
cell_type_btn1.select()
cell_type_btn2 = Radiobutton(app,variable = cell_type_text, text = "Macrocell", value = 2, anchor =W)
cell_type_btn2.grid(row = 5, column = 2)

#text box for showing result
#textbox = Text(app,width =30,height =10)
outputbox_left = Text(app,font=app.customFont,width =30,height =10)
outputbox_left.grid(row =8 ,column =0 ,columnspan=2,padx=10,ipadx=10,ipady=2)
outputbox_left.insert(END,"Output:")
#method for interaction

valid_reusefactor =[1,3,4,7,9,12,13,16,19]

def checkRadius(cell_type,radius):
    if(cell_type == 1 and radius <= 1.0 and radius >= 0.1):
        return True
    elif (cell_type == 1 and radius > 1.0 or radius < 0.1):
        return "invalid Microcell Radius"
    elif(cell_type == 2 and radius >= 1.0 and radius <= 20.0):
        return True

    elif (cell_type == 2 and radius < 1.0 or radius > 20.0):
        return "invalid Macrocell Radius"

def checkReuseFactor(reusefactor):
    if reusefactor not in valid_reusefactor:
        return False
    else :
        return True

def CalculateCellProperty() :
    #textbox = Text(app,,padx =20 ,pady=10)
    
    area = float(area_size_text.get())
    radius = float(cell_radius_text.get())
    reusefactor = int(frf_text.get())
    traffic = float(traffic_text.get())
    cell_type = int(cell_type_text.get())

    rf_validity = checkReuseFactor(reusefactor)
    radius_validity = checkRadius(cell_type,radius)

    if(rf_validity == True and radius_validity ==True ) :
   
        total_cell = area // (radius*radius*2.598)   # sqrt(3)*1.5 =2.598
        channel_per_cell = traffic // reusefactor
        cell_capacity = total_cell * channel_per_cell
        concurrent_cell =cell_capacity
        outputbox_left.delete(1.0,END)
        outputbox_left.insert(END,"TotalCell : {} ".format(total_cell) + "\n\n")
        outputbox_left.insert(END,"ChannelPerCell : {} ".format(channel_per_cell) + "\n\n")
        outputbox_left.insert(END,"CellCapacity : {} ".format(cell_capacity) + "\n\n")
        outputbox_left.insert(END,"ConcurrentCell : {} ".format(cell_capacity) + "\n\n")
    else :
        outputbox_left.delete(1.0,END)
        if(rf_validity ==False ) :
            outputbox_left.insert(END,"Inavlid Frequency reuse factor\n")
            if(radius_validity != True ) :
                outputbox_left.insert(END,radius_validity)
            else :
                pass
        else :
            outputbox_left.insert(END,radius_validity)



#calculate button
b1 = Button(app, text="CalculateCell", width=12,padx=10,pady = 20, bg = "#53a69c", command=CalculateCellProperty)
b1.grid(row=6, column=0)



#seperator line between two interface
tkinter.ttk.Separator(app, orient=VERTICAL).grid(column=4, row=0, rowspan=12, sticky='ns',padx=30)


#UI Code for second task

#Carrier frequency
fc_text = StringVar()  # return value in string format entered by user
fc_label = Label(app, text = 'CarrierFrequency (MHz)', font = app.customFont, pady = 20 , padx = 10)
fc_label.grid(row =1 ,column = 5, sticky =W)
fc_entry = Entry(app,textvariable = fc_text)
fc_entry.grid(row = 1, column = 6)

#height of transmitting antenna
ht_text = StringVar()
ht_label = Label(app, text = 'TransmissionAntenna (m)', font = app.customFont, pady = 20 , padx = 10)
ht_label.grid(row =2 ,column = 5, sticky = W)
ht_entry = Entry(app,textvariable = ht_text)
ht_entry.grid(row = 2, column = 6)


#height of receiving antenna
hr_text = StringVar()  
hr_label = Label(app, text = "ReceivingAntenna (m)", font = app.customFont, pady = 20, padx =10)
hr_label.grid(row =3 ,column = 5, sticky = W)
hr_entry = Entry(app,textvariable = hr_text)
hr_entry.grid(row = 3, column = 6)

#propagation distance
pd_text = StringVar()
pd_label = Label(app, text = 'PropagationDistance (Km)', font = app.customFont, pady = 20, padx =10)
pd_label.grid(row =4 ,column = 5, sticky = W)
pd_entry = Entry(app,textvariable = pd_text)
pd_entry.grid(row = 4, column = 6)


#City size
city_size_text= StringVar()
city_size_label = Label(app, text = 'CitySize', font = app.customFont, pady = 20 ,padx = 10)
city_size_label.grid(row =5 ,column = 5, sticky = W)
city_size_btn1 = Radiobutton(app,variable = city_size_text, text = "Small/Medium", value = 1)
city_size_btn1.grid(row = 5, column = 6)
city_size_btn1.select()
city_size_btn2 = Radiobutton(app,variable = city_size_text, text = "Large", value = 2)
city_size_btn2.grid(row = 5, column = 7)

#Area type
area_type_text= StringVar()
area_type_label = Label(app, text = 'AreaType', font = app.customFont, pady = 20 ,padx = 10)
area_type_label.grid(row =6 ,column = 5, sticky = W)
area_type_btn1 = Radiobutton(app,variable = area_type_text, text = "Urban", value = 1)
area_type_btn1.grid(row = 6, column = 6)
area_type_btn1.select()
area_type_btn2 = Radiobutton(app,variable = area_type_text, text = "Suburban", value = 2)
area_type_btn2.grid(row = 6, column = 7)
area_type_btn3 = Radiobutton(app,variable = area_type_text, text = "Open Area", value = 3)
area_type_btn3.grid(row = 6, column = 8)



#text box for showing output
outputbox_right = Entry(app,font=app.customFont)
outputbox_right.grid(row =7 ,column =6,columnspan=2,ipadx=80,ipady =20)
outputbox_right.insert(INSERT,"Output:")

#function for button activity

def calcA ( city_size , hr ,fc ) :
    if ( city_size == 1.0 ):
        logfc = math.log(fc, 10)
        a =(1.1 * logfc - 0.7 ) * hr - (1.56 * logfc - 0.8)
        
    elif ( city_size == 2.0  and fc <= 300 ):
        loghr = math.log((1.54*hr),10)
        a = (8.29 * loghr *loghr) - 1.1
       
    else : 
        loghr = math.log((11.75*hr),10)
       
        a = (3.2 * loghr *loghr) - 4.97
        
    return a


def calcPathLoss() :
    #textbox = Text(app,width =40,height =10,padx =20 ,pady=10)
    #getting the value from the string variable
    fc = float(fc_text.get())
    ht = float(ht_text.get())
    hr = float(hr_text.get())
    pd = float(pd_text.get())
    city_size = float(city_size_text.get())
    area_type = float(area_type_text.get())
    
    a = calcA(city_size,hr,fc)

    logfc = math.log ( fc,10)
    loghr= math.log(hr,10)
    loght = math.log( ht ,10)
    logpd = math.log(pd,10)
    loss = 69.55 + 26.16 * logfc - 13.82 * loght - a + (44.9 - 6.55 * loght) * logpd
    if(area_type == 1.0 ) :
        pass
    elif(area_type == 2.0 ) :
        logfc = math.log ((fc/28),10)
        loss = loss - 2 * logfc * logfc -5.4
     
    else :
        loss = loss - 4.78 * logfc *logfc - 18.733 * logfc -40.98
    
    #textbox.delete("1",END)
    #textbox.insert(INSERT,"CellRadius: " + cell_radius_text.get()+"\n Area size" + area + " \n Frequency Reuse Factor" + reusefactor + "\n Cell Type :" + cell_type)
    #textbox.grid(row =7,column = 0,columnspan = 2)
    outputbox_right.delete(0,END)
    outputbox_right.insert(INSERT," PathLoss : " + str(loss) + " dB")

#calculate button
b1 = Button(app, text="CalculatePathLoss", width=6,padx=40,pady = 20,bg = "#53a69c",command=calcPathLoss)
b1.grid(row=7, column=5)

#start program
app.mainloop()

