
import json
import pathlib
from tkinter import *


CONFIG_FILE = pathlib.Path(__file__).parent.joinpath('config.json')
DARK_COLOR = '#1d3557'
NORMAL_COLOR = '#457b9d'
LIGHT_COLOR = '#f1faee'
ATTENTION_COLOR = '#e63946'


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
        self.hall_wrapper = Frame(self)
        self.hall_frame = Frame(self.hall_wrapper)
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
        self.controls_frame.pack(side=LEFT, fill=Y)
        self.hall_frame.pack()
        self.hall_wrapper.pack(anchor=CENTER, expand=TRUE, fill=BOTH)
        
        #  main menu
        ## create menubar
        self.option_add('*tearOff', False)
        root_menubar = Menu(self)

        ## attach menubar to window
        self.config(menu=root_menubar)

        ## add menu items to file menu
        root_menubar.add_command(label='Admin login', command=lambda: print('Log in as Admin'))
        root_menubar.add_command(label='Save al data', command=self.save_hall)
        root_menubar.add_command(label='Exit', command=lambda: self.destroy())
        

        # read config
        with open(CONFIG_FILE) as f:
            self.all_cinema_halls = json.load(f)
            pass
        
        # print (self.all_cinema_halls)
        # print (self.all_cinema_halls[0].get("state")[0])
        # print (self.all_cinema_halls[0].get("state")[0][0])
        
        # create halls selector -> Buttons
        # hall_numberames = [hall.get("name") for hall in all_cinema_halls]
        """
        {
        "name":"First hall",
        "rows":7,
        "places":9
        },

        """
        for next_hall_index in range(len(self.all_cinema_halls)):
           
            
            btn = Button(
                self.controls_frame,
                text=self.all_cinema_halls[next_hall_index].get("name"), 
                width=15,
                command=lambda hall_number = next_hall_index: self.draw_hall(hall_number))
            btn.pack(**self.control_frame_widgets_options)
        
        self.mainloop()
        
        pass
    
    def draw_hall(self, hall_number):
        
        self.remove_hall()
        
        self.hall_title_label.config(text=self.all_cinema_halls[hall_number].get('name'))

        for i in range(len(self.all_cinema_halls[hall_number].get("state"))):
            row = []
            for j in range(len(self.all_cinema_halls[hall_number].get("state")[i])):
                
                btn = Checkbutton(
                    self.hall_frame,
                    indicatoron=0,
                    activebackground=DARK_COLOR,
                    activeforeground=LIGHT_COLOR,
                    selectcolor=ATTENTION_COLOR,
                    background=NORMAL_COLOR,
                    foreground=LIGHT_COLOR,
                    text=f'{i}:{j}', 
                    width=5,
                    border=1,
                    justify=CENTER,
                    command = lambda row = i, col = j: self.check_button_click(row, col))
                
                if self.all_cinema_halls[hall_number].get("state")[i][j] == 1:btn.select()
                else: btn.deselect()
                
                btn.grid(column=j, row=i, padx=0, pady=0)
                # to do - > attach variable ...
                row.append(btn)        
                pass
            self.hall_boxes.append(row)
            # root_w.after(2000, resize)
        
        
        pass
    
    def remove_hall(self):
        # save hall data to file
        self.save_hall()
        for next_row in self.hall_boxes: 
            for next_box in next_row: 
                next_box.destroy()
        self.hall_boxes = []
        
        
        pass
    
    def save_hall(self):
        # if len(self.hall_boxes) == 0 : return
        # # old data:
        # # print (self.all_cinema_halls)
        # # get list item to change:
        # for next_hall_index in range(len(self.all_cinema_halls)):
        #     print (next_hall_index)
        #     next_hall = self.all_cinema_halls[next_hall_index]
        #     next_hall_name = next_hall.get('name')
        #     curent_hall_name = self.hall_title_label.cget('text')
        #     if next_hall_name == curent_hall_name :
        #         current_hall = next_hall
        #         current_hall_index = next_hall_index
        #         pass
        #     pass
        # current_hall_state = []
        # for row_index in range(len(self.hall_boxes)):
        #     row = []
        #     for place_index in range(len(self.hall_boxes[row_index])):
        #         print(self.hall_boxes[row_index][place_index].cget('state'))
        #         row.append(int())
                
        #         pass
        #     pass
        # current_hall['state'] = current_hall_state
        
        # self.all_cinema_halls[current_hall_index] = current_hall
        
        # print(self.all_cinema_halls)
        
        
        
        # # with open(file_name) as f:
        # #     json.dump(dict_to_save, f)
        # #     pass
        
        # self.hall_boxes
        
        
        
        pass
    
    def check_button_click(self, row, col):
        print (f'Button clicked: {self.hall_boxes[row][col]}\trow: {row}\tcolumn: {col}')
        
        
        
        pass
    
    
    
    pass

