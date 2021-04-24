#from main import handle_msg
import random

class Dudes:
  def responses(self,author,cmd=None):
    cmd=cmd.lower()

    if cmd=="tyler":
      return str("Tyler Toney is one of the Dude Perfect members. He is the youngest out of the group and has the most battle wins. His aliases are The Beard, TT, and TyNaTo.")
    
    if cmd=="coby":
      return str("Coby Cotton is a shooter for Dude Perfect. He used to lose every battle until the Giant Sumo Battle. He has a twin brother name Cory Cotton.")
    
    if cmd=="cody":
      return str("The tall man with the plan is Cody Jones. He is a fan of the show just don’t let him enter the DP Gaming Room when the game is on the line.")
    
    if cmd=="cory":
      return str("Cory Cotton is one of the five members of Dude Perfect. Cory is known for losing Wheel Unfortunate, and getting bottle busted. He is also known for saying Let’s GO as he runs with his arms out.")
    
    if cmd=="garrett":
      return str("The cleanest dude that always needs sunscreen Garrett or the Purple Hoser is always on the podium.")
    
    if cmd=="sparky":
      return str("Sparky is the DP Ambassador of Gaming. You will recognize him as the MVP of ASBR 2, host of Quarantine Classic, and everyone’s favorite Get Crafty Judge! Follow him on IG @sparky_man4.")
    
    if cmd=="monstie":
      rand = random.randint(0,10)
      return str(f"@{author}'s monstie crack scored a {rand} on the monstie meter!")
    
    if cmd=="jonah":
      return str('Jonah will forever be our Joan Boy! Even while in school, he is the president of our hearts. We will never forget his love of sushi, monstie runs, and IG filter prowess. Follow him on IG @j_levy14')

    if cmd=="jack":
      return str('Jack is the DP intern. We already love him so much. Jack is a Fall Guys wizard. Welcome Jack!!!!')
    
    if cmd=="derek":
      return str('Derek is one of the DP Editors. Derek is a Photoshop Ninja and Fact Of The Day Legend. Derek is the unofficial leader of the DPG Dance Crew. He is a good luck charm and his visits to the stream almost always precede a dub.')

    if cmd=="tim":
      return str('This DP Editor has never met a technical issue that he couldn’t help Sparky solve. Additionally TimBits is an NHL gaming phenom (did someone say Red Wings?) and he rocks at Rocket League! He is known as a Senior Production Editor which he videotapes and edits the videos.')

    if cmd=="chad":
      return str('Chad is a Senior Production Editor for DP. He has yet to meet a drone he can’t fly. He is a Certified Drone Pilot, as well as a Certified Scuba Diver. Hand him a camera and watch the magic happen.')
    
    if cmd=="shon":
      return str('Shon is the newest DP Editor. Shoeless Shon is on track to become a Spikeball Legend. He is also an absolute face melter in Warzone. Follow on IG @shonsterthemonster ')
    
    if cmd=="panda":
      return str('The Panda is a recurring figure on DP. It is currently unknown who they are, but DP says they will reveal him when they #TieThePie which means if they get as many subscribers as PewDiePie.')
    
    if cmd=="minecraft":
      return str('Please watch the following instructional video for connecting to the DPG Minecraft Server: https://www.youtube.com/watch?v=hnO1PFVvbmI For more help, visit: https://sites.google.com/view/dpgnbot/minecraft ')

    if cmd=="au":
      return str('How to Join Sparky in Among Us. 1. Click on the  #Waiting Room (OPEN) voice channel. 2. Make sure you have push to talk enabled 3. To check your place in the queue go to the #waiting-room-queue (In the discord). 4. You will be provided with the game code, once you have been pulled into a stream room. For more help, visit: https://sites.google.com/view/dpgnbot/among-us')

    if cmd=="discord":
      return str('Join the DPG Discord! https://discord.gg/A68YFtC')

    if cmd=="rules":
      return str('To Enjoy the Stream Chat: 1. Keep it civil. No language or vulgar comments. 2. No politics. 3. No self-promos, advertising, or links. 4. No spam. 5. No personal info(age, name, etc) ')

    if cmd== "regiment" :
      return str('JOIN THE REGIMENT Step 1. Join the discord: https://discord.gg/6WgKkcF8rT Step 2. Add your Gamertag to the #callofduty-regiment channel. An officer will send a regiment invite.')

    if cmd=='fortnite':
      return str('DPG runs Fortnite with Fans every Wednesday for the most of the stream.')

    if cmd=='fncode':
      return str('NA-EAST | Code: Changes each game. The code will be in the chat. So look for it for the next game.')

    if cmd=='spikeball':
      return str('The DP Crew plays until 21. Unless they tie it at 20 then they have to play until they win by 2.')

    if cmd=='spikesound':
      return str('When playing Spikeball the microphone will only send sound out of one channel (left or right). That is just the way it is. It is not a glitch.')

    if cmd=='games':
      return str('Sparky plays Warzone, Among Us, Fortnite, Apex, PGA Tour, Madden, CHEL, FIFA, Fall Guys, Rocket League, and really any other game he feels like playing.')

    if cmd=='bou':
      return str('Not all of us can say they graduate from oof university with top honors.')

    if cmd=='oops':
      return str('There are consequences to breaking the rules. You hate receiving negative consequences. Mods hate giving out negative consequences. So everyone JUST FOLLOW THE RULES. xoxo, The Mods')

    if cmd=='youdont' :
      return str('How to Be a Mod: It’s 10% luck. 20% skill. 15% concentrated power of will. 5% pleasure. 50% pain....and 100% not by asking for it. Because it’s not a cool status thing...it’s a ton of work. Now VIP...that *is* a cool status thing.')

    if cmd=='headset':
      return str('Headset: Astro A40s')

    if cmd=='ttcam':
      return str('No we do not have TT cam. It’s not set up.')

    if cmd=='stream':
      return str('"Spark after Dark" on Mon @ 5-8 PM CST. Wed/Fri on YT, Tue/Th on Twitch @ 1-4 PM CDT. Changes are announced on Instagram and Discord.')

    if cmd=='comms':
      return str('Sparky always wants his squad to show up with comms and confidence. In the heat of battle, things can get a little spicy. To stay family friendly, we do not hear comms, but we hear the confidence.')

    if cmd=='instagram':
      return str('Follow Dude Perfect Gaming on instagram!Instagram Link https://www.instagram.com/dudeperfectgaming/')

    if cmd=='engineer':
      return str('Engineer is a mod without peer. This fine gentleman is the reason we have a Minecraft Server, and so much more. He’s pretty much a Master of Bots and Discord Wizard.')  

    if cmd=='amber' or cmd=='ambam':
      return str('AmberBrainWaves. AmBam. Lady Stud Pro Third Imposter. It’s been said she’s the Wendy to this band of Lost Boys. You may not want her on your team, but she’d bring excellent snacks.')

    if cmd=='mikee':
      return str('Mikee is a true hero. (Seriously, he’s a nurse.) Along with travelling the world saving lives, he saves records and clips of the streams. He’s the GIF hero DPG needs and deserves.')

    if cmd=='djl':
      return str('DJL stands for Discord Jampacked Life! (Not really) But @djl_345 really is the master of the DPG Discord. Come on over to the Discord to make DJL happy. -discord')

    if cmd=='foster':
      return str('Fosterkitten has been a kitten foster mom for 10+ years. She’s found homes for over 450 kittens. She is the Siri of the chat, if you have a stream question, she has the answer.')

    if cmd=='phantom':
      return str('This man is a legend if I do say so myself, he is the reason our DPG community servers exist. He would love it if you joined the minecraft server!')

    if cmd=='jer':
      return str('JerTrigger’s just a guy who loves DP and DPG. Plain and simple. You know things are bad when he drops “ouchy momma’s” in the chat. Keeper of the Quotes. Descended from Nordic Royalty.')

    if cmd=='reformed':
        return str('ReformedGamer3 watched the DPG stream on the day of his son’s birth. That is a true fan. Rege is an amazing mod and all around good guy (despite his hat of bone-in wings).')

    if cmd=='woodsy':
      return str('Woodsy is a super mod. Be nice to him or he’ll growl at yo. Despite many unfounded rumors, he has never been convicted of hacking. He games so hard he must be strapped to his chair.')

    if cmd=='philly':
      return str('Our newest mod ThePhillyCheese is not from Philadelphia, but he does love the Eagles. He may be the funniest mod in the bunch, and really does love queso. He’s a Warzone Legend.')

    if cmd=='mods':
      return str('JerTrigger, ReformedGamer3, AmberBrainWaves, DJL, FosterKitten, MikeeStarke, Engineer, WoodsnTrails, ThePhillyCheese. Trust the mods. Listen to the mods. Respect the mods.')

    else:
      return "None"