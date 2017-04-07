##import pygame.mixer, pygame.time
##import time
##
##pygame.mixer.init(44100)
##music = pygame.mixer.music
##music.load('C:\\Users\\felipe.simao\\Documents\\Desenvolvimento de Utilidades\\alarme1.mp3')
##music.play(-1)
##music.set_volume(1)
###music.fadeout(3000)

#!/usr/bin/env python
#Boa:PyApp:main
modules = {}


import ctypes

mixerSetControlDetails = (
    ctypes.windll.winmm.mixerSetControlDetails)

mixerGetControlDetails = (
    ctypes.windll.winmm.mixerGetControlDetailsA)

# Some constants
MIXER_OBJECTF_MIXER = 0 # mmsystem.h
VOLUME_CONTROL_ID = 1     # Same on all machines?
SPEAKER_LINE_FADER_ID = 1 # "Identifier <identifier> in OID value does not
resolve to a positive integer"
MINIMUM_VOLUME = 0     # fader control (MSDN Library)
MAXIMUM_VOLUME = 65535 # fader control (MSDN Library)

class MIXERCONTROLDETAILS(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('cbStruct', ctypes.c_ulong),
                ('dwControlID', ctypes.c_ulong),
                ('cChannels', ctypes.c_ulong),
                ('cMultipleItems', ctypes.c_ulong),
                ('cbDetails', ctypes.c_ulong),
                ('paDetails', ctypes.POINTER(ctypes.c_ulong))]

def setVolume(volume):
    """Set the speaker volume on the 'Volume Control' mixer"""
    if not (MINIMUM_VOLUME <= volume <= MAXIMUM_VOLUME):
        raise ValueError, "Volume out of range"
    cd = MIXERCONTROLDETAILS(ctypes.sizeof(MIXERCONTROLDETAILS),
                             SPEAKER_LINE_FADER_ID,
                             1, 0,
                             ctypes.sizeof(ctypes.c_ulong),
                             ctypes.pointer(ctypes.c_ulong(volume)))
    ret = mixerSetControlDetails(VOLUME_CONTROL_ID,
                                 ctypes.byref(cd),
                                 MIXER_OBJECTF_MIXER)
    if ret != 0:
        print WindowsError, "Error %d while setting volume" % ret

    ret = mixerGetControlDetails(VOLUME_CONTROL_ID,
                                 ctypes.byref(cd),
                                 MIXER_OBJECTF_MIXER)
    if ret != 0:
        print WindowsError, "Error %d while setting volume" % ret
    else:
        print 'cbStruct', cd.cbStruct
        print 'dwControlID', cd.dwControlID
        print 'cChannels', cd.cChannels
        print 'cMultipleItems', cd.cMultipleItems
        print 'cbDetails', cd.cbDetails
        print 'paDetails', cd.paDetails.contents
    return

#setVolume((2**16-1)/2)
setVolume(0)   ## added by me, neither value does anything
