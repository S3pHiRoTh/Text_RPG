"""
- Project : Text RPG!
- Class description : Text RPG! interface module
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh
"""

# Import andre's CLI color wrapper
import color_console as cons

# Global properties
# Properties for CLI font color
default_colors = cons.get_text_attr()
default_bg = default_colors & 0x0070
cons.set_text_attr(cons.FOREGROUND_GREY | default_bg |
cons.FOREGROUND_INTENSITY)

class Interface_Menu(object) :
	""" Text RPG! interface class, all interface related stuff goes into this module """
		
	def __init__(self) :
		""" Class constructor """
		self.TextRPG_MENU(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		
	def TextRPG_MENU(self, color_grey) :
		menu_opts = \
		"""
\t\t\t 1 - New Game
\t\t\t 2 - Credits
\t\t\t 3 - Quit Game \n
		"""
		print menu_opts
		
class Interface_Game_Intro(object) :

	def __init__(self) :
		""" Class constructor """
		self.Game_Intro(color_red = cons.set_text_attr(cons.FOREGROUND_RED))
		
	def Game_Intro(self, color_red) :
		intro_text = \
			"""
	Welcome to Text RPG! This game is like the old school days
	of gaming. The days of command line interface games that
	had no fancy sprite animations, and no cool MIDI sound effects!
	Prepare to immerse yourself in the byte - sized Text RPG!
	( Or at least try to! )
			"""
			
		print intro_text

class Interface_Story_Intro(object) :

	def __init__(self) :
		""" Class constructor """
		self.Beg_Story(color_red = cons.set_text_attr(cons.FOREGROUND_RED))
		
	def Beg_Story(self, color_red) :
		story = \
		"""
	In the land of MU. The continent known as the land
	that has had a bitter blood fued with the magic gladiators
	and dark lords for over a century. The city of
	Lorencia Prospered for many ages. Until.. A recently ascended
	Blade Knight, who calls himself 'The Destroyer' laid waste to Lorencia.
	However, a young hero survived. A hero that has the potential within
	to vanquish this great evil. And so the story begins... \n
		"""
		
		print story
		
class Interface_Tutorial(object) :
	
	def __init__(self) :
		""" Class constructor """
	
	def Tutorial_Text(self) :
		Tut_text = \
		"""
	Welcome to Text RPG! My name is the Tutorial master. 
	I will teach you the basic game mechanics ! What would you like to know? \n
	1 - How to use the inventory
	2- How to go encounter monsters
	3 - How to travel between locations
	4 - Advanced options
		"""
		
		print Tut_text
		
class Hero_Types_Menu(object) :
	""" Hero Types menu"""
	
	def __init__(self) :
		""" Class constructor """
		self.Type_Menu(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		
	def Type_Menu(self, color_yellow) :
		type_menu = \
		"""
	Before you start your quest in Text RPG! You first need
	to choose a class type that you wish to play. Each class
	has its own bonuses and weaknesses. So choose wisely!
	Below, there is 3 class types to choose from. \n
		"""
		print type_menu
		self.Dark_Knight(color_red = cons.set_text_attr(cons.FOREGROUND_RED))
		self.Dark_Wizard(color_blue = cons.set_text_attr(cons.FOREGROUND_BLUE))
		self.Fairy_Elf(color_purple = cons.set_text_attr(cons.FOREGROUND_MAGENTA))
		self.Classhelp(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		
	def Dark_Knight(self, color_red) :
		DK = "\t1 - Dark Knight"
		print DK
		
	def Dark_Wizard(self, color_blue) :
		DW = "\t2 - Dark Wizard"
		print DW
		
	def Fairy_Elf(self, color_purple) :
		FE = "\t3 - Fairy Elf"
		print FE
	
	def Classhelp(self, color_yellow) :
		CH = "\t4 - Class types Help \n"
		print CH

class Hero_Class_Types_Help(object) :
	""" Hero class Types help """
	
	def __init__(self) :
		""" Class constructor """
		self.DK_Class_Help(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		self.DW_Class_Help(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		self.FE_Class_Help(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		
	def DK_Class_Help(self, color_yellow) :
		DKclass_help = \
		"""
		Dark Knight
		------------
		
The Dark Knight class type is a high strength type. It deals high raw
damage to monsters. If you wish to mow monsters down easily, then this class
is for you!

Bonus Stats : Str : + 10 , HP : + 20
Class Weakness Stats : Magic : - 5
\n
		"""
		
		print DKclass_help
		
	def DW_Class_Help(self, color_yellow) :
		DWclass_help = \
		"""
		Dark Wizard
		------------
		
The Dark Wizard class type is a high magicka type class. This class has a wide
variety of spells. Each spell has a different element school, such as fire, water.
This class has a healing spell that it can use during battle.
	
Bonus Stats : Magic : + 20 , HP : + 15
Class Weakness Stats : Str : - 2
\n
		"""
		
		print DWclass_help
		
	def FE_Class_Help(self, color_yellow) :
		FEclass_help = \
		"""
		Fairy Elf
		------------
		
The Fairy Elf class deals bonus damage, due to being more of a
dexterity character. If you love dealing bonus damage to mobs.
Then this class is for you! \n
The fairy Elf has no weaknesses due to elfs robust bloodline that is
immune from diseases.
	
Bonus Stats : Str : + 5 , Magic : + 5 , HP : + 5
Class Weakness Stats : None
\n
		"""
		
		print FEclass_help

class Lorencia(object) :
	
	def __init__(self) :
		self.lorencia()
		
	def lorencia(self) :
		Lorencia = \
		"""
	Lorencia
	---------
Now a wreckage from the destruction from the rogue Blade Knight.
Lorencia is Home to the Dark Knights and Dark Wizards.
		"""
		print Lorencia
		
class Credits(object) :
	
	def __init__(self) :
		""" Class Constructor """
		self.Creds(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		
	def Creds(self, color_yellow) :
		credits = \
		"""
\t\t\tCredits
\t\t\t--------

- A.Taylor - S3pHiRoTh / Programmer
- G.Rossum - Python
- Notepad ++ ( Best theme = obsidian! )
- Andre - CLI color wrapper
- WEBZEN - Story Theme / Class Type Idea
	"""
		print credits