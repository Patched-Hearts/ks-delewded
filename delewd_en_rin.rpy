# Signal Interference (Rin Act 2 High Sick Visit)
label en_delewd_R15:
scene bg school_girlsdormhall
with locationchange

"Even though I'm feeling more energetic, I'm still hesitant about going over there to talk to Rin."

"It's not until two days later, on Friday, that I finally gather enough courage to enter the girls' dorm. I ask the first person I meet inside for directions to Rin's room."



play sound sfx_doorknock2

"I knock on Rin's unmarked door and wait."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_rustling
$ renpy.music.set_volume(1.0, 10.0, channel="sound")

"After a few seconds of silence I hear something rustling inside the room. I start wondering if maybe I should've brought something for her, like a can of warm coffee or some oranges. I could have peeled them for her. Well, too late now."

"The door opens soundlessly - it was already unlocked - and I find myself staring at Rin, who stares back at me."

"She looks like she just got out of bed, with her hair all messed up."

show rinpan basic_deadpanamused at Slide(1.05,1.0,1.0,1.0,0.5)
with charaenter

"…and barely any clothes on."

"…"

show rinpan basic_amused at right
with charachange

rin "Hellooooo."

play music music_rin fadein 0.5

"There is a strange, stupid-looking smile on Rin's face. I'm not exactly sure why."

"Rin smiles so rarely that it seems to be out of place every time. Especially so now, given her partially undressed state. Said state makes me feel extremely conflicted about whether or not this was a good idea."

"Her cheeks are flushed rose-red, contrasting with the milky-pale complexion of a person who doesn't get enough sunlight. Her forehead looks sweaty, as though she might have a fever."

hi "Um, hi."

show rinpan basic_absent
with charachange

"Now what? I didn't plan anything further than this, and Rin is staring at me with those expectant eyes of hers again."

"Something about this situation gives me very strange vibes. Her eyes are even more vacant than usual and she seems to have a hard time focusing them on anything."

"The lack of clothing is disturbing, but since she herself doesn't seem to be bothered, why should I be?"

"I keep telling myself that."

hi "Err, I thought I'd pay you a visit since you haven't been at the art club… and I wanted to talk with you and wish you well."

"Rin doesn't show any sign of recognizing what I just said, making me wonder if she actually understood my words, or if she even heard them."

"Maybe it's the fever making her groggy; she might've actually been asleep before I came over."

show rinpan basic_deadpan
with charachange

rin "Okay."

show rinpan basic_deadpan:
    easeout 0.5 alpha 0.0 xpos 1.05
with Pause(0.5)

hide rinpan
with None

"She turns on her heel and withdraws from the door, walking back inside the small room. From the doorway I can see her walk to her bed and half fall down, half sit down on the messy pile of bedsheets."

"The open doorway seems to be more of an obstacle in my mind than the closed door was, but since Rin doesn't say anything else, I step through it, and into her room."

scene bg school_dormrin
with locationchange

"Rin is on her bed leaning against the wall, leaving the only chair in the room for me."

"She keeps quiet even after I sit down, so maybe she meant to invite me in but just forgot to say so aloud? An implied invitation, as it were."

show rinpan basic_deadpanamused at twoleft
with charaenter

rin "Very exciting. Nobody has visited me before."

"The breaking of the silence draws my attention from the room to its inhabitant, who currently seems to be in the middle of a very profound thought process."

show rinpan basic_awayabsent
with charachange

rin "Actually that was not true. About visiting. But Emi doesn't count even if she visits."

show rinpan basic_deadpan
with charachange

rin "She always pampers me too much. I think she's having too much fun."

show rinpan basic_absent
with charachange

rin "I think I've forgot how to put a bra on by myself."

"She looks groggily down at her chest."

show rinpan basic_surprised
with charachange

rin "Which is probably why I don't have one on, now that I think about it."

"I haven't failed to notice that Rin doesn't have her shirt buttoned up either, but I try to keep my eyes strictly locked on hers."

"It's rather evident that she's not a very body-conscious person. My own body, however, is quite conscious of hers right now."

show rinpan relaxed_sleepy
with charachange

rin "She came to wake me up at half past seven today!"

show rinpan relaxed_doubt
with charachange

rin "Can you imagine that?"

"She pauses for a while and glances up at my dumbfounded face."

show rinpan basic_lucid
with charachange

rin "On second thought, you probably can. It's not like that reverse rainbow fish I tried to imagine earlier. That was hard."

hi "Well yes, that seems like a pretty normal time to wake up if you want to go to class in the morning."

"I'm trying to sound as reasonable as possible to counteract Rin's unreasonable annoyance."

show rinpan basic_deadpanupset
with charachange

rin "Told her to sod off."

show rinpan relaxed_nonchalant
with charachange

rin "She gave me these meds and told me to take them."

"I follow her eyes to the night table and then to the pill bottle sitting on top of it."

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"I pick it up and turn it around to look at the label so I can see what kind of medication Emi brought."

"Active ingredient… codeine?"

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

hi "You took all of these?"

show rinpan relaxed_surprised
with charachange

rin "No. Yes. I've been eating some since there's so many of them. Seem to make this thing not so bad."

show rinpan relaxed_sleepy
with charachange

rin "Actually… I think I'm feeling just fine."

"Her head lolls round and round, making it look like she is either trying to stretch her neck muscles or possibly pass out."

"She took several of these pills? Can that be safe? At least it's bound to have some side effects… which I'm afraid I am witnessing right now."

show rinpan basic_deadpanupset
with charachange

rin "I am feeling just fine… I am fine… just someone take this buzzing away from my head. I can't think straight."

"The annoyed expression returns to Rin's face."

show rinpan basic_upset
with charachange

rin "It's like many of those insect things… or one really big insect thing."

show rinpan basic_awayabsent
with charachange

rin "With lots of wings. Very much color and everything."

show rinpan basic_absent
with charachange

rin "What's the word for those?"

show rinpan basic_deadpanamused
with charachange

rin "Oh, never mind. I remembered. It's butterflies."

"She smiles slightly at her last observation. The small pause in her monologue is not long enough for me to dare saying something that could potentially, but not likely, salvage this discussion."

show rinpan basic_amused
with charachange

rin "I love butterflies. They are the best animal."

show rinpan basic_awayabsent
with charachange

rin "Did you see any on your way here?"

show rinpan basic_deadpansurprised
with charachange

rin "Hisao."

"She utters my name as an afterthought, possibly to make clear that she is now addressing me instead of just speaking her mind to whoever might be listening."

"This odd situation has left me speechless more or less since the moment Rin first opened her mouth. Now that she herself doesn't seem to have anything else to add, silence fills the small room."

"It makes me glance around again in an attempt to find something to talk about."

"Rin's room is about as small as mine. The big window, which takes up most of the wall furthest from the door, opens to the east just like mine."

"It looks very normal, which strikes me as strange. I expected something more… different."

"About a dozen paintings - most of them in Rin's signature abstract style - and a few art posters are taking up almost all of the available wall space, but that's about the only real difference between her room and mine."

"The room is not exactly ascetic, but it doesn't look like what I'd expected from a girl's room, either."

"A faint smell of art… of paint and paper is floating in the air. It's the same smell the art room has."

"Rin isn't too concerned about being tidy, it seems; everything she owns seems to be arranged in various piles around her room."

hi "Your room looks nice."

"It's an empty sentence one uses to fill empty spaces in conversations, but my wits are failing me pretty hard right now."

show rinpan relaxed_nonchalant
with charachange

rin "Yeah. Would you like me to show you the places?"

"She looks down at her half-open shirt quizzically, making me inadvertently follow her gaze to her chest."

show rinpan relaxed_sleepy
with charachange

rin "Oh… I guess I already did."

"I can't deny that, no matter how hard I tried to act properly."

show rinpan basic_absent
with charachange

rin "It is very nice that you came to see me."

show rinpan basic_deadpancontemplation
with charachange

rin "It makes me feel very… what's that word… you know, the one about things and stuff."

show rinpan basic_lucid
with charachange

rin "Anyway, you came."

"Rin's rambling makes me remember that I actually came here for a reason."

hi "Hey, about what we talked on Monday. On the rooftop, remember?"

stop music fadeout 4.0

show rinpan relaxed_surprised
with charachange

rin "Hmmm?"

"Rin doesn't seem to be exactly attentive right now, not that she ever is. I plow ahead and get it off my chest anyway."

hi "I just wanted to tell you that I'm going to be better from now on, I guess."

hi "I hate being pathetic, so I decided that I'm not going to be, any more."

hi "I guess… that's all."

show rinpan relaxed_sleepy
with charachange

rin "Okay. Isn't that good?"

"The blurry words flow out of her lips slowly and uncontrollably."

show rinpan relaxed_nonchalant
with charachange

rin "I'm happy for you I think. That's what I think."

show rinpan basic_deadpannormal
with charachange

rin "You shouldn't look so sad all the time. I mean, looking sad is fine if you are not sad, but you look sad like you actually sad."

show rinpan basic_deadpan
with charachange

rin "That's no good."

show rinpan basic_awayabsent
with charachange

play music music_rin fadein 0.5

rin "Are you going on some training camp where they make men out of boys? Or mountaintop meditation?"

hi "No, I don't think so."

show rinpan basic_absent
with charachange

rin "Oh. I guess that's fine too."

"The sentences come out of her mouth, and probably her brain, one at a time with a small pause between each, making her gibberish hard to understand."

show rinpan relaxed_doubt
with charachange

rin "I just think it seemed like a good idea. Maybe it's not."

"Rin finishes with one more line, getting to say the last word over herself, an impressive display of what I can only describe as mental shadowboxing."

hi "While I'm embarrassing myself, might as well tell you that I'm sorry that I said some stupid things to you last week."

hi "It's your own business to decide what you're going to do."

show rinpan basic_absent
with charachange

"She seems to not register my words first, but then understanding lights in her eyes and she waves her head around in a way that could be interpreted as anything."

show rinpan basic_deadpancontemplation
with charachange

rin "It's OK."

show rinpan basic_lucid
with charachange

rin "I probably said stupid things too."

rin "It's just sometimes a bit hard to keep my thoughts the way I like them."

show rinpan relaxed_nonchalant
with charachange

rin "They are not very straight, at least most of the time."

rin "Not that I want to have them straight… I just wish they were at least in some shape."

rin "Round is fine too. But I need more definition."

show rinpan relaxed_boredom
with charachange

rin "My thoughts are very messy."

show rinpan relaxed_sleepy
with charachange

rin "Messy."

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

scene ev rin_high_frown
with locationchange




"She repeats the word melancholically, then flops lying down on her bed and nuzzles her head against her pillow, shutting her eyes."

rin "Enough. Tired. You should go. I'm going to sleep again."

scene ev rin_high_oneeye
with locationchange

"She opens one of her eyes to look at me."




rin "Was it you who likes to look at sleeping girls? Or someone else?"

rin "Maybe there were many of those."

scene ev rin_high_frown
with locationchange

rin "I can't remember."




rin "You can stay if you want."

hi "No no, I'll leave. I have to… do homework anyway."

stop music fadeout 2.0




scene bg school_dormrin
with locationchange

"I stand up from the chair and take a step towards the door."

rin "Wait."

"Her request stops me in my tracks, not that I intended to scoot off right away."

scene ev rin_high_grin
with locationchange






"I look over my shoulder at the girl lying on her bed, again with the strangest kind of smile on her features."

"She should smile more often."

rin "I can walk you to the door."

scene ev rin_high_grinwide
with locationchange




rin "It's the least a gentleman can do."




scene ev rin_high_smile
with locationchange

"Rin giggles like a little kid, making me beyond absolutely certain that she took far too much of her cold medication today."

rin "I have always wanted to say that."

scene bg school_dormrin
with locationchange

show rinpan invis:
    twoleft
    ypos 1.1
with None

show rinpan basic_deadpandelight at twoleft
with dissolvecharamove

"Slowly and with difficulty, Rin first rises to a sitting position again, then she stands up with even more difficulty and more slowly still."

"As if guided by some masculine automation, my eyes instantly lower to the curve of her thighs and the striped panties, at which point my manners force me to lift my gaze back to Rin's eye level."

"It's getting almost too hard to do that."

"Rin is standing, although barely. It looks like she has trouble keeping her usually decent balance; again, probably a side effect of the medicine."

show rinpan basic_deadpandelight:
    ease 1.0 center
with None

show rinpan basic_deadpandelight_close:
    twoleft
    ease 1.0 center
with Dissolve(1.0)

"She takes an unsteady step towards me, then another smaller one as she notices that it's not a good idea to try to take big steps."

"I feel my muscles tense as I prepare to catch Rin if she falls down."

play music music_twinkle fadein 3.0

scene ev rin_kiss:
    center
    yalign 0.0 zoom 4.0 subpixel True
    easein 0.4 zoom 1.05
    easein 5.0 zoom 1.0
with flash

"She manages to take two more steps before she falls against me. To my surprise, neither her downwards momentum nor our slight height difference are able to stop Rin from pressing her heart-shaped lips squarely against mine."

"As our lips part after a confusing moment of nothing but the taste of… Rin, I look down at her, trying to find some explanation for this bewildering event."

$ renpy.music.set_volume(0.7, 2.0, channel="music")

scene bg school_dormrin
show rinpan basic_deadpandelight_close at center
with locationchange

"The euphoric smile of a madman broadens on Rin's lips again and—"

show rinpan relaxed_sleepy_close
with charachange

rin "I wonder if I will remember this tomorrow."

"I am absolutely stumped on how to respond."

show rinpan relaxed_sleepy_close:
    ease 1.0 twoleft
with None

show rinpan relaxed_sleepy:
    center
    ease 1.0 twoleft
with Dissolve(1.0)

"Rin takes a step backwards, separating her body from mine, and making me only now realize that they were even connected in the first place."

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

"The second step is actually a fall backwards, luckily straight onto her bed."

"The soft thud Rin's thin body makes against the mattress breaks the silence."

scene ev rin_high_open
with locationchange

"I move quickly over to her to see if she hurt herself, only to be met with the peaceful face of dreaming."

"Rin sleeps."

"She is lying diagonally across the bed, somehow managing to have simultaneously fallen asleep while standing up, and fallen down in a way that she didn't injure herself."

"Fool's luck."

scene ev rin_high_sleep
with locationchange

"I tuck Rin in, covering her with the sheets as well as I can."

"She feels very light, even though I am not that strong."

show ev rin_high_sleep:
    subpixel True xalign 1.0 yalign 0.0
    ease 10.0 zoom 1.1
with None

"I stand up to look at her, the oval-shaped face, the dark eyelashes shut against the feverish cheeks, the slender body covered with the pale sheets."

"Rin sleeps."

"A conflict - no. Conflicts, plural, churn inside of me. I think about calling a nurse to keep an eye on her, but decide against it. After taking one more glance at her peaceful face, I decide that she'll be fine."

"I do pocket the remaining pills, though."

stop music fadeout 5.0

scene bg school_girlsdormhall
with locationchange

"I exit the room, and close the door soundlessly behind me."

"I exhale deeply, only now realizing I had held my breath for the better part of a minute. Taking a moment to relax, I try to calm down my heart, racing like a jackrabbit."

$ suppress_window_after_timeskip = True

scene black
with dissolve

# Closer (Rin Act 3 Broken Masturbation)
label en_delewd_R27:
stop ambient fadeout 0.5

scene bg gallery_staircase
with locationchange

"I climb upstairs and enter carefully."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg gallery_atelier_ni
with locationchange

"The room is dark because of the quickly falling night, but I can see Rin, or rather her silhouette, sitting on the floor."

"So she's got her inspiration back like Sae said, and moved from easel to painting on the floor."

stop ambient fadeout 1.0

"Before I manage five steps I stop, frozen in my tracks."

scene ev rin_masturbate_away:
    truecenter
    subpixel True zoom 1.0
    acdc_warp 16.0 zoom 0.8
with whiteout

play music music_moonlight fadein 0.5

"Rin is sitting on the floor with her legs under her."

"Something in the atmosphere of the room changes, a little thing, not consciously noticeable, but it changes."

"Perhaps a timid current from the opened door, or a minute change in air pressure, the sound of my breathing (even though I notice I haven't taken a breath for many many seconds), the aura of my presence."

"That something catches Rin's senses."

show ev rin_masturbate_away:
    ease 0.5 zoom 0.8
with None

show ev rin_masturbate_surprise:
    ease 0.5 zoom 0.8
with charachange

"She freezes, and slowly turns to the door."

show ev rin_masturbate_away
with charachange

"Drooping her chin against her chest, she lets her mess of a hair hide her face from me even further."

"I feel like I should either walk out or walk to her, but I can't do either."

rin "I told you to stay away."

"Her words are… defeated, painful as if she was suffering."

"Rin doesn't have anything other than her shirt on."

"I can see the last wisps of the twilight against the pale skin of her thighs and bottom."

"There is no way I can back off any more, I lost that chance, so I do the next best thing."

"I quickly avert my gaze even though Rin doesn't see what I'm looking at."

hi "I'm sorry. I didn't think…"

show ev rin_masturbate_doubt
with charachange

rin "It's not like that…"

"Her voice is raspy, shivering from held back tears or something else."

"She is shaking, looking like she is physically in pain."

show ev rin_masturbate_frown
with charachange

rin "It's not like that. I…"

nvl clear

rinbabble "I had no idea what it really means to change but I know now you have no idea what I've had to do and all the things that pass through and I think I forget I really don't they just build up inside and grow and grow and grow until they flow out like a flow of everything that has ever been wrong I can't take it I can't think of the things I want because there's only so many things that I can think four six seven doesn't matter it's never enough I have to let this out I have to destroy forget it and nothing else—"
nvl clear

"Rin is mumbling her words into the air more than talking to me."

"It is the rambling, ranting, raving speech of a lunatic, even and steady in tone, but taking the form of a never-ending stream of words almost simultaneously spawning from between her lips."

"It feels like she forgot it is me who is present, or that someone actually is present. Maybe she vaguely recognizes what is real and what is not."

"Maybe in her mind I am a voice inside her head."

"I look down at Rin's sorry figure, cowering on the floor with only the white shirt of her usual attire on."

"It neither preserves her modesty that is gone nor her body warmth that she doesn't seem to care about."

"She looks more broken than I imagined a human person being capable of, and the hospital and school have given me some real perspective on that."

"I remember the hazy blue smoke, and myself wondering what Rin would do for the sake of art."

"The realization that Rin really is always serious hits me with its entire weight."

"She really and truly would destroy herself if her art required it."

"I thought she was so silly with her strange ways, talking about personal change as if it was something sudden and concrete, like waking up."

"I had no idea."

"This is her, laid bare in front of my eyes in all possible meanings of the word."

"Complete isolation here in the top floor of this building, in this room, in her mind."

"Day after day, working on her paintings with no heed paid to anything else."

"Breaking herself to reach that which she wishes to reach."

"I feel sad, scared, excited, disgusted, worried and a number of emotions I can't remember the name of now. I feel conflicted."

hi "I should go. I'm really sorry."

show ev rin_masturbate_away
with charachange

rin "It doesn't matter."

"My voice is dry and quiet, like sandpaper coming out of my throat. I really am sorry, sorry for seeing this."

"I don't want to see Rin like this."

"All I can see is her sadness. Her stress and despair. Is this what a 'limit' means? Why would - how could Sae and Nomiya let Rin go this far? Or is it me who is to blame?"

stop music fadeout 6.0

show ev rin_masturbate_hug
with charachange

"I almost walk out, right there, but at the last moment I turn around, steel myself and walk to Rin to crouch down behind her and lightly touch her forehead. She doesn't resist or react."

"I can't leave her like this. She's not well."

"She feels like she has a fever, freezing cold and burning hot at the same time. I wonder if she got sick from staying out all night with me back then. It seems she's prone to getting ill."

"There is a blanket on the couch, but I wrap my arms around Rin instead of fetching it."

"She does not resist my clumsy hug, only slumps her head lower, deepening the shadows hiding her face from me."

show ev rin_masturbate_hug:
    acdc_warp 40.0 zoom 1.0
with None

rin "What are you doing?"

hi "Nothing."

"I am not embracing her out of love, nor out of forgiveness; for am I in love, or is she sorry?"

"I just want to hug her."

"For a moment, the only sound in the room is her heavy breathing."

"My body warmth, shared between two people, is barely enough but slowly, painfully slowly it spreads from me to her."

"The small warmth returning to Rin makes me more conscious of her body against mine."

"Even in the darkness, I can feel the fleeting scent of Rin's hair, the sweat on her skin, the dried paint stuck in her shirt."

"I feel the hardness of her bones and the softness of her flesh."

"Her heartbeats echoing mine, out of rhythm just like always."

"The hot blood rushing inside me reminds me why I said what I said back then, why I came here even after that, why I am here tonight again."

"Why I am hugging her now to keep her safe against the cold and the sadness."

"Rin has really grown on me inside my heart, claiming a small part of it as her own without even particularly trying."

window hide

centered "Rin." with dissolve

window show

"Even if she wanted to push me away, I can't help this feeling."

hi "Are you all right, Rin?"

rin "I'm not."

rin "I… think I broke. I painted. I painted some really good things. Incredible."

rin "But it hurt me. I can't handle this."

"Her voice cuts out, as there are no more words for her to say."

"It's not an angry voice nor a sad voice."

"It is a lifeless voice."

"I pet her head and shoulders, the physical equivalent of saying 'there, there.' It's not like I could reassure her with the sweet nothings that people are supposed to say in this kind of situation."

"I'm not sure if she would even listen, or be reassured."

"She didn't react much to my embrace either, as if she didn't care."

"Maybe she doesn't."

"At least she doesn't care if she looks sad or not, there are no facades, no attempts to explain herself, no faux happiness."

label en_delewd_R27h:


label en_delewd_R27x:

rin "What will happen now?"

hi "I don't know. Nothing, I suppose. You look tired."

scene bg gallery_atelier_ni
with locationchange

show rinpan relaxed_sleepy_close_ni
with charachange

rin "I am tired. It feels strange. Like I lost something."

hi "Don't say something like that. I don't want to lose you."

show rinpan relaxed_surprised_close_ni
with charachange

rin "What does that mean? I'm not going anywhere."

hi "I'm afraid that you are. All the time."

"In that moment, I felt that it was not only Rin who lost something of hers. I felt like I was losing a part of myself, or maybe all of me."

"But if you were to ask what was it that I lost, I couldn't say, because I had already forgotten it."

"I broke another promise by coming out with my honest feelings to Rin. That's two in one day."

hi "I just - I hate the distance between you and me, so every time it gets a little bit closer I become afraid of losing it."

show rinpan relaxed_boredom_close_ni
with charachange

rin "That's weird."

hi "I guess so."

show rinpan basic_awayabsent_close_ni
with charachange

rin "Do you mind if I sleep a little - no, I guess you don't. You like watching, don't you?"

show rinpan basic_lucid_close_ni
with charachange

"She closes her eyes and swallows with a loud gulp, trying to relax herself, fighting against the urge to paint."

hi "Yes. Yes I do."

show rinpan invis_close:
    ypos 1.2
with Dissolvemove(2.0)

hide rinpan
with None

"Rin moves her body in my arms, searching for a comfortable position in our very uncomfortable position."

"She leans against me, closing her eyes, and lets one last long breath out before settling into the steady rhythm of sleep."

"With her last moment of awareness she whispers something to me but I can't hear it."

"Rin drifts deeper into sleep with a deep sigh that releases all remaining tension from her muscles."

"I try to shift around to place both of us more comfortably."

"It takes a while because I don't want to wake up Rin even though she probably wouldn't, but eventually I find a position I am somewhat comfortable with."

scene ovl rin_galleryskylight:
    truecenter
    zoom 0.8 subpixel True
    linear 30.0 zoom 1.0
with locationchange

"I lean against the soft cushions of the couch and breathe in the cool air of the atelier."

"Rin's head rests against my chest, as if she were listening to my heartbeats."

"Echoes of her dream ripple as small twitches on her face, like a cat sleeping the mouse-hunter's dream."

"The full moon, shining her pale light upon us from beyond the skylight, reflects from a blank canvas standing forgotten on the easel."

"Its whiteness is glowing against the dark night of the atelier."

stop music fadeout 2.0

scene black
with dissolve

# Without Breathing, Without a Sound (Rin Act 4 Soaked By Rain)
label en_delewd_R41:
play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

"The first day of summer vacation is a disappointment."

"I woke up. Water came down from the leaden sky in Biblical proportions."

"I was optimistic at the time."

"A quick summer shower, I thought. Torrents of rain for a few minutes, then it's gone."

show rain normal behind bg
with None

"No such luck."

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg
show bg misc_sky_rn as bg2 behind rain
show hisaowindow
with locationchange

"Rainwater is relentlessly pouring down from the blue-gray sky outside, streaming down the glass of my window in small brooks and rivers and gathering together to form miniature ponds on the walkways."

"Just like it has done for the past two and a half hours."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with charachange

"So I've been half-assedly cleaning up in between half-assedly reading a book, packing my stuff on the side when I get bored of the first two."

"The weather drags my spirits pretty down too, making it harder to do anything properly."

play sound sfx_impact2

"Something bumping quite loudly against my door rouses me from my apathy."

"I hope it's not Kenji and his crazy indoors bowling alley."

"…"

"I hear no more sounds from the corridor until I walk to the door and open it."

play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent
with locationchange

"Rin."

"I wish seeing her would evoke some more emotion in me, but for one, I'm too surprised that she came to see me and for two, she is soaking wet."

"Her uniform shirt is drenched and she is standing in a self-created puddle."

"Droplets of rainwater are dripping from her short bangs and sliding down her nose until they fall down from the tip."

"One.{w=0.7} By.{w=0.7} One."

hi "Umm… hi."

hi "How are you feeling?"

show rin basic_deadpannormal
with charachange

rin "Medium normal."

play music music_rin fadein 2.0

"The relative questionability of her statement aside, she sure doesn't look too good."

hi "You're all wet."

show rin basic_absent
with charachange

rin "It's because I come from the outside. Do you know it?"

hi "Why'd you be outside? It's raining buckets out there, if you haven't noticed."

show rin basic_deadpancontemplation
with charachange

rin "I haven't. It's raining pretty hard though. I was on a walk."

hi "Is this what you call 'wallowing in self-pity?'"

show rin basic_deadpanupset
with charachange

rin "Do you think I'm pitiful?"

hi "No, I implied that you think you are."

show rin basic_awayabsent
with charachange

rin "I'm not, and rain is not a sad thing."

show rin basic_absent
with charachange

rin "Don't you ever walk in the rain?"

hi "I do, but only with proper equipment, like an umbrella."

show rin basic_lucid
with charachange

rin "You just need to imagine you have a blue umbrella with white stripes."

hi "It might be tough when rain is falling on my head."

show rin basic_deadpannormal
with charachange

rin "Just imagine harder."

"…"

"Yeah, she definitely is back to normal."

"Those half-sarcastic, inconsiderate remarks that really push my buttons even though she doesn't mean it, that vacant, spaced-out stare that always expects more than it gives."

"It's so… very much like her."

show rin basic_deadpan
with charachange

rin "I may need to come in. I need some help with this water and clothes I'm wearing."

"My brain quickly solves this equation, and I stumble with my words, a stark display of contrast against Rin's easygoing self-invitation."

hi "But, Emi…"

show rin basic_lucid
with charachange

"Rin shakes her head vehemently, causing water to sprinkle everywhere."

rin "She left."

show rin basic_awayabsent
with charachange

rin "Besides she would just worry and fuss until she could not worry or fuss any more, which always takes a troublesomely long time."

show rin basic_absent
show rain normal behind bg
with charachange

rin "It's in fact longer than I want to hear her fussing, and I thought you probably are not the fussing kind."





$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg
show rin invis_close at center
show bg misc_sky_rn as bg2 behind rain
show hisaowindow behind rin
with locationchange

show rin relaxed_nonchalant_close_rn:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling

"She slumps down on my desk with a squishy sound."

"Her soaked clothes are making the desk and everything on it wet but she doesn't care."

"…"

hi "Okay. Fine. I'll help you out."

hi "I have a towel somewhere. Do you want dry clothes? Is a uniform fine? I'm taller than you, but…"

show rin basic_lucid_close_rn
with charachange

rin "Everything is fine."

show bg school_dormhisao_rn
with locationchange

"With a little searching I find a fresh uniform and a fluffy towel from the depths of my closet."

hide bg
with locationchange

"The towel in one hand and the uniform in the other, I turn to face Rin again, uncertain of the next step."

"There is something wrong with me, a normal guy would just—{w=1.0}{nw}"

show rin basic_absent_close_rn
with charachange

rin "Stop worrying. It is not a problem."

"She probably could see right through my hesitant demeanor."

"As if I was completely transparent to her."

"I push my anxiety away and concentrate on the eight buttons lined on her shirt, just like mine has."

"Only the first button is an obstacle, and after getting it over I undo the others with slightly less shaking hands."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout

"Throwing the soaked shirt aside, I reveal Rin's pale upper body, shrouded only in her light blue brassiere which instantly reminds me of her saying it's her favorite color."

"I try not to think too much about… stuff, but it's hard not to look at her body with what I can only think of as mixed feelings."

"I don't know what to think of this, so I just watch her. Rin looks… brittle."

"She is like a shell, a fragile thing just barely holding together."

"Her ribs, each of them visible under her pale skin, are moving up and down in the rhythm of her breaths."

"Rin always struck me as quite thin, but I realize now that the manic creative period before the exhibition opening might've caused her to lose weight."

"Did she eat properly and enough? Definitely not and probably not."

"This ugly, yet beautiful bare minimum of a human body that belongs to someone I care about is a contradiction of aesthetics in itself, oddly becoming of her."

"My eyes follow her collarbone to her shoulder and down her arm until the abrupt end."

"No, it's less than the bare minimum, I think with a passing pang of sadness and some guilt for thinking like that."

scene ev rin_wet_arms:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash

"Her arms, degenerated into almost nothing but bone and skin due to lack of use, look very short now that the long sleeves of her uniform are not covering them:"

"My lack of any negative reaction makes me think that I've actually grown pretty accustomed of the various physical abnormalities of my schoolmates."




"I always wondered why Rin keeps her shirt sleeves long, only tying them in a simple knot at where the elbow would be."

"It seems a bit impractical, but then again she is not exactly the pinnacle of practicality."

"Maybe she likes it, maybe it is somehow important to her. Maybe there is no deeper meaning to it."

"I feel like asking, and almost do, but Rin's miserable state requires a higher priority of my attention."

scene ev rin_wet_face_down:
    center
    yalign 0.0
with flash

"She's stopped talking too, after we ran out of spiky greetings."

"I guess there is no need for chitchat then."

scene ev rin_wet_towel_down
with charachange

"I pick up the towel from the bed and wrap it around her head, rumpling it all over her hair until most of the rainwater is hopefully soaked into the fabric."

scene ev rin_wet_towel_up
with charachange

"She peeks from below the towel at me, looking up with impassive eyes."

"It looks like she wants to say something without saying it."

"It's that kind of a look."

"But I can't read what she is thinking about from her face, so I just keep on fussing with the towel around her shoulders and hair."

"The silence is oppressive, terrifying."

"I think I can hear her heartbeats, or maybe they are just mine redoubled."

scene ev rin_wet_towel_touch
with charachange

"Here we are, a boy and girl, both in love or something like that with each other, or maybe not… and yet…"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nSomething is broken, I can feel it in me and in Rin; in the way our gazes merely brush against each other, shying away from contact; in her closed, timid posture and in my way of touching her like a china doll, afraid of shattering her delicate form."

n "In how we are closer than we have ever been, yet I'm not feeling happy. It's like yesterday."

n "When did tenderness and forlornness become one and the same word, acts of affection start invoking only longing? …How, why did we end up like this?"

n "'No, don't answer that,' I'd like to say to myself, but fighting against the omniscience of self-awareness is a lost cause."

n "Still, I am here, and Rin is here, and it feels like she might be able to solve whatever problems she has."

n "And if she can, why couldn't I? Why couldn't we?"

n "It feels like taking that step is too much, too difficult, too uncertain."

n "So for now, all I can do is dry her up so she won't get a cold again."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg misc_sky
with charachange
show hisaowindow
with locationchange

show rinpan relaxed_nonchalant_close
with charachange

"I pet her head, trying to sort out the hair that refuses to be sorted out even when wet."

"A pair of dark, glazed eyes follows my every movement."

label en_delewd_R41h:

hi "You know, this really is not what friends should be doing."

"I whisper, once again noticing how such a simple matter as talking can be overbearingly difficult at times."

show rinpan relaxed_doubt_close
with charachange

rin "Will you stop being my friend?"

"That wasn't what I meant, but her serious tone and the layers of connotations behind Rin's question give me pause."


hi "Nah."

rin "I… think it might be all right. Even if you did."

"I hug her and smile into her hair, understanding Rin perfectly for once."

show rinpan basic_deadpanamused_close
with charachange

rin "You are wet."

"The remnants of water on her skin have drained into my shirt."

"Somehow, even her statements of the obvious make me glad right now."

hi "You're right. I am. But that's your fault."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "The same feeling that clutched my heart yesterday makes its appearance."

n "We are together. In a way that is difficult to define, it eludes description as stubbornly as it evades change."

n "\nWould a relationship like this be all right? Could we ever change to become closer?"

n "Even though we would stay together for all of eternity, we might never find our mutual understanding."

n "But there is no such thing as eternity. This may mean that we will not be together forever."

n "If not our differences, then the flow of time will pull us apart with irresistible force."

nvl clear

n "\n\nRin is a creature of the moment, of whim and of impulse."

n "\nI am nothing of the sort."

n "\nThis is a fact that I can understand very clearly."

n "If for no other reason, for this reason I should grasp this moment. Even if it's the only moment we will ever have, I should not let myself spoil it."

n "Even if I can't escape myself. Rin can't either, I know it now."

n "\nWe both have things we can't let go, things we can't not think."

n "Feelings we can't not feel."

n "But she allows herself to want me without any restraint. Here and now."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

hi "I'm sorry, you know…"

show rinpan basic_lucid_close
with charachange

rin "Hisao, you really have to stop worrying."

"Rin interrupts me before I get further, which is good because I don't know what I could have said."

"Her voice, void of its usual spaciness, scolds me softly, without an edge."

show rinpan basic_deadpanamused_close
with charachange

rin "You really have to learn to let go."

"She scans me calmly, almost calculatingly."

"I wonder what I look like through her eyes."

"Damn. They are so green it almost hurts."

"I always was so enchanted by her eyes, those mysterious, captivating eyes that always were too restless for their own good."

"But I was also always intimidated by them."

"Yeah. Rin is intimidating, on more than one level and especially right now."

"She is frighteningly lucid, the goosebumps on her skin giving away that she is cold, or scared too."

"Either way, I steel myself and step back to Rin, embracing her to feel her in my arms again and to banish my doubts."

"The sight of her gentle, loving eyes seems to melt those doubts away like the last snow of winter."

rin "You should forget about stuff like future and past, it's not like you can change those kinds of things."

"I wanted to say something to her, but I have lost my voice so I just mumble something unintelligible at her."

rin "You should just be with me now."

show rinpan relaxed_surprised_close
with charachange

"She looks at me in a way that I can't really begin to interpret."

rin "Is this it?"

hi "…Huh?"

rin "You said I don't have to be alone."

"Her eyes are full of an innocent, fuzzyheaded confusion that makes me chuckle a little and pet the back of her head."

hi "Yeah. This is what I meant."

hi "That you have someone you can come to when you get soaked in a rain."

hi "It means you are not alone."

hi "If there is such a person for you."

return