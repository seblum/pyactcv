# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:22:41 2019

@author: Sebastian Blum
"""
import actr
import pandas as pd


class ActCV():

    def __init__(self):
        self.header =  list # []
        self.statelist = list()
        self.state_start = pd.Series
        self.time_offset = 0
        self.index  = 0
        actr.add_command("current-to-visicon", current_to_visicon, "connection to put the current line in the visicon")
        actr.add_command("initialize-visicon", initialize_visicon, "connection to run initialize the visicon")

    def initialize_visicon(self):
        for headiter in self.header:
             head_name = headiter
             value = (self.state_start[headiter])
             actr.add_visicon_features(['isa', 'visual-location', 
                                        'value', value,
                                        'color', head_name,
                                        'screen-x', 0, 
                                        'screen-y', 0, 
                                        'width', 50, 
                                        'height', 15])        

    def current_to_visicon(self,index):
        state_current = self.statelist[index]
        actr.delete_all_visicon_features()        
        for headiter in self.header:
            head_name = headiter
            value = state_current[headiter]
            actr.add_visicon_features(['isa', 'visual-location', 
                                       'value', value,
                                       'color', head_name,
                                       'screen-x', 0, 
                                       'screen-y', 0, 
                                       'width', 50, 
                                       'height', 15])

    # readin with header
    def schedule_Visicon(self, data, head, alarmactivecolumn, alarmnumbercolumn, timecolumnname, freq, duration, starttime = 0, indexinput = 0, timebreak = 0.01):            
        print("-"*30 + " Start scheduling ")         
        
        self.index = indexinput
        tmp = data
        self.header = head
        
        # set start time    
        time_start = tmp[timecolumnname][0]
        time_last_current = time_start

        # set states
        self.state_start = tmp.iloc[0] # the iloc seems critical
        state_previous = self.state_start

            
        actr.schedule_event(starttime, "initialize-visicon", maintenance = True )     

        for state_iter in tmp.index:
            time_current = tmp[timecolumnname][state_iter]
            self.time_offset = time_current - time_start
            self.time_offset = self.time_offset + starttime
            time_difference = time_current - time_last_current

            if time_difference > timebreak:          
                time_last_current = time_current
                state_current = tmp.iloc[state_iter]
                previous_value = state_previous[alarmnumbercolumn]
                current_value = state_current[alarmnumbercolumn]
                alarm_active = state_current[alarmactivecolumn]
                
                self.statelist.append(state_current)
                #savestate(state_current)

                actr.schedule_event(self.time_offset, "current-to-visicon", params = [self.index], maintenance = True )     
                self.index += 1

                ### ----- ----- ----- PROCEDURE ALERT ----- ----- -----
                if previous_value != current_value and previous_value == 0.0 and alarm_active == 1.0:
                    actr.new_tone_sound(freq, duration, self.time_offset) # input these variables
                    print("-"*30 + f" Tone scheduled at {self.time_offset}")     
                    
                state_previous = state_current               

        print("-"*30 + " Scheduling successful ")         

'''
I probably do not need this anymore
def init_actcv():    
    global index
    global time_offset
    
    index = 0
    time_offset = 0
    statelist.clear()
    actr.add_command("current-to-visicon", current_to_visicon, "connection to put the current line in the visicon")
    actr.add_command("initialize-visicon", initialize_visicon, "connection to run initialize the visicon")
'''
    
    def getstatelist(self):
        return self.statelist

    def getindex(self):
        return self.index

    def gettimeoffset(self):
        return self.time_offset


    

