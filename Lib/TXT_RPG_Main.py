"""
- Project : Text RPG!
- Project description : A text based RPG. This program was written to simply brush up on my python programming skills :-)
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh


Just a note from the author :
---------------------------------

Text RPG is written by A.Taylor. This source is free to use in any of your projects, however, if you intend to use this source for any college/University projects please email me and i will be delighted to help. Emailing me for permission to use this source
in your educational projects enables you, to not include my name in the source. Effectively making you credible for this source AND its affliated class files ( Except andre's CLI color wrapper ) . 
If you think my code may be badly written, I'm not worried about bad code at this moment in time, as long as my code works, I'm a happy man. 
This project was written up to test my python programming skills, because i had been caught up with RL stuff ;-) .

Contact me at : Ashtrix2k@googlemail.com

Credits
--------

- A.Taylor - S3pHiRoTh / Programmer
- Notepad ++ ( Best theme = obsidian! )
- G.Rossum - Python
- Andre - CLI color wrapper
- WEBZEN - Story Theme / Class Type Idea

Changelog : ( Yes, every project needs one! ) 
--------------
* Current project version : V.0.0.30

V.0.0.10
======
- Start of project
- Started writing text RPG in OOP ( Object Orientated and not procedural programming )
- Later i will create a nice API for those who want to add their own missions/quests/mobs.
(Obviously need to focus on more important things first!)
- Start working on noted ideas from : Text RPG implementation elements.txt
- Text RPG currently uses simple CLI
- Started work on monster system ( Partially )

V.0.0.20
======
- Integrated andre's CLI font color wrapper
- Created Hero properties
- Wrote hero inventory code
- Wrote base NPC code ( Still needs ALOT of work. NPC system will have basic functionality by V.0.0.40 )
- Wrote base game location
- Created the following Text RPG! class modules : interface, level_up_and_battle_sys, npc 
- Wrote level up, exp, and battle / menu system.
- Level up / Experience system formula = TETNL  = NEXF  * 10 + ETNL | TEFNLF += TEFNL ( ETNL is the experience factor that is added on to TETNL for the next level. Example Each level made + 50 experience.
The formula may seem confusing, but it is a rather simple, yet effective system. {TETNL = self.total_exp_for_next_level |  NEXF = self.New_EXP_WF_FACTOR | ETNL = self.exp_to_next_lvl | TEFNLF = self.total_exp_for_next_level_FACTOR}
- Reworked the levelup_and_battle_sys class. It is more organized now, and clear for other programmers to read the source
- Spell system will be usable by V.0.0.30 .

V.0.0.30
======
- Squashed bugs that was accidentally created in V.0.0.20 due to rushing to implement new features.
- Deleted monster class file & npc class file. Instead I will integrate the monster code into the levelup_and_battle_sys class module.
- Deleted Hero_class_types class module, instead I've integrated the code into the interface class module.
- Monster system, with random encounters will be available in V.0.0.40 .
- Created Class system ( Fully working, with each classes bonus attributes! )
- Level up bonus stats are added and accounted for when hero makes a level! ( Stats are different for each class! )
- Hero has max hp and max mana. This is so that when hero levels up, the hero can have more hp and more mana than what it started with.
- Stats system fully updates properly now within the battle loop!
- Test Spells and Fairy Elf skills are now working in the main game loop!!
- Created more special class attributes : Dark Wizard has min/max magic power and Fairy Elf has min/max skill power. Dark Knight
has no special class atrributes due to having raw strength. New Attributes are shown in hero stats, but do not currently do anything as of this update.
- In V.0.0.40 hero should be able to travel between locations.

"""

# Import seperate modules
from sys import exit
from os import system
from os import sys
from random import choice
from random import randrange
from random import sample

# Import Text RPG! specific class'es from the interface module
# This saves using a initialization variable to call the class'es!
from interface import Interface_Menu
from interface import Interface_Game_Intro
from interface import Interface_Story_Intro
from interface import Hero_Types_Menu
from interface import Hero_Class_Types_Help
from interface import Credits

# Import Text RPG! specific class'es from the hero module
from levelup_and_battle_sys import Battle_Phase
from levelup_and_battle_sys import bonus_DK
from levelup_and_battle_sys import bonus_DW
from levelup_and_battle_sys import bonus_FE

# Import whole modules from the standard library
import os

# Import andre's CLI color wrapper
import color_console as cons
		
class BaseFramework(object) :
	""" This class will be the foundations of the games framework """

	# Properties for CLI font color
	default_colors = cons.get_text_attr()
	default_bg = default_colors & 0x0070
	cons.set_text_attr(cons.FOREGROUND_GREY | default_bg |
	cons.FOREGROUND_INTENSITY)
	
	
	def __init__(self, w_title) :
		""" Base Framework initial constructor """
		
		# Prepare the framework class contructor
		self.Game_title_Intro(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		Interface_Game_Intro()
		Interface_Menu()
		# Call Game class
		self.call_game = Game()
		self.call_game.Game_Start(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		
	def Game_title_Intro(self, color_yellow) :
		Game_title = "\t\t\t Text RPG! V.0.0.30"
		Game_underline = "\t\t\t ------------------ \n"
		
		print Game_title
		print Game_underline
					 
class Game(object) :
	""" This class is for Text RPG!'s menu selecting functions. """

	# Variables for this class will be stored here for the functions to access
	
	def Game_Start(self, color_grey) :
		menu_choice = raw_input("(Enter a number to start the game. To start the game press 1, to quit press 3) ")
		if 	menu_choice == "1" :
			system('cls')
			self.Game_title_Story(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
			Interface_Story_Intro()
			self.Class_Select()
			self.Hero()
			Battle_Phase()
		elif menu_choice == "2" :
			Credits()
			return self.Game_Start(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		elif menu_choice == "3" :
			exit()
		else :
			print "You need to enter a valid number range!"
			self.Game_Start(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
			
	def Hero(self) :
		print \
		"""
	If you're not bothered about a hero name, you could alternatively type
	\"default" .
		"""
		
		hero_name = raw_input("Enter your desired Hero's name : ")
		Battle_Phase.HERO_NAME.remove("Hero")
		Battle_Phase.HERO_NAME.append(hero_name)
		if str(hero_name) in Battle_Phase.DEFAULT :
			print "Default player name is %s " %(Battle_Phase.HERO_DEFAULT_NAME[0])
		else :
			pass
		print "Your journey begins, %s! " %(Battle_Phase.HERO_NAME[0])
		
	def Game_title_Story(self, color_yellow) :
		Game_title = "\t\t\t The Story so far..."
		Game_underline = "\t\t\t------------------- \n"
		
		print Game_title
		print Game_underline
		
	def Class_Select(self) :
		Hero_Types_Menu()
		c_select = raw_input("Select the type of class that you would like to play as : ")
		if c_select == "1" :
		# If user chooses option 1 to be the Dark Knight class type
			print "You have chosen the Dark Knight class!"
			Battle_Phase.HERO_CLASS.remove("Placeholder")
			Battle_Phase.HERO_CLASS.append(Battle_Phase.DARK_KNIGHT)
		# Add the classes bonus attributes to the base hero stats
			bonus_DK()
		elif c_select == "2" :
		# If user chooses option 2 to be the Dark Wizard class type
			print "You have chosen the Dark Wizard class!"
			Battle_Phase.HERO_CLASS.remove("Placeholder")
			Battle_Phase.HERO_CLASS.append(Battle_Phase.DARK_WIZARD)
		# Add the classes bonus attributes to the base hero stats
			bonus_DW()
		elif c_select == "3" :
		# If user chooses option 3 to be the Fairy Elf class type
			print "You have chosen the Fairy Elf class!"
			Battle_Phase.HERO_CLASS.remove("Placeholder")
			Battle_Phase.HERO_CLASS.append(Battle_Phase.FAIRY_ELF)
		# Add the classes bonus attributes to the base hero stats
			bonus_FE()
		elif c_select == "4" :
		# If user chooses option 4 to view the class help options
		# Dark Knight class type help description
			system('cls')
			Hero_Class_Types_Help()
			self.Class_Select()
		else :
			print "%s You didn't type a valid number range! Please try again." %(Battle_Phase.Help_MSG)
			self.Class_Select()
		
class runapp(object) :
	
	def __init__(self) :
		""" Constructor that loads whatever functions is wrote in this class on class call """
		self.initialize()
		
	def initialize(self) :
		init = BaseFramework(w_title = os.system("title Text RPG! [ Version 0.0.30 ]"))
		raw_input()
