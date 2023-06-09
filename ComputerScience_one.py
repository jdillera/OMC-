import sys
import random

# starting up the game----> begin the story
start = "Start"
end = "End"
def start_game():
  while True:
    start_game = input('Start game? Start/End ')
    if start_game in start:
      print('You chose to start the game. ')
      print("""
You play as Kevin, a 15 year old sophomore, you wake up in a random forest in the middle of the night. 
You don’t recall how you ended up in the forest, however, 
""")
      return False
    elif start_game in end:
      print('You chose not to start the game. ')
      print('Have a nice day! ')
      sys.exit('Have a nice day! ')
    else:
      start_game = input('Would you please state again- ')
      
walk_away = 'Walk away'
stay_listen = 'Stay and listen'
go_to_man = 'Go to him'
stay_away = 'Stay put'
def old_man():
  while True:
    old_man = input('in the distance you spot an elderly man staring at a river... Go to him/Stay put ')

# greating the old man
    if old_man in go_to_man:
# story starts
      print('You go towards the man by the river. ')
      print(' ')
      print('The old man turns towards you...his eyes grows larger. ')
      print('You look down at what the man was previously looking at. It starts to glow ')
      print('The old man: YOU! THE CHOSEN ONE! ')
      print('The old man: You must find the three crystals and get my dear brother out of the oblivian! ')
      talk_old_man = input('Do you want to stay and hear the strange man out?  Stay and listen/ Walk away ')
# given task regarding the three crystals
      if talk_old_man in stay_listen:
        print('''
        The old man:
        My brother was capture by a strange light the other day and was brought here.
        I tried everything in my power to get my brother out. 
        The three crystals I mentioned earlier, I wasn't able to successfully get them.
        You must find them for me.
        Bring them to me and I can grant you whatever you please.
        ''')
        print(' ')
        print('The elderly man left, jumping into the water without a trace ')
        return False
# never talked to the old man
      elif talk_old_man in walk_away:
        print('You left the old man by the river. ')
        print('He looked sad...  ')
        print('You walk further away to the center of this dark forest')
        print('You get attacked by a random forest creature. It rips your arm off. ')
        print('Blood is pouring out of you')
        print('You died...')
        sys.exit('You died...')
      else:
        talk_old_man = input('Would you please state again- ')
# never talked to the old man
    elif old_man in stay_away:
      print('You stay away from the odd man by the river')
      print('He looked sad...  ')
      print('You walk further away to the center of this dark forest')
      print('You get attacked by a random forest creature. It rips your arm off. ')
      print('Blood is pouring out of you')
      print('You died...')
      sys.exit('You died...')
    else:
      old_man = input('Would you please state again- ')

monster = ['goblin', 'demon', 'werewolf', 'minatour', 'centaur', 'orge', 'golem', 'monster panda']
rand_num = random.random()
rand_num_two = random.random()
rand_num_three = random.random()
threshold = 0.7
health = 1
kill_it = 'Kill it'
run_away = 'Run away'
mountain = 'Mountain'
forest = 'Forest'
along_river = 'Along the river'
yes = 'Yes'
no = 'No'
hide = 'Hide'
fight = 'Fight'
check_rock = "Check rock"
leave_rock = "Leave rock"
check_stick = "Check stick"
leave_stick = "Leave stick"
def crystal_hunt_one():
  while True:
# first crystal hunt --> decided where you want to hunt for the first crystal
    first_crystal = input('Do you want to look for the first crystal?  Yes/No ')
    if first_crystal in yes:
      place_one = input('Where do you want to look first? Along the ______   Mountain/Forest ')
# mountain situation
      if place_one in mountain:
        print('You go to the floor of the mountain. ')
        print('There is a path up in front of you, leading to the top of the mountain. ')
        mountain_start = input('Would you like to go up the mountain? Yes/No ')
        if mountain_start in yes:
          print('You start to go up the mountain. ')
# encountering first monster
          monster_one = input('You encounter a ' + random.choice(monster) + '.   Kill it/Run away ' )
          if monster_one in kill_it:
            if rand_num <= threshold:
              print('You hit the monster! ')
              print('Out of the monster came a shiney rock...')
# crystal came out of monster
              inspect = input('Do you want to check the rock out?   Check rock/Leave rock ')
              if inspect in check_rock:
                print('YOU FOUND THE FIRST CRYSTAL!!!')
# return false
                return False
              elif inspect in leave_rock:
                print('A random arrow came out of nowhere.')
                print('You died...')
                sys.exit('You died...')
# monster hit player
            else:
              print('You missed. ')
              print('The monster stuck you. ')
              monster_one = input('Do you want to attack again?  Kill it/Run away ')
              if rand_num_two <= threshold:
                print('You hit the monster! ')
                print('Out of the monster came a shiney rock...')
# crystal came out of monster
                inspect = input('Do you want to check the rock out?   Check rock/Leave rock ')
                if inspect in check_rock:
                  print('YOU FOUND THE FIRST CRYSTAL!!!')
# returned false
                  return False
                else:
                  print('You walk off into the distance...')
                  sys.exit('''An arrow hit you from the side... 
                  you died... ''')
# monster killed player
              else:
                print('You missed. ')
                print('The monster attacked you')
                health = 0
                sys.exit('You died...')

# running away from the monster
          elif monster_one in run_away:
            print('You ran away from the monster. ')
            print('It starts to chase you. ')
            decide = input('What do you want to do?  Hide/Fight')
            if decide in hide:
              print('You hid from the monster behind a boulder.')
              print(' ')
              print(' ')
              print('He found you. ')
              print('You tried to run away but he caught up to you. ')
              print('He got a hold of you. ')
              print('...')
              print('You died...')
              sys.exit('You died...')
            elif decide in fight:
              if rand_num_three <= threshold:
                print('You hit the monster! ')
                print('Out of the monster came a shiney rock...')
# crystal came out of monster
                inspect = input('Do you want to check the rock out?   Check rock/Leave rock ')
                if inspect in check_rock:
                  print('YOU FOUND THE FIRST CRYSTAL!!!')
# returned false
                  return False
                else:
                  print('You walk off into the distance...')
                  sys.exit('''An arrow hit you from the side... 
                  you died... ''')
              else:
                print('You missed. ')
                health = 0.5
        elif mountain_start in no:
          print('You turn back and do not go out the mountain.')
          first_crystal = input('Would you like to change the location? Mountain/Forest/Along the river ')

        else:
          place_one = input('Would you please state again- ')

# FOREST SITUATION
      elif place_one in forest:
        print('You turn around and begin to go deeper into the forest. ')
        print('There is a path up in front of you, lighting lining the way. ')
        forest_start = input('Would you like to follow the path? Yes/No ')
        if forest_start in yes:
          print('You start to follow the path. ')
# encountering first monster
          monster_one = input('You encounter a ' + random.choice(monster) + '.   Kill it/Run away ' )
          if monster_one in kill_it:
            if rand_num <= threshold:
              print('You hit the monster! ')
              print('Out of the monster came a shiney rock...')
# crystal came out of monster
              inspect = input('Do you want to check the rock out?   Check rock/Leave rock ')
              if inspect in check_stick:
                print('YOU FOUND THE FIRST CRYSTAL!!!')
# return false
                return False
              elif inspect in leave_stick:
                print('A random arrow came out of nowhere.')
                sys.exit('You died...')
# monster hit player
            else:
              print('You missed. ')
              print('The monster stuck you. ')
              monster_one = input('Do you want to attack again?  Kill it/Run away ')
              if rand_num_two <= threshold:
                print('You hit the monster! ')
                print('Out of the monster came glittering stick...')
# crystal came out of monster
                inspect = input('Do you want to check the stick out?   Check rock/Leave rock ')
                if inspect in check_stick:
                  print('YOU FOUND THE FIRST CRYSTAL!!!')
# returned false
                  return False
                else:
                  print('You walk off into the distance...')
                  print('''An arrow hit you from the side... 
                  you died... ''')
                  sys.exit('''An arrow hit you from the side... 
                  you died... ''')
# monster killed player
              else:
                print('You missed. ')
                print('The monster attacked you')
                health = 0
                print('You died...')
                sys.exit('You died...')

# running away from the monster
          elif monster_one in run_away:
            print('You ran away from the monster. ')
            print('It starts to chase you. ')
            decide = input('What do you want to do?  Hide/Fight')
            if decide in hide:
              print('You hid from the monster behind a tree.')
              print(' ')
              print(' ')
              print('He found you. ')
              print('You tried to run away but he caught up to you. ')
              print('He got a hold of you. ')
              print('...')
              sys.exit('You died...')
            elif decide in fight:
              if rand_num_three <= threshold:
                print('You hit the monster! ')
                print('Out of the monster came a glittering stick...')
# crystal came out of monster
                inspect = input('Do you want to check the stick out?   Check stick/Leave stick ')
                if inspect in check_stick:
                  print('YOU FOUND THE FIRST CRYSTAL!!!')
# returned false
                  return False
                else:
                  print('You walk off into the distance...')
                  print('''An arrow hit you from the side... 
                  you died... ''')
                  sys.exit('''An arrow hit you from the side... 
                  you died... ''')
              else:
                print('You missed. ')
                health = 0.5
        elif forest_start in no:
          print('You turn back and do not go deeper into the forest.')
          first_crystal = input('Would you like to change the location? Mountain/Forest ')

        else:
          place_one = input('Would you please state again- ')



    elif first_crystal in no:
      print('You do not want to look for these crystals  ')
      print('You walk around, further away to the center of this dark forest')
      print('You get attacked by a random forest creature. It rips your arm off. ')
      print('Blood is pouring out of you')
      print('You died..')
      sys.exit('You died...')
      
    else:
      first_crystal = input('Would you please state again- ')
      
# forest walking around story
def forest_story():
    while True:
# old man talk
        print("""
Congradulations on finding the first crystal!
But wait, there are still two more crystals to find!.
As you depart the area where you found the crystal, meet back where you first met the old man.

You see him again, but this time he is wearing some old back cloak.
You take the crystal out that you found and showed it to him.

The old man:
OH THANK YOU!
THE FIRST CRYSTAL!
My brother...My brother!!!!

The old man jumps around, holding his beloved crystal in the air. He then goes to the now glowing water and drops it in.
After a small thump when hitting the water, the water glows brighter, then fades once more.

The old man:
YES IT WORKED!!
YOU MUST FIND THE OTHER TWO CRYSTALS FOR ME!
I think I heard that one of them are in one of the buildings down this path.

The old man now pointed to a path. As you looked away to look at the direction he points, the man disappeared once more.

""")
        print('''
You start to walk down the path as directed by the man.
You pass a small little cabin.
Curious, you knock on the door.
An old lady greets you.

Old lady:
Hello deary.

You inform the old lady about your mission, to find the two crystals.

Old lady:
Oh my!
That sounds like a challenging task.
Come in, come in, stay the night.

Even though you are suspicious, you walk into the lady's home.
She allows you to put down your things and provides you with an extra plush bedding for you to rest your head.

The morning rises and the lady is nowhere to be found.
However, a little fairy flutters in front of you.

Fairy:
Hello deary!
I am the old lady you met yesterday.
This is my old cottage.
Because of your kindness and you hard work on your journey, I am willing to grant you three wishes.
''')
        return False

        
# finding things in the forest list
def forest_list():
    while True:
        print('What wishes do you have for the fairy...limit to three wishes ')
        print('NOTE: the wishes must be reasonable and will be granted after you find the crystals.')
        input_string = input("Enter all three wishes - separated by a comma:  ")
# Split string into words
        wish_list = input_string.split(",")

        print("\n")
# Iterate a list
        print("Printing all wanted wishes:")
        for wish in wish_list:
            print(wish)
        
        print('''
Fairy:
Alright deary!
All your wishes shall be granted after you finish your mission requested by the old man.
If you decided to fail to finish the task, your wishes will be as if they were never requested.
''')
        
        return False

import random
import sys

yes =  'Yes'
no = 'No'
castle_path = "Castle path"
tower_path = "Tower path"
monster = ['goblin', 'demon', 'werewolf', 'minatour', 'centaur', 'orge', 'golem', 'monster panda']
kill_it = 'Kill it'
run_away = 'Run away'
threshold = 0.6
threshold_one = 0.4
rand_num_three = random.random()
rand_num_four = random.random()
rand_num_five = random.random()
rand_num_six = random.random()
# starting the second crystal      
def crystal_hunt_two():
    while True:
        two_crystal = input('Would you you like to begin looking for the next crystal? Yes/No ')
        if two_crystal in yes:
            print("You leave the fairy's house and continue down the path directed by the old man")
            print('Soon the path leads to a fork in the road. As you look down the path, one leads to a tower, and the other a castle.')
            castle_tower = input('Which would path would you rather continue down? Castle path/Tower path ')
            
# castle path
            if castle_tower in castle_path:
                print('You went down the path towards the castle.')
                print('You reach the castle and entered it.')
                print('You sense a monster.')
# encounter a monster
                monster_one_castle = input('A ' + random.choice(monster) + ' jumped out at you.  Kill it/Run away ')
                if monster_one_castle in kill_it:
                    
# killed monster - continue deeper into the castle
                    if rand_num_three <= threshold:
                        print('You hit the monster. It died.')
                        print('You checked the monster for any signs of things falling out of it like the other monster.')
                        print('Nothing fell out')
                        print('It must be located elsewhere. You decided to proceed deeper into the castle.')
                        print('''You look down a dark hallway, there is a staircase that leads to the next floor.
''')
                        print('You go up the staircase')
                        print('''
At the top of the staircase, it leads you to a single hallway with a single door.
You open the door.
You find a large cat, triple to size of the average human.
At first you think that its simple an abnormal sized cat, with the same tempermate.
However, you notice that behind it is a chest.
The moment you look at it, the cat changes.
Its vicious with its hair pointed up straight, growling at you.
You take a step back.
''')
# mean cat fight one
                        mean_catfight = input('Do you want to fight the mean cat? Kill it/Run away ')
                        if mean_catfight in kill_it:
                            if rand_num_five <= threshold_one:
                                print('You hit the cat!')
                                print('Since you hit it, it is damaaged, but it is still alive.')
                                mean_catfight_two = input('Will you hit the cat again? Kill it/Run away ')
                                if mean_catfight_two in kill_it:
                                    if rand_num_six <= threshold:
                                        print('YOU KILLED THE CAT!')
                                        print('You go around the dead cat and have access to the chest.')
                                        chest = input('Will you look inside the chest? Yes/No ')
                                        if chest in yes:
                                            print('YOU FOUND THE SECOND CRYSTAL!!!')
                                            print('Fairy appeared in front of you. She cheered and disappeared once more.')
                                            print('You must report to the old man right away.')
                                            return False
                                        elif chest in no:
                                            print('You did not open the chest.')
                                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
YOU HAD THE PERFECT OPPORTUNITY TO OPEN THE CHEST!!!!
WHY!!!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                        else:
                                            chest = input('Please state again - ')
                                    else:
                                        print('The cat clawed you.')
                                        print('The impact was so intense, it sliced your face.')
                                        print('You are losing blood rapidly fast.')
                                        print('You died from blood loss.')
                                        sys.exit('You died from blood loss')
                                elif mean_catfight_two in run_away:
                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                    print('You died')
                                    sys.exit('You died.')
                            
                            else:
                                print('The cat clawed you.')
                                print('The impact was so intense, it sliced your face.')
                                print('You are losing blood rapidly fast.')
                                print('You died from blood loss.')
                                sys.exit('You died from blood loss')
                                
                        elif mean_catfight in run_away:
                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                            print('You died')
                            sys.exit('You died.')
                        
                                
                                                
# missed
                    else:
                        print('You missed the monster')
                        print('He attacked you.')
                        print('If the monster manages to attack you one more time you are done for.')
                        try_again = input('Would you like attack the monster again? Kill it/Run away ')
                        if try_again in kill_it:
                            
# killed monster (second try) - continue deeper into the castle
                            if rand_num_four <= threshold:
                                print('You hit the monster. It died.')
                                print('You checked the monster for any signs of things falling out of it like the other monster.')
                                print('Nothing fell out.')
                                print('It must be located elsewhere. You decided to proceed deeper into the castle.')
                                print('''You look down a dark hallway, there is a staircase that leads to the next floor.
''')
                                print('You go up the staircase')
                                print('''
At the top of the staircase, it leads you to a single hallway with a single door.
You open the door.
You find a large cat, triple to size of the average human.
At first you think that its simple an abnormal sized cat, with the same tempermate.
However, you notice that behind it is a chest.
The moment you look at it, the cat changes.
Its vicious with its hair pointed up straight, growling at you.
You take a step back.
''')
# mean cat fight one
                                mean_catfight = input('Do you want to fight the mean cat? Kill it/Run away ')
                                if mean_catfight in kill_it:
                                    if rand_num_five <= threshold_one:
                                        print('You hit the cat!')
                                        print('Since you hit it, it is damaaged, but it is still alive.')
                                        mean_catfight_two = input('Will you hit the cat again? Kill it/Run away ')
                                        if mean_catfight_two in kill_it:
                                            if rand_num_six <= threshold:
                                                print('YOU KILLED THE CAT!')
                                                print('You go around the dead cat and have access to the chest.')
                                                chest = input('Will you look inside the chest? Yes/No ')
                                                if chest in yes:
                                                    print('YOU FOUND THE SECOND CRYSTAL!!!')
                                                    print('Fairy appeared in front of you. She cheered and disappeared once more.')
                                                    print('You must report to the old man right away.')
                                                    return False
                                                elif chest in no:
                                                    print('You did not open the chest.')
                                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
YOU HAD THE PERFECT OPPORTUNITY TO OPEN THE CHEST!!!!
WHY!!!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                                else:
                                                    chest = input('Please state again - ')
                                            else:
                                                print('The cat clawed you.')
                                                print('The impact was so intense, it sliced your face.')
                                                print('You are losing blood rapidly fast.')
                                                print('You died from blood loss.')
                                                sys.exit('You died from blood loss')
                                        elif mean_catfight_two in run_away:
                                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                            print('You died')
                                            sys.exit('You died.')
                            
                                    else:
                                        print('The cat clawed you.')
                                        print('The impact was so intense, it sliced your face.')
                                        print('You are losing blood rapidly fast.')
                                        print('You died from blood loss.')
                                        sys.exit('You died from blood loss')
                                
                                elif mean_catfight in run_away:
                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                    print('You died')
                                    sys.exit('You died.')
                        
                                
# failed to kill monster --> dead
                            else:
                                print('You missed... again.')
                                print('The monster hit you.')
                                print('The monster severed your leg.')
                                print('Blood is pouring out of you')
                                print('The fairy appeared in front of you.')
                                print('''
Fairy:
Hello deary.
You were not able to successfully help the old man and his brother.
I can not give you your wishes.
But I thank you for trying.
That child in the river was my son, until I fell into a magical well.
The well turned me into what you see now.
Anyways, good bye.
''')
                                print('You died from blood loss...')
                                sys.exit('You died from blood loss...')
                        elif try_again in run_away:
                            print('The fairy appeared in front of you, she is angry.')
                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                    print('You died...')
                    sys.exit('You died...')
                elif monster_one_castle in run_away:
                    print('The fairy appeared in front of you, she is angry.')
                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                    print('You died.')
                    sys.exit('You died.')
                else:
                    monster_one_castle = input('Would you please state again? - ')
#--------------------------------------------------------------------------------------------------------                    
# tower path
            elif castle_tower in tower_path:
                print('You went down the path towards the tower.')
                print('You reach the large tower and entered it.')
                print('You sense a monster.')
# encounter a monster
                monster_one_tower = input('A ' + random.choice(monster) + ' jumped out at you.  Kill it/Run away ')
                if monster_one_castle in kill_it:
                    
# killed monster - continue deeper into the tower
                    if rand_num_three <= threshold:
                        print('You hit the monster. It died.')
                        print('You checked the monster for any signs of things falling out of it like the other monster.')
                        print('Nothing fell out')
                        print('It must be located elsewhere. You decided to proceed deeper into the higher up the tower.')
                        print('''You look down  small dark hallway, there continues the staircase that leads to the next floor.
''')
                        print('You go up the staircase')
                        print('''
At the top of the staircase, it leads you to a single hallway with a single door.
You open the door.
You find a large cat, triple to size of the average human.
At first you think that its simple an abnormal sized cat, with the same tempermate.
However, you notice that behind it is a chest.
The moment you look at it, the cat changes.
Its vicious with its hair pointed up straight, growling at you.
You take a step back.
''')
# mean cat fight one
                        mean_catfight = input('Do you want to fight the mean cat? Kill it/Run away ')
                        if mean_catfight in kill_it:
                            if rand_num_five <= threshold_one:
                                print('You hit the cat!')
                                print('Since you hit it, it is damaaged, but it is still alive.')
                                mean_catfight_two = input('Will you hit the cat again? Kill it/Run away ')
                                if mean_catfight_two in kill_it:
                                    if rand_num_six <= threshold:
                                        print('YOU KILLED THE CAT!')
                                        print('You go around the dead cat and have access to the chest.')
                                        chest = input('Will you look inside the chest? Yes/No ')
                                        if chest in yes:
                                            print('YOU FOUND THE SECOND CRYSTAL!!!')
                                            print('Fairy appeared in front of you. She cheered and disappeared once more.')
                                            print('You must report to the old man right away.')
                                            return False
                                        elif chest in no:
                                            print('You did not open the chest.')
                                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
YOU HAD THE PERFECT OPPORTUNITY TO OPEN THE CHEST!!!!
WHY!!!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                        else:
                                            chest = input('Please state again - ')
                                    else:
                                        print('The cat clawed you.')
                                        print('The impact was so intense, it sliced your face.')
                                        print('You are losing blood rapidly fast.')
                                        print('You died from blood loss.')
                                        sys.exit('You died from blood loss')
                                elif mean_catfight_two in run_away:
                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                    print('You died')
                                    sys.exit('You died.')
                            
                            else:
                                print('The cat clawed you.')
                                print('The impact was so intense, it sliced your face.')
                                print('You are losing blood rapidly fast.')
                                print('You died from blood loss.')
                                sys.exit('You died from blood loss')
                                
                        elif mean_catfight in run_away:
                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                            print('You died')
                            sys.exit('You died.')
                        
                                
                                                
# missed
                    else:
                        print('You missed the monster')
                        print('He attacked you.')
                        print('If the monster manages to attack you one more time you are done for.')
                        try_again = input('Would you like attack the monster again? Kill it/Run away ')
                        if try_again in kill_it:
                            
# killed monster (second try) - continue higher up the tower
                            if rand_num_four <= threshold:
                                print('You hit the monster. It died.')
                                print('You checked the monster for any signs of things falling out of it like the other monster.')
                                print('Nothing fell out.')
                                print('It must be located elsewhere. You decided to proceed deeper into the castle.')
                                print('''You look down a dark hallway, there is a staircase that leads to the next floor.
''')
                                print('You go up the staircase')
                                print('''
At the top of the staircase, it leads you to a single hallway with a single door.
You open the door.
You find a large cat, triple to size of the average human.
At first you think that its simple an abnormal sized cat, with the same tempermate.
However, you notice that behind it is a chest.
The moment you look at it, the cat changes.
Its vicious with its hair pointed up straight, growling at you.
You take a step back.
''')
# mean cat fight one
                                mean_catfight = input('Do you want to fight the mean cat? Kill it/Run away ')
                                if mean_catfight in kill_it:
                                    if rand_num_five <= threshold_one:
                                        print('You hit the cat!')
                                        print('Since you hit it, it is damaaged, but it is still alive.')
                                        mean_catfight_two = input('Will you hit the cat again? Kill it/Run away ')
                                        if mean_catfight_two in kill_it:
                                            if rand_num_six <= threshold:
                                                print('YOU KILLED THE CAT!')
                                                print('You go around the dead cat and have access to the chest.')
                                                chest = input('Will you look inside the chest? Yes/No ')
                                                if chest in yes:
                                                    print('YOU FOUND THE SECOND CRYSTAL!!!')
                                                    print('Fairy appeared in front of you. She cheered and disappeared once more.')
                                                    print('You must report to the old man right away.')
                                                    return False
                                                elif chest in no:
                                                    print('You did not open the chest.')
                                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
YOU HAD THE PERFECT OPPORTUNITY TO OPEN THE CHEST!!!!
WHY!!!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                                else:
                                                    chest = input('Please state again - ')
                                            else:
                                                print('The cat clawed you.')
                                                print('The impact was so intense, it sliced your face.')
                                                print('You are losing blood rapidly fast.')
                                                print('You died from blood loss.')
                                                sys.exit('You died from blood loss')
                                        elif mean_catfight_two in run_away:
                                            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                            print('You died')
                                            sys.exit('You died.')
                            
                                    else:
                                        print('The cat clawed you.')
                                        print('The impact was so intense, it sliced your face.')
                                        print('You are losing blood rapidly fast.')
                                        print('You died from blood loss.')
                                        sys.exit('You died from blood loss')
                                
                                elif mean_catfight in run_away:
                                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                                    print('You died')
                                    sys.exit('You died.')
                        
                                
# failed to kill monster --> dead
                            else:
                                print('You missed... again.')
                                print('The monster hit you.')
                                print('The monster severed your leg.')
                                print('Blood is pouring out of you')
                                print('The fairy appeared in front of you.')
                                print('''
Fairy:
Hello deary.
You were not able to successfully help the old man and his brother.
I can not give you your wishes.
But I thank you for trying.
That child in the river was my son, until I fell into a magical well.
The well turned me into what you see now.
Anyways, good bye.
''')
                                print('You died from blood loss...')
                                sys.exit('You died from blood loss...')
                        elif try_again in run_away:
                            print('The fairy appeared in front of you, she is angry.')
                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                    print('You died...')
                    sys.exit('You died...')
                elif monster_one_tower in run_away:
                    print('The fairy appeared in front of you, she is angry.')
                    print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!
WHY ARE YOU SUCH A COWARD!?!?!? IT WAS ONLY A MONSTER!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
                    print('You died.')
                    sys.exit('You died.')
                else:
                    monster_one_tower = input('Would you please state again? - ')
                
#-----------------------------------------------------------------------------------------------------------
                        
# fairy gets angry as you go back on your word
        elif two_crystal in no:
            print('The fairy became angry at you.')
            print('''
HOW DARE YOU GO BACK ON YOUR WORD!
THIS IS DISGRACEFUL!

She pulled out her wand.
You tried to evade her but she managed to zap you.
The zap extremely electrocuted you.
''')
            print('You died...')
            sys.exit('You died')
        else:
            two_crystal = input('Would you please state again... ')

def crystal_hunt_three():
    while True:
        print('The second crystal was found.')
        print('Lets take a small break')
        print('Adios player')
        sys.exit('End later')

start_game()
old_man()
crystal_hunt_one()
forest_story()
forest_list()
crystal_hunt_two()
crystal_hunt_three()

