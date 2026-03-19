import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import tkinter as tk
from tkinter import messagebox

class SunriseSunset():
    def __init__(self):
        
        self.screen = tk.Tk()
        self.screen.title('Weather & Sun Times')
        self.screen.minsize(width = 500, height = 500)
        self.screen.config(bg = '#2b2b2b', padx = 20)
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_columnconfigure(1, weight=1)
        
    def window(self):
        window_title = tk.Label(
            self.screen,
            text = 'Weather & Sun Tracker',
            fg='#50C878',
            bg = '#2b2b2b',
            font = ('Georgia', '22', 'bold')
            )
        window_title.grid(row=0, column=0, columnspan=2, pady=30)
    
    def entry_label(self):
         city_name = tk.Label(
             self.screen,
             text = 'Enter city name',
             fg='#D7D9D7',
             bg = '#2b2b2b',
             font = ('Georgia', '10', 'bold'))
         city_name.grid(row  = 2, column = 0)
        
        
    def text_entry(self):
        self.city_input = tk.Entry(self.screen, width = 20)
        self.city_input.grid(row  = 2, column = 1)
       
    def button_click(self):
        endpoint = 'http://api.openweathermap.org/geo/1.0/direct'
        params = {
            'q': self.city_input.get(),
            'appid': 'Write_Your_API_Key' # For user
            }
        
        if self.city_input.get() == '':
            messagebox.showerror(title= 'Error', message= 'Enter values.')
            return
        else:                 
            response = requests.get(url = endpoint, params = params)
            data = response.json()
            if data == []:
                messagebox.showerror(title= 'Error', message= 'Enter values.')
                return
            else:
                try:
                    lat_value = data[0]['lat']
                    long_value = data[0]['lon']
                    
                    # Weather API
                    end_point = 'https://api.openweathermap.org/data/2.5/weather'
                    parameters = {
                        'lat' : f'{lat_value}',
                        'lon' : f'{long_value}',
                        'appid' : 'Write_Your_API_Key', # For user
                        'units' : 'metric'
                        }
                    
                    result = requests.get(url = end_point, params = parameters)
                    json_file = result.json()
                    weather_data = json_file['main']
                    
                    # Container
                    self.container = tk.Frame(self.screen, bg='#1f3b4d') 
                    self.container.grid(row=7, column=0, columnspan=2, pady=20, sticky="nsew")

                    # Equal columns inside container
                    self.container.grid_columnconfigure(0, weight=1)
                    self.container.grid_columnconfigure(1, weight=1)
                    
                    weather_label = tk.Label(
                        self.container,
                        text='── Weather ──',
                        fg='#2b2b2b',
                        bg = '#d4f1f4',
                        font = ('Georgia', '12', 'bold'))
                    weather_label.grid(row = 0, column = 0, pady = 10)
                    
                    # Frame
                    self.frame1 = tk.Frame(self.container, bg='#d4f1f4')
                    self.frame1.grid(row=1, column=0, padx=10, pady = 10, ipadx=20)
                    
                    row1 = 0
                    for key, value in weather_data.items():
                        key_text = f'{key.capitalize()}'
                        value_text = f'{value}'
                    
                        key_label = tk.Label(
                            self.frame1,
                            text = f'{key_text}',
                            fg='#1a5c38',
                            bg = '#d4f1f4',
                            font = ('Georgia', '10', 'bold'))
                            
                        key_label.grid(row = row1, column = 0, padx = 15, pady = 10)
                            
                        value_label = tk.Label(
                            self.frame1,
                            text = f'{value_text}',
                            fg='#000000',
                            bg = '#d4f1f4',
                            font = ('Georgia', '10', 'bold'))
                            
                        value_label.grid(row = row1, column = 1, padx = 15, pady = 10)
                        row1 = row1 + 1

                    # Sunrise & Sunset API
                    sun_label = tk.Label(
                        self.container,
                        text='── Sunrise & Sunset ──',
                        fg='#2b2b2b',
                        bg = '#fce1e4',
                        font = ('Georgia', '12', 'bold'))
                    
                    sun_label.grid(row = 0, column = 1, pady = 10)
                    
                    endpoint = 'https://api.sunrisesunset.io/json'
                    params = {
                        'lat': lat_value,
                        'lng': long_value
                        }

                    response = requests.get(url= endpoint, params= params)
                    result = response.json()
                    outcome = result['results']
                    
                    # Frame 2
                    
                    self.frame2 = tk.Frame(self.container, bg='#fce1e4')
                    self.frame2.grid(row=1, column=1, padx=10, pady = 10, ipadx=20)
                
                    row = 0
                    for key, value in outcome.items():
                        text1 = f'{key.capitalize()}'
                        text2 = f'{value}'
                    
                        label1 = tk.Label(
                            self.frame2,
                            text = f'{text1}',
                            fg='#8b0000',
                            bg = '#fce1e4',
                            font = ('Georgia', '10', 'bold'))
                            
                        label1.grid(row = row, column = 0, pady = 10)
                            
                        label2 = tk.Label(
                            self.frame2,
                            text = f'{text2}',
                            fg='#000000',
                            bg = '#fce1e4',
                            font = ('Georgia', '10', 'bold'))
                            
                        label2.grid(row = row, column = 1, pady = 10)
                            
                        row = row + 1
                except ConnectionError:
                    messagebox.showerror(title= 'Error', message= 'Could not connect to the server.\n'
                                         '1. Check your internet connection.\n'
                                         '2. Check if a VPN is blocking the app.\n'
                                         '3. Try after a few minutes.')
                
                except Timeout:
                     messagebox.showwarning(title = 'Timeout', message = 'The server is taking too long to respond')
                 
                except RequestException:
                    messagebox.showerror(title= 'Error', message= 'An unexpected error occurred.')
                
         
    def button_creation(self):
        button = tk.Button(self.screen, text = 'Weather & Sun Tracker', command = self.button_click, font = ('Georgia', '10', 'bold'))
        button.grid(row = 6, column = 0, columnspan=2, pady = 40)
                
    def sunrisesunset(self):
        self.window()
        self.entry_label()
        self.text_entry()
        self.button_creation()
        self.screen.mainloop()
        
            