#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 17, 2023, at 16:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'psychopy project'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\mateu\\OneDrive\\Desktop\\Stanford\\01_Fall 2023\\Rescue Project\\psychopy project_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    welcome_msg = visual.TextStim(win=win, name='welcome_msg',
        text='This experiment will take approximately 15 minutes to complete. This task is investigating object recognition under distracting conditions. \nYou will be asked to quickly identify objects while being distracted by other stimuli.\n\nPlease press SPACE when you are ready to begin.',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "consent" ---
    text_consent = visual.TextStim(win=win, name='text_consent',
        text='\nBy answering the following questions, you are participating in a study being performed by cognitive scientists in the Stanford Department of Psychology. If you have questions about this research, please contact us at stanfordpsych251@gmail.com. You must be at least 18 years old to participate. Your participation in this research is voluntary. You may decline to answer any or all of the following questions. You may decline further participation, at any time, without adverse consequences. Your anonymity is assured; the researchers who have requested your participation will not receive any personal information about you.\n\nPress SPACE to accept these conditions and continue to the experiment.',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    press_space_consent = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instruction1" ---
    instruction_text = visual.TextStim(win=win, name='instruction_text',
        text='In this study, you will see pairs of pictures flashed briefly on the screen. \nYou should do nothing in response to the first picture, which will always be a face. This face will signal that the second picture is about to be presented. \n\nYour task is to classify the second picture as either a gun or a toy. \n\nIf the second picture is a gun, press Q.\nIf the target picture is a toy, press P. \n\nAfter each trial, you will be asked to press the space bar to proceed.',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instruction2" ---
    text_intruction2 = visual.TextStim(win=win, name='text_intruction2',
        text='You have to respond as quickly and accurately as you can. If you make a mistake, don\'t worry. Just keep going to the next trial. \n\nIf you take too long to respond, you will see this message:\n"Please respond faster!"\n\nIf you see this message, please try to press the keys faster. \n\nPress SPACE to continue with instructions',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction2_space = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practice_ready" ---
    text_practice_ready = visual.TextStim(win=win, name='text_practice_ready',
        text='The first round of pictures will be a series of practice trials. \n\nPlease place your fingers over the "Q" (GUN) and "P" (TOY) keys on the keyboard so that you are ready to register your resp  onses. \n\nPlease click SPACE when you are ready to begin the practice trials.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_ready_space = keyboard.Keyboard()
    
    # --- Initialize components for Routine "press_space" ---
    press_space_cont = keyboard.Keyboard()
    press_space_remember = visual.TextStim(win=win, name='press_space_remember',
        text='Q: TOY           REMEMBER!           P:GUN\n\n\n\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_trial" ---
    face_img_practice = visual.ImageStim(
        win=win,
        name='face_img_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    object_img_practice = visual.ImageStim(
        win=win,
        name='object_img_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mask_practice = visual.ImageStim(
        win=win,
        name='mask_practice', 
        image='stimuli/Mask.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_pract = keyboard.Keyboard()
    too_slow_practice = keyboard.Keyboard()
    too_slow_text_practice = visual.TextStim(win=win, name='too_slow_text_practice',
        text='Please respond more quickly!\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "transition" ---
    transition_text = visual.TextStim(win=win, name='transition_text',
        text='Well done!\n\nNow we will begin with the actual trials. Feel free to take breaks in between trials if you want. If you do not take breaks, the whole experiment should take around 10 minutes. \n\nGood luck!\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    press_space_cont_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "press_space" ---
    press_space_cont = keyboard.Keyboard()
    press_space_remember = visual.TextStim(win=win, name='press_space_remember',
        text='Q: TOY           REMEMBER!           P:GUN\n\n\n\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    face_img = visual.ImageStim(
        win=win,
        name='face_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    object_img = visual.ImageStim(
        win=win,
        name='object_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mask = visual.ImageStim(
        win=win,
        name='mask', 
        image='stimuli/Mask.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp = keyboard.Keyboard()
    too_slow_resp = keyboard.Keyboard()
    too_slow_text = visual.TextStim(win=win, name='too_slow_text',
        text='Please respond more quickly!\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "halfway" ---
    text_halfway = visual.TextStim(win=win, name='text_halfway',
        text='You are halfway through the experiment! \n\nFeel free to take a short break if you want.\n\nPress SPACE when you are ready to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_halfway = keyboard.Keyboard()
    
    # --- Initialize components for Routine "press_space" ---
    press_space_cont = keyboard.Keyboard()
    press_space_remember = visual.TextStim(win=win, name='press_space_remember',
        text='Q: TOY           REMEMBER!           P:GUN\n\n\n\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    face_img = visual.ImageStim(
        win=win,
        name='face_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    object_img = visual.ImageStim(
        win=win,
        name='object_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    mask = visual.ImageStim(
        win=win,
        name='mask', 
        image='stimuli/Mask.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp = keyboard.Keyboard()
    too_slow_resp = keyboard.Keyboard()
    too_slow_text = visual.TextStim(win=win, name='too_slow_text',
        text='Please respond more quickly!\n\nPress SPACE to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "ethnicity_check" ---
    text_ethnicity_check = visual.TextStim(win=win, name='text_ethnicity_check',
        text='Before we finalize, we would like to know some additional information about you. This information will NOT affect your payment through Prolific. \n\nDo you identify as Hispanic or Latinx?\n\nY: YES\nN: NO',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_ethnicity = keyboard.Keyboard()
    
    # --- Initialize components for Routine "race_check" ---
    text_race_check = visual.TextStim(win=win, name='text_race_check',
        text='How would you describe your race?\n\nW: White or Caucasian\nB: Black or African American\nN: American Indian or Alaska Native\nA: Asian\nP: Native Hawaiian or Other Pacific Islander \nO: Other or Mixed',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_race_check = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    text = visual.TextStim(win=win, name='text',
        text='This is the end of the experiment. \n\nThis study examines the effect of facial priming with categorization of threatening and nonthreatening objects. Please do not to share this information with any other potential participants.\n\nThank you for your participation! Your Prolific completion code is CE8VG5D0. \n\nPress SPACE to exit. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_to_exit = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
    intro_key.keys = []
    intro_key.rt = []
    _intro_key_allKeys = []
    # keep track of which components have finished
    welcomeComponents = [welcome_msg, intro_key]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_msg* updates
        
        # if welcome_msg is starting this frame...
        if welcome_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_msg.frameNStart = frameN  # exact frame index
            welcome_msg.tStart = t  # local t and not account for scr refresh
            welcome_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_msg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_msg.started')
            # update status
            welcome_msg.status = STARTED
            welcome_msg.setAutoDraw(True)
        
        # if welcome_msg is active this frame...
        if welcome_msg.status == STARTED:
            # update params
            pass
        
        # *intro_key* updates
        waitOnFlip = False
        
        # if intro_key is starting this frame...
        if intro_key.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            intro_key.frameNStart = frameN  # exact frame index
            intro_key.tStart = t  # local t and not account for scr refresh
            intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_key.started')
            # update status
            intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intro_key.status == STARTED and not waitOnFlip:
            theseKeys = intro_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro_key_allKeys.extend(theseKeys)
            if len(_intro_key_allKeys):
                intro_key.keys = _intro_key_allKeys[-1].name  # just the last key pressed
                intro_key.rt = _intro_key_allKeys[-1].rt
                intro_key.duration = _intro_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcome.stopped', globalClock.getTime())
    # check responses
    if intro_key.keys in ['', [], None]:  # No response was made
        intro_key.keys = None
    thisExp.addData('intro_key.keys',intro_key.keys)
    if intro_key.keys != None:  # we had a response
        thisExp.addData('intro_key.rt', intro_key.rt)
        thisExp.addData('intro_key.duration', intro_key.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "consent" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('consent.started', globalClock.getTime())
    press_space_consent.keys = []
    press_space_consent.rt = []
    _press_space_consent_allKeys = []
    # keep track of which components have finished
    consentComponents = [text_consent, press_space_consent]
    for thisComponent in consentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consent" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_consent* updates
        
        # if text_consent is starting this frame...
        if text_consent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_consent.frameNStart = frameN  # exact frame index
            text_consent.tStart = t  # local t and not account for scr refresh
            text_consent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_consent, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_consent.started')
            # update status
            text_consent.status = STARTED
            text_consent.setAutoDraw(True)
        
        # if text_consent is active this frame...
        if text_consent.status == STARTED:
            # update params
            pass
        
        # *press_space_consent* updates
        waitOnFlip = False
        
        # if press_space_consent is starting this frame...
        if press_space_consent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_space_consent.frameNStart = frameN  # exact frame index
            press_space_consent.tStart = t  # local t and not account for scr refresh
            press_space_consent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_space_consent, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'press_space_consent.started')
            # update status
            press_space_consent.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(press_space_consent.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(press_space_consent.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if press_space_consent.status == STARTED and not waitOnFlip:
            theseKeys = press_space_consent.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _press_space_consent_allKeys.extend(theseKeys)
            if len(_press_space_consent_allKeys):
                press_space_consent.keys = _press_space_consent_allKeys[-1].name  # just the last key pressed
                press_space_consent.rt = _press_space_consent_allKeys[-1].rt
                press_space_consent.duration = _press_space_consent_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('consent.stopped', globalClock.getTime())
    # check responses
    if press_space_consent.keys in ['', [], None]:  # No response was made
        press_space_consent.keys = None
    thisExp.addData('press_space_consent.keys',press_space_consent.keys)
    if press_space_consent.keys != None:  # we had a response
        thisExp.addData('press_space_consent.rt', press_space_consent.rt)
        thisExp.addData('press_space_consent.duration', press_space_consent.duration)
    thisExp.nextEntry()
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction1.started', globalClock.getTime())
    instruction_key.keys = []
    instruction_key.rt = []
    _instruction_key_allKeys = []
    # keep track of which components have finished
    instruction1Components = [instruction_text, instruction_key]
    for thisComponent in instruction1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_text* updates
        
        # if instruction_text is starting this frame...
        if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text.frameNStart = frameN  # exact frame index
            instruction_text.tStart = t  # local t and not account for scr refresh
            instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text.started')
            # update status
            instruction_text.status = STARTED
            instruction_text.setAutoDraw(True)
        
        # if instruction_text is active this frame...
        if instruction_text.status == STARTED:
            # update params
            pass
        
        # *instruction_key* updates
        waitOnFlip = False
        
        # if instruction_key is starting this frame...
        if instruction_key.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            instruction_key.frameNStart = frameN  # exact frame index
            instruction_key.tStart = t  # local t and not account for scr refresh
            instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_key.started')
            # update status
            instruction_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_key.status == STARTED and not waitOnFlip:
            theseKeys = instruction_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instruction_key_allKeys.extend(theseKeys)
            if len(_instruction_key_allKeys):
                instruction_key.keys = _instruction_key_allKeys[-1].name  # just the last key pressed
                instruction_key.rt = _instruction_key_allKeys[-1].rt
                instruction_key.duration = _instruction_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction1" ---
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction1.stopped', globalClock.getTime())
    # check responses
    if instruction_key.keys in ['', [], None]:  # No response was made
        instruction_key.keys = None
    thisExp.addData('instruction_key.keys',instruction_key.keys)
    if instruction_key.keys != None:  # we had a response
        thisExp.addData('instruction_key.rt', instruction_key.rt)
        thisExp.addData('instruction_key.duration', instruction_key.duration)
    thisExp.nextEntry()
    # the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction2.started', globalClock.getTime())
    instruction2_space.keys = []
    instruction2_space.rt = []
    _instruction2_space_allKeys = []
    # keep track of which components have finished
    instruction2Components = [text_intruction2, instruction2_space]
    for thisComponent in instruction2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_intruction2* updates
        
        # if text_intruction2 is starting this frame...
        if text_intruction2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_intruction2.frameNStart = frameN  # exact frame index
            text_intruction2.tStart = t  # local t and not account for scr refresh
            text_intruction2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_intruction2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_intruction2.started')
            # update status
            text_intruction2.status = STARTED
            text_intruction2.setAutoDraw(True)
        
        # if text_intruction2 is active this frame...
        if text_intruction2.status == STARTED:
            # update params
            pass
        
        # *instruction2_space* updates
        waitOnFlip = False
        
        # if instruction2_space is starting this frame...
        if instruction2_space.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            instruction2_space.frameNStart = frameN  # exact frame index
            instruction2_space.tStart = t  # local t and not account for scr refresh
            instruction2_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction2_space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction2_space.started')
            # update status
            instruction2_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction2_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction2_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction2_space.status == STARTED and not waitOnFlip:
            theseKeys = instruction2_space.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instruction2_space_allKeys.extend(theseKeys)
            if len(_instruction2_space_allKeys):
                instruction2_space.keys = _instruction2_space_allKeys[-1].name  # just the last key pressed
                instruction2_space.rt = _instruction2_space_allKeys[-1].rt
                instruction2_space.duration = _instruction2_space_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction2" ---
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction2.stopped', globalClock.getTime())
    # check responses
    if instruction2_space.keys in ['', [], None]:  # No response was made
        instruction2_space.keys = None
    thisExp.addData('instruction2_space.keys',instruction2_space.keys)
    if instruction2_space.keys != None:  # we had a response
        thisExp.addData('instruction2_space.rt', instruction2_space.rt)
        thisExp.addData('instruction2_space.duration', instruction2_space.duration)
    thisExp.nextEntry()
    # the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_ready" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice_ready.started', globalClock.getTime())
    practice_ready_space.keys = []
    practice_ready_space.rt = []
    _practice_ready_space_allKeys = []
    # keep track of which components have finished
    practice_readyComponents = [text_practice_ready, practice_ready_space]
    for thisComponent in practice_readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_ready" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_practice_ready* updates
        
        # if text_practice_ready is starting this frame...
        if text_practice_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_ready.frameNStart = frameN  # exact frame index
            text_practice_ready.tStart = t  # local t and not account for scr refresh
            text_practice_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_ready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_practice_ready.started')
            # update status
            text_practice_ready.status = STARTED
            text_practice_ready.setAutoDraw(True)
        
        # if text_practice_ready is active this frame...
        if text_practice_ready.status == STARTED:
            # update params
            pass
        
        # *practice_ready_space* updates
        waitOnFlip = False
        
        # if practice_ready_space is starting this frame...
        if practice_ready_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_ready_space.frameNStart = frameN  # exact frame index
            practice_ready_space.tStart = t  # local t and not account for scr refresh
            practice_ready_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_ready_space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_ready_space.started')
            # update status
            practice_ready_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_ready_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_ready_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_ready_space.status == STARTED and not waitOnFlip:
            theseKeys = practice_ready_space.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _practice_ready_space_allKeys.extend(theseKeys)
            if len(_practice_ready_space_allKeys):
                practice_ready_space.keys = _practice_ready_space_allKeys[-1].name  # just the last key pressed
                practice_ready_space.rt = _practice_ready_space_allKeys[-1].rt
                practice_ready_space.duration = _practice_ready_space_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_ready" ---
    for thisComponent in practice_readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice_ready.stopped', globalClock.getTime())
    # check responses
    if practice_ready_space.keys in ['', [], None]:  # No response was made
        practice_ready_space.keys = None
    thisExp.addData('practice_ready_space.keys',practice_ready_space.keys)
    if practice_ready_space.keys != None:  # we had a response
        thisExp.addData('practice_ready_space.rt', practice_ready_space.rt)
        thisExp.addData('practice_ready_space.duration', practice_ready_space.duration)
    thisExp.nextEntry()
    # the Routine "practice_ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('loop3.xlsx'),
        seed=None, name='practice_trials')
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            globals()[paramName] = thisPractice_trial[paramName]
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                globals()[paramName] = thisPractice_trial[paramName]
        
        # --- Prepare to start Routine "press_space" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('press_space.started', globalClock.getTime())
        press_space_cont.keys = []
        press_space_cont.rt = []
        _press_space_cont_allKeys = []
        # keep track of which components have finished
        press_spaceComponents = [press_space_cont, press_space_remember]
        for thisComponent in press_spaceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "press_space" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *press_space_cont* updates
            waitOnFlip = False
            
            # if press_space_cont is starting this frame...
            if press_space_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_cont.frameNStart = frameN  # exact frame index
                press_space_cont.tStart = t  # local t and not account for scr refresh
                press_space_cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_cont, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_cont.started')
                # update status
                press_space_cont.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(press_space_cont.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(press_space_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if press_space_cont.status == STARTED and not waitOnFlip:
                theseKeys = press_space_cont.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _press_space_cont_allKeys.extend(theseKeys)
                if len(_press_space_cont_allKeys):
                    press_space_cont.keys = _press_space_cont_allKeys[-1].name  # just the last key pressed
                    press_space_cont.rt = _press_space_cont_allKeys[-1].rt
                    press_space_cont.duration = _press_space_cont_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *press_space_remember* updates
            
            # if press_space_remember is starting this frame...
            if press_space_remember.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_remember.frameNStart = frameN  # exact frame index
                press_space_remember.tStart = t  # local t and not account for scr refresh
                press_space_remember.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_remember, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_remember.started')
                # update status
                press_space_remember.status = STARTED
                press_space_remember.setAutoDraw(True)
            
            # if press_space_remember is active this frame...
            if press_space_remember.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in press_spaceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "press_space" ---
        for thisComponent in press_spaceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('press_space.stopped', globalClock.getTime())
        # check responses
        if press_space_cont.keys in ['', [], None]:  # No response was made
            press_space_cont.keys = None
        practice_trials.addData('press_space_cont.keys',press_space_cont.keys)
        if press_space_cont.keys != None:  # we had a response
            practice_trials.addData('press_space_cont.rt', press_space_cont.rt)
            practice_trials.addData('press_space_cont.duration', press_space_cont.duration)
        # the Routine "press_space" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice_trial.started', globalClock.getTime())
        face_img_practice.setImage(face)
        object_img_practice.setImage(object)
        key_pract.keys = []
        key_pract.rt = []
        _key_pract_allKeys = []
        too_slow_practice.keys = []
        too_slow_practice.rt = []
        _too_slow_practice_allKeys = []
        # keep track of which components have finished
        practice_trialComponents = [face_img_practice, object_img_practice, mask_practice, key_pract, too_slow_practice, too_slow_text_practice]
        for thisComponent in practice_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_img_practice* updates
            
            # if face_img_practice is starting this frame...
            if face_img_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_img_practice.frameNStart = frameN  # exact frame index
                face_img_practice.tStart = t  # local t and not account for scr refresh
                face_img_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_img_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_img_practice.started')
                # update status
                face_img_practice.status = STARTED
                face_img_practice.setAutoDraw(True)
            
            # if face_img_practice is active this frame...
            if face_img_practice.status == STARTED:
                # update params
                pass
            
            # if face_img_practice is stopping this frame...
            if face_img_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > face_img_practice.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    face_img_practice.tStop = t  # not accounting for scr refresh
                    face_img_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'face_img_practice.stopped')
                    # update status
                    face_img_practice.status = FINISHED
                    face_img_practice.setAutoDraw(False)
            
            # *object_img_practice* updates
            
            # if object_img_practice is starting this frame...
            if object_img_practice.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                object_img_practice.frameNStart = frameN  # exact frame index
                object_img_practice.tStart = t  # local t and not account for scr refresh
                object_img_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_img_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'object_img_practice.started')
                # update status
                object_img_practice.status = STARTED
                object_img_practice.setAutoDraw(True)
            
            # if object_img_practice is active this frame...
            if object_img_practice.status == STARTED:
                # update params
                pass
            
            # if object_img_practice is stopping this frame...
            if object_img_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > object_img_practice.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    object_img_practice.tStop = t  # not accounting for scr refresh
                    object_img_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'object_img_practice.stopped')
                    # update status
                    object_img_practice.status = FINISHED
                    object_img_practice.setAutoDraw(False)
            
            # *mask_practice* updates
            
            # if mask_practice is starting this frame...
            if mask_practice.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                mask_practice.frameNStart = frameN  # exact frame index
                mask_practice.tStart = t  # local t and not account for scr refresh
                mask_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mask_practice.started')
                # update status
                mask_practice.status = STARTED
                mask_practice.setAutoDraw(True)
            
            # if mask_practice is active this frame...
            if mask_practice.status == STARTED:
                # update params
                pass
            
            # if mask_practice is stopping this frame...
            if mask_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask_practice.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    mask_practice.tStop = t  # not accounting for scr refresh
                    mask_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mask_practice.stopped')
                    # update status
                    mask_practice.status = FINISHED
                    mask_practice.setAutoDraw(False)
            
            # *key_pract* updates
            waitOnFlip = False
            
            # if key_pract is starting this frame...
            if key_pract.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_pract.frameNStart = frameN  # exact frame index
                key_pract.tStart = t  # local t and not account for scr refresh
                key_pract.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_pract, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_pract.started')
                # update status
                key_pract.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_pract.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_pract.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_pract is stopping this frame...
            if key_pract.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_pract.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_pract.tStop = t  # not accounting for scr refresh
                    key_pract.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_pract.stopped')
                    # update status
                    key_pract.status = FINISHED
                    key_pract.status = FINISHED
            if key_pract.status == STARTED and not waitOnFlip:
                theseKeys = key_pract.getKeys(keyList=['q','p'], ignoreKeys=["escape"], waitRelease=False)
                _key_pract_allKeys.extend(theseKeys)
                if len(_key_pract_allKeys):
                    key_pract.keys = _key_pract_allKeys[-1].name  # just the last key pressed
                    key_pract.rt = _key_pract_allKeys[-1].rt
                    key_pract.duration = _key_pract_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_practice* updates
            waitOnFlip = False
            
            # if too_slow_practice is starting this frame...
            if too_slow_practice.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_practice.frameNStart = frameN  # exact frame index
                too_slow_practice.tStart = t  # local t and not account for scr refresh
                too_slow_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_practice.started')
                # update status
                too_slow_practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(too_slow_practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(too_slow_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if too_slow_practice.status == STARTED and not waitOnFlip:
                theseKeys = too_slow_practice.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _too_slow_practice_allKeys.extend(theseKeys)
                if len(_too_slow_practice_allKeys):
                    too_slow_practice.keys = _too_slow_practice_allKeys[-1].name  # just the last key pressed
                    too_slow_practice.rt = _too_slow_practice_allKeys[-1].rt
                    too_slow_practice.duration = _too_slow_practice_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_text_practice* updates
            
            # if too_slow_text_practice is starting this frame...
            if too_slow_text_practice.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_text_practice.frameNStart = frameN  # exact frame index
                too_slow_text_practice.tStart = t  # local t and not account for scr refresh
                too_slow_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_text_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_text_practice.started')
                # update status
                too_slow_text_practice.status = STARTED
                too_slow_text_practice.setAutoDraw(True)
            
            # if too_slow_text_practice is active this frame...
            if too_slow_text_practice.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_trial" ---
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice_trial.stopped', globalClock.getTime())
        # check responses
        if key_pract.keys in ['', [], None]:  # No response was made
            key_pract.keys = None
        practice_trials.addData('key_pract.keys',key_pract.keys)
        if key_pract.keys != None:  # we had a response
            practice_trials.addData('key_pract.rt', key_pract.rt)
            practice_trials.addData('key_pract.duration', key_pract.duration)
        # check responses
        if too_slow_practice.keys in ['', [], None]:  # No response was made
            too_slow_practice.keys = None
        practice_trials.addData('too_slow_practice.keys',too_slow_practice.keys)
        if too_slow_practice.keys != None:  # we had a response
            practice_trials.addData('too_slow_practice.rt', too_slow_practice.rt)
            practice_trials.addData('too_slow_practice.duration', too_slow_practice.duration)
        # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'practice_trials'
    
    
    # --- Prepare to start Routine "transition" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('transition.started', globalClock.getTime())
    press_space_cont_2.keys = []
    press_space_cont_2.rt = []
    _press_space_cont_2_allKeys = []
    # keep track of which components have finished
    transitionComponents = [transition_text, press_space_cont_2]
    for thisComponent in transitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "transition" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *transition_text* updates
        
        # if transition_text is starting this frame...
        if transition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            transition_text.frameNStart = frameN  # exact frame index
            transition_text.tStart = t  # local t and not account for scr refresh
            transition_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(transition_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'transition_text.started')
            # update status
            transition_text.status = STARTED
            transition_text.setAutoDraw(True)
        
        # if transition_text is active this frame...
        if transition_text.status == STARTED:
            # update params
            pass
        
        # *press_space_cont_2* updates
        waitOnFlip = False
        
        # if press_space_cont_2 is starting this frame...
        if press_space_cont_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            press_space_cont_2.frameNStart = frameN  # exact frame index
            press_space_cont_2.tStart = t  # local t and not account for scr refresh
            press_space_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_space_cont_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'press_space_cont_2.started')
            # update status
            press_space_cont_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(press_space_cont_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(press_space_cont_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if press_space_cont_2.status == STARTED and not waitOnFlip:
            theseKeys = press_space_cont_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _press_space_cont_2_allKeys.extend(theseKeys)
            if len(_press_space_cont_2_allKeys):
                press_space_cont_2.keys = _press_space_cont_2_allKeys[-1].name  # just the last key pressed
                press_space_cont_2.rt = _press_space_cont_2_allKeys[-1].rt
                press_space_cont_2.duration = _press_space_cont_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "transition" ---
    for thisComponent in transitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('transition.stopped', globalClock.getTime())
    # check responses
    if press_space_cont_2.keys in ['', [], None]:  # No response was made
        press_space_cont_2.keys = None
    thisExp.addData('press_space_cont_2.keys',press_space_cont_2.keys)
    if press_space_cont_2.keys != None:  # we had a response
        thisExp.addData('press_space_cont_2.rt', press_space_cont_2.rt)
        thisExp.addData('press_space_cont_2.duration', press_space_cont_2.duration)
    thisExp.nextEntry()
    # the Routine "transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('loop2.xlsx', selection='0:72'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "press_space" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('press_space.started', globalClock.getTime())
        press_space_cont.keys = []
        press_space_cont.rt = []
        _press_space_cont_allKeys = []
        # keep track of which components have finished
        press_spaceComponents = [press_space_cont, press_space_remember]
        for thisComponent in press_spaceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "press_space" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *press_space_cont* updates
            waitOnFlip = False
            
            # if press_space_cont is starting this frame...
            if press_space_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_cont.frameNStart = frameN  # exact frame index
                press_space_cont.tStart = t  # local t and not account for scr refresh
                press_space_cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_cont, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_cont.started')
                # update status
                press_space_cont.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(press_space_cont.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(press_space_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if press_space_cont.status == STARTED and not waitOnFlip:
                theseKeys = press_space_cont.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _press_space_cont_allKeys.extend(theseKeys)
                if len(_press_space_cont_allKeys):
                    press_space_cont.keys = _press_space_cont_allKeys[-1].name  # just the last key pressed
                    press_space_cont.rt = _press_space_cont_allKeys[-1].rt
                    press_space_cont.duration = _press_space_cont_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *press_space_remember* updates
            
            # if press_space_remember is starting this frame...
            if press_space_remember.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_remember.frameNStart = frameN  # exact frame index
                press_space_remember.tStart = t  # local t and not account for scr refresh
                press_space_remember.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_remember, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_remember.started')
                # update status
                press_space_remember.status = STARTED
                press_space_remember.setAutoDraw(True)
            
            # if press_space_remember is active this frame...
            if press_space_remember.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in press_spaceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "press_space" ---
        for thisComponent in press_spaceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('press_space.stopped', globalClock.getTime())
        # check responses
        if press_space_cont.keys in ['', [], None]:  # No response was made
            press_space_cont.keys = None
        trials.addData('press_space_cont.keys',press_space_cont.keys)
        if press_space_cont.keys != None:  # we had a response
            trials.addData('press_space_cont.rt', press_space_cont.rt)
            trials.addData('press_space_cont.duration', press_space_cont.duration)
        # the Routine "press_space" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        face_img.setImage(face)
        object_img.setImage(object)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        too_slow_resp.keys = []
        too_slow_resp.rt = []
        _too_slow_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [face_img, object_img, mask, key_resp, too_slow_resp, too_slow_text]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_img* updates
            
            # if face_img is starting this frame...
            if face_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_img.frameNStart = frameN  # exact frame index
                face_img.tStart = t  # local t and not account for scr refresh
                face_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_img.started')
                # update status
                face_img.status = STARTED
                face_img.setAutoDraw(True)
            
            # if face_img is active this frame...
            if face_img.status == STARTED:
                # update params
                pass
            
            # if face_img is stopping this frame...
            if face_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > face_img.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    face_img.tStop = t  # not accounting for scr refresh
                    face_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'face_img.stopped')
                    # update status
                    face_img.status = FINISHED
                    face_img.setAutoDraw(False)
            
            # *object_img* updates
            
            # if object_img is starting this frame...
            if object_img.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                object_img.frameNStart = frameN  # exact frame index
                object_img.tStart = t  # local t and not account for scr refresh
                object_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'object_img.started')
                # update status
                object_img.status = STARTED
                object_img.setAutoDraw(True)
            
            # if object_img is active this frame...
            if object_img.status == STARTED:
                # update params
                pass
            
            # if object_img is stopping this frame...
            if object_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > object_img.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    object_img.tStop = t  # not accounting for scr refresh
                    object_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'object_img.stopped')
                    # update status
                    object_img.status = FINISHED
                    object_img.setAutoDraw(False)
            
            # *mask* updates
            
            # if mask is starting this frame...
            if mask.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                mask.frameNStart = frameN  # exact frame index
                mask.tStart = t  # local t and not account for scr refresh
                mask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mask.started')
                # update status
                mask.status = STARTED
                mask.setAutoDraw(True)
            
            # if mask is active this frame...
            if mask.status == STARTED:
                # update params
                pass
            
            # if mask is stopping this frame...
            if mask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    mask.tStop = t  # not accounting for scr refresh
                    mask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mask.stopped')
                    # update status
                    mask.status = FINISHED
                    mask.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['q','p'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_resp* updates
            waitOnFlip = False
            
            # if too_slow_resp is starting this frame...
            if too_slow_resp.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_resp.frameNStart = frameN  # exact frame index
                too_slow_resp.tStart = t  # local t and not account for scr refresh
                too_slow_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_resp.started')
                # update status
                too_slow_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(too_slow_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(too_slow_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if too_slow_resp.status == STARTED and not waitOnFlip:
                theseKeys = too_slow_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _too_slow_resp_allKeys.extend(theseKeys)
                if len(_too_slow_resp_allKeys):
                    too_slow_resp.keys = _too_slow_resp_allKeys[-1].name  # just the last key pressed
                    too_slow_resp.rt = _too_slow_resp_allKeys[-1].rt
                    too_slow_resp.duration = _too_slow_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_text* updates
            
            # if too_slow_text is starting this frame...
            if too_slow_text.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_text.frameNStart = frameN  # exact frame index
                too_slow_text.tStart = t  # local t and not account for scr refresh
                too_slow_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_text.started')
                # update status
                too_slow_text.status = STARTED
                too_slow_text.setAutoDraw(True)
            
            # if too_slow_text is active this frame...
            if too_slow_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # check responses
        if too_slow_resp.keys in ['', [], None]:  # No response was made
            too_slow_resp.keys = None
        trials.addData('too_slow_resp.keys',too_slow_resp.keys)
        if too_slow_resp.keys != None:  # we had a response
            trials.addData('too_slow_resp.rt', too_slow_resp.rt)
            trials.addData('too_slow_resp.duration', too_slow_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "halfway" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('halfway.started', globalClock.getTime())
    key_halfway.keys = []
    key_halfway.rt = []
    _key_halfway_allKeys = []
    # keep track of which components have finished
    halfwayComponents = [text_halfway, key_halfway]
    for thisComponent in halfwayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "halfway" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_halfway* updates
        
        # if text_halfway is starting this frame...
        if text_halfway.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_halfway.frameNStart = frameN  # exact frame index
            text_halfway.tStart = t  # local t and not account for scr refresh
            text_halfway.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_halfway, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_halfway.started')
            # update status
            text_halfway.status = STARTED
            text_halfway.setAutoDraw(True)
        
        # if text_halfway is active this frame...
        if text_halfway.status == STARTED:
            # update params
            pass
        
        # *key_halfway* updates
        waitOnFlip = False
        
        # if key_halfway is starting this frame...
        if key_halfway.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            key_halfway.frameNStart = frameN  # exact frame index
            key_halfway.tStart = t  # local t and not account for scr refresh
            key_halfway.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_halfway, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_halfway.started')
            # update status
            key_halfway.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_halfway.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_halfway.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_halfway.status == STARTED and not waitOnFlip:
            theseKeys = key_halfway.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_halfway_allKeys.extend(theseKeys)
            if len(_key_halfway_allKeys):
                key_halfway.keys = _key_halfway_allKeys[-1].name  # just the last key pressed
                key_halfway.rt = _key_halfway_allKeys[-1].rt
                key_halfway.duration = _key_halfway_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in halfwayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "halfway" ---
    for thisComponent in halfwayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('halfway.stopped', globalClock.getTime())
    # check responses
    if key_halfway.keys in ['', [], None]:  # No response was made
        key_halfway.keys = None
    thisExp.addData('key_halfway.keys',key_halfway.keys)
    if key_halfway.keys != None:  # we had a response
        thisExp.addData('key_halfway.rt', key_halfway.rt)
        thisExp.addData('key_halfway.duration', key_halfway.duration)
    thisExp.nextEntry()
    # the Routine "halfway" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('loop2.xlsx', selection='73:144'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "press_space" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('press_space.started', globalClock.getTime())
        press_space_cont.keys = []
        press_space_cont.rt = []
        _press_space_cont_allKeys = []
        # keep track of which components have finished
        press_spaceComponents = [press_space_cont, press_space_remember]
        for thisComponent in press_spaceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "press_space" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *press_space_cont* updates
            waitOnFlip = False
            
            # if press_space_cont is starting this frame...
            if press_space_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_cont.frameNStart = frameN  # exact frame index
                press_space_cont.tStart = t  # local t and not account for scr refresh
                press_space_cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_cont, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_cont.started')
                # update status
                press_space_cont.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(press_space_cont.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(press_space_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if press_space_cont.status == STARTED and not waitOnFlip:
                theseKeys = press_space_cont.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _press_space_cont_allKeys.extend(theseKeys)
                if len(_press_space_cont_allKeys):
                    press_space_cont.keys = _press_space_cont_allKeys[-1].name  # just the last key pressed
                    press_space_cont.rt = _press_space_cont_allKeys[-1].rt
                    press_space_cont.duration = _press_space_cont_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *press_space_remember* updates
            
            # if press_space_remember is starting this frame...
            if press_space_remember.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_space_remember.frameNStart = frameN  # exact frame index
                press_space_remember.tStart = t  # local t and not account for scr refresh
                press_space_remember.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_space_remember, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press_space_remember.started')
                # update status
                press_space_remember.status = STARTED
                press_space_remember.setAutoDraw(True)
            
            # if press_space_remember is active this frame...
            if press_space_remember.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in press_spaceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "press_space" ---
        for thisComponent in press_spaceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('press_space.stopped', globalClock.getTime())
        # check responses
        if press_space_cont.keys in ['', [], None]:  # No response was made
            press_space_cont.keys = None
        trials_2.addData('press_space_cont.keys',press_space_cont.keys)
        if press_space_cont.keys != None:  # we had a response
            trials_2.addData('press_space_cont.rt', press_space_cont.rt)
            trials_2.addData('press_space_cont.duration', press_space_cont.duration)
        # the Routine "press_space" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        face_img.setImage(face)
        object_img.setImage(object)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        too_slow_resp.keys = []
        too_slow_resp.rt = []
        _too_slow_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [face_img, object_img, mask, key_resp, too_slow_resp, too_slow_text]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_img* updates
            
            # if face_img is starting this frame...
            if face_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_img.frameNStart = frameN  # exact frame index
                face_img.tStart = t  # local t and not account for scr refresh
                face_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_img.started')
                # update status
                face_img.status = STARTED
                face_img.setAutoDraw(True)
            
            # if face_img is active this frame...
            if face_img.status == STARTED:
                # update params
                pass
            
            # if face_img is stopping this frame...
            if face_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > face_img.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    face_img.tStop = t  # not accounting for scr refresh
                    face_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'face_img.stopped')
                    # update status
                    face_img.status = FINISHED
                    face_img.setAutoDraw(False)
            
            # *object_img* updates
            
            # if object_img is starting this frame...
            if object_img.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                object_img.frameNStart = frameN  # exact frame index
                object_img.tStart = t  # local t and not account for scr refresh
                object_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'object_img.started')
                # update status
                object_img.status = STARTED
                object_img.setAutoDraw(True)
            
            # if object_img is active this frame...
            if object_img.status == STARTED:
                # update params
                pass
            
            # if object_img is stopping this frame...
            if object_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > object_img.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    object_img.tStop = t  # not accounting for scr refresh
                    object_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'object_img.stopped')
                    # update status
                    object_img.status = FINISHED
                    object_img.setAutoDraw(False)
            
            # *mask* updates
            
            # if mask is starting this frame...
            if mask.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                mask.frameNStart = frameN  # exact frame index
                mask.tStart = t  # local t and not account for scr refresh
                mask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mask.started')
                # update status
                mask.status = STARTED
                mask.setAutoDraw(True)
            
            # if mask is active this frame...
            if mask.status == STARTED:
                # update params
                pass
            
            # if mask is stopping this frame...
            if mask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    mask.tStop = t  # not accounting for scr refresh
                    mask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mask.stopped')
                    # update status
                    mask.status = FINISHED
                    mask.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['q','p'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_resp* updates
            waitOnFlip = False
            
            # if too_slow_resp is starting this frame...
            if too_slow_resp.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_resp.frameNStart = frameN  # exact frame index
                too_slow_resp.tStart = t  # local t and not account for scr refresh
                too_slow_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_resp.started')
                # update status
                too_slow_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(too_slow_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(too_slow_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if too_slow_resp.status == STARTED and not waitOnFlip:
                theseKeys = too_slow_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _too_slow_resp_allKeys.extend(theseKeys)
                if len(_too_slow_resp_allKeys):
                    too_slow_resp.keys = _too_slow_resp_allKeys[-1].name  # just the last key pressed
                    too_slow_resp.rt = _too_slow_resp_allKeys[-1].rt
                    too_slow_resp.duration = _too_slow_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *too_slow_text* updates
            
            # if too_slow_text is starting this frame...
            if too_slow_text.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                too_slow_text.frameNStart = frameN  # exact frame index
                too_slow_text.tStart = t  # local t and not account for scr refresh
                too_slow_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(too_slow_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'too_slow_text.started')
                # update status
                too_slow_text.status = STARTED
                too_slow_text.setAutoDraw(True)
            
            # if too_slow_text is active this frame...
            if too_slow_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials_2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_2.addData('key_resp.rt', key_resp.rt)
            trials_2.addData('key_resp.duration', key_resp.duration)
        # check responses
        if too_slow_resp.keys in ['', [], None]:  # No response was made
            too_slow_resp.keys = None
        trials_2.addData('too_slow_resp.keys',too_slow_resp.keys)
        if too_slow_resp.keys != None:  # we had a response
            trials_2.addData('too_slow_resp.rt', too_slow_resp.rt)
            trials_2.addData('too_slow_resp.duration', too_slow_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "ethnicity_check" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ethnicity_check.started', globalClock.getTime())
    key_resp_ethnicity.keys = []
    key_resp_ethnicity.rt = []
    _key_resp_ethnicity_allKeys = []
    # keep track of which components have finished
    ethnicity_checkComponents = [text_ethnicity_check, key_resp_ethnicity]
    for thisComponent in ethnicity_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ethnicity_check" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_ethnicity_check* updates
        
        # if text_ethnicity_check is starting this frame...
        if text_ethnicity_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ethnicity_check.frameNStart = frameN  # exact frame index
            text_ethnicity_check.tStart = t  # local t and not account for scr refresh
            text_ethnicity_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ethnicity_check, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_ethnicity_check.started')
            # update status
            text_ethnicity_check.status = STARTED
            text_ethnicity_check.setAutoDraw(True)
        
        # if text_ethnicity_check is active this frame...
        if text_ethnicity_check.status == STARTED:
            # update params
            pass
        
        # *key_resp_ethnicity* updates
        waitOnFlip = False
        
        # if key_resp_ethnicity is starting this frame...
        if key_resp_ethnicity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_ethnicity.frameNStart = frameN  # exact frame index
            key_resp_ethnicity.tStart = t  # local t and not account for scr refresh
            key_resp_ethnicity.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_ethnicity, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_ethnicity.started')
            # update status
            key_resp_ethnicity.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_ethnicity.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_ethnicity.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_ethnicity.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_ethnicity.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_ethnicity_allKeys.extend(theseKeys)
            if len(_key_resp_ethnicity_allKeys):
                key_resp_ethnicity.keys = _key_resp_ethnicity_allKeys[-1].name  # just the last key pressed
                key_resp_ethnicity.rt = _key_resp_ethnicity_allKeys[-1].rt
                key_resp_ethnicity.duration = _key_resp_ethnicity_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ethnicity_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ethnicity_check" ---
    for thisComponent in ethnicity_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ethnicity_check.stopped', globalClock.getTime())
    # check responses
    if key_resp_ethnicity.keys in ['', [], None]:  # No response was made
        key_resp_ethnicity.keys = None
    thisExp.addData('key_resp_ethnicity.keys',key_resp_ethnicity.keys)
    if key_resp_ethnicity.keys != None:  # we had a response
        thisExp.addData('key_resp_ethnicity.rt', key_resp_ethnicity.rt)
        thisExp.addData('key_resp_ethnicity.duration', key_resp_ethnicity.duration)
    thisExp.nextEntry()
    # the Routine "ethnicity_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "race_check" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('race_check.started', globalClock.getTime())
    key_resp_race_check.keys = []
    key_resp_race_check.rt = []
    _key_resp_race_check_allKeys = []
    # keep track of which components have finished
    race_checkComponents = [text_race_check, key_resp_race_check]
    for thisComponent in race_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "race_check" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_race_check* updates
        
        # if text_race_check is starting this frame...
        if text_race_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_race_check.frameNStart = frameN  # exact frame index
            text_race_check.tStart = t  # local t and not account for scr refresh
            text_race_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_race_check, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_race_check.started')
            # update status
            text_race_check.status = STARTED
            text_race_check.setAutoDraw(True)
        
        # if text_race_check is active this frame...
        if text_race_check.status == STARTED:
            # update params
            pass
        
        # *key_resp_race_check* updates
        waitOnFlip = False
        
        # if key_resp_race_check is starting this frame...
        if key_resp_race_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_race_check.frameNStart = frameN  # exact frame index
            key_resp_race_check.tStart = t  # local t and not account for scr refresh
            key_resp_race_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_race_check, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_race_check.started')
            # update status
            key_resp_race_check.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_race_check.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_race_check.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_race_check.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_race_check.getKeys(keyList=['w', 'b', 'n', 'a', 'p', 'o'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_race_check_allKeys.extend(theseKeys)
            if len(_key_resp_race_check_allKeys):
                key_resp_race_check.keys = _key_resp_race_check_allKeys[-1].name  # just the last key pressed
                key_resp_race_check.rt = _key_resp_race_check_allKeys[-1].rt
                key_resp_race_check.duration = _key_resp_race_check_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in race_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "race_check" ---
    for thisComponent in race_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('race_check.stopped', globalClock.getTime())
    # check responses
    if key_resp_race_check.keys in ['', [], None]:  # No response was made
        key_resp_race_check.keys = None
    thisExp.addData('key_resp_race_check.keys',key_resp_race_check.keys)
    if key_resp_race_check.keys != None:  # we had a response
        thisExp.addData('key_resp_race_check.rt', key_resp_race_check.rt)
        thisExp.addData('key_resp_race_check.duration', key_resp_race_check.duration)
    thisExp.nextEntry()
    # the Routine "race_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    space_to_exit.keys = []
    space_to_exit.rt = []
    _space_to_exit_allKeys = []
    # keep track of which components have finished
    endComponents = [text, space_to_exit]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *space_to_exit* updates
        waitOnFlip = False
        
        # if space_to_exit is starting this frame...
        if space_to_exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_to_exit.frameNStart = frameN  # exact frame index
            space_to_exit.tStart = t  # local t and not account for scr refresh
            space_to_exit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_to_exit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_to_exit.started')
            # update status
            space_to_exit.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_to_exit.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_to_exit.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_to_exit.status == STARTED and not waitOnFlip:
            theseKeys = space_to_exit.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_to_exit_allKeys.extend(theseKeys)
            if len(_space_to_exit_allKeys):
                space_to_exit.keys = _space_to_exit_allKeys[-1].name  # just the last key pressed
                space_to_exit.rt = _space_to_exit_allKeys[-1].rt
                space_to_exit.duration = _space_to_exit_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if space_to_exit.keys in ['', [], None]:  # No response was made
        space_to_exit.keys = None
    thisExp.addData('space_to_exit.keys',space_to_exit.keys)
    if space_to_exit.keys != None:  # we had a response
        thisExp.addData('space_to_exit.rt', space_to_exit.rt)
        thisExp.addData('space_to_exit.duration', space_to_exit.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
