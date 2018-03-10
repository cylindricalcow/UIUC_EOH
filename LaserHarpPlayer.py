#ON means sound is ON

#Make sure thresholf isn't too high like 850. Instead choose ~500-600.
#Ambient is ~200.

import serial,time, sched
import pygame
from pygame import mixer

# manages how often the program runs
s = sched.scheduler(time.time, time.sleep)

#create channels to prevent echo from speaker and python
mixer.init(channels=1)
channel_0=mixer.Channel(0)
channel_1=mixer.Channel(1)
channel_2=mixer.Channel(2)
xx = mixer.Sound('pokemon.wav')
pluck= mixer.Sound('Darude-Sandstorm.wav')
drums  = mixer.Sound('Smash-Mouth-All-Star.wav')



ser = serial.Serial('COM3', 9600)


# state= ser.readline()
# print(state)

#checks the state of the arduino
def check_state(sc): 
    
    #global ser
   
    st = str(ser.readline()).split(",")
    return st
    '''

    if st[0] == b'ON':
        return True
    elif state[0] == b'OFF':
        return False
    if st[1] == 'ON':
        return True
    elif state[1] == 'OFF':
        return False
    if st[2] == 'ON\r\n':
        return True
    elif state[2] == 'OFF\r\n':
        return False
    '''

#Create sound for channel then pause. Loops -1 means infinite power!
#Use channel.set_volume() to change volume if one channel is too low    
channel_0.play(xx, loops=-1)
channel_0.pause()
channel_1.play(drums, loops=-1)
channel_1.pause()
channel_2.play(pluck, loops=-1)
channel_2.pause()

s.run()
while True:
    st=check_state(s)
    print(st)
    if st[0] == "b'ON":
        channel_0.unpause()
    elif st[0] == "b'OFF":
        channel_0.pause()
    if st[1] == 'ON':
        channel_1.unpause()
    elif st[1] == 'OFF':
        channel_1.pause()
    if st[2] == "ON\\r\\n'":
        channel_2.unpause()
    elif st[2] == "OFF\\r\\n'":
        channel_2.pause()
    
    while(any(i in check_state(s) for i in ["b'ON",'ON',"ON\\r\\n'"])):
        if any(i in check_state(s) for i in ["b'OFF",'OFF',"OFF\\r\\n'"]):
            break
           
# st=(check_state(s))
# for i in st:
#     print(i)
# print(type(st))
# '''       
# s.run()

'''
while(True):
    
    st=check_state(s)
    print(st)
    if st[0] == b'ON':
        xx.play
    elif st[0] == b'OFF':
        xx.stop

#     if st[1] == 'ON':
#         mixer.music('the xx intro.wav').play
#     elif st[1] == 'OFF':
#         mixer.music('the xx intro.wav').stop
#     if st[2] == 'ON\r\n':
#         mixer.music('amsterdam-daughter.wav').play
#     elif st[2] == 'OFF\r\n':
#         mixer.music('amsterdam-daughter.wav').stop
        
    while(check_state(s) in [b'ON','ON','ON\r\n']):
        continue
'''
