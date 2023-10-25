# Up, Down, and Up Again (Emi Act 3 Bedroom Grinding)
label en_delewd_E20:
play music music_happiness fadein 2.0
scene bg school_library
with locationskip_out

"The library always seems cooler than the rest of the building."

"Probably to keep the books from getting damaged by excessive heat and humidity."

"Books are sturdy objects, but if you want to keep them in good condition it takes a little effort."

"I've got several books that are so well-worn the pages are barely clinging to the spine."

"It seems impossible for them to still be usable, but if you handle them with care…"

"I make my way to the main desk, where I spot Yuuko busying herself with something or another."

show yuuko neutral_up at center
with charaenter

"She smiles at me as I enter and waves."

show yuuko closedhappy_down
with charachange

yu "Hello, Hisao."

show yuuko happy_down
with charachange

yu "Good to see you again! What are you looking for this time?"

hi "Nothing in particular, I guess. I just didn't really feel like going back to my room, is all."

show yuuko neutral_down
with charachange

"Yuuko nods."

show yuuko smile_up
with charachange

yu "Well, if you're unoccupied, maybe you could help me look for something?"

hi "Sure, what do you need?"

stop music fadeout 5.0

show yuuko worried_up
with charachange

"Yuuko brings a finger to her lips and looks around furtively."

"She seems to be looking for eavesdroppers."

yu "Come closer."

show yuuko worried_up_close
with characlose

"I take a few hesitant steps forward while feeling distinctly unnerved."

"Yuuko lowers her voice to a confidential whisper."

show yuuko neutral_up_close
with charachange

yu "I'm on the trail of the Yamaku Cat Burglar."

play music music_tension fadein 0.5

hi "The what?"

show yuuko panic_up_close
with charachange

yu "Shh! The walls have ears, Hisao!"

yu "Or they might."

show yuuko worried_down_close
with charachange

yu "But listen! Those missing books, remember them?"

hi "Er, yeah?"

show yuuko worried_up_close
with charachange

yu "Well, they weren't missing! They were stolen!"

yu "I'm convinced of it!"

hi "I remember you saying something of the sort earlier, but how do you know?"

"Yuuko leans in closer and, if possible, whispers even lower."

show yuuko closedhappy_down_close
with charachange

yu "Because I found one of his hiding places!"

hi "You did what?"

"Yuuko looks triumphant."

show yuuko happy_up_close
with charachange

yu "Found one of his stashes! It was under one of the stairwells in the boy's dorm!"

yu "Three books I'd been looking for, all there!"

show yuuko closedhappy_up_close
with charachange

yu "I'd suspected a thief before, but this proves it!"

hi "So did you take back the books?"

show yuuko panic_up_close
with charachange

"Yuuko looks as if I've just suggested she walk around naked."

yu "Are you nuts?"

show yuuko worried_down_close
with charachange

yu "He can't know I'm on to him! He might go to ground and evade capture!"

hi "Uh… huh. So what do you need my help with, then?"

"Yuuko casts another glance around the library and leans in closer."

show yuuko neutral_down_close
with charachange

yu "You've got to spy for me."

hi "Spy?"

yu "Yeah, like when you're in the dorms, you know."

show yuuko closedhappy_down_close
with charachange

yu "Keep an eye out for suspicious activity."

"What constitutes suspicious, anyway?"

"I mean Kenji's a pretty suspicious dude, but I'll wager he barely goes to class, much less sneaks into the library to pilfer books."

"Still, what's the harm in saying yes? At the least it'll get me out of this weird conversation."

hi "Yeah, I can do that. No problem."

show yuuko closedhappy_down
with charadistant

"Yuuko straightens up and claps excitedly."

yu "Great!"

show yuuko worried_down
with charachange

yu "Now, hurry up and talk about something else in case someone comes in!"

stop music fadeout 2.0

show yuuko happy_down
with charachange

yu "How's the school treating you?"

hi "Er, pretty well, actually."

hi "I've been running in the mornings with—"

show yuuko closedhappy_up
with charachange

yu "Emi Ibarazaki, right?"

play music music_comedy fadein 2.0

hi "Uh, yeah."

hi "How'd you know?"

show yuuko smile_down
with charachange

yu "I served you two in the teahouse, remember?"

show yuuko closedhappy_down
with charachange

yu "I deduced that if you were going to run with anyone, it would probably be her."

"She looks pleased with herself."

hi "Impressive."

hi "Anyway, yes. We've been running in the mornings."

hi "And uh, we kinda started dating."

show yuuko closedhappy_up
with charachange

"Yuuko claps her hands together excitedly."

yu "Really? That's great!"

yu "I'll bet you two are great together!"

show yuuko neutral_down
with charachange

yu "I love seeing people find one another like that, you know?"

yu "I even thought to myself when you walked into the Shanghai that one time, 'I wonder if that kid will wind up with one of those girls.'"

hi "…Really?"

"Yuuko doesn't seem to notice my somewhat weirded out tone and nods affirmatively."

show yuuko closedhappy_down
with charachange

yu "Yup! I could tell that you'd wind up with one of them, you know."

show yuuko neutral_down
with charachange

yu "I've got an eye for that sort of thing."

show yuuko worried_down
with charachange

yu "Of course…"

"Her expression droops slightly."

yu "I'm not so good at it myself."

hi "Aw, I'm sure that's not true."

show yuuko neutral_down
with charachange

yu "Oh, it's true."

yu "I met this guy once…"

show yuuko smile_down
with charachange

yu "We got along really great, but it turned out he was younger than me."

show yuuko neutral_up
with charachange

yu "And that was kinda weird, but not terribly so."

yu "What was really weird was that he disappeared one day, and I've not seen him since then."

hi "Huh. That does seem kind of odd."

show yuuko worried_up
with charachange

yu "Doesn't it?"

show yuuko neurotic_down
with charachange

yu "I hope it wasn't something I did…"

"I feel compelled to reassure her."

hi "I'm sure it wasn't."

stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up
with vpunch

"I intend to try and calm her down further, but the both of us jump in surprise at the ringing suddenly coming from my pocket."

show yuuko worried_down
with charachange

"Yuuko sighs to steady herself as I pull the phone from my pocket. I feel a little sheepish for indirectly causing the incident."

scene bg school_library_yuuko_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Emi? What's up?"

emi "Oh thank God I haven't called your phone before so I didn't know if this number would work or whether you would pick up and I can't—"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0

hi "Woah there Emi, slow down."

hi "What's wrong?"

"There's a pause on the other side of the line, during which I can hear Emi trying to control her breathing in order to calm down."

"Something's got her terribly agitated, and it's starting to agitate me."

emi "Can you just…"

emi "Can you stop by?"

emi "Like, now? Or shortly after now?"

emi "I really, really need to talk to you."

"There's a tone of pleading in the last sentence that I don't think I've ever heard from her."

hi "Of course, I'll be right there."

hi "Hold steady, okay?"

"In my increasingly agitated state I've apparently started saying things that don't quite make sense."

emi "Okay. I'll be okay."

hi "See you soon."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library
show yuuko worried_down at center
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

with charaexit

"I press the button to end the call before slipping the phone back into my pocket, apologize to Yuuko for running off, and run off."

scene bg school_girlsdormhall
with locationskip

"Perhaps at some point I would have stopped to think about the time, or how suspicious it looks for a guy to enter the girls' dorm at this hour."

"Except right now I'm just concerned with getting to Emi and finding out what's wrong and how I can help her."

play sound sfx_doorknock2

"I knock on the door and am greeted with a subdued 'Come in.'"

scene bg school_dormemi at left
with locationchange

"Something is very wrong as I stare at the scene before me."

"Emi's there, yes."

"But she's in a wheelchair."

"And her legs are missing. I glance around the room and see them sitting in a corner, looking like they've been thrown there."

show emiwheel weaksmile at center
with charaenter

"Emi responds to my entrance with a lopsided grin that is both pleased to see me and completely, utterly heartbroken."

emi "Hi, Hisao."

"It looks like she's been crying, but if she was, she's stopped now."

"I notice that I'm a little out of breath, having taken the stairs two at a time in order to get here."

"My heart doesn't seem to mind the strain, though. I file this happy fact away for later consideration."

"Like when I am not staring somewhat dumbstruck at my girlfriend in a wheelchair."

"Realizing I've still not responded to her greeting, my brain lurches into gear."

hi "Emi? What happened?"

show emiwheel pout
with charachange

emi "Guess I should've listened to you, Hisao."

show emiwheel sad
with charachange

emi "My leg's got a nasty infection. I'm not allowed to run on it for at least a couple of weeks."

"She gives a bitter laugh that shouldn't be coming from her."

show emiwheel frown
with charachange

emi "Heh, I can't even walk on it."

emi "I could have used a crutch and kept one of my legs, but I didn't see the point."

show emiwheel awayfrown
with charachange

emi "Why hop? You can't run on one leg."

show emiwheel pout
with charachange

emi "At least this way I can still, I dunno, roll fast or something."

hi "Y-yeah, that's good, right?"

"My awkward attempt to look on the bright side seems appreciated, but not really effective."

"Emi shrugs again."

show emiwheel awayfrown
with charachange

emi "It's just… kind of a nuisance."

show emiwheel frown
with charachange

emi "I mean, we can't even eat up on the roof now. No wheelchair access."

hi "Yeah, but that's not a big deal, right?"

hi "I mean we can still eat together, and that's the important thing."

show emiwheel weaksmile
with charachange

"That lopsided grin again. It hurts to look at."

emi "I suppose so, yeah."

show emiwheel frown
with charachange

emi "But like I said, it's a nuisance."

show emiwheel awayfrown
with charachange

emi "I mean, I haven't really used a wheelchair in…"

stop music fadeout 10.0

"She thinks for a minute."

show emiwheel pout
with charachange

emi "Maybe seven years? Something like that, anyway."

emi "A long time."

show emiwheel weaksmile
with charachange

emi "I'm afraid I'm a bit out of practice."

hi "Well, fortunately it's only temporary, right?"

"Emi nods."

show emiwheel neutral
with charachange

emi "Oh yeah, of course."

emi "It's not like I've lost 'em permanently."

show emiwheel awayfrown
with charachange

emi "But it's a pain in the ass all the same."

"I nod sympathetically."

"There's not much else I can do, after all."

"What am I gonna do, say 'I told you so?'"

"Although I {b}did{/b} tell her to get that leg looked at."

"But by the time I noticed, it was too late anyway."

hi "Do you need help with anything?"

hi "Er, that is, can I help with anything?"

show emiwheel closedsmile
with charachange

"Emi shakes her head and there's a bit of her usual grin back."

emi "Nah, I can manage fine by myself."

show emiwheel grin
with charachange

emi "Although if you want to help me over to my bed, it would save me the trouble of rolling over there myself."

"I blush, in spite of myself."

"Emi giggles."

play music music_heart fadein 0.5

show emiwheel wink
with charachange

emi "You're such a prude, Hisao."

hi "I'm not a prude! I just wouldn't want to take advantage of a young woman such as yourself."

hi "It's ungentlemanly."

hide emiwheel
with charaexit

show bg school_dormemi at right
with charamove

"I wheel Emi's chair to her bed, and easily scoop her up and deposit her there. She quickly sorts herself out and sits on the side."

show emi basic_grin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

"She's actually a little heavier than she looks. It would be rude of me to observe this aloud, of course."

hi "Man, you're kind of heavy."

play sound sfx_pillow
show comic vfx2
show emi excited_amused:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

"Emi hits me with a pillow."

show emi basic_closedgrin
with charachange

emi "Ass."

hi "Just sayin', is all."

hi "Must be all that running."

show emi sad_shy
with charachange

"At the mention of running Emi's grin falters slightly."

show emi sad_pout
with charachange

emi "Heh, well I guess I won't have to worry about that for a bit, huh?"

show emi sad_grin
with charachange

emi "Maybe I'll lose some weight."

hi "That's what you do to lose weight, right? Cease physical activity?"


show emi basic_closedgrin
with charachange

emi "I'm pretty sure that's what the nurse would recommend."

hi "Speaking of which, are you going to still be showing up in the mornings?"

hi "I'd hate to run alo—"

show emi sad_depressed
with charachange

emi "Ah, shit…"

"Emi's sudden interjection, more a disquieted muttering than anything too profane, causes me to look over in shock."

"She's leaning forward, trying to cover the fact that she's crying by covering her eyes with a hand."

"Of course, the subdued sobbing makes it pretty obvious that she's crying."

hi "Hey, I'm sorry."

hi "Forget I said anything, okay?"

show emi sad_depressed_close at center
with characlose

"I place a hand gingerly around her and pull her close."

"I can think of nothing else to say or do. How do you comfort someone who's just lost their legs again?"

show emi sad_pout_close
with charachange

"Emi wraps me in a hug and stays that way for a while."

hi "Sorry."

hi "I'm pretty bad at this whole comforting thing, I guess."

emi "Don't say that."

emi "I'm fine, really."

"Her voice is slightly muffled by my chest. I pat her head reassuringly."

hi "That's the spirit, right?"

hi "You'll get through this fine, I know it."

hi "Besides, I'm here to help you, remember?"

show emi sad_shy_close
with charachange

"Emi lifts her head and stares at me with tear-stained eyes."

show emi sad_grin_close
with charachange

emi "Can you? Can you really?"

"She's grinning lopsidedly, and something sparkles in her gaze."

"I can't tell if I'm being mocked or not."

hi "Of course. I mean sure, you're a bit heavy, but -{w=0.5}{nw}"

play sound sfx_impact

show emi excited_amused_close
with vpunch

extend " mmph!"

"My witty comment is cut off by the sudden press of Emi's lips on mine. I'm caught off guard, and am rewarded by hitting my head on the wall behind her bed."

hi "Ow."

show emi basic_hes
with charadistant

"Emi pulls back, trying to look concerned rather than like she's about to laugh."

emi "Are you okay?"

show emi excited_proud
with charachange

emi "Sorry!"

"I rub my head ruefully and grin back at her."

hi "Caught me off guard, there."

hi "Is that going to become a habit? Am I going to be lectured by Shizune and Misha more?"

"At the mention of the duo, Emi giggles."

show emi basic_closedgrin
with charachange

emi "Honestly, those two…"

show emi basic_grin
with charachange

emi "If I didn't know why, I'd be utterly confused as to why she hangs around with someone so bossy."

hi "Which one are we talking about?"

show emi basic_closedhappy
with charachange

emi "You know exactly which one, Hisao. Misha's hardly bossy."

hi "So what's the reason, then?"

show emi basic_confused
with charachange

emi "Huh?"

hi "The reason why Misha hangs around Shizune."

show emi basic_closedgrin
with charachange

"Emi waves my question off with a smile."

emi "No idea."

hi "I see."

show emi basic_grin
with charachange

emi "Anyway, you seem to be forgetting the original question, don't you?"

hi "Oh yeah, I guess I am."

hi "You wouldn't mind giving a guy a little warning, would you?"

hi "Otherwise I'm liable to wind up with a concussion."

"I emphasize the point by rubbing at the back of my head."

show emi excited_amused
with charachange

"Emi giggles madly."

emi "You could wear a helmet."

show emi excited_proud
with charachange

emi "Some kids here do, you know."

stop music fadeout 1.0

hi "Or I could just take revenge!"

play sound sfx_pillow

show emi excited_circle
with vpunch

"I grab a pillow from beside me and whack Emi over the head."

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi
with vpunch

"Emi topples off the bed and lands on the floor with a thump."

show emi sad_pout:
    center
    ypos 1.2
    ease 1.0 ypos 1.0
with Dissolve(1.0)

"Her arms promptly reappear on the bed, and she manages to pull herself back up."

"She really has a surprising amount of strength in that little body."

"Her face is turned downwards and away from mine, making me think I might have accidentally hurt her."

hi "Emi? You okay?"

hi "You didn't hit your—{w=0.3}{nw}"

show emi excited_smile_close
with vpunch

"A hand shoots up and grabs my collar. She pulls me in with a sharp tug, her face now barely an inch away from mine as she grins cheekily."

hi "Emi…?"

show emi excited_smile_close:
    subpixel True
    linear 0.1 ypos 1.7 zoom 2.0
with None

scene white
with Dissolve(0.1)

play sound sfx_impact

scene black
with Dissolve(0.75)

"She gives me a sharp headbutt, our foreheads making quite a loud thud."

scene bg school_dormemi at right
show emi basic_closedgrin at center
with openeye

"I sit back and rub my now sore head as Emi smirks victoriously."

show emi basic_grin
with charachange

emi "How's {b}that{/b} for revenge?"

play music music_running

hi "No fair!"

hi "You can't take revenge for revenge!"

"For someone missing most of her legs, Emi's surprisingly agile."

show emi basic_grin:
    center
    parallel:
        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"I swipe at her, but she deftly rolls out of the way and lands a hit with her pillow."

"Of course, the odds are against her. I can stand up, for starters."

scene black
with vpunch

"Oof!"

window hide

scene evh emi_grinding_victory
with locationchange

"Guess I can't, after all. Emi seems to have effectively tripped me up, and is now sitting primly astride me as I lay on my back. I'm not even sure how she managed it."

emi "I win!"

"Her eyes twinkle mischievously. I've been thoroughly defeated, and by a girl that's a fraction of my size, at that."

"Then again, being defeated doesn't seem quite so bad."

scene bg school_dormemi
with locationchange

"I open my lips to speak, but Emi's head darts downwards before I can get so much as a word out. I give no resistance as she presses her mouth to mine, not that I'd want to."

"This is… different, somehow."

"She pulls back, nips at my lower lip, and reinitiates the embrace. Her tongue darts inside my mouth, exploring. I can feel a warmth spreading through my body as my heart begins to beat faster."

"My mind starts to go foggy, then there's a giggle, and then—"

scene evh emi_grinding_victory
with locationchange

"I stare up at a grinning Emi."

emi "Told you. That makes my second win, now."

hi "What? That doesn't count; you used feminine wiles."

show evh emi_grinding_wink
with charachange

emi "'All's fair in love and war,' right?"

emi "Ha, and you're even blushing! I didn't know you were a blusher, Hisao."

hi "You were blushing too, you know. Probably because of your prudish ways."

"Even I've got to admit this is a stupid thing to say to a woman who is currently straddling me and has been, up until a few seconds ago, playing tonsil hockey with me."

show evh emi_grinding_grin
with charachange

emi "A prude, am I?"

emi "Well then, let's see who blushes first, shall we?"

label en_delewd_E20h:

"With her eyes closed, her lips purse expectantly. I just manage to lift myself up for a few moments, our mouths seeking one another."

"As I flop back down, my trousers are soaked with sweat. I would take them off if it didn't mean stopping what we're doing."

label en_delewd_E20x:

scene bg school_dormemi at right
with locationchange

show emi basic_closedgrin_close
with vpunch

emi "So… did I blush?"

hi "I didn't notice."

hi "Did I?"

show emi basic_confused_close
with charachange

"Emi shrugs, still breathing a little heavily."

show emi basic_grin_close
with charachange

emi "Didn't notice either."

hi "Well, maybe we should—"

play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind emi:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show emi basic_shock_close
with vpunch

rin "I need to use your window."

show rin basic_awayabsent:
    right alpha 1.0
with charachange

show rin basic_absent
with charachange

show rin basic_awayabsent
with charachange

"Rin's eyes pass over Emi, and me, and focus on the window."

show rin basic_deadpannormal
with charachange

rin "There was a cloud."

play music music_comedy fadein 0.5

show emi basic_grin_close
with charachange

emi "A cloud?"

show rin basic_lucid
with charachange

"Rin nods."

show rin relaxed_nonchalant
with charachange

rin "I was watching it from my window, but it didn't stay in my window."

show rin negative_spaciness
with charachange

rin "So I need to use your window."

show emi basic_closedgrin_close
with charachange

"Emi shifts a little, causing me to cough in order to cover up a giggle of my own."

emi "How long do you need the window for?"

emi "We're uh."

show emi excited_amused_close
with charachange

emi "Busy."

"This time I can't contain my laughter."

show rin negative_annoyed
with dissolvecharamove

"Rin ignores both Emi and me and peers out the window."

show rin basic_deadpanupset
with charachange

"Her shoulders slump, and she looks disappointed."

rin "Hmm."

rin "It changed into something else."

rin "Disappointing."

show emi basic_grin_close
with charachange

"Emi is having trouble keeping a straight face."

emi "Sorry to hear that, Rin."

show emi sad_pout_close
with charachange

emi "Could we have a little privacy now, please?"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin relaxed_nonchalant:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True
with Pause(1.0)

play sound sfx_doorclose

hide rin
with None

"Rin shrugs, as if to say 'Can you?' and hooks her foot around the door, pulling it closed behind her."

show emi excited_laugh_close
with charachange

"We both dissolve into raucous laughter, unable to deal with Rin's bizarrely timed visit any other way."

"After our laughter dies down, I look to Emi."

stop music fadeout 5.0

hi "Well."

show emi basic_grin_close
with charachange

"Emi raises an eyebrow."

emi "Well?"

hi "Again?"

show emi excited_proud_close
with charachange

"Emi grins and laughs, and then she nods."

$ suppress_window_after_timeskip = True

scene black
with dissolve

# Storage Space (Emi Act 3 Shed)
label en_delewd_E21:

window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

"The sunlight breaks through my window shortly before my alarm ruins the morning silence."

play music music_dreamy fadein 6.0

"I feel sore."

"The events of the previous evening suddenly intrude upon my consciousness, and I find myself blushing."

"That was an eventful evening - and it explains perfectly the soreness in my lower back."

"The walk back, as I recall, had been rather tense."

"My trousers having been… soiled, I had washed them off in the bathroom before going back to my room."

"But there was still a fairly obvious-looking stain on the front."

"Fortunately for me, the only person I ran into on my way back was Kenji."

"And he didn't notice a thing."

"Well, apart from my being in the general vicinity."

"Of course he'd asked how the night went, and whether or not I'd learned anything of importance."

"I don't even know if I opened my mouth to answer; I was too tired to care."

"And this morning, I'll admit that I'm feeling pretty worn out."

"Still, Emi had promised to meet me at the track, and I'd hate to disappoint."

scene bg school_track
show emiwheel weaksmile at center
with locationskip

"She is indeed waiting for me when I arrive."

"Doing her best to look cheery, despite the fact that she's sitting in a wheelchair."

"I wave to her and begin stretching."

hi "You're early."

show emiwheel frown
with charachange

"Emi frowns and shakes her head."

show emiwheel angry
with charachange

emi "Ridiculous."

emi "{b}You're{/b} late."

show emiwheel grin
with charachange

emi "Overslept, Hisao?"

show emiwheel wink
with charachange

emi "All tuckered out?"

"Well, at least she seems more like her old self."

"And as expected, she doesn't seem that shy about mentioning our… previous activities."

hi "Hey, you're lucky I could show up at all."

hi "All that cardiovascular activity last night, I nearly thought I'd have to see the nurse afterwards."

show emiwheel wink
with charachange

"Emi laughs out loud, then her face suddenly becomes concerned."

show emiwheel blush
with charachange

stop music fadeout 8.0

emi "Hey, that's not uh…"

emi "I mean, you're not…"

hi "Go on, spit it out."

show emiwheel awayfrown
with charachange

emi "It's just that it would be hard to explain if you had an episode while we were…"

hi "Oh."

hi "{b}Oh.{/b}"

"Now that she mentions it, it really is a legitimate concern."

"I certainly hadn't thought of it last night, of course - other, more pressing concerns had been at hand."

hi "Well, I don't think anything we, er, {b}do{/b} is going to be any more of a strain than these morning runs, and I handle those fine, so…"

show emiwheel frown
with charachange

"Emi considers this point."

show emiwheel evil
with charachange

"A devious light appears in her eyes."

play music music_emi fadein 2.0

emi "Say…"

hi "Hmm?"

show emiwheel grin
with charachange

"The light vanishes, and Emi grins ruefully at me."

"I can't help but feel vaguely suspicious."

show emiwheel happy
with charachange

emi "I seem to have forgotten a pair of gloves."

hi "What do you need gloves for?"

show emiwheel smile
with charachange

"Emi indicates the chair upon which she is seated."

emi "For this, of course!"

show emiwheel wink
with charachange

emi "Sure, regular moving around is all well and good without 'em, but I want to be able to get a good workout."

show emiwheel grin
with charachange

emi "And to get that kind of speed, you gotta have gloves if you don't want blisters."

hi "So what, are you wussing out on me then? Do I have to go it alone?"

show emiwheel awayfrown
with charachange

"Emi thinks for a minute - or pretends to think."

show emiwheel closedsmile
with charachange

emi "Hmm… if I remember right, there's a spare pair or two in the track shed."

"So she does seriously want to do it, then."

"But in her normal school uniform? I'd have expected her to wear her gym outfit for something like this."

hi "Wait, what are they doing there?"

show emiwheel frown
with charachange

"Emi looks askance at me."

emi "Seriously? You can't think of why a shed full of track supplies at a school for the disabled would have racing gloves?"

"Well, when she puts it that way, I suppose that makes perfect sense."

hi "Hey, I'm still getting used to this place. Give me a break, huh?"

show emiwheel grin
with charachange

emi "I guess I can let it slide this time."

show emiwheel wink
with charachange

emi "Now come on, I'll need your help."

"I can't imagine what for, but then again I didn't have a clue why racing gloves would be in the shed, so I'm not willing to press the issue."

scene bg school_sportsstoreext
with locationchange

"Emi navigates her way to the shed easily enough, though I can hear her grumbling under her breath."

"It's actually kinda cute."

"I hurry a little to reach the door first. Opening it will be easier for me than for her."

play sound sfx_door_creak

show emiwheel neutral:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


"The door opens, and Emi starts to wheel inside, only to come to a sudden halt at the doorway."

"It seems the doorsill is slightly too high for her to get over by herself."

show emiwheel awayfrown:
with charachange

show emiwheel awayfrown:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)

"She makes a few runs at it, unsuccessfully, before crossing her eyes and glaring at the offending object."

show emiwheel angry at center
with charaenter

emi "Stupid wheelchair."

show emiwheel frown
with charachange

emi "Hisao, can you give me a hand here?"

hi "Sure, no problem."

scene bg school_sportsstoreroom
with locationchange

"It's a simple enough matter for me to bump Emi over the doorway, jostling her slightly."

show emiwheel blush_close_ni at center
with charaenter

emi "Hey, easy there!"

hi "Whoops! Sorry."

"It's at about this time that I fail to notice where I'm going and run Emi's chair into a mat."

play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel
with None

"She gives a startled yelp and topples forward out of her chair."

"There's a moment of silence as I gaze in horror upon what I've done, and Emi glares at me."

emi "Hisao…"

hi "Yes?"

emi "Promise me you'll never work at a hospital."

hi "Sorry! I didn't mean to!"

"Emi giggles, and holds up a hand."

emi "Would you kindly help me back into my chair, Hisao?"

show emi basic_closedgrin_close_ni:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

"As I bend down to pick up Emi, she grins in triumph and pulls me into a kiss that quickly has us both entirely unconcerned about getting her back into the chair."

play sound sfx_door_creak

"In fact, as I move to a more comfortable position, I confess that the chair is pushed out the door, which, startled by the passage, swings shut."

play sound sfx_rustling

hide emi
show eminude smile_close_ni at center
with charachange

"Well, at least we've got privacy now, which is a good thing as my hands work quickly to remove Emi's blouse and skirt."

"I'm startled to discover that she's forgotten to put her bra on today. Did she plan this?"

show eminude blush_close_ni
with charachange

"Her arms hook under mine and rest on my shoulders as I kiss my way down Emi's neck, pausing to give special attention to a spot right where the neck meets the shoulder that I'd found last night."

emi "Y-you've gotten pretty good at th-hee!"

hi "I do try."

show eminude frown_close_ni
with charachange

"Emi pushes on my chest, insistently, and I draw back with a puzzled expression."

emi "I've got a confession, Hisao."

hi "Oh?"

"Having pulled back, I decide instead to focus my attention on her breasts."

show eminude blush_close_ni
with vpunch

"As she attempts to speak, her words are interspersed with giggles that I find incredibly cute."

show eminude wink_close_ni
with charachange

emi "I don't ac-hee hee hee-actually w-woah! Wear gloves."

"My own reply is rather mumbled onto her chest instead of being addressed to her face."

hi "Should've known…"

"Words quickly become irrelevant."

show eminude closedsmile_close_ni
with vpunch

"Emi's movements are almost frantic, as if she's been holding something back since we met this morning, and now she has an outlet."

"I'm very nearly caught off guard by her aggressiveness, feeling her nearly rip my shirt off, the way she seems to vie to be in the dominant position."

"For my part, I confess that I'm caught up in her attitude as well, fighting back, rolling and wrestling even as I caress her breasts, even as her fingers dig into my shoulders, and I lose track of where we are."

show eminude blush_ni
with vpunch

"So much so that I roll right off the mat and land on something small and rather hard."

hi "Ow!"

show eminude weaksmile_ni
with charachange

"Emi, still flushed and breathing a little heavily, peers at me and bursts into laughter."

emi "I'm sorry, I'm sorry. Are you all right?"

hi "Yeah, I think so. Not sure what I landed on, though…"

"I reach under my back and pull the offending object out, inspecting it closely."

stop music fadeout 0.2

"'Personal lubricant. Lemon-flavored.'"

"Wait, what?"

play music music_running

show eminude happy_ni
with charachange

"Emi's eyes shoot upwards and she begins, if possible, to laugh even harder."

hi "Somehow, I don't think this is… this isn't track-related."

show eminude closedsmile_ni
with charachange

emi "Oh man, I know whose that is!"

hi "What?"

show eminude wink_ni
with charachange

emi "It's the track captain's!"

"Ah, my old nemesis. Or, kind of."

hi "How d'you know it's his?"

show eminude awayfrown_ni
with charachange

"It appears that I've asked a stupid question, or at least Emi thinks so."

show eminude frown_ni
with charachange

emi "Because he's the one who told me the track shed was a good place for… what did he call them?"

show eminude pout_ni
with charachange

emi "'Clandestine encounters.'"

hi "Oh? He invite you to one or something?"

show eminude happy_ni
with charachange

"Emi bursts into more laughter."

"I confess the sight of a naked Emi laughing is oddly beautiful."

"I feel an eagerness to end conversation and get back to what we were doing, despite my rather pointed questioning."

show eminude closedsmile_ni
with charachange

emi "Hisao, the track captain's gay."

"Huh."

hi "Really? And here I initially thought you two were a couple."

show eminude awayfrown_ni
with charachange

emi "Well… I did have a crush on him when I first joined up, but he wasn't interested."

show eminude frown_ni
with charachange

emi "Obviously."

show eminude neutral_ni
with charachange

emi "But we are good friends, I guess."

show eminude grin_ni
with charachange

emi "I mean he told me about all this, you know."

hi "I hesitate to ask,"

"And really, I do. But I ask anyway."

hi "But what does he need the uh… lube for, anyway?"

hi "I mean, he doesn't… er…"

"How the hell does Emi always manage to not blush?"

show eminude wink_ni
with charachange

emi "Obviously he uses it for, you know."

show eminude evil_ni
with charachange

emi "Anal."

"I try to suppress a snicker."

"I fail."

show eminude happy_ni
with charachange

"Emi's giggling too."

hi "And he {b}tells{/b} you about all this?"

show eminude awayfrown_ni
with charachange

"Emi shrugs."

show eminude neutral_ni
with charachange

emi "Yeah, of course."

stop music fadeout 10.0

show eminude closedsmile_ni
with charachange

emi "He's kinda wild about the whole thing."

emi "Says it's a feeling that can't be beat."

hi "Uh… huh."

"The air in the track shed seems charged with some kind of horrible curiosity."

hi "That's interesting."

hi "I suppose I'll have to take his word for it."

show eminude neutral_ni
with charachange

emi "Well…"

"Birds outside stop chirping."

"The wind dies down."

"Somewhere, a man is drinking a cup of coffee. He freezes with the cup at his lips."

show eminude neutral_ni
with charachange

emi "We could…"

extend " maybe…"

show eminude blush_ni
with charachange

emi "Try it."

play music music_one fadein 5.0

"My jaw suddenly and spontaneously unhinges and hits the floor."

hi "W-what?"

"Emi is finally blushing, rubbing the back of her head ruefully."

show eminude pout_ni
with charachange

emi "Well, it's just that we really can't… do what we did last night, you know?"

emi "It would be a little… it wouldn't be safe, you know?"

show eminude weaksmile_ni
with charachange

emi "I mean it wasn't exactly a great idea last night."

show eminude closedsmile_ni
with charachange

emi "So you know, we could try this to see if it uh…"

hi "Is as good?"

show eminude weaksmile_ni
with charachange

emi "Well uh, yeah. Basically."

hi "Huh."

label en_delewd_E21h:

scene evh emi_shed_base1
show emi emi_shed_grin
show hisao emi_shed_neutral
show evh_l emi_shed_up
show evh_r emi_shed_down
with shorttimeskip

emi "Careful!"

hi "Are you sure about this?"

"I'm positioned behind Emi, who is looking back over her shoulder, looking a little flushed."

"Well obviously once we decided to go ahead with this idea, we had to get back into the mood."

"That accomplished, we emptied the bottle of lube and…"

"Here we are."

show emi emi_shed_hesitant
with charachange

emi "Yes, I'm sure! Come on, before I calm down and think too much about this."

"Emi's breathing is still coming a little heavily, and her response is almost impatient."

"Which is to be expected, I suppose. We were both so close, and this is kind of delaying things."

"I think we've both gone temporarily insane."

"At least that's going to be my claim from here on out."

"I try hard not to think about the specifics of what I'm about to get myself into."

"There's no way this is going to be very clean."

show evh emi_shed_base2
show hisao emi_shed_closed
with charachange

"Taking a breath that is as much for me as it is for her, I enter slowly."

"There's a lot of resistance, and it's like both our bodies are reluctant to actually go through with it."

show emi emi_shed_shock
with hpunch

"Emi's whole body tenses, and as I'm only partially in by this point, it feels surprisingly good, if a bit odd."

"Emi, on the other hand, looks uncomfortable."

"The expression is almost comical."

show hisao emi_shed_neutral
with charachange

hi "Should I stop?"

"Emi's breath hitches in her throat, and it seems to take a few seconds longer than it should to formulate a reply."

show emi emi_shed_closed
with charachange

emi "N-no, keep going. It just feels weird."

"She giggles."

"I can't blame her. I'm surprised that I even managed to form a sentence."

show hisao emi_shed_closed
with charachange

"It's… hot."

"Feels exceedingly odd."

"The lube glistens unnaturally."

"It makes me uncomfortable."

"I continue to work my way inside her, working slowly and listening carefully to Emi's breathing."

show evh emi_shed_base3
show emi emi_shed_hesitant
with charachange

"I reach my limit and pause. Emi looks back again, biting her lower lip."

emi "Are you going to try moving, or are we just going to sit here feeling silly?"

show hisao emi_shed_neutral
with charachange

hi "No, I just wanted to give you a chance to adjust."

"This doesn't make any sense."

"How did we even decide to do this?"

show emi emi_shed_grin
with charachange

emi "I don't think there's really any adjusting to this, Hisao."

show emi emi_shed_hesitant
with charachange

emi "Try moving. Maybe it'll feel better?"

"She sounds doubtful, but certainly unwilling to admit defeat now that we've come so far."

show emi emi_shed_closed
with charachange

"I begin a slow motion that seems to work well for both myself and Emi, as she closes her eyes in an attempt to concentrate on this new feeling."

"As I begin to find a rhythm, I begin to feel that familiar falling-away sensation I got yesterday."

show hisao emi_shed_closed
with charachange

"I close my eyes and try to lose myself in the feeling, except…"

"It doesn't seem right."

"Emi's not making any noise."

"I learned very quickly yesterday that Emi is somewhat less than quiet when she's enjoying herself."

show hisao emi_shed_neutral
with charachange

"As I open my eyes, I see that Emi's trying to get into things, but it just doesn't seem to be working for her."

"Her eyes are closed, and she's biting her lip, but it seems to be out of toleration rather than enjoyment."

"A sort of 'well, this was a failure, but hopefully it'll be over soon' look."

"I'm caught in a bit of a situation here."

"In truth, I don't want to stop."

"But at the same time, it doesn't seem to be doing much for Emi - or if it is, it's coming on far slower than I am."

"I feel bad. I want Emi to enjoy this, too."

show evh_r emi_shed_up
show emi emi_shed_shock
with charachange

"I reach one arm around to tease at Emi's chest, which startles her."

show hisao emi_shed_sweat
with charachange

"This in turn causes her to tighten around me considerably, causing a wave of pleasure to blindside me."

show evh emi_shed_base4
show hisao emi_shed_neutral
show emi emi_shed_closed
show evh_l emi_shed_down
with charachange

"My gasp seems to amuse Emi, but her grin quickly turns to a gasp as I move my other hand casually down her front and begin to stroke gently at the soft patch of hair between her legs."

"The motion of my own hips increases as my hand's ministrations to Emi's front bring back the gasps and yelps that I'm used to."

show hisao emi_shed_sweat
with charachange

"I concentrate only on the feelings of my hands, one now slick and sliding, the other on skin soft and responsive, goosebumps on her flesh, shivers and sweats, as her own building climax causes her to tighten, until finally I can't possibly—"

"NoIcan'tpossibly"

show hisao emi_shed_closed
with charachange

"OhgodI'msorryEmiI'mgoingto"

"I give a final thrust, my fingers tense around Emi's nipples, dive between her legs."

window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show

"Emi's back spasms and she arches up, a high, girlish cry that echoes off the walls, and I feel the wave of my own climax annihilate all other sensations in my body."

show evh_l emi_shed_up
show evh_r emi_shed_down
with charachange

"Emi's arms give out and she falls forward, rather violently disengaging us and pulling something dear to me in the process."

label en_delewd_E21x:


play sound sfx_impact

scene bg school_sportsstoreroom
with vpunch

"The sudden switch from pleasure to pain causes me to lose my balance, and I fall forward on top of Emi."

stop music fadeout 2.0

emi "Ow!"

hi "Ow."

"I quickly roll off Emi and prop myself up, breathing heavily and trying to ignore the pain in my crotch."

"Emi yelps a little as she rolls over. She grabs a couple of the tissues we'd kept handy earlier, and cleans up before getting her panties back on and awkwardly leaning against a wall."

"Still breathing heavily, I decide to sit against the wall next to her. The feeling of the cool concrete against my sweating back is a welcome sensation."

show eminude sad_close_ni at center
with charaenter

emi "That {b}hurt{/b} at the end!"

hi "Yeah, I uh…"

hi "This was probably not a great idea."

"Emi squirms in order to try and sit down beside me without too much pain. Judging by her wincing, it doesn't really work."

show eminude pout_close_ni
with charachange

emi "Yeah, I'm going to have words with the captain."

show eminude angry_close_ni
with charachange

emi "He was clearly lying."

play music music_ease

"The utter and absolute ridiculousness of the situation suddenly hits, and I begin laughing."

show eminude happy_close_ni
with charachange

"Emi shakes her head and begins laughing with me."

show eminude grin_close_ni
with charachange

emi "Hey, Hisao."

hi "Yeah?"

show eminude pout_close_ni
with charachange

emi "We're never doing this again, right?"

hi "Yeah, I think my curiosity is satisfied on this one."

"Emi nods, satisfied."

show eminude closedsmile_close_ni
with charachange

emi "Good."

show eminude smile_close_ni
with charachange

emi "I think we should maybe stick to the basics, don't you?"

show eminude blush_close_ni
with charachange

emi "I mean most of this is new to me anyway."

hi "What d'you mean, 'most?'"

show eminude grin_close_ni
with charachange

"Emi grins impishly."

show eminude closedsmile_close_ni
with charachange

emi "I'll never tell."

"An unpleasant thought strikes me."

"Even more unpleasant is the thought of having to ask Emi about it."

"Still, after what we've just done, it should be a cakewalk."

hi "Hey, is there a sink?"

hi "I'd kinda like to, er."

hi "Wash off a little."

show eminude blush_close_ni
with charachange

"Emi's jaw drops."

emi "In the {b}sink{/b}?"

hi "Well, there's not really anywhere else to do it, is there?"

hi "And it uh… I want to avoid a smell."

hi "That the nurse might notice."

"This is the most awkward conversation I have ever had."

show eminude closedsmile_close_ni
with charachange

emi "You're right."

show eminude grin_close_ni
with charachange

emi "Yeah, there's uh… It's on the back wall."

show eminude smile_close_ni
with charachange

emi "There might be some soap, too."

hi "Thanks."

hide eminude
with charaexit

"There is in fact a little hand soap, which is better than nothing."

"No towel, though. Guess I'll just have to drip dry."

show eminude grin_ni at center
with charaenter

emi "All finished?"

hi "Yeah, that'll do for now. It's not like I'm not going to take a shower after we see the nurse."

show eminude weaksmile_ni
with charachange

emi "Glad to hear it."

show eminude wink_ni
with charachange

emi "Now help me find my clothes. You tossed 'em somewhere."

hi "Hey, you were no better! How am I supposed to explain that hole in my shirt, hmm?"

show eminude closedsmile_ni
with charachange

emi "Heh, sorry. I got a little excited earlier."

scene bg school_sportsstoreroom
with shorttimeskip

"It takes some time, but finally we're both more or less clothed."

"There's a frantic moment where neither of us knows where Emi's wheelchair is, but I recall it going through the door and rescue it."

show emiwheel neutral_close_ni at center
with charaenter

emi "Now be more careful going through the door this time, would you?"

show emiwheel awayfrown_close_ni
with charachange

emi "Bumps are not my friend right now."

hi "I am so sorry we tried this."

show emiwheel grin_close_ni
with charachange

"Emi shrugs and grins."

show emiwheel wink_close_ni
with charachange

emi "Well, it was worth a shot, right?"

show emiwheel closedsmile_close_ni
with charachange

emi "And anyway, it was good exercise, right?"

"Can't argue that."

scene bg school_nursehall
with shorttimeskip

"As we make our way up to the nurse's office, I notice that Emi keeps shifting uncomfortably in her seat."

show emiwheel awayfrown
with charachange

emi "God, this feels weird."

show emiwheel neutral
with charachange

emi "Good thing I'm in a wheelchair, Hisao."

hi "Why's that?"

show emiwheel weaksmile
with charachange

emi "Because, now I don't have to explain to the nurse why I'm walking funny."

hi "Oh."

hi "We're never doing this again."

scene bg school_nurseoffice
show nurse fabulous at center
with locationchange

"The nurse is at least kind enough to not comment on the marks that Emi left on my shoulders."

"Nor does he say a word about Emi's constant shifting about in her wheelchair."

"Either he didn't notice, or he didn't want to notice."

"All the same, I'm going to have to make sure he didn't slip cyanide into my medication for a little while."

"Just to be safe."

stop music fadeout 4.0
scene bg school_dormhisao
with locationskip

"I shower for longer than usual, just to be sure I'm clean of our little 'experiment', and then collapse on my bed."

"Class is in twenty minutes, so I can probably afford a nap."

scene black
with shuteye

# After-school Plans (Emi Act 3 Day after shed)
label en_delewd_E22:

scene black
with dissolve

with Pause(5.0)

play sound sfx_doorknock

"Knock knock."

"Who's there?"

play sound sfx_doorknock

"Knock knock."

"That's not how the joke goes at all."

play sound sfx_doorknock

"Knock knock."

"I already said who's there!"

"More importantly, what time is it?"

"Even more importantly, what day…?"

scene bg school_dormhisao
with openeyefast

"I am suddenly catapulted into wakefulness by both the fact that the knocking still hasn't stopped and the fact that it's noon."

"On a school day."

"Now fully awake, I can remember why I was napping."

play sound sfx_doorknock

"I wonder how long this knocking is going to continue."

"Guess I ought to answer the door."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

"I'm strangely unsurprised to see Kenji on the other side."

"Though it appears that Kenji is surprised to see me."

ke "What the hell are you doing here, man?"

play music music_kenji fadein 0.5

hi "Well, I was sleeping."

show kenji neutral
with charachange

"Kenji nods in understanding."

show kenji happy
with charachange

ke "Knocked out. I see."

show kenji tsun
with charachange

ke "I told you to be careful around that Ibarazaki chick, man."

ke "This is the sort of thing that happens when you aren't cautious."

"He makes an attempt to look at the back of my head."

show kenji neutral
with charachange

ke "Did she hit you with something?"

ke "Or was it a drug?"

hi "Stop trying to touch me."

with flash

"Kenji produces a flashlight and shines it in my eyes."

ke "You got a concussion?"

hi "I wasn't knocked out!"

show kenji happy
with charachange

ke "Maybe you just don't remember."

"This conversation isn't going anywhere."

hi "No, I just had a tiring morning and fell asleep."

show kenji tsun
with charachange

ke "Whatever, man."

ke "If you want to be in denial about this, I guess I can't stop you."

ke "But you gotta watch out for that girl, man. She's not safe."

hi "What?"

show kenji rage
with charachange

ke "She's not safe to be around; she's one of their most sinister agents!"

ke "If you're not careful, there's no telling what could happen!"

ke "She's brought down stronger men than you, you know!"

hi "What the hell are you talking about?"

hi "She's not an agent of anything, and she didn't knock me out, okay?"

hi "I also highly doubt that she's brought down anyone at all."

show kenji tsun
with charachange

"Kenji looks almost offended."

"I have no idea why."

ke "You don't believe me?"

ke "That's cold, man. Real cold."

ke "I'm just trying to look out for you. That's what friends do, you know."

"We're friends? I had no idea."

"Then again, I wonder if Kenji knows what being a friend even entails."

"I feel something like pity for him, standing there before me."

"Maybe he does think he's looking out for me."

hi "I know, I know."

hi "I'm sorry about that. Thanks for the warning."

"I hold out my hand as a sign of peace."

show kenji neutral_close
with characlose

"Kenji shakes it gingerly, like my hand could possibly be on fire."

"There's an awkward silence for a few seconds before Kenji remembers that he's still shaking my hand."

show kenji happy_close
with charachange

ke "Anyway, I need a favor."

hi "What kind of favor? I'm out of money…"

ke "No you aren't. You've got money kept in your desk drawer under a black notebook. For emergencies."

hi "Did you ransack my room?"

show kenji neutral_close
with charachange

ke "That's not important."

ke "I don't need money, anyway."

"He adopts a very serious tone."

show kenji tsun_close
with charachange

ke "I'm about to undertake a major op."

ke "It'll blow the whole conspiracy wide open if I'm right."

ke "But it's dangerous, so I need you to do something for me in case I don't come back."

hi "Uh, sure man. Anything."

"What the hell is he planning on doing?"

"Should I be telling someone about this?"

show kenji neutral_close
with charachange

ke "If I go missing, wait three days and then mail my journal off to the newspapers."

ke "It's hidden in my room under a false bottom in one of my desk drawers."

hi "How do I get into your room? I don't have a key."

show kenji tsun_close
with charachange

"Kenji looks at me like I'm crazy."

ke "So pick the lock. You know how to do that, right?"

ke "It's an important skill to learn at a young age!"

hi "Uh, yeah, of course I know how."

hi "I'll be sure to uh, do that for you. If you go missing."

"I don't think I want to read Kenji's journal."

"Either way, Kenji seems pretty happy that I've agreed to do this thing for him."

show kenji happy_close
with charachange

ke "Great, man. Great."

ke "I'll see you around, I got stuff to do."

stop music fadeout 5.0

show kenji happy_close:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji
with None

"And he's gone, dashing down the hallway."

"He made it seem so final."

"I hope I don't have to carry out his final wishes."

scene bg school_dormhisao
with locationchange

play sound sfx_doorclose

"Shaking my head, I close my door and walk back to my bed."

"Guess I should go to class, if only to catch the last half of the day."

"But I've come this far without going to class today…"

"And I did want to read more of that Hawking book Mutou lent me…"

"I'm sure he'll understand."

with shorttimeskip

play sound sfx_hammer

"Knock knock."

"This time the noise jerks my attention away from my book."

"An experience not unlike being woken up."

hi "Who's there?"

emi "Me! Aren't you glad?"

play music music_emi fadein 4.0

"The voice is muffled through the door, but unmistakably Emi's."

play sound sfx_dooropen

scene bg school_dormhallway
show emiwheel smile at center
with locationchange

"I hop up and open the door, smiling broadly."

hi "Hey! Nice to see you again!"

show emiwheel grin
with charachange

"Emi grins back, staring up at me from her wheelchair."

show emiwheel closedsmile
with charachange

emi "Yeah, you would have seen me earlier, but the damned elevator wasn't working."

show emiwheel pout
with charachange

emi "Had to wait for them to fix it."

show emiwheel awayfrown
with charachange

emi "You'd think they could keep it in better order, but nooo…"

"I chuckle a bit at her vexed expression and invite her in."

scene bg school_dormhisao
with locationchange

"She wheels in easily, and with my help she hops onto my bed."

show emi basic_closedgrin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

emi "There. Much more comfortable than that stupid chair."

show emi basic_grin:
    ypos 1.1
with charachange

"A sigh of contentment hangs in the air, and for a minute we both just stare at one another."

"It's at that point that I notice the circles under Emi's eyes."

"They're not that dark, but they definitely weren't there before."

"Before I can ask about them, Emi fixes me with a mischievous stare."

show emi excited_happy
with charachange

emi "So, I couldn't help but notice you weren't at lunch today."

emi "In fact, I don't think I saw you at all."

show emi excited_proud
with charachange

emi "What happened, hmmm?"

hi "Fell asleep."

hi "I actually didn't wake up until lunch, and only then because Kenji woke me up."

"A yawn escapes her, and I raise an eyebrow."

hi "Tired?"

show emi sad_grin
with charachange

"Emi nods sleepily."

play music music_serene fadein 8.0

show emi sad_depressed
with charachange

emi "Haven't slept well."

"Not sleeping well?"

"I can tell that she didn't mean to tell me this either, because she gives a little start like she's just been caught lying and hastens to add,"

show emi basic_closedgrin
with charachange

emi "It's not a big deal, though."

hi "What's the trouble?"

show emi basic_grin
with charachange

"Emi shrugs and refuses to elaborate."

hi "Stressed over exams?"

"Another shrug, but after a pause, Emi nods hesitantly."

show emi sad_shy
with charachange

emi "Er, yeah, I guess."

emi "Actually, that's why I stopped by."

"She begins to look more and more miserable."

"Not so you'd notice, of course; but her eyes are on her lap, she's fidgeting and her voice is quiet."

show emi sad_pout
with charachange

emi "We uh, we need to stop hanging out so much."

hi "Huh? Why?"

"Emi takes a deep breath, like she's been practicing this."

show emi sad_shy
with charachange

emi "Because you're too much fun to be around."

emi "And I can't concentrate when you're near me."

emi "With exams coming up soon, I just… can't have that distraction."

show emi sad_depressed
with charachange

emi "Otherwise my grades will be pretty lousy, I'm afraid."

hi "I could help you study…"

show emi sad_grin
with charachange

"She smiles at me, clearly unhappy with the situation."

emi "I'd love it if you could, but we wouldn't actually study, would we?"

show emi sad_shy
with charachange

emi "I mean even now, I'm trying to have a conversation with you but I kinda just want to, uh…"

show emi sad_shyblush
with charachange

emi "Not converse."

hi "Ah."

hi "Overwhelmed by my rugged manliness. I understand."

show emi basic_grin
with charachange

"That earns me a grin, at least."

"Emi shakes her head."

show emi basic_closedgrin
with charachange

emi "Idiot. You're full of yourself."

hi "Well, I am pretty irresistible."

show emi sad_shyblush
with charachange

emi "Er, more or less. I guess."

show emi sad_grin
with charachange

emi "So that's the situation, Hisao."

emi "I have too much fun around you, and if I'm going to go into exams prepared, I need to be alone."

hi "Hey, that's okay."

"It really seems to have been bothering her."

"Besides, it's only a couple of weeks. And we'll still see each other in the mornings, and at lunch."

hi "We can just hang out at school, no problem."

hi "And after exams, we'll go on a date to celebrate their being over, okay?"

show emi basic_closedgrin
with charachange

"Emi grins, pleased by this proposal."

show emi basic_happy
with charachange

emi "Yeah, sure! That sounds great!"

show emi excited_amused_close at center
with characlose

"As if to signal the end of the conversation, she leans in and kisses me."

"The rest of the night is not spent worrying about exams."

stop music fadeout 2.0

scene black
with dissolve

# Hooray for Socks (Emi Act 4 Makeup Sex)
label en_delewd_E31:
scene bg school_gate_ss
with shorttimeskip

"Emi's mother drives us back to Yamaku. The trip back is very quiet."

show emicas neutral_close_ss
with charaenter

"We wave goodbye as the car drives off, and I glance down at the girl leaning on my arm."

hi "How are you feeling?"

show emicas awayfrown_close_ss
with charachange

"Emi shrugs noncommittally."

show emicas frown_close_ss
with charachange

emi "I'll be fine. Come on, let's go."

scene bg school_dormext_full_ss
with locationskip

"We pause outside the girls' dorm and I turn to face Emi, ready to say goodbye."

show emicas weaksmile_close_ss
with charaenter

emi "Why don't you come up for a while?"

hi "Okay."

scene bg school_girlsdormhall_ss
with locationskip

"The walk up to her room is in silence. I'm not sure why I supposed I'd be turned away at the door."

"I guess I just assumed she'd want to be alone."

"Her mom, the nurse, hell, everyone who knew the significance of today seemed to think it best to leave Emi alone."

"But she took me into the graveyard with her. She told me the whole story of what happened on the day she lost her legs."

"She wanted me around. The significance of this does not escape me."

play sound sfx_dooropen

"Emi opens the door and steps into her room, not even bothering to invite me in, holding the door for me expectantly."

scene bg school_dormemi_ss at left
with locationskip

play sound sfx_doorclose

"I step in, and the door swings shut behind me."

show emicas weaksmile_close_ss
with charaenter

emi "Hey, can I ask you a favor?"

hi "Sure. Can't guarantee I'll do it, but…"

show emicas closedsmile_close_ss
with charachange

"Emi giggles and pulls me into a kiss that starts out soft but deepens into something almost desperate."

show emicas smile_close_ss
with charachange

emi "Stay with me? Please?"

"Her voice has dropped to a whisper, the question is barely audible over the sound of my own breathing."

"There's something about the way that she asks that question, the hesitancy in it, the quiet voice, that makes me think she doesn't mean tonight."

"No, she means exactly what she said. 'Stay with me.' Not 'tonight' or 'forever,' because both of us know there's no such thing as forever."

"There's no time limit to her request, there's just the request."

"The favor."

"Can I do that?"

"Can I stay with her?"

hi "Of course."

label en_delewd_E31h:


label en_delewd_E31x:
scene bg school_dormemi_ss at right
with shorttimeskip

"I collapse next to Emi, who almost immediately curls against me, smiling."

"For a while, we lay in silence, savoring the feeling of being next to one another."

"Emi is the first to speak."

show emicas smile_close_ss
with charaenter

emi "Hey, Hisao."

hi "Hmm?"

show emicas closedsmile_close_ss
with charachange

emi "Thanks for coming with me today."

"I smile and plant a kiss on her head."

show emicas blush_close_ss
with charachange

hi "Of course. My pleasure."

show emicas closedsmile_close_ss
with charachange

"Emi snuggles closer, and I can feel her breathing begin to slacken as she begins to drift off to sleep."

"Just as she's about to fall asleep, she wakes up enough to mutter a single sentence."

emi "I love you, Hisao."

"Then she's out like a light, leaving me feeling like I'm on top of the world."

"I draw the slumbering Emi as close as possible, pull the covers over us to keep the chill off, and fall asleep as happy as I've ever been."

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve

return