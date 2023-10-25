# Whispered Touch (Hanako Act 4 Undressing)
label en_delewd_H29:
scene bg school_scienceroom
with locationchange

play music music_normal fadein 2.0

"Finally reaching the classroom after the usual walk from the dormitories, I step inside. My eyes immediately turn to the third seat from the left in the back row; Hanako's seat."

"It's empty, and after glancing around the classroom, it looks like she isn't here yet. The two girls from the newspaper club are here in the two seats to the left of Hanako's, as are Shizune and Misha, but that's about it."

"We exchange morning greetings before I take my seat. I have to admit that this is a bit of a relief. This gives me at least a few more minutes to think."

"Not that I haven't been doing so previously; ever since our trip to town, Hanako's been on my mind."

"I still don't know what to make of my relationship to Hanako. I like her, I can admit that much to myself. I want to protect and shield her from the pain she feels. I really don't think my feelings are just those of friendship any more."

"But that said… I feel like I don't even know her."

"If I made a move on her, how would she take it? Is she in an emotional state that allows her to make a reasonable decision about a relationship? How would she cope with anything that might happen afterwards?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_footsteps_hard fadein 4.0

"There's also the possibility that I'm just completely misinterpreting Hanako; not a difficult thing to do with someone whose social skills seem to be so underdeveloped."

"The sound of footsteps comes up to the door, making me perk up."

stop ambient fadeout 0.3

show miki invis:
    right
    xpos 1.1
with None

show miki whistle at right
with dissolvecharamove

"It ends up just being Miki."

show miki smile
with charachange

show miki invis at Position (xpos=0.9)
with dissolvecharamove

"She barely acknowledges my existence when I accidentally make eye contact with her. I'm about to look away, but another person comes in not long after she takes her seat."

show hanako invis:
    right
    xpos 1.1
with None

show hanako emb_downtimid at right
with dissolvecharamove

stop music fadeout 2.0

"I feel myself freeze as I see Hanako enter. This isn't a rational reaction, but I have no idea about how I should act or what I should say to her."

show hanako emb_timid
with charachange

"For a moment, our eyes meet."

show hanako emb_downtimid
with charachange

show hanako invis at Position (xpos=0.9)
with dissolvecharamove

"And then, just as quickly, she looks away and moves to her seat without saying a single word."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"As is now usual for the period following classes, my face is buried deep in a book that I find thoroughly uninteresting."

"Studying is not something that comes naturally to me. I didn't study a lot before coming to Yamaku, and until now I've largely managed to coast through on talent alone. It's frustrating that I can't do that any more."

"Judging by the faces of the other few students in the library, I don't think I'm alone in my distaste for this. Misery loves company, I suppose."

"I decided to spend lunchtime with Hanako, since we haven't had lunch together for a while now. I may as well have spent the time studying, though; aside from pathetically small snippets of smalltalk, there was barely a word said between us."

"Why does she keep doing this to me? I just want to protect her, to be there for her, but every time I feel like we're coming closer, we end up further away."

ha "A-are you busy…?"

$ renpy.music.set_volume(0.0, 0.3, channel="music")

show hanako defarms_shock_ss at center
with vpunch

hi "Hanako!?"

"My head whips around in surprise, causing her to retreat in fright."

show hanako emb_downsad_ss
with charachange

"That was bad timing. If I hadn't been thinking about her at that very moment, I probably wouldn't have been nearly so startled."

$ renpy.music.set_volume(1.0, 5.0, channel="music")

hi "Sorry, you just startled me."

"I find myself staring at her longer than I should, so I go back to the text lying on the table in front of me. I feel more like I'm just staring at the words rather than actually reading."

"I get the feeling Hanako can notice this as well, so I sigh and close the book."

hi "What's up?"

show hanako emb_sad_ss
with charachange

ha "I was just… w-wondering what you were r-reading…"

"She looks a little downcast after my reaction to seeing her. Giving up on the prospect of getting any more work done, I get up and return the book to its place on a nearby shelf."

hi "Just an English textbook."

show hanako basic_normal_ss
with charachange

ha "H-has it helped?"

hi "It helped me realize that I don't like English, yeah."

show hanako basic_smile_ss
with charachange

"Hanako gives a small giggle. I may muse on the strange state of our friendship, but I do know that such little gestures are things that I wouldn't see were I not at least some distance closer to her than when we first met."

"I look at her for a moment, thinking about what I do and don't know about her. It's a slightly depressing topic."

show hanako basic_worry_ss
with charachange

ha "I-is something… wrong?"

stop music fadeout 5.0

"If I want to know more about her, maybe I should stop being so evasive about it."

"Talking with Lilly as an equal rather than being constantly in fear of causing her to become upset worked fine, so I should just try a straightforward approach with Hanako as well."

hi "Hey Hanako, do you mind if I ask you a question?"

show hanako cover_worry_ss
with charachange

ha "I-I don't mind."

hi "I… want to know what your life was like. Your life before coming to Yamaku."

show hanako emb_blushing_ss
with charachange

"She hesitates. I briefly consider backing off, but she seems to be taking the question quite seriously."

"I sit and watch her, silently letting her take her time. She's not making eye contact with me, and looks almost as if she's arguing with herself into letting herself open up to me more."

"Her answer finally comes in a stiff, almost reluctant nod. She looks far more tense than she did before I'd asked."

show hanako basic_worry_ss
with charachange

ha "Okay. B-but in return… you have to t-tell me about your life as well…"

hide hanako
with charaexit

"I nod, and follow her as she begins to walk out the library so we can talk."

scene bg school_hallway3
show hanako basic_normal at center
with locationchange

play music music_serene fadein 0.5

"By now most of the students have already left the main building, so apart from a few people hovering around club rooms, the hallways are largely empty."

hi "I guess… we'll start with coming to Yamaku."

hi "Let's see… I was in the hospital when my parents first told me about Yamaku Academy."

hi "The doctors told me I shouldn't go to my old school any more. My parents agreed and persuaded me to apply for Yamaku, even though it would mean living away from them for the first time."

show hanako cover_worry
with charachange

ha "It must have… been hard for you."

hi "Well… yeah, I have to admit that it was. My parents both work long hours and full-time, so having to live reasonably independently wasn't anything new to me. It was the fact that I was going to a school for disabled students that hit hardest, I think."

hi "And you?"

scene bg school_staircase2
show hanako emb_downtimid_close at right
with locationchange

"A small group of chatting girls passes us as we near the stairs, with Hanako pressing herself tightly to my side until we reach the ground floor. She doesn't usually come this close while just walking in the school, so I'm left a little put off."

show hanako emb_downsad_close
with charachange

ha "The staff at the o-orphanage offered me some options on what I could do. Middle school… hadn't been good, so I thought that Yamaku might be better."

ha "It was isolated, and I thought it might be easier to get by here with most of the others being disabled."

scene bg school_lobby_ss
with locationchange

"It's pretty ironic that the reasons Hanako looked forward to Yamaku are the exact reasons I hated the idea. To me, it felt like I was being shunted somewhere away from society, and everyone I knew. To Hanako, that was probably an inviting prospect."

hi "What was life like at the orphanage?"

show hanako emb_timid_ss at center
with charaenter

ha "It was… okay. The staff there were nice, and they took care of us. The children there didn't talk to me much, but I didn't really want to talk with them either, so I didn't mind."

show hanako emb_downsmile_ss
with charachange

ha "The orphanage had a little library, so I started to read to pass the time. The staff didn't mind it, because it made me easier to handle than many of the other children."

hi "You didn't make any friends there?"

show hanako basic_worry_ss
with charachange

ha "No. I think… my life was on hold… during that time. I knew that, but I didn't mind."

"To think her life was on hold for all that time, though… depending on when the fire happened, that was a huge chunk of her life. No parents, no friends, apparently no relatives…"

scene bg school_courtyard_ss
with locationchange

"We walk through the door into the courtyard. I expect to need to avert my eyes from the sun, but by now it's well into sunset."

show hanako emb_timid_ss at center
with charaenter

"Hanako's eyes keep flicking to me, so I look away from her for a bit."

ha "What was it like in the hospital?"

"I quickly clear my thoughts and try to refocus them."

"I hesitate for a bit, but I know that I have to tell her. We're close enough for her to feel comfortable telling me this, so it's only fair that I reciprocate."

hi "It was okay at times, but at others, it was pretty bad. At the beginning, everyone sent their sympathies, and came to visit often. It was just like breaking an arm or something."

hi "Meeting all my friends was one of the good times. Iwanako came in often as well; more often than anyone else."

hi "But there were bad times, too. When my friends slowly stopped visiting, I began to realize how grave my situation was. It reminded me that this wasn't just a broken limb, but that I was now a different person than before."

hi "Even the times Iwanako would spend with me became torturous. By the end, we were reduced to silence, whereas before, she'd be talking constantly."

"But that's how Iwanako always was. She may have been a fragile person, but she would talk constantly to try and hide that fact. Not about anything in particular, just… talk."

hi "I think the three lowest points would have been when my parents told me I wouldn't be going to my old school any more, my birthday passing while in the hospital, and… when Iwanako left for the last time."

scene bg school_gardens_ss
with locationchange

"We leave the school buildings behind us as we begin to follow the main path through the gardens. There may have been the odd bystander in the school buildings, but outside, we're practically alone."

show hanako basic_worry_ss at center
with charaenter

ha "What was your middle school like?"

hi "I liked it. I grew up in a really metropolitan area, and the middle school was nearby, so it was pretty crowded. I didn't mind it, probably because I'm used to being in crowds and around lots of other people."

hi "I got good grades, and I played soccer with my friends. I spent a fair bit of time hanging out with them after school as well. Did get teased a bit over my hair, though."

show hanako def_worry_ss
with charachange

ha "Your hair?"

"I grimace a little as I put a hand over my hair to cover it."

hi "I'd keep getting tufts and strands that refused to flatten or stay where I wanted them, and my mother wouldn't let me just get my hair shaved. It had a habit of popping out, no matter how much I tried to brush it down."

show hanako basic_smile_ss
with charachange

ha "It still does, a little."

hi "I was worried I'd get that reply."

show hanako cover_worry_ss
with charachange

ha "S-sorry, I didn't mean to…!"

"I give a mild laugh and wave it off."

hi "It's fine, I know it still does."

"It feels strange to have someone act so interested in my past. If it were anyone else I'd think they were just acting polite, but that's something I really don't think Hanako would do. Or if she did, she'd do it so badly that it would be obvious."

scene bg school_dormhallground
show hanako emb_downtimid_close at right
with locationskip

"There are a number of girls in the common room on the ground floor, and Hanako presses herself to my side once more as we pass them. I expect her to break off, but instead she continues to cling onto me as we walk towards the stairway."

stop music fadeout 5.0

"Something about the way she's holding onto me feels… different from the usual."

scene bg school_girlsdormhall
with locationchange

"I'm left deep in thought as we walk up the stairs and down the hallway. It's only when we stop that I look up and realize that I've been following her without question."

hi "Why did we come to your dormitory room?"

show hanako basic_distant_close at center
with charaenter

"She looks straight at the door, without so much as a glance in my direction."

hi "Hanako?"

show hanako basic_normal_close
with charachange

"She moves to answer, but stops herself."

hide hanako
with charaexit

play sound sfx_dooropen

"Instead, she silently breaks from my side, opens her door, and steps inside."

"I look up and down the hallway, a bit lost as to exactly what I should do. Shrugging, I decide to follow her since I don't have any reason to do otherwise."

scene bg school_dormhanako_ss
show hanako basic_normal_ss at center
with locationchange

"Hanako stands in the middle of her room and looks straight at me. It's unnerving when she does this, as it's such an unusual action for her. I open my mouth to speak, but she preempts me."

ha "Could you… close and lock the door?"

"Hanako's hand reaches for her chest, grabbing her blouse at her heart."

hide hanako
with charaexit

play sound sfx_doorclose
with Pause (0.8)                                                                                                                            

play sound sfx_lock

"I turn and lock the door shut, then freeze."

"The atmosphere is beginning to feel quite strange. This feeling is only made more profound when I hear the curtains being pulled behind me."

"It's going to be night soon. We're a guy, and a girl, in a bedroom. She's closing the curtains, and I'm shutting and locking the door. She can't… she can't really have that in mind… can she?"

"I gulp and turn around very, very slowly. Hanako is in the center of the room, but hasn't turned back to face me."

show hanako emb_downtimid_ss at center
with charaenter

ha "You told me about your past, so I have to tell you mine."

"She takes a deep, shuddering breath, and pauses for a number of seconds. Her hands move to her ribbon and begin to tug, all but confirming my thoughts."

hi "H-Hanako…"

show hanako emb_timid_ss
with charachange

ha "P-please… don't say anything."

"I obediently stay hushed as she slips off her ribbon and continues to unbutton her blouse, before working the clip on her bra. The process is slow. Perhaps it just feels slow because of what she's doing. I'm not sure."

"Frozen to the spot, all I can do is watch as Hanako, hands trembling, unclips her skirt and lets it drop to the ground."

play music music_hanako fadein 1.0

scene ev hanako_scars:
with whiteout

"Finally, she takes her blouse in her hands and draws it off, her bra falling from her shoulders. And so, Hanako stands in the middle of the room all but bared, save for her stockings and underwear."

ha "This is me. All… of me."

show ev hanako_scars_large:
    xalign 0.6 yalign 0.4 subpixel True
    acdc_warp 30.0 xalign 1.0 yalign 0.0
with locationchange

"My eyes are immediately drawn to the scarring on her back. The skin on her right side is of a similar texture to that of her face, but it's also stretched taut and covering a much larger area. The scarring is by far the worst on the shoulder, buttock, and thigh."

"Just as my heart attack redefined my life… this is the event that redefined Hanako's."

"If I'd seen this when I first met her, I'd have been shocked. Not only at the sight, but also at the idea that something like this was survivable."

"But after having had time to get used to the idea, and after seeing the scars on her face, hands and collar, my reaction is more measured. My reaction right now is not due to her scarring, but to her body."

ha "The fire happened when I was eight years old. It was night, and we were sleeping when it started."

"Hanako's voice trembles, the shaking of her blouse giving away the fact that her hands are doing just the same."

ha "I… curled up into a ball… when the fire swept over me. My mother… tried to shield me. Th-that's the only reason… I lived…"

"Hanako's eyes begin to moisten, her voice cracking under the combined pressure of exposing herself to me like this, and reliving those painful memories from so long ago."

"I want to say something, anything, to make her feel better. I can't, though. I feel completely useless when faced with a situation like this. She's forcing herself to come so close, yet it's at times like this that I feel most distant to her."

ha "I'm sorry… for making you see this."

"There's no point in denying the obvious. I think what I should say now, and what Hanako wants me to say now, is the truth. What I genuinely, honestly, believe."

hi "It doesn't matter. You're a wonderful person, Hanako. Your body doesn't change that."

"She looks at me for a long time, her breathing uneven as she tries to remain steady amidst the emotions we're both feeling. It feels less like she's looking at me than she's looking through me."

"I slowly walk towards her, and gently place my hands on her shoulders as she lets go of her blouse. She gasps a little; not in fright, but in simple startlement."

"Being so close to her causes my mind to become a jumble of feelings. The scarring on her shoulder, plain to see and leather-like to the touch, conflicts strangely with her otherwise soft skin and silky dark hair."

"Hanako is a girl, with all that entails. She's taller than usual for a woman, but still has curves in all the right places. The nape of her neck, just visible thanks to her hair slung over her shoulder, is alluring."

ha "I know… that I'm not pretty… like Lilly. I just… wanted you… to see me. The real me."

hi "I've already seen the real you, though. You didn't need to take off your clothes for that."

scene bg school_dormhanako_ss
with locationchange

"Her lips are open, just a little. She lets out a sharp breath as, without thinking, I breathlessly lean forwards and press my lips to hers."

"The kiss only lasts for a fleeting moment before our faces part, our breathing quick and nervous. The feeling of Hanako's mouth lingers, and her eyes remain locked to mine."


"Trembling a little myself, I remove my tie and begin undoing the buttons of my shirt. Hanako remains standing where she is, looking at the ground in front of her rather than watching me undress."

"On the one hand, I'm thankful for that. I've always been somewhat self-conscious of my body, but my scarring has made that quite a lot worse. On the other, though, this atmosphere feels very strange."


"My shirt falls to the floor in a heap, as untidy and crumpled as Hanako's blouse and skirt. Hanako's entire body visibly flinches at the sound of the zipper on my trousers being pulled down."

"My trousers join my shirt on Hanako's floor next to the bed, as do my socks in short measure."

hi "Hanako…"

"She gives a nod without so much as glancing at me, and makes her way to the bed as I do. She walks as if her legs were wooden sticks. I'd find it amusing if I weren't doing exactly the same thing."

"I take the initiative, turning around and sitting on the side of the bed. I look to her face to invite her to take a seat either next to me or in front of me, but end up awkwardly looking down to stop myself from staring at her body."

label en_delewd_H29h:

"I don't know which one of us is more apprehensive right now."

"I push myself back onto the bed. For her part, she lies down with her head on her pillow, breathing heavily all the while."

"Hanako lying in front of me, her chest heaving, her face flushed, and her eyes looking into mine… her scars just make her look all the more unique. I'm left without words that she'd allow me to see her like this."

"I bring myself closer to her, closing my hands on her waist."

"Hanako's entire body tenses as I bring myself closer to her, her eyes widening. She's… scared?"

"I take a long breath, before realizing something I should have thought of before. I close my eyes and concentrate deeply."

"My heart thumps away as I focus my mind on its beating. It's faster than usual, of course, but the beat is regular. I… think… I can keep it in check."

ha "Are you… okay…?"

"I open my eyes and look at her. I guess that must have looked pretty worrying to someone else watching me."

hi "I'm okay. I was just making sure that I was."

"She hesitates a little before nodding. She looks a little less afraid than before, so maybe showing her that I was also worried helped reassure her."

"I lean over her and press my lips to hers, our tongues tentatively touching."

label en_delewd_H29x:

scene bg school_dormhanako_ni
show white
with Dissolve(3.0)

window show

"The sound of Hanako's breathing and my own rings in my ears, almost painfully loudly."

stop music fadeout 10.0

show white:
    linear 10.0 alpha 0.0

"As I hold myself over her, suddenly my arms almost give way and my vision distorts, as if someone's grabbed it and pulled sideways. I let myself fall sideways onto the bed beside Hanako, for fear of falling onto her instead."

"We both lie beside each other, pressed against one another in order to fit on a bed made for a single person. My eyes try to focus on the ceiling, to not much success. Pulling a blanket over us to stave off the cold is all I can do."

"The only sound in the room is that of our breathing."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"My vision slowly begins to return to normal as I continue to stare at the ceiling, but my limbs still feel like jelly. I try to concentrate on my chest, and find its beat irregular and mildly painful."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"This is a dangerous time. I have to think this through and not panic, lest I make my situation any worse."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"With a huge effort, I take control of my erratic breathing, forcing myself to make long, deep breaths. I count half a dozen before I start to feel physically calm again, and press my hand to my chest to assure myself."

"My heartbeat's back to normal. I'm okay."

scene ev hanako_after_worry
with locationchange

play music music_twinkle fadein 1.0

"I turn my face towards Hanako, who's already looking at me. There's definitely a look of concern. She's realized what happened."

hi "I'm… okay. Everything's… back to normal."

"I find myself barely able to get the words out between breaths. Why did my body have to do this right now?"

scene ev hanako_after_smile
with charachange

"All thoughts of my heart, though, are pushed aside as I see the wide smile forming on Hanako's face."

"As always, I smile back without another thought. Hanako's smile has always been infectious in its almost childlike sweetness and earnesty, something that sets her apart from anyone else I know."

"Right now… we don't need words. Everything we want to communicate to each other, we can share just fine without them."

stop music fadeout 2.0

scene black
with shuteye

return