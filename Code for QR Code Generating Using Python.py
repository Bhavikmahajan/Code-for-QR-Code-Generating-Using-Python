# GUI tool-kit
from tkinter import*

# Python QR Genrator 
import qrcode

#image Loader Pillow
from PIL import ImageTk

# Resize Image 
from resizeimage import resizeimage

# Define Class 
class Qr_Genrator:
    def __init__(self,root):
        self.root=root

        # Framwork 
        self.root.geometry("900x500+200+50")

        #Frame Name 
        self.root.title("QR GENRATOR | DEVLOPED BY BHAVIK MAHAJAN")

        #Frame Resize 
        self.root.resizable(False, False) 

        # Main Title 
        title=Label(self.root,text="                   QR Code Generator",font=("times new roman",40),bg='#212A31',fg='#D3D9D4',anchor='w').place(x=0,y=0,relwidth=1)

        # Product Details Window:-

        pro_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='#EAE7DC')
        pro_Frame.place(x=50,y=100,width=500,height=380)

        # Variables for Taking User Input:-

        self.var_pro_id = StringVar()
        self.var_pro_name = StringVar()
        self.var_pro_price = StringVar()
        self.var_pro_category = StringVar()

        # Main Title of Product Window:-
        pro_title = Label(pro_Frame, text="Product Details", font=("goudy old style", 30, 'bold'), bg='#212A31',fg='Orange').place(x=0, y=0, relwidth=1)
        
        # List Labels of Product Window:-

        lbl_pro_id = Label(pro_Frame, text="Product ID", font=("times new roman", 15,'bold'), bg='#EAE7DC').place(x=20, y=60)
        lbl_pro_name = Label(pro_Frame, text="Name", font=("times new roman", 15, 'bold'), bg='#EAE7DC').place(x=20,y=100)
        lbl_pro_price = Label(pro_Frame, text="Price", font=("times new roman", 15, 'bold'), bg='#EAE7DC').place(x=20,y=140)
        lbl_pro_category = Label(pro_Frame, text="Category", font=("times new roman", 15, 'bold'), bg='#EAE7DC').place(x=20,y=180)

        # Input Textfields(Entry) of Product Window:-

        txt_pro_id = Entry(pro_Frame, font=("times new roman", 15),textvariable=self.var_pro_id,bg='White').place(x=200,y=60)
        txt_pro_name = Entry(pro_Frame, font=("times new roman", 15),textvariable=self.var_pro_name,bg='white').place(x=200,y=100)
        txt_pro_price = Entry(pro_Frame, font=("times new roman", 15),textvariable=self.var_pro_price,bg='white').place(x=200, y=140)
        txt_pro_category = Entry(pro_Frame, font=("times new roman", 15),textvariable=self.var_pro_category,bg='white').place(x=200, y=180)
       
        # Buttons Generate & Clear Button:-

        btn_generate_qr = Button(pro_Frame, text="Generate QR",command=self.generate,font=("times new roman",18,'bold'),bg='#006FFF',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear = Button(pro_Frame, text="Clear",command=self.clear,font=("times new roman", 18, 'bold'), bg='#e42b2b', fg='white').place(x=300, y=250, width=104, height=30)

        # Printing Message after Pressing Generate Button:-

        self.message = " "
        self.lbl_message = Label(pro_Frame, text=self.message, font=("times new roman", 20, 'bold'), bg='#EAE7DC',fg='#21EF6D')
        self.lbl_message.place(x=0,y=310,relwidth=1) 

        # QR Code Window:-

        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        # Title of QR Code Window:-
        qr_title = Label(qr_Frame, text="Product QR Code", font=("goudy old style", 20, 'bold'), bg='#043256',fg='white').place(x=0, y=0, relwidth=1)

        # QR Not Available Window:-

        self.qr_code = Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

        # Clear Button Logic(Function):-

    def clear(self):
        self.var_pro_id.set('')
        self.var_pro_name.set('')
        self.var_pro_price.set('')
        self.var_pro_category.set('')
        self.message = ''
        self.lbl_message.config(text=self.message)
        self.qr_code.config(image='')
        

        # Generate QR Button Logic(Function):-
    def generate(self):
        
        # Use If - Else Statement 

        if self.var_pro_id.get()=='' or self.var_pro_name.get()=='' or self.var_pro_price.get()=='' or self.var_pro_category.get()=='':
           self.message = "All Fields are Required!!!"
           self.lbl_message.config(text=self.message,fg='Dark Red')
        else:
           # Using QR Code Module:-

            qr_data = (f"Product ID:- {self.var_pro_id.get()}\nName:- {self.var_pro_name.get()}\nPrice:- {self.var_pro_price.get()}\nCategory:- {self.var_pro_category.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)

            # Saving the QR Code in Folder:-

            qr_code.save("Product_QR/Prod_"+str(self.var_pro_id.get())+'.png')

            # Resizing the Image in to Small Image:-

            qr_code = resizeimage.resize_cover(qr_code,[180,180])


            # QR Code Image Update:-

            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

           # Updating Notification:-

            self.message = "QR Generated Successfully!!!"
            self.lbl_message.config(text=self.message, fg='green')  

root=Tk()
obj =Qr_Genrator(root)
root.mainloop()

# Remember To install librareies in device using Cmd in Vs Code 
# pip install pillow
# pip install qrcode 
# pip install python-resize-image 
