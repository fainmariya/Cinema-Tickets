
import json
import pathlib
from tkinter import *


CONFIG_FILE = pathlib.Path(__file__).parent.joinpath('config.json')
DARK_COLOR ='#1d3557'
class Cinema(Tk):
    
    def __init__(self) -> None:
        # initialize main window
        super().__init__()
        self.title("Cinema tickets")        
        pass
   
    def start(self):
        self.hall_boxes = [] # two-dimensional list of CheckButtons

        # creating main window template
        self.controls_frame = Frame(self)
        self.hall_frame = Frame(self)
        self.hall_title_label = Label(self.controls_frame, text="Hall title")
        self.user_name_label = Label(self.controls_frame, text="User: guest")
        self.control_frame_widgets_options = {
            'anchor':"w",
            'padx':10,
            'pady':2,
            'ipadx':2,
            'ipady':2
        }
        self.hall_title_label.pack(**self.control_frame_widgets_options)
        self.user_name_label.pack(**self.control_frame_widgets_options)
        self.controls_frame.pack(side=LEFT,  ipadx=50, ipady=50)
        self.hall_frame.pack(ipadx=50, ipady=50)
        
        #  main menu
        ## create menubar
        self.option_add('*tearOff', False)
        root_menubar = Menu(self)

        ## attach menubar to window
        self.config(menu=root_menubar)

        ## add menu items to file menu
        root_menubar.add_command(label='Admin login', command=lambda: print('Log in as Admin'))
        root_menubar.add_command(label='Save al data', command=lambda: print('Savind all ...'))
        root_menubar.add_command(label='Exit', command=lambda: self.destroy())
        

        # read config
        with open(CONFIG_FILE) as f:
            self.halls_from_file = json.load(f)
            pass
        
        print (self.halls_from_file)
        print (self.halls_from_file[0].get("state")[0])
        print (self.halls_from_file[0].get("state")[0][0])
        
        # create halls selector -> Buttons
        # hall_names = [hall.get("name") for hall in halls_from_file]
        """
        {
        "name":"First hall",
        "rows":7,
        "places":9
        },

        """
        for next_hall in self.halls_from_file:
           
            
            btn = Button(
                self.controls_frame,
                text=next_hall.get("name"), 
                width=15,
                command=lambda h = next_hall: self.draw_hall(h))
            btn.pack(**self.control_frame_widgets_options)
            

            
        
        
        
        self.mainloop()
        
        pass
    
            
            
            
    def draw_hall(self, hall):
        
        self.remove_hall( hall)
        
        self.hall_title_label.config(text=hall.get('name'))

        for i in range(len(hall.get("state"))):
            row = []
            for j in range(len(hall.get("state")[i])):
                
                btn = Checkbutton(
                    self.hall_frame,
                    indicatoron=0,
                    # activebackground='red',
                    highlightbackground = "yellow",
                    selectcolor="red",
                    background="green",
                    text=f'{i}:{j}', 
                    width=5,
                    height=5,
                    border=0,
                    foreground='#FFF',
                    justify=CENTER,
                    command = lambda row = i, col = j: self.check_button_click(row, col))
                
                if hall.get('state')[i][j]== 1:btn.select()
                else: btn.deselect()
                btn.grid(column=j, row=i, padx=5, pady=5)
                # to do - > attach variable ...
                row.append(btn)        
                pass
            self.hall_boxes.append(row)
            # root_w.after(2000, resize)
        
        
        pass
    
    def remove_hall(self, hall):
        # save hall data to file
        self.save_hall(hall)
        for next_row in self.hall_boxes: 
            for next_box in next_row: 
                next_box.destroy()
        self.hall_boxes = []
        
        
        pass
    # def save_hall(self, row, col):
        # TO DO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        # hall_number_list = next((i for i, x in enumerate(self.halls_from_file) if x["name"] == hall.get('name')), None)
        # self.halls_from_file[hall_number_list].get("state")[self.check_button_click(row)][self.check_button_click(c)]
        
        # print (f'Button clicked: {self.hall_boxes[row][col]}\trow: {row}\tcolumn: {col}')
        
    def check_button_click(self, row, col):
        print (f'Button clicked: {self.hall_boxes[row][col]}\trow: {row}\tcolumn: {col}')
        
        
        
        
        
        pass
    
    pass

