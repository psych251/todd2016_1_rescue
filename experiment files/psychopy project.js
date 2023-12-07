/************************* 
 * Psychopy Project *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'psychopy project';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(instruction1RoutineBegin());
flowScheduler.add(instruction1RoutineEachFrame());
flowScheduler.add(instruction1RoutineEnd());
flowScheduler.add(instruction2RoutineBegin());
flowScheduler.add(instruction2RoutineEachFrame());
flowScheduler.add(instruction2RoutineEnd());
flowScheduler.add(practice_readyRoutineBegin());
flowScheduler.add(practice_readyRoutineEachFrame());
flowScheduler.add(practice_readyRoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin(practice_trialsLoopScheduler));
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);



flowScheduler.add(transitionRoutineBegin());
flowScheduler.add(transitionRoutineEachFrame());
flowScheduler.add(transitionRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(halfwayRoutineBegin());
flowScheduler.add(halfwayRoutineEachFrame());
flowScheduler.add(halfwayRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);



flowScheduler.add(ethnicity_checkRoutineBegin());
flowScheduler.add(ethnicity_checkRoutineEachFrame());
flowScheduler.add(ethnicity_checkRoutineEnd());
flowScheduler.add(race_checkRoutineBegin());
flowScheduler.add(race_checkRoutineEachFrame());
flowScheduler.add(race_checkRoutineEnd());
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'loop3.xlsx', 'path': 'loop3.xlsx'},
    {'name': 'stimuli/b01.bmp', 'path': 'stimuli/b01.bmp'},
    {'name': 'stimuli/g1.bmp', 'path': 'stimuli/g1.bmp'},
    {'name': 'stimuli/g2.bmp', 'path': 'stimuli/g2.bmp'},
    {'name': 'stimuli/t1.bmp', 'path': 'stimuli/t1.bmp'},
    {'name': 'stimuli/t2.bmp', 'path': 'stimuli/t2.bmp'},
    {'name': 'stimuli/w01.bmp', 'path': 'stimuli/w01.bmp'},
    {'name': 'loop2.xlsx', 'path': 'loop2.xlsx'},
    {'name': 'stimuli/b03.bmp', 'path': 'stimuli/b03.bmp'},
    {'name': 'stimuli/t1.bmp', 'path': 'stimuli/t1.bmp'},
    {'name': 'stimuli/b02.bmp', 'path': 'stimuli/b02.bmp'},
    {'name': 'stimuli/g2.bmp', 'path': 'stimuli/g2.bmp'},
    {'name': 'stimuli/b05.bmp', 'path': 'stimuli/b05.bmp'},
    {'name': 'stimuli/g6.bmp', 'path': 'stimuli/g6.bmp'},
    {'name': 'stimuli/w01.bmp', 'path': 'stimuli/w01.bmp'},
    {'name': 'stimuli/t2.bmp', 'path': 'stimuli/t2.bmp'},
    {'name': 'stimuli/g3.bmp', 'path': 'stimuli/g3.bmp'},
    {'name': 'stimuli/w02.bmp', 'path': 'stimuli/w02.bmp'},
    {'name': 'stimuli/w04.bmp', 'path': 'stimuli/w04.bmp'},
    {'name': 'stimuli/b06.bmp', 'path': 'stimuli/b06.bmp'},
    {'name': 'stimuli/t6.bmp', 'path': 'stimuli/t6.bmp'},
    {'name': 'stimuli/t3.bmp', 'path': 'stimuli/t3.bmp'},
    {'name': 'stimuli/b04.bmp', 'path': 'stimuli/b04.bmp'},
    {'name': 'stimuli/w05.bmp', 'path': 'stimuli/w05.bmp'},
    {'name': 'stimuli/b01.bmp', 'path': 'stimuli/b01.bmp'},
    {'name': 'stimuli/g5.bmp', 'path': 'stimuli/g5.bmp'},
    {'name': 'stimuli/g4.bmp', 'path': 'stimuli/g4.bmp'},
    {'name': 'stimuli/w06.bmp', 'path': 'stimuli/w06.bmp'},
    {'name': 'stimuli/t5.bmp', 'path': 'stimuli/t5.bmp'},
    {'name': 'stimuli/w03.bmp', 'path': 'stimuli/w03.bmp'},
    {'name': 'stimuli/g1.bmp', 'path': 'stimuli/g1.bmp'},
    {'name': 'stimuli/t4.bmp', 'path': 'stimuli/t4.bmp'},
    {'name': 'loop2.xlsx', 'path': 'loop2.xlsx'},
    {'name': 'stimuli/b03.bmp', 'path': 'stimuli/b03.bmp'},
    {'name': 'stimuli/t1.bmp', 'path': 'stimuli/t1.bmp'},
    {'name': 'stimuli/b02.bmp', 'path': 'stimuli/b02.bmp'},
    {'name': 'stimuli/g2.bmp', 'path': 'stimuli/g2.bmp'},
    {'name': 'stimuli/b05.bmp', 'path': 'stimuli/b05.bmp'},
    {'name': 'stimuli/g6.bmp', 'path': 'stimuli/g6.bmp'},
    {'name': 'stimuli/w01.bmp', 'path': 'stimuli/w01.bmp'},
    {'name': 'stimuli/t2.bmp', 'path': 'stimuli/t2.bmp'},
    {'name': 'stimuli/g3.bmp', 'path': 'stimuli/g3.bmp'},
    {'name': 'stimuli/w02.bmp', 'path': 'stimuli/w02.bmp'},
    {'name': 'stimuli/w04.bmp', 'path': 'stimuli/w04.bmp'},
    {'name': 'stimuli/b06.bmp', 'path': 'stimuli/b06.bmp'},
    {'name': 'stimuli/t6.bmp', 'path': 'stimuli/t6.bmp'},
    {'name': 'stimuli/t3.bmp', 'path': 'stimuli/t3.bmp'},
    {'name': 'stimuli/b04.bmp', 'path': 'stimuli/b04.bmp'},
    {'name': 'stimuli/w05.bmp', 'path': 'stimuli/w05.bmp'},
    {'name': 'stimuli/b01.bmp', 'path': 'stimuli/b01.bmp'},
    {'name': 'stimuli/g5.bmp', 'path': 'stimuli/g5.bmp'},
    {'name': 'stimuli/g4.bmp', 'path': 'stimuli/g4.bmp'},
    {'name': 'stimuli/w06.bmp', 'path': 'stimuli/w06.bmp'},
    {'name': 'stimuli/t5.bmp', 'path': 'stimuli/t5.bmp'},
    {'name': 'stimuli/w03.bmp', 'path': 'stimuli/w03.bmp'},
    {'name': 'stimuli/g1.bmp', 'path': 'stimuli/g1.bmp'},
    {'name': 'stimuli/t4.bmp', 'path': 'stimuli/t4.bmp'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'stimuli/Mask.bmp', 'path': 'stimuli/Mask.bmp'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.com/submissions/complete?cc=CE8VG5D0', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var welcome_msg;
var intro_key;
var consentClock;
var text_consent;
var press_space_consent;
var instruction1Clock;
var instruction_text;
var instruction_key;
var instruction2Clock;
var text_intruction2;
var instruction2_space;
var practice_readyClock;
var text_practice_ready;
var practice_ready_space;
var press_spaceClock;
var press_space_cont;
var press_space_remember;
var practice_trialClock;
var face_img_practice;
var object_img_practice;
var mask_practice;
var key_pract;
var too_slow_practice;
var too_slow_text_practice;
var transitionClock;
var transition_text;
var press_space_cont_2;
var trialClock;
var face_img;
var object_img;
var mask;
var key_resp;
var too_slow_resp;
var too_slow_text;
var halfwayClock;
var text_halfway;
var key_halfway;
var ethnicity_checkClock;
var text_ethnicity_check;
var key_resp_ethnicity;
var race_checkClock;
var text_race_check;
var key_resp_race_check;
var endClock;
var text;
var space_to_exit;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_msg',
    text: 'This experiment will take approximately 15 minutes to complete. This task is investigating object recognition under distracting conditions. \nYou will be asked to quickly identify objects while being distracted by other stimuli.\n\nPlease press SPACE when you are ready to begin.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  intro_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  text_consent = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_consent',
    text: '\nBy answering the following questions, you are participating in a study being performed by cognitive scientists in the Stanford Department of Psychology. If you have questions about this research, please contact us at stanfordpsych251@gmail.com. You must be at least 18 years old to participate. Your participation in this research is voluntary. You may decline to answer any or all of the following questions. You may decline further participation, at any time, without adverse consequences. Your anonymity is assured; the researchers who have requested your participation will not receive any personal information about you.\n\nPress SPACE to accept these conditions and continue to the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  press_space_consent = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction1"
  instruction1Clock = new util.Clock();
  instruction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text',
    text: 'In this study, you will see pairs of pictures flashed briefly on the screen. \nYou should do nothing in response to the first picture, which will always be a face. This face will signal that the second picture is about to be presented. \n\nYour task is to classify the second picture as either a gun or a toy. \n\nIf the second picture is a gun, press Q.\nIf the target picture is a toy, press P. \n\nAfter each trial, you will be asked to press the space bar to proceed.\n\nPress SPACE to continue with the instructions. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruction_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction2"
  instruction2Clock = new util.Clock();
  text_intruction2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_intruction2',
    text: 'You have to respond as quickly and accurately as you can. If you make a mistake, don\'t worry. Just keep going to the next trial. \n\nIf you take too long to respond, you will see this message:\n"Please respond faster!"\n\nIf you see this message, please try to press the keys faster. \n\nPress SPACE to continue with instructions',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruction2_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_ready"
  practice_readyClock = new util.Clock();
  text_practice_ready = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_practice_ready',
    text: 'The first round of pictures will be a series of practice trials. \n\nPlease place your fingers over the "Q" (TOY) and "P" (GUN) keys on the keyboard so that you are ready to register your responses. \n\nPlease click SPACE when you are ready to begin the practice trials.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  practice_ready_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "press_space"
  press_spaceClock = new util.Clock();
  press_space_cont = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  press_space_remember = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_space_remember',
    text: 'Q: TOY           REMEMBER!           P:GUN\n\n\n\n\nPress SPACE to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practice_trial"
  practice_trialClock = new util.Clock();
  face_img_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'face_img_practice', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  object_img_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'object_img_practice', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mask_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_practice', units : undefined, 
    image : 'stimuli/Mask.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_pract = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  too_slow_practice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  too_slow_text_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'too_slow_text_practice',
    text: 'Please respond more quickly!\n\nPress SPACE to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "transition"
  transitionClock = new util.Clock();
  transition_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'transition_text',
    text: 'Well done!\n\nNow we will begin with the actual trials. Feel free to take breaks in between trials if you want. If you do not take breaks, the whole experiment should take around 10 minutes. \n\nGood luck!\n\nPress SPACE to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  press_space_cont_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  face_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'face_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  object_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'object_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mask = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask', units : undefined, 
    image : 'stimuli/Mask.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  too_slow_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  too_slow_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'too_slow_text',
    text: 'Please respond more quickly!\n\nPress SPACE to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "halfway"
  halfwayClock = new util.Clock();
  text_halfway = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_halfway',
    text: 'You are halfway through the experiment! \n\nFeel free to take a short break if you want.\n\nPress SPACE when you are ready to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_halfway = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ethnicity_check"
  ethnicity_checkClock = new util.Clock();
  text_ethnicity_check = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_ethnicity_check',
    text: 'Before we finalize, we would like to know some additional information about you. This information will NOT affect your payment through Prolific. \n\nDo you identify as Hispanic or Latinx?\n\nY: YES\nN: NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_ethnicity = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "race_check"
  race_checkClock = new util.Clock();
  text_race_check = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_race_check',
    text: 'How would you describe your race?\n\nW: White or Caucasian\nB: Black or African American\nN: American Indian or Alaska Native\nA: Asian\nP: Native Hawaiian or Other Pacific Islander \nO: Other or Mixed',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_race_check = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'This is the end of the experiment. \n\nThis study examines the effect of facial priming with categorization of threatening and nonthreatening objects. Please do not to share this information with any other potential participants.\n\nThank you for your participation! \nPress SPACE to exit. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_to_exit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _intro_key_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    intro_key.keys = undefined;
    intro_key.rt = undefined;
    _intro_key_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_msg);
    welcomeComponents.push(intro_key);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_msg* updates
    if (t >= 0.0 && welcome_msg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_msg.tStart = t;  // (not accounting for frame time here)
      welcome_msg.frameNStart = frameN;  // exact frame index
      
      welcome_msg.setAutoDraw(true);
    }
    
    
    // *intro_key* updates
    if (t >= 2 && intro_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_key.tStart = t;  // (not accounting for frame time here)
      intro_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_key.clearEvents(); });
    }
    
    if (intro_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_key.getKeys({keyList: ['space'], waitRelease: false});
      _intro_key_allKeys = _intro_key_allKeys.concat(theseKeys);
      if (_intro_key_allKeys.length > 0) {
        intro_key.keys = _intro_key_allKeys[_intro_key_allKeys.length - 1].name;  // just the last key pressed
        intro_key.rt = _intro_key_allKeys[_intro_key_allKeys.length - 1].rt;
        intro_key.duration = _intro_key_allKeys[_intro_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(intro_key.corr, level);
    }
    psychoJS.experiment.addData('intro_key.keys', intro_key.keys);
    if (typeof intro_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('intro_key.rt', intro_key.rt);
        psychoJS.experiment.addData('intro_key.duration', intro_key.duration);
        routineTimer.reset();
        }
    
    intro_key.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _press_space_consent_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('consent.started', globalClock.getTime());
    press_space_consent.keys = undefined;
    press_space_consent.rt = undefined;
    _press_space_consent_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(text_consent);
    consentComponents.push(press_space_consent);
    
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_consent* updates
    if (t >= 0.0 && text_consent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_consent.tStart = t;  // (not accounting for frame time here)
      text_consent.frameNStart = frameN;  // exact frame index
      
      text_consent.setAutoDraw(true);
    }
    
    
    // *press_space_consent* updates
    if (t >= 0.0 && press_space_consent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_consent.tStart = t;  // (not accounting for frame time here)
      press_space_consent.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { press_space_consent.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { press_space_consent.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { press_space_consent.clearEvents(); });
    }
    
    if (press_space_consent.status === PsychoJS.Status.STARTED) {
      let theseKeys = press_space_consent.getKeys({keyList: ['space'], waitRelease: false});
      _press_space_consent_allKeys = _press_space_consent_allKeys.concat(theseKeys);
      if (_press_space_consent_allKeys.length > 0) {
        press_space_consent.keys = _press_space_consent_allKeys[_press_space_consent_allKeys.length - 1].name;  // just the last key pressed
        press_space_consent.rt = _press_space_consent_allKeys[_press_space_consent_allKeys.length - 1].rt;
        press_space_consent.duration = _press_space_consent_allKeys[_press_space_consent_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    for (const thisComponent of consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('consent.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(press_space_consent.corr, level);
    }
    psychoJS.experiment.addData('press_space_consent.keys', press_space_consent.keys);
    if (typeof press_space_consent.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('press_space_consent.rt', press_space_consent.rt);
        psychoJS.experiment.addData('press_space_consent.duration', press_space_consent.duration);
        routineTimer.reset();
        }
    
    press_space_consent.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _instruction_key_allKeys;
var instruction1Components;
function instruction1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction1' ---
    t = 0;
    instruction1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instruction1.started', globalClock.getTime());
    instruction_key.keys = undefined;
    instruction_key.rt = undefined;
    _instruction_key_allKeys = [];
    // keep track of which components have finished
    instruction1Components = [];
    instruction1Components.push(instruction_text);
    instruction1Components.push(instruction_key);
    
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction1' ---
    // get current time
    t = instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text* updates
    if (t >= 0.0 && instruction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text.tStart = t;  // (not accounting for frame time here)
      instruction_text.frameNStart = frameN;  // exact frame index
      
      instruction_text.setAutoDraw(true);
    }
    
    
    // *instruction_key* updates
    if (t >= 2 && instruction_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_key.tStart = t;  // (not accounting for frame time here)
      instruction_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction_key.clearEvents(); });
    }
    
    if (instruction_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction_key.getKeys({keyList: ['space'], waitRelease: false});
      _instruction_key_allKeys = _instruction_key_allKeys.concat(theseKeys);
      if (_instruction_key_allKeys.length > 0) {
        instruction_key.keys = _instruction_key_allKeys[_instruction_key_allKeys.length - 1].name;  // just the last key pressed
        instruction_key.rt = _instruction_key_allKeys[_instruction_key_allKeys.length - 1].rt;
        instruction_key.duration = _instruction_key_allKeys[_instruction_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction1' ---
    for (const thisComponent of instruction1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruction_key.corr, level);
    }
    psychoJS.experiment.addData('instruction_key.keys', instruction_key.keys);
    if (typeof instruction_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction_key.rt', instruction_key.rt);
        psychoJS.experiment.addData('instruction_key.duration', instruction_key.duration);
        routineTimer.reset();
        }
    
    instruction_key.stop();
    // the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _instruction2_space_allKeys;
var instruction2Components;
function instruction2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction2' ---
    t = 0;
    instruction2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instruction2.started', globalClock.getTime());
    instruction2_space.keys = undefined;
    instruction2_space.rt = undefined;
    _instruction2_space_allKeys = [];
    // keep track of which components have finished
    instruction2Components = [];
    instruction2Components.push(text_intruction2);
    instruction2Components.push(instruction2_space);
    
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction2' ---
    // get current time
    t = instruction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_intruction2* updates
    if (t >= 0.0 && text_intruction2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_intruction2.tStart = t;  // (not accounting for frame time here)
      text_intruction2.frameNStart = frameN;  // exact frame index
      
      text_intruction2.setAutoDraw(true);
    }
    
    
    // *instruction2_space* updates
    if (t >= 2 && instruction2_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction2_space.tStart = t;  // (not accounting for frame time here)
      instruction2_space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction2_space.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction2_space.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction2_space.clearEvents(); });
    }
    
    if (instruction2_space.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction2_space.getKeys({keyList: ['space'], waitRelease: false});
      _instruction2_space_allKeys = _instruction2_space_allKeys.concat(theseKeys);
      if (_instruction2_space_allKeys.length > 0) {
        instruction2_space.keys = _instruction2_space_allKeys[_instruction2_space_allKeys.length - 1].name;  // just the last key pressed
        instruction2_space.rt = _instruction2_space_allKeys[_instruction2_space_allKeys.length - 1].rt;
        instruction2_space.duration = _instruction2_space_allKeys[_instruction2_space_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction2' ---
    for (const thisComponent of instruction2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruction2_space.corr, level);
    }
    psychoJS.experiment.addData('instruction2_space.keys', instruction2_space.keys);
    if (typeof instruction2_space.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction2_space.rt', instruction2_space.rt);
        psychoJS.experiment.addData('instruction2_space.duration', instruction2_space.duration);
        routineTimer.reset();
        }
    
    instruction2_space.stop();
    // the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _practice_ready_space_allKeys;
var practice_readyComponents;
function practice_readyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_ready' ---
    t = 0;
    practice_readyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_ready.started', globalClock.getTime());
    practice_ready_space.keys = undefined;
    practice_ready_space.rt = undefined;
    _practice_ready_space_allKeys = [];
    // keep track of which components have finished
    practice_readyComponents = [];
    practice_readyComponents.push(text_practice_ready);
    practice_readyComponents.push(practice_ready_space);
    
    for (const thisComponent of practice_readyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_readyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_ready' ---
    // get current time
    t = practice_readyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_practice_ready* updates
    if (t >= 0.0 && text_practice_ready.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_practice_ready.tStart = t;  // (not accounting for frame time here)
      text_practice_ready.frameNStart = frameN;  // exact frame index
      
      text_practice_ready.setAutoDraw(true);
    }
    
    
    // *practice_ready_space* updates
    if (t >= 0.0 && practice_ready_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_ready_space.tStart = t;  // (not accounting for frame time here)
      practice_ready_space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_ready_space.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_ready_space.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_ready_space.clearEvents(); });
    }
    
    if (practice_ready_space.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_ready_space.getKeys({keyList: ['space'], waitRelease: false});
      _practice_ready_space_allKeys = _practice_ready_space_allKeys.concat(theseKeys);
      if (_practice_ready_space_allKeys.length > 0) {
        practice_ready_space.keys = _practice_ready_space_allKeys[_practice_ready_space_allKeys.length - 1].name;  // just the last key pressed
        practice_ready_space.rt = _practice_ready_space_allKeys[_practice_ready_space_allKeys.length - 1].rt;
        practice_ready_space.duration = _practice_ready_space_allKeys[_practice_ready_space_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_readyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_readyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_ready' ---
    for (const thisComponent of practice_readyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_ready.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_ready_space.corr, level);
    }
    psychoJS.experiment.addData('practice_ready_space.keys', practice_ready_space.keys);
    if (typeof practice_ready_space.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_ready_space.rt', practice_ready_space.rt);
        psychoJS.experiment.addData('practice_ready_space.duration', practice_ready_space.duration);
        routineTimer.reset();
        }
    
    practice_ready_space.stop();
    // the Routine "practice_ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'loop3.xlsx',
      seed: undefined, name: 'practice_trials'
    });
    psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
    currentLoop = practice_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_trial of practice_trials) {
      snapshot = practice_trials.getSnapshot();
      practice_trialsLoopScheduler.add(importConditions(snapshot));
      practice_trialsLoopScheduler.add(press_spaceRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(press_spaceRoutineEachFrame());
      practice_trialsLoopScheduler.add(press_spaceRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(practice_trialRoutineEachFrame());
      practice_trialsLoopScheduler.add(practice_trialRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialsLoopEndIteration(practice_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'loop2.xlsx', '0:72'),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(press_spaceRoutineBegin(snapshot));
      trialsLoopScheduler.add(press_spaceRoutineEachFrame());
      trialsLoopScheduler.add(press_spaceRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'loop2.xlsx', '73:144'),
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(press_spaceRoutineBegin(snapshot));
      trials_2LoopScheduler.add(press_spaceRoutineEachFrame());
      trials_2LoopScheduler.add(press_spaceRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _press_space_cont_allKeys;
var press_spaceComponents;
function press_spaceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'press_space' ---
    t = 0;
    press_spaceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('press_space.started', globalClock.getTime());
    press_space_cont.keys = undefined;
    press_space_cont.rt = undefined;
    _press_space_cont_allKeys = [];
    // keep track of which components have finished
    press_spaceComponents = [];
    press_spaceComponents.push(press_space_cont);
    press_spaceComponents.push(press_space_remember);
    
    for (const thisComponent of press_spaceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function press_spaceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'press_space' ---
    // get current time
    t = press_spaceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *press_space_cont* updates
    if (t >= 0.0 && press_space_cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_cont.tStart = t;  // (not accounting for frame time here)
      press_space_cont.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { press_space_cont.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { press_space_cont.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { press_space_cont.clearEvents(); });
    }
    
    if (press_space_cont.status === PsychoJS.Status.STARTED) {
      let theseKeys = press_space_cont.getKeys({keyList: ['space'], waitRelease: false});
      _press_space_cont_allKeys = _press_space_cont_allKeys.concat(theseKeys);
      if (_press_space_cont_allKeys.length > 0) {
        press_space_cont.keys = _press_space_cont_allKeys[_press_space_cont_allKeys.length - 1].name;  // just the last key pressed
        press_space_cont.rt = _press_space_cont_allKeys[_press_space_cont_allKeys.length - 1].rt;
        press_space_cont.duration = _press_space_cont_allKeys[_press_space_cont_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *press_space_remember* updates
    if (t >= 0.0 && press_space_remember.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_remember.tStart = t;  // (not accounting for frame time here)
      press_space_remember.frameNStart = frameN;  // exact frame index
      
      press_space_remember.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of press_spaceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function press_spaceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'press_space' ---
    for (const thisComponent of press_spaceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('press_space.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(press_space_cont.corr, level);
    }
    psychoJS.experiment.addData('press_space_cont.keys', press_space_cont.keys);
    if (typeof press_space_cont.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('press_space_cont.rt', press_space_cont.rt);
        psychoJS.experiment.addData('press_space_cont.duration', press_space_cont.duration);
        routineTimer.reset();
        }
    
    press_space_cont.stop();
    // the Routine "press_space" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_pract_allKeys;
var _too_slow_practice_allKeys;
var practice_trialComponents;
function practice_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_trial' ---
    t = 0;
    practice_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_trial.started', globalClock.getTime());
    face_img_practice.setImage(face);
    object_img_practice.setImage(object);
    key_pract.keys = undefined;
    key_pract.rt = undefined;
    _key_pract_allKeys = [];
    too_slow_practice.keys = undefined;
    too_slow_practice.rt = undefined;
    _too_slow_practice_allKeys = [];
    // keep track of which components have finished
    practice_trialComponents = [];
    practice_trialComponents.push(face_img_practice);
    practice_trialComponents.push(object_img_practice);
    practice_trialComponents.push(mask_practice);
    practice_trialComponents.push(key_pract);
    practice_trialComponents.push(too_slow_practice);
    practice_trialComponents.push(too_slow_text_practice);
    
    for (const thisComponent of practice_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practice_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_trial' ---
    // get current time
    t = practice_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *face_img_practice* updates
    if (t >= 0.0 && face_img_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      face_img_practice.tStart = t;  // (not accounting for frame time here)
      face_img_practice.frameNStart = frameN;  // exact frame index
      
      face_img_practice.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (face_img_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      face_img_practice.setAutoDraw(false);
    }
    
    // *object_img_practice* updates
    if (t >= 0.2 && object_img_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      object_img_practice.tStart = t;  // (not accounting for frame time here)
      object_img_practice.frameNStart = frameN;  // exact frame index
      
      object_img_practice.setAutoDraw(true);
    }
    
    frameRemains = 0.2 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (object_img_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      object_img_practice.setAutoDraw(false);
    }
    
    // *mask_practice* updates
    if (t >= 0.4 && mask_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_practice.tStart = t;  // (not accounting for frame time here)
      mask_practice.frameNStart = frameN;  // exact frame index
      
      mask_practice.setAutoDraw(true);
    }
    
    frameRemains = 0.4 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mask_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mask_practice.setAutoDraw(false);
    }
    
    // *key_pract* updates
    if (t >= 0.4 && key_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_pract.tStart = t;  // (not accounting for frame time here)
      key_pract.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_pract.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_pract.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_pract.clearEvents(); });
    }
    
    frameRemains = 0.4 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_pract.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_pract.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_pract.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_pract.getKeys({keyList: ['q', 'p'], waitRelease: false});
      _key_pract_allKeys = _key_pract_allKeys.concat(theseKeys);
      if (_key_pract_allKeys.length > 0) {
        key_pract.keys = _key_pract_allKeys[_key_pract_allKeys.length - 1].name;  // just the last key pressed
        key_pract.rt = _key_pract_allKeys[_key_pract_allKeys.length - 1].rt;
        key_pract.duration = _key_pract_allKeys[_key_pract_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *too_slow_practice* updates
    if (t >= 0.9 && too_slow_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      too_slow_practice.tStart = t;  // (not accounting for frame time here)
      too_slow_practice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { too_slow_practice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { too_slow_practice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { too_slow_practice.clearEvents(); });
    }
    
    if (too_slow_practice.status === PsychoJS.Status.STARTED) {
      let theseKeys = too_slow_practice.getKeys({keyList: ['space'], waitRelease: false});
      _too_slow_practice_allKeys = _too_slow_practice_allKeys.concat(theseKeys);
      if (_too_slow_practice_allKeys.length > 0) {
        too_slow_practice.keys = _too_slow_practice_allKeys[_too_slow_practice_allKeys.length - 1].name;  // just the last key pressed
        too_slow_practice.rt = _too_slow_practice_allKeys[_too_slow_practice_allKeys.length - 1].rt;
        too_slow_practice.duration = _too_slow_practice_allKeys[_too_slow_practice_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *too_slow_text_practice* updates
    if (t >= 0.9 && too_slow_text_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      too_slow_text_practice.tStart = t;  // (not accounting for frame time here)
      too_slow_text_practice.frameNStart = frameN;  // exact frame index
      
      too_slow_text_practice.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_trial' ---
    for (const thisComponent of practice_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_trial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_pract.corr, level);
    }
    psychoJS.experiment.addData('key_pract.keys', key_pract.keys);
    if (typeof key_pract.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_pract.rt', key_pract.rt);
        psychoJS.experiment.addData('key_pract.duration', key_pract.duration);
        routineTimer.reset();
        }
    
    key_pract.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(too_slow_practice.corr, level);
    }
    psychoJS.experiment.addData('too_slow_practice.keys', too_slow_practice.keys);
    if (typeof too_slow_practice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('too_slow_practice.rt', too_slow_practice.rt);
        psychoJS.experiment.addData('too_slow_practice.duration', too_slow_practice.duration);
        routineTimer.reset();
        }
    
    too_slow_practice.stop();
    // the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _press_space_cont_2_allKeys;
var transitionComponents;
function transitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transition' ---
    t = 0;
    transitionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('transition.started', globalClock.getTime());
    press_space_cont_2.keys = undefined;
    press_space_cont_2.rt = undefined;
    _press_space_cont_2_allKeys = [];
    // keep track of which components have finished
    transitionComponents = [];
    transitionComponents.push(transition_text);
    transitionComponents.push(press_space_cont_2);
    
    for (const thisComponent of transitionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function transitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transition' ---
    // get current time
    t = transitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transition_text* updates
    if (t >= 0.0 && transition_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transition_text.tStart = t;  // (not accounting for frame time here)
      transition_text.frameNStart = frameN;  // exact frame index
      
      transition_text.setAutoDraw(true);
    }
    
    
    // *press_space_cont_2* updates
    if (t >= 3.0 && press_space_cont_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_space_cont_2.tStart = t;  // (not accounting for frame time here)
      press_space_cont_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { press_space_cont_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { press_space_cont_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { press_space_cont_2.clearEvents(); });
    }
    
    if (press_space_cont_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = press_space_cont_2.getKeys({keyList: ['space'], waitRelease: false});
      _press_space_cont_2_allKeys = _press_space_cont_2_allKeys.concat(theseKeys);
      if (_press_space_cont_2_allKeys.length > 0) {
        press_space_cont_2.keys = _press_space_cont_2_allKeys[_press_space_cont_2_allKeys.length - 1].name;  // just the last key pressed
        press_space_cont_2.rt = _press_space_cont_2_allKeys[_press_space_cont_2_allKeys.length - 1].rt;
        press_space_cont_2.duration = _press_space_cont_2_allKeys[_press_space_cont_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of transitionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function transitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transition' ---
    for (const thisComponent of transitionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transition.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(press_space_cont_2.corr, level);
    }
    psychoJS.experiment.addData('press_space_cont_2.keys', press_space_cont_2.keys);
    if (typeof press_space_cont_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('press_space_cont_2.rt', press_space_cont_2.rt);
        psychoJS.experiment.addData('press_space_cont_2.duration', press_space_cont_2.duration);
        routineTimer.reset();
        }
    
    press_space_cont_2.stop();
    // the Routine "transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var _too_slow_resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    face_img.setImage(face);
    object_img.setImage(object);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    too_slow_resp.keys = undefined;
    too_slow_resp.rt = undefined;
    _too_slow_resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(face_img);
    trialComponents.push(object_img);
    trialComponents.push(mask);
    trialComponents.push(key_resp);
    trialComponents.push(too_slow_resp);
    trialComponents.push(too_slow_text);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *face_img* updates
    if (t >= 0.0 && face_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      face_img.tStart = t;  // (not accounting for frame time here)
      face_img.frameNStart = frameN;  // exact frame index
      
      face_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (face_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      face_img.setAutoDraw(false);
    }
    
    // *object_img* updates
    if (t >= 0.2 && object_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      object_img.tStart = t;  // (not accounting for frame time here)
      object_img.frameNStart = frameN;  // exact frame index
      
      object_img.setAutoDraw(true);
    }
    
    frameRemains = 0.2 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (object_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      object_img.setAutoDraw(false);
    }
    
    // *mask* updates
    if (t >= 0.4 && mask.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask.tStart = t;  // (not accounting for frame time here)
      mask.frameNStart = frameN;  // exact frame index
      
      mask.setAutoDraw(true);
    }
    
    frameRemains = 0.4 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mask.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mask.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.4 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    frameRemains = 0.4 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['q', 'p'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *too_slow_resp* updates
    if (t >= 0.9 && too_slow_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      too_slow_resp.tStart = t;  // (not accounting for frame time here)
      too_slow_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { too_slow_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { too_slow_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { too_slow_resp.clearEvents(); });
    }
    
    if (too_slow_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = too_slow_resp.getKeys({keyList: ['space'], waitRelease: false});
      _too_slow_resp_allKeys = _too_slow_resp_allKeys.concat(theseKeys);
      if (_too_slow_resp_allKeys.length > 0) {
        too_slow_resp.keys = _too_slow_resp_allKeys[_too_slow_resp_allKeys.length - 1].name;  // just the last key pressed
        too_slow_resp.rt = _too_slow_resp_allKeys[_too_slow_resp_allKeys.length - 1].rt;
        too_slow_resp.duration = _too_slow_resp_allKeys[_too_slow_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *too_slow_text* updates
    if (t >= 0.9 && too_slow_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      too_slow_text.tStart = t;  // (not accounting for frame time here)
      too_slow_text.frameNStart = frameN;  // exact frame index
      
      too_slow_text.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(too_slow_resp.corr, level);
    }
    psychoJS.experiment.addData('too_slow_resp.keys', too_slow_resp.keys);
    if (typeof too_slow_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('too_slow_resp.rt', too_slow_resp.rt);
        psychoJS.experiment.addData('too_slow_resp.duration', too_slow_resp.duration);
        routineTimer.reset();
        }
    
    too_slow_resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_halfway_allKeys;
var halfwayComponents;
function halfwayRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'halfway' ---
    t = 0;
    halfwayClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('halfway.started', globalClock.getTime());
    key_halfway.keys = undefined;
    key_halfway.rt = undefined;
    _key_halfway_allKeys = [];
    // keep track of which components have finished
    halfwayComponents = [];
    halfwayComponents.push(text_halfway);
    halfwayComponents.push(key_halfway);
    
    for (const thisComponent of halfwayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function halfwayRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'halfway' ---
    // get current time
    t = halfwayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_halfway* updates
    if (t >= 0.0 && text_halfway.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_halfway.tStart = t;  // (not accounting for frame time here)
      text_halfway.frameNStart = frameN;  // exact frame index
      
      text_halfway.setAutoDraw(true);
    }
    
    
    // *key_halfway* updates
    if (t >= 3 && key_halfway.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_halfway.tStart = t;  // (not accounting for frame time here)
      key_halfway.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_halfway.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_halfway.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_halfway.clearEvents(); });
    }
    
    if (key_halfway.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_halfway.getKeys({keyList: ['space'], waitRelease: false});
      _key_halfway_allKeys = _key_halfway_allKeys.concat(theseKeys);
      if (_key_halfway_allKeys.length > 0) {
        key_halfway.keys = _key_halfway_allKeys[_key_halfway_allKeys.length - 1].name;  // just the last key pressed
        key_halfway.rt = _key_halfway_allKeys[_key_halfway_allKeys.length - 1].rt;
        key_halfway.duration = _key_halfway_allKeys[_key_halfway_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of halfwayComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function halfwayRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'halfway' ---
    for (const thisComponent of halfwayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('halfway.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_halfway.corr, level);
    }
    psychoJS.experiment.addData('key_halfway.keys', key_halfway.keys);
    if (typeof key_halfway.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_halfway.rt', key_halfway.rt);
        psychoJS.experiment.addData('key_halfway.duration', key_halfway.duration);
        routineTimer.reset();
        }
    
    key_halfway.stop();
    // the Routine "halfway" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_ethnicity_allKeys;
var ethnicity_checkComponents;
function ethnicity_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ethnicity_check' ---
    t = 0;
    ethnicity_checkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ethnicity_check.started', globalClock.getTime());
    key_resp_ethnicity.keys = undefined;
    key_resp_ethnicity.rt = undefined;
    _key_resp_ethnicity_allKeys = [];
    // keep track of which components have finished
    ethnicity_checkComponents = [];
    ethnicity_checkComponents.push(text_ethnicity_check);
    ethnicity_checkComponents.push(key_resp_ethnicity);
    
    for (const thisComponent of ethnicity_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ethnicity_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ethnicity_check' ---
    // get current time
    t = ethnicity_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_ethnicity_check* updates
    if (t >= 0.0 && text_ethnicity_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_ethnicity_check.tStart = t;  // (not accounting for frame time here)
      text_ethnicity_check.frameNStart = frameN;  // exact frame index
      
      text_ethnicity_check.setAutoDraw(true);
    }
    
    
    // *key_resp_ethnicity* updates
    if (t >= 0.0 && key_resp_ethnicity.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_ethnicity.tStart = t;  // (not accounting for frame time here)
      key_resp_ethnicity.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_ethnicity.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_ethnicity.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_ethnicity.clearEvents(); });
    }
    
    if (key_resp_ethnicity.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_ethnicity.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_ethnicity_allKeys = _key_resp_ethnicity_allKeys.concat(theseKeys);
      if (_key_resp_ethnicity_allKeys.length > 0) {
        key_resp_ethnicity.keys = _key_resp_ethnicity_allKeys[_key_resp_ethnicity_allKeys.length - 1].name;  // just the last key pressed
        key_resp_ethnicity.rt = _key_resp_ethnicity_allKeys[_key_resp_ethnicity_allKeys.length - 1].rt;
        key_resp_ethnicity.duration = _key_resp_ethnicity_allKeys[_key_resp_ethnicity_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ethnicity_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ethnicity_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ethnicity_check' ---
    for (const thisComponent of ethnicity_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ethnicity_check.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_ethnicity.corr, level);
    }
    psychoJS.experiment.addData('key_resp_ethnicity.keys', key_resp_ethnicity.keys);
    if (typeof key_resp_ethnicity.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_ethnicity.rt', key_resp_ethnicity.rt);
        psychoJS.experiment.addData('key_resp_ethnicity.duration', key_resp_ethnicity.duration);
        routineTimer.reset();
        }
    
    key_resp_ethnicity.stop();
    // the Routine "ethnicity_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_race_check_allKeys;
var race_checkComponents;
function race_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'race_check' ---
    t = 0;
    race_checkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('race_check.started', globalClock.getTime());
    key_resp_race_check.keys = undefined;
    key_resp_race_check.rt = undefined;
    _key_resp_race_check_allKeys = [];
    // keep track of which components have finished
    race_checkComponents = [];
    race_checkComponents.push(text_race_check);
    race_checkComponents.push(key_resp_race_check);
    
    for (const thisComponent of race_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function race_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'race_check' ---
    // get current time
    t = race_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_race_check* updates
    if (t >= 0.0 && text_race_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_race_check.tStart = t;  // (not accounting for frame time here)
      text_race_check.frameNStart = frameN;  // exact frame index
      
      text_race_check.setAutoDraw(true);
    }
    
    
    // *key_resp_race_check* updates
    if (t >= 0.0 && key_resp_race_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_race_check.tStart = t;  // (not accounting for frame time here)
      key_resp_race_check.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_race_check.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_race_check.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_race_check.clearEvents(); });
    }
    
    if (key_resp_race_check.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_race_check.getKeys({keyList: ['w', 'b', 'n', 'a', 'p', 'o'], waitRelease: false});
      _key_resp_race_check_allKeys = _key_resp_race_check_allKeys.concat(theseKeys);
      if (_key_resp_race_check_allKeys.length > 0) {
        key_resp_race_check.keys = _key_resp_race_check_allKeys[_key_resp_race_check_allKeys.length - 1].name;  // just the last key pressed
        key_resp_race_check.rt = _key_resp_race_check_allKeys[_key_resp_race_check_allKeys.length - 1].rt;
        key_resp_race_check.duration = _key_resp_race_check_allKeys[_key_resp_race_check_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of race_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function race_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'race_check' ---
    for (const thisComponent of race_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('race_check.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_race_check.corr, level);
    }
    psychoJS.experiment.addData('key_resp_race_check.keys', key_resp_race_check.keys);
    if (typeof key_resp_race_check.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_race_check.rt', key_resp_race_check.rt);
        psychoJS.experiment.addData('key_resp_race_check.duration', key_resp_race_check.duration);
        routineTimer.reset();
        }
    
    key_resp_race_check.stop();
    // the Routine "race_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_to_exit_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    space_to_exit.keys = undefined;
    space_to_exit.rt = undefined;
    _space_to_exit_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text);
    endComponents.push(space_to_exit);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *space_to_exit* updates
    if (t >= 0.0 && space_to_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_exit.tStart = t;  // (not accounting for frame time here)
      space_to_exit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_to_exit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_to_exit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_to_exit.clearEvents(); });
    }
    
    if (space_to_exit.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_exit.getKeys({keyList: ['space'], waitRelease: false});
      _space_to_exit_allKeys = _space_to_exit_allKeys.concat(theseKeys);
      if (_space_to_exit_allKeys.length > 0) {
        space_to_exit.keys = _space_to_exit_allKeys[_space_to_exit_allKeys.length - 1].name;  // just the last key pressed
        space_to_exit.rt = _space_to_exit_allKeys[_space_to_exit_allKeys.length - 1].rt;
        space_to_exit.duration = _space_to_exit_allKeys[_space_to_exit_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_to_exit.corr, level);
    }
    psychoJS.experiment.addData('space_to_exit.keys', space_to_exit.keys);
    if (typeof space_to_exit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_to_exit.rt', space_to_exit.rt);
        psychoJS.experiment.addData('space_to_exit.duration', space_to_exit.duration);
        routineTimer.reset();
        }
    
    space_to_exit.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
