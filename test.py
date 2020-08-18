from tkinter import*
import sys
import os
import predict
def open_window():
    top=Toplevel()
    top.title("app 1st ui")
    top.geometry("900x600+120+120")
    
    button1=Button(top, text="close",command=top.destroy)
    button1.pack()
    button2=Button(top, text="health",command=open_window2)
    button2.pack()
def open_window2():
    top=Toplevel()
    top.title("choose")
    top.geometry("900x600+120+120")
    button1=Button(top, text="Survival",command=open_window3)
    button1.pack()
    button4=Button(top,text="disease prediction",command=diseaseprediction)
    button4.pack()

    
def open_window3():
    top=Toplevel()
    top.title("list of common diseases")
    top.geometry("900x600+120+120")
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button2=Button(top,text="Start fire",command=fire)
    button2.pack()
    button3=Button(top,text="Self Defense",command=defense)
    button3.pack()
    button4=Button(top,text="Surviving Wildlife Encounters",command=wildlife)
    button4.pack()
    button5=Button(top,text="Poisning",command=poison)
    button5.pack()
    button6=Button(top,text="How to Survive a Wildfire",command=survive)
    button6.pack()
    button7=Button(top,text="How to Survive in tropical Island ",command=island)
    button7.pack()
    button8=Button(top,text="Survival Rule of 3",command=rule3)
    button8.pack()
    
def drug():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""Signs of depressant drug overdose - Not all may be present
 
Opioids, benzodiazepines and alcohol are all depressants, which means they slow the central nervous system, including breathing and heart rate. Too much of any one of these substances on their own or in combination can kill or cause permanent brain damage. (e.g. heroin, morphine, oxycodone, fentanyl, methadone) include:
 
shallow breathing or not breathing at all
snoring or gurgling sounds (this can mean that a person’s airway is partly blocked)
blue lips or fingertips
floppy arms and legs
unrousable (can’t be woken up) unconsciousness
pale, cold and clammy skin
nausea or vomiting
seizures
abdominal pain
evidence of poisons, containers, smells, etc
 
DO NOT
Things you shouldn't do when tending to someone who has overdosed:
 
Do NOT put your own safety in danger. Some drugs can cause violent and unpredictable behavior. Call for medical help.
Do NOT try to reason with someone who is on drugs.
Do not expect them to behave reasonably.
Do NOT offer your opinions when giving help. You don't need to know why drugs were taken in order to give effective first aid.
How you can help
Assess the patient
 
Check the level of consciousness. If the patient is not fully conscious and alert, turn them onto their side and ensure they are not left alone.
 
Reassure the patient calmly
 
Talk to the patient in a quiet and reassuring manner.
Sometimes patients may become agitated. Enlist friends or family to calm and reassure the patient. Consider calling the police if the safety of the patient or others becomes threatened.
 
 Identify the drug taken if you can
 
Ask what the patient has taken, how muchit was taken, when it was taken, and whether it was swallowed, inhaled or injected.
Look for evidence that might assist the hospital staff with treatment and keep any container, syringe or needle and any vomit to aid analysis and identification.
 
Do Not let victim sleep off Call 911 (your local emergency professionals)
 
If you can't reach try to transport victim to near by hospital
 
Call Poison control
 
seeks and follow their assistance until emergency crew arrives
 
Untill Emergency Arrives
 

 
If personis not breathing and has no pulse? perform CPR
If the person not breathing, but has a pulse? Perform Rescue Breathing (CPR)
If the patient is not fully conscious and alert, turn them onto their side and ensure they are not left alone.
Some drugs create serious overheating of the body, and if this is noticed, remove unnecessary clothing to allow air to reach the skin surface to assist with cooling.""")
    text.pack()
def fire():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""How to Start Fire without matches or lighter


Friction Based

You can use a bow drill to start a fire. Make a bow and blunt Arrow (drill). instead of shooting the arrow you twist the arrow in chord and place hard object on top end of the arrow and at bottom placed soft wood etc. now go side by side with bow so the chord makes the drill rotate thus creating friction on the wood which will cause to start fire. Use some dry sticks/tinder/char cloth etc to help catch fire fast.

Similar to bow drill you could instead just use a softwood and hardwood preferably and just scrape the softwood on top of hardwood back and forth untill u see spark/fire again place dry sticks/tinder/char cloth etc to help catch fire fast.


Sunlight

Magnifying Glass

Use Magnifying Glass to direct wider sunlight beam to more condense focused beam thatfocus on very tight spot on dry sticks/tinder/char cloth/paper etc to help catch fire fast. once the sunlight (photons) pass and concentrate on the lense the energy that falls in smae place concentrates enough heat to start fire.

Plastic bag or a condom

Similarly you can use a transparent plastic bag or a condom and fill water in it and let the sunlight pass like you would use a magnifying glass.

You could actually use this smae prinicple to start fire using ice.

Soda Can

Use the bottom part of soda can, make sure it is super clean as close as possible to a mirror in order for it to reflect sunlight. In this process instead of passing sunlight through like in magnifying glass you let it reflect in to one tight spot on tinder like paper/dry stick/wood chips etc to catch fire.

 


Chemical and Physics

Fferrocerium rod, Magnesium rod with steel scraper. Scrape magensium rod to get some tinder than. Use a dry leaf to contain the scraped pices as you are trying to spark. You can use a duct tape can be used to keep the wind from blowing the scraped pices away. Scrape the flint hard and fast to get spark to light the scraped piece. later then add small tinder paper/charcloth etc to let it catch into fire

 
Electric

Use a 9v Battery and steel wool to catch fire. Just touch the positive and negative output to steel wool inorder to get spark agani use this spark to to ctacth fire with addind small piec of paper/wood chips/stick etc.

 
 
In all cases if you have wax/gasoline etc will help to speed up to start fire after getting the spark .""")
    
    text.pack()
def defense():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""Self Defense Attack Tips

Headlock:
Grab onto one or both legs and lift up to knock the attacker over.The attacker should let go of you to catch the fall.You could also try to hit the groain.

Rear bear hug:
Head-butt him in the nose or hit the groin,since both of the attacker’s hands are occupied and will not be used to block you.

Choking:
Get your hand between his arm and you neck.Push away to prevent your air from being cut off.This may also be a good chance to use the shin scrape,stomp.

Weak body parts to target
These are the most sensitive part of the body.The bone in the nose is thin and can beeasily broken. Attacking eyes will cause a loss of sight for a short period of time, giving you a chance to escape.


Nose
With hand in a paw-like position,jab toward nose,
palm first.Strike nose with bottom of oalm,where it is strongest.But be careful;
this can kill someone.
With your hand in a fist,strike down on the nose.


Eyes
Grab head securely.Then push thumbs into the inside corner of the eyes .Rake your thumbs to the outside across the eyes.


Throat
Strike the throat with the “V” of your hand. OR grab his windpipe and squeeze, so that he cantnot breathe.


Legs
If the attacker is behind you,or you cannot reach the knee,this method will aslo work.End with a swift heel stomp to the foot
Groin
With your hand in a fist,strike down on the nose.
 
Remember...
The best defence is AWARENESS.
Only injure the attacker enough to get away.
Shout”NO!” or “FREE!” “HELP!”
Be loud,quick and aggressive""")
    
    text.pack()
def wildlife():
    top=toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""Surviving Wildlife Encounters

Grizzly Bear
If you run into a Grizzly bear then Slowly back away
If you too near or can’t go away then find a tree big enough so you can climb around 12ft (approx 2 people’s height)
If Bear Attacks
Lie face down clasp your hands behind neck and spread your legs.
Black Bear

If you run into a black bear then wave your hands up down side ways
Speak calmly if you are in pairs or small group
Drop bottle or any material to distract
Walk away as soon as bear gets distracted
If Bear Attacks
Stand your ground
If you can use bear spray
Cougar / Puma

If you run into a Cougar then wave your hands up down side ways
Maintain Eye contact
Slowly back away
If Cougar Attacks
Stand straight up to give impression you are big
And be ready to fight
Wolf

If you run into a wolf then Maintain Eye contact
Slowly back away
If wolf advances towards you then lunge towards it make noise, clap and if possible throw stones or branches/stickes etc
If Wolf Attacks
Stand straight up to give impression you are big
And be ready to fight""")
    
    text.pack()
def poison():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,""" What To Do When You Or Someone Is Poisoned Or You Think Have Been Poisoned
Identify Poisoning Signs and Symptoms
Signs and symptoms of poisoning may include:
Burns or redness around the mouth and lips
Breath that smells like chemicals, such as gasoline or paint thinner
Vomiting
Difficulty breathing
Drowsiness
Confusion or other altered mental status
Drowsy or unconscious
Having difficulty breathing or has stopped breathing
Uncontrollably restless or agitated
Having seizures
Known to have taken medications, or any other substance, intentionally or accidentally overdosed (in these situations the poisoning typically involves larger amounts, often along with alcohol).
 
Call 911 if you or someone is poisned or if you feel presence of above symptoms
Call your regional poison control center
Follow their instruction
Like Describing your/ person's symptoms, age, weight, other medications he or she is taking, and any information you have about the poison.
How much amount ingested and how long since the person was exposed to it. Have pill bottle or label of substance you think is the cause to describe to the conserned authorities.
What to do while waiting for help
Take the following actions until help arrives:
Swallowed poison Remove anything remaining in the person's mouth. If the suspected poison is a household cleaner or other chemical, read the container's label and follow instructions for accidental poisoning.
Poison on the skin Remove any contaminated clothing using gloves. Rinse the skin for 15 to 20 minutes in a shower or with a hose.
Poison in the eye Gently flush the eye with cool or lukewarm water for 20 minutes or until help arrives.
Inhaled poison Get the person into fresh air as soon as possible.
If the person vomits turn his or her head to the side to prevent choking.
Begin CPR if the person shows no signs of life, such as moving, breathing or coughing.
Caution (Do Not)
Don't make person vomit, give syrup of ipecac or do anything to induce vomiting.
Dont give raw eggs, no salt water..
Don't Give an unconscious person anything by mouth.
Don't givelemon juice or vinegar, or any other substance.
Don't give any false claimed "cure-all" type antidote.
Don't Wait for symptoms to develop if you suspect that someone has been poisoned.
Disclaimer:  The above information is for informational/emergency use purposes ONLY in absence of any professional/medical help and is not meant to replace any medical advice or treatment you are receiving OR may receive from your physician. If you are pregnant or nursing, always consult your physician before starting any and all home remedies. This information is gather from various resources avaliable online and general cultural practice.""")
    
    text.pack()

def survive():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""How to Survive Wildfire
If told to evacuate, do so. But if you do get trapped at home, stay inside where the structure will protect you. Move to a central room, away from exterior walls. Close the doors to cut down on air circulation, which can feed flames. And if you’re caught outside near a wildfire, remember that the most dangerous places to be are uphill from the fire and downwind from the flames.
Stay Calm: Remain Calm and confident this will be key for to get out alive and safe. Try breathing technique if air is not smokey take a deep breath in for 4 seconds, then exhale slowly for 4 seconds.
Leave the area. Don’t wait around to see how things develop. If the wind is blowing past you and toward the fire, then run into the wind. If the wind is behind the fire and blowing toward you, run perpendicular to the fire
Maintain situational awareness. Be aware of what’s going on around you at all times. Simple but crucial.
Choose downhill routes, not uphill routes if possible. Fire moves faster uphill due to updrafts.
Plan ahead. If time permits Identify escape routes/safe zones where you could take shelter if a fire came roaring through the area. Safe zones include rivers, lakes (get in the water), or large level spots out in the open away from combustible material. remember that the most dangerous places to be are uphill from the fire and downwind from the flames.
Save yourselves! If you are trapped above a fire, get out as fast as you can. Don’t try to save your belongings. Material is replaceable, lives are not.
Get low. If the flames are upon you, seek low ground — in a ditch or the notch in a forest road that will allow the superheated convective current to pass overhead. The lower you are the better your chances might be.
Breathing. Breathe inside your clothing next to your body to protect your respiratory tract so you don’t inhale hot gasses.
If you can find an area that has already burned over, leaving no residual fuel to reignite, that might be a safe place. But the ambient temperature of the scorched earth, rocks and timber will feel like an oven. Watch overhead to avoid snags and standing dead trees that might fall on you.""")
    text.pack()
    
def island():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""If you ever got lost on an island in tropical world then below tips might help you to survive for short term until you get help or long term depending where you landed.
Follow below steps and "remember to refer to survival rule of 3"
If its still early in the day then before venturing in to the woods / mainland gather any thing you see around you may be left over by some one that could help you later like knife, rope, plastic bottles,  soda cans etc
Try locate source of water preferably running water as still water may be contaminated, water falls etc or stream wood be good
Once you locate you want to start working on building a shelter to stay in shade during sunny day or from rain and cold night. even though days may be hot/warm nights in open may turn out to be very cold. Try find large branch of tree or fallen logs etc and put it against big tree or rock. then gather some small branches and put or large log and make a shade.
Gather some dry wood and start fire.. starting fire can help you stay warm at night, and also help you signal passing by planes or boats/ships
If you have enough time look for food from trees or may be try create bow/spear to hunt fish or small animals. Be carefully not to go to far into the woods as you never know what dangerous animals may be there. When picking fruits be carefully you know them some may be poisonous.
Finally once you have done enough to sustain yourself long. Its time to get some help by connecting passer by planes, trekkers, ships etc. Try to make huge fire or write big letters on sand as "SOS". Make smokey fire enough to signal but stay safe in doing so and don't burn down whole place.""")
    text.pack()
def rule3():
    top=Toplevel()
    text=Text(top,width=70,height=100,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
    text.insert(INSERT,"""

Always remember these 3 basics of survival in extreme conditions. Although some people may have more tolerance than others below is guide based on an average person
You can survive:
3 minutes without air After 3 minutes without air, the heart can stop.
     If you are caught in a building with fire and heavy smoke then try to get A gas mask to cover your nose. If you can't find gas mask then use any cloth your shirt etc dampen it with water and use it as gas mask. Try to get out smokey place and look for fresh air
3 hours without shelter can cause hypothermia or heat stroke 
Always carry a tarp or emergency blanket in your car or bug-out bag etc. In emergency situation if you ever get stuck out of civil world either one can be used to make a descent shelter.
3 days without water can lead to dehydration which may become life-threatening to you.
Try to find fresh water to stay away from getting sick. if you can find fresh water learn ways to filter it or use water purifying pills or portable systems to clean water where ever you go.
3 weeks without food. Without adequate food your body will stop functioning. 
If you have enough time look for food from trees or may be try create bow/spear to hunt fish or small animals. Be carefully not to go to far into the woods as you never know what dangerous animals may be there. When picking fruits be carefully you know them some may be poisonous.""")
    text.pack()
def diseaseprediction():
    predict.fun()

root=Tk()
button=Button(root,text="open app", command=open_window)
button.pack()



root.geometry("900x600+120+120")
root.mainloop()
