"""
- Project : Text RPG!
- Class description : Battle system/Level up system/Hero properties Class module
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh
"""

# Import Modules
from random import randrange

# Import andre's CLI color wrapper
import color_console as cons

# Import map descriptions
from interface import Lorencia

# Properties for CLI font color
default_colors = cons.get_text_attr()
default_bg = default_colors & 0x0070
cons.set_text_attr(cons.FOREGROUND_GREY | default_bg |
cons.FOREGROUND_INTENSITY)
				
class Battle_Phase(object) :
	# These variables should update in real time
	# Hero Properties

	# Hero Base level
	Hero_LVL = 1
	
	# Hero default name
	HERO_NAME = ['Hero']
	HERO_DEFAULT_NAME = ['Hero']
	HERO_CLASS = ['Placeholder']
	DEFAULT = "default"
	
	# Class selector variables.
	DARK_KNIGHT = "Dark Knight"
	DARK_WIZARD = "Dark Wizard"
	FAIRY_ELF = "Fairy Elf"
	
	# Hero base health
	Hero_base_health = 50
	# Hero max health
	Hero_max_health = 50
	# Hero base Magicka
	Hero_base_magic = 10
	# Hero max Magicka
	Hero_max_magic = 10
	# Hero current magic power
	# These attributes won't be added until user picks the class
	# They will stay at default 0 if user plays as a Dark Knight & Fairy Elf
	Hero_min_magic_power = 0
	Hero_max_magic_power = 0
	# Hero current skill power. This is for the Fairy Elf, to deal bonus damage ;
	# same as above, these attributes are only available to the Fairy elf, and not the other two classes
	Hero_min_skill_power = 0
	Hero_max_skill_power = 0
	# Hero base strength
	Hero_base_str = 10
	Hero_min_dmg = 1
	
	# Hero weapon slot
	HERO_WEAPON_SLOT = ['']	# Max slot = [1]
	# Hero inventory
	HERO_INVENTORY = ['']
	# Hero total gold
	Hero_total_gold = 0

	# These variables are here so the game can change them in real-time.
	# Also if other programmers wish to edit the values, they can, EASILY! ;-)
	# Without tinkering with the main event loop! 
	
	mob_exp = 100
	mob_hp = 15
	
	mob_hp_reset = 15
	
	total_experience = 0
	total_exp_for_next_level = 50
	total_exp_for_next_level_FACTOR = 50
	exp_to_next_lvl = 50
	New_EXP_WF_FACTOR = 100
	
	# Hero class bonus attributes
	# Dark knight bonus stats & weakness stats
	DARK_KNIGHT_STR_BONUS = 10
	DARK_KNIGHT_HP_BONUS = 20
	DARK_KNIGHT_MAGIC_WEAKNESS = 5
	
	# Dark Wizard bonus stats & weakness stats
	DARK_WIZARD_MAGIC_BONUS = 20
	DARK_WIZARD_HP_BONUS = 15
	DARK_WIZARD_STR_WEAKNESS = 2
	DARK_WIZARD__MIN_MAGIC_POWER = 2
	DARK_WIZARD_MAX_MAGIC_POWER = 6
	
	# Fairy Elf bonus stats & weakness stats
	FAIRY_ELF_STR_BONUS = 5
	FAIRY_ELF_MAGIC_BONUS = 15
	FAIRY_ELF_HP_BONUS = 5
	FAIRY_ELF_MIN_SKILL_POWER = 1
	FAIRY_ELF_MAX_SKILL_POWER = 4
	
	# Game location variable
	# This variable will be updated constantly when user
	# switches locations
	current_location = ['Lorencia']
	
	# Message variables
	Spell_MSG = "[SPELL SYSTEM]"
	Battle_MSG = "[BATTLE SYSTEM]"
	Help_MSG = "[HELP SYSTEM]"
	Lvl_MSG = "[LEVEL-UP SYSTEM]"
	Boss_MSG = "[BOSS ENCOUNTERED]"
	Game_Over_MSG = "[GAME OVER!]"
	
	def __init__(self) :
		# Call Menu_System function and color it cyan using andre's color wrapper
		self.HP_Restore_Onlevelup()
		self.Mana_Restore_Onlevelup()
		self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		
	def Hero_Start_town(self) :
		# I only want this function to be called once, because this function is only
		# for the starting town for the hero.
		while True :
		# If class = Dark Knight. Player starts in Lorencia 
			if self.DARK_KNIGHT in self.HERO_CLASS[0] :
				pass
		# If class = Dark Wizard, Player starts in Lorencia
			elif self.DARK_WIZARD in self.HERO_CLASS[0] :
				pass
		# If class = Fairy Elf, Player starts in Noria
			elif self.FAIRY_ELF in self.HERO_CLASS[0] :
				pass
		
	def hero_spell_check(self) :
		# This function is for checking if the hero is a wizard.
		# So user can access spells. Other class's can't.
		if self.DARK_KNIGHT in self.HERO_CLASS[0] :
			print "%s Dark Knight class cannot use spells!" %(self.Help_MSG)
			return
		if self.DARK_WIZARD in self.HERO_CLASS[0] :
			# Spell function will go here
			self.test_wiz_spell()
			return
		if self.FAIRY_ELF in self.HERO_CLASS[0] :
			print "%s Fairy Elf cannot use spells!" %(self.Help_MSG)
			return
			
	def hero_skill_check(self) :
		# This function is for checking if the hero is a Elf.
		# So user can access Fairy Elf skills & Other class's can't.
		if self.DARK_KNIGHT in self.HERO_CLASS[0] :
			print "%s Dark Knight class cannot use skills!" %(self.Help_MSG)
			return
		if self.DARK_WIZARD in self.HERO_CLASS[0] :
			print "%s Dark Wizard class cannot use skills!" %(self.Help_MSG)
			return
		if self.FAIRY_ELF in self.HERO_CLASS[0] :
			print "%s Fairy Elf can use skills!" %(self.Help_MSG)
			return
			
	def test_wiz_spell(self) :
		spell_opt = \
		"""
		%s's Spells
		-------------
		1 - Full Heal - magicka use : 40
		2 - Heal small wounds - Magicka use : 5
		"""%(self.HERO_NAME[0])
		
		print spell_opt
		
		Use_spell = raw_input("%s What spell would you like to use? : " %(self.Spell_MSG))
		if Use_spell == "1" :
			print "%s You have chosen to use the Full heal spell!" %(self.Spell_MSG)
			self.full_heal_spell()
	
	def full_heal_spell(self) :
	# Function for restoring the heros health while using a spell
		while self.Hero_base_health <= self.Hero_max_health :
			if self.Hero_base_health >= self.Hero_max_health :
				break
		# Restores the heros base health in 1 increments until it reaches the max hp quota
			self.Hero_base_health += 1
		self.Hero_base_magic = self.Hero_base_magic - 30
			
	def Menu_System(self, color_cyan) :
		menu_OP = \
		"""
			0 - Acess Inventory
			1 - Location Select
			2 - Hero stats
			3 - Enter Battle location
			4 - Enter Town
		"""
		
		print menu_OP
		MS = raw_input("Select the option from the menu : ")
		if MS == "0" :
			print "Your current inventory is : %s" %(self.HERO_INVENTORY[0:10])
			return self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		if MS == "1" :
			print "Location Module not available yet!"
			return self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		elif MS == "2" :
			self.Stats_title(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
			self.Stats(color_green = cons.set_text_attr(cons.FOREGROUND_GREEN))
			return self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		elif MS == "3" :
			print "You have chosen to enter a battle!"
			self.Encounter_Phase(color_red = cons.set_text_attr(cons.FOREGROUND_RED))
		elif MS == "4" :
			print "Town Module not available yet!"
			return self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		else :
			print "You didn't enter a vaild number range!"
			self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
			
	def Encounter_Phase(self, color_red) :
		# This function is just for looping back and forth between phases.
		raw_input("You have encountered a hostile monster! %s Press the ENTER Key!" %(self.Help_MSG))
		self.Battle_mob_phase(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))

	def PlayerDieMSG(self) :
		print "%s %s Died! But you gained a grand total of %i experience! " %(self.Game_Over_MSG, self.HERO_NAME[0], self.total_experience)
		
	def Battle_mob_phase(self, color_yellow) :
		# Monster battle phase
		while self.Hero_base_health > 0 :
			self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
			# Monster & Player battle phase properties
			# Hero's min - max damage | max dmg = base_str
			self.player_dmg = randrange(self.Hero_min_dmg, self.Hero_base_str)
			self.mob_dmg = randrange(1,5)
			self.mob_hp = self.mob_hp - self.player_dmg
			print "%s You did %i of damage to the monster! \n" %(self.Battle_MSG, self.player_dmg)
			self.continue_mob_battle_phase(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
			print "%s mob hits you for %i damage! \n" %(self.Battle_MSG, self.mob_dmg)
			self.Hero_base_health = self.Hero_base_health - self.mob_dmg
			# Certain battle phase conditions. These will execute if the conditions are met!
			if self.mob_hp < 0 :
				self.mob_hp += 15
				self.total_experience = self.mob_exp + self.total_experience
				print "%s You defeated the mob! With %i life remaining!" %(self.Battle_MSG, self.Hero_base_health)
			# Return to the menu after monster has been defeated
				self.Menu_System(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
			elif self.Hero_base_health < 10 :
				print "%s NO!! You're near death! With only %i hp left! Use a potion!" %(self.Help_MSG, self.Hero_base_health)
			# Level up system
			elif self.total_experience >= self.total_exp_for_next_level :
				self.Level_System_Function(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
				self.Next_LVL()
				self.Next_LVL_PHASE()
				return
				
		# If player dies
		self.PlayerDieMSG()
		return
		
	def continue_mob_battle_phase(self, color_yellow) :
		raw_input("%s Press enter to continue the battle phase. " %(self.Battle_MSG))
		# Add new line in console..
		print "\n"
		# return to the battle phase
		return
		
	def continue_player_battle_phase(self, color_yellow) :
		raw_input("%s Press enter to attack the monster! " %(self.Battle_MSG))
		# Add new line in console..
		print "\n"
		# return to the battle phase
		return
		
	def Level_System_Function(self, color_yellow) :
		self.Hero_LVL += 1
		self.Onlevelup()
		self.HP_Restore_Onlevelup()
		self.Mana_Restore_Onlevelup()
		print "%s Your hero has grown a level! You're now level %i ! " %(self.Lvl_MSG, self.Hero_LVL)
		return
	
	def Onlevelup(self) :
		# Bonus stats to add when hero levels up
		# Checks what race the hero is ( Dark Knight, Dark Wizard, etc )
		# If race = Dark Knight
		if self.DARK_KNIGHT in self.HERO_CLASS[0] :
		# Strength stats to be added to hero stats on level-up!
			self.Hero_base_str +=1
		# HP stats to be added to hero stats on level-up!
			self.Hero_max_health +=2
		# If race = Dark Wizard
		elif self.DARK_WIZARD in self.HERO_CLASS[0] :
		# Magicka stats to be added to hero stats on level-up!
			self.Hero_max_magic +=2
		# HP stats to be added to hero stats on level-up!
			self.Hero_max_health +=1
		# If race = Fairy Elf
		elif self.FAIRY_ELF in self.HERO_CLASS[0] :
		# Strength stats to be added to hero stats on level-up!
			self.Hero_base_str +=1
		# HP stats to be added to hero stats on level-up!
			self.Hero_max_health +=1
		# Magicka stats to be added to hero stats on level-up!
			self.Hero_max_magic +=1
		
	def HP_Restore_Onlevelup(self) :
		# Function for restoring the heros health on level up
		while self.Hero_base_health <= self.Hero_max_health :
			if self.Hero_base_health >= self.Hero_max_health :
				break
		# Restores the heros base health in 1 increments until it reaches the max hp quota
			self.Hero_base_health += 1
	
	def Mana_Restore_Onlevelup(self) :
		# Function for restoring the heros magicka on level up
		while self.Hero_base_magic <= self.Hero_max_magic :
			if self.Hero_base_magic >= self.Hero_max_magic :
				break
		# Restores the heros base magicka in 1 increments until it reaches the max mana quota
			self.Hero_base_magic += 1
			
	def Next_LVL(self) :
		self.total_exp_for_next_level = self.New_EXP_WF_FACTOR * 10 + self.exp_to_next_lvl
		self.total_exp_for_next_level_FACTOR += self.total_exp_for_next_level
		
	def Next_LVL_PHASE(self) :
		self.total_exp_for_next_level = self.New_EXP_WF_FACTOR * 10 + self.total_exp_for_next_level_FACTOR
		
	def Menu_options(self, color_cyan) :
		inv_menu = \
		"""
\t\t\t %s's Battle Menu
\t\t\t ---------------------
\t\t\t 1 - Attack
\t\t\t 2 - Spell Book (Dark Wizard Only)
\t\t\t 3 - Skill List (Fairy Elf Only)
\t\t\t 4 - Access Inventory
\t\t\t 5 - Show Current hero stats
		"""%(self.HERO_NAME[0])
		
		print inv_menu
		
	def Stats(self, color_green) :
		# These stats update in real time, even within the main game loop!
		hero_stats = \
		"""
\t\t\t Name : %s	Level : %i
\t\t\t Race : %s
\t\t\t Health : %i/%i	 Magicka : %i/%i
\t\t\t Min Skill power : %i	Max Skill power : %i
\t\t\t Min Magic power : %i	Max Magic power : %i
\t\t\t Strength : %i 	    Total Gold : %i
\t\t\t Total Experience gained : %i
		"""%(self.HERO_NAME[0], self.Hero_LVL, self.HERO_CLASS[0], self.Hero_base_health, self.Hero_max_health,
				self.Hero_base_magic, self.Hero_max_magic, self.Hero_min_skill_power, self.Hero_max_skill_power,
				self.Hero_min_magic_power, self.Hero_max_magic_power,
				self.Hero_base_str, self.Hero_total_gold, self.total_experience)
		
		print hero_stats
		
	def Stats_title(self, color_yellow) :
		hero_stats_title = \
		"""
\t\t\t %s's Character Stats
\t\t\t --------------------
		"""%(self.HERO_NAME[0])
		
		print hero_stats_title
		
	def Hero_Battle_Menu(self, color_grey) :
		self.Menu_options(color_cyan = cons.set_text_attr(cons.FOREGROUND_CYAN))
		battle_menu = raw_input("%s Select the option you wish to choose : " %(self.Battle_MSG))
		# Add a newline in the console...
		print "\n"
		if battle_menu == "1" :
			# Attack choice
			self.continue_player_battle_phase(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
		elif battle_menu == "2" :
			# Spell book choice
			self.hero_spell_check()
			return self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		elif battle_menu == "3" :
			# Access Fairy Elf skill list choice
			self.hero_skill_check()
			return 	self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		elif battle_menu == "4" :
			# Inventory choice
			print "Your current inventory is %s " %(self.HERO_INVENTORY)
			self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		elif battle_menu == "5" :
			# View hero stats choice
			self.Stats_title(color_yellow = cons.set_text_attr(cons.FOREGROUND_YELLOW))
			self.Stats(color_green = cons.set_text_attr(cons.FOREGROUND_GREEN))
			return self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))
		else : 
			# if invalid number range entered
			print "%s You didn't enter a valid number range!" %(self.Battle_MSG)
			self.Hero_Battle_Menu(color_grey = cons.set_text_attr(cons.FOREGROUND_GREY))

class Game_Locations(object) :
	""" Game Locations class """
	
	def Lorencia(self) :
		None
		
	def Noria(self) :
		None
		
	def Devias(self) :
		None
		
	def Dungeon(self) :
		None
		
	def LostTower(self) :
		None
		
class bonus_DK(object) :
	
	def __init__(self) :
		self.DK_bonus_stats()
		
	def DK_bonus_stats(self) :
		# function for the class bonus's!
		# When this function is called, the Dark Knight bonus attributes will be added to the base variables.
		# Add the Dark knight strength bonus to the base hero strength stats
		Battle_Phase.Hero_base_str = Battle_Phase.Hero_base_str + Battle_Phase.DARK_KNIGHT_STR_BONUS
		
		# Add the Dark knight health bonus to the base hero health stats
		Battle_Phase.Hero_max_health = Battle_Phase.Hero_max_health + Battle_Phase.DARK_KNIGHT_HP_BONUS
		
		# Add the Dark Knight magicka weakness attribute to the base magicka stats
		Battle_Phase.Hero_max_magic = Battle_Phase.Hero_max_magic - Battle_Phase.DARK_KNIGHT_MAGIC_WEAKNESS
		Battle_Phase.Hero_base_magic = Battle_Phase.Hero_base_magic - Battle_Phase.DARK_KNIGHT_MAGIC_WEAKNESS

class bonus_DW(object) :
	
	def __init__(self) :
		self.DW_bonus_stats()
		
	def DW_bonus_stats(self) :
		# function for the class bonus's!
		# When this function is called, the Dark Wizard bonus attributes will be added to the base variables.
		# Add the Dark Wizard magicka bonus to the base hero magicka stats
		Battle_Phase.Hero_max_magic = Battle_Phase.Hero_max_magic + Battle_Phase.DARK_WIZARD_MAGIC_BONUS
		
		# Add the Dark Wizard health bonus to the base hero health stats
		Battle_Phase.Hero_max_health = Battle_Phase.Hero_max_health + Battle_Phase.DARK_WIZARD_HP_BONUS
		
		# Add the Dark Wizard min/max magic power class specific attributes
		Battle_Phase.Hero_min_magic_power = Battle_Phase.Hero_min_magic_power + Battle_Phase.DARK_WIZARD__MIN_MAGIC_POWER
		Battle_Phase.Hero_max_magic_power = Battle_Phase.Hero_max_magic_power + Battle_Phase.DARK_WIZARD_MAX_MAGIC_POWER
		
		# Add the Dark Wizard strength weakness attribute to the base strength stats
		Battle_Phase.Hero_base_str = Battle_Phase.Hero_base_str - Battle_Phase.DARK_WIZARD_STR_WEAKNESS

class bonus_FE(object) :

	def __init__(self) :
		self.FE_bonus_stats()
		
	def FE_bonus_stats(self) :
		# function for the class bonus's!
		# When this function is called, the Fairy Elf bonus attributes will be added to the base variables.
		# The Fairy Elf is the only class to not have a weakness atrribute
		# Add the Fairy Elf strength bonus to the base hero strength stats
		Battle_Phase.Hero_base_str = Battle_Phase.Hero_base_str + Battle_Phase.FAIRY_ELF_STR_BONUS
		
		# Add the Fairy Elf health bonus to the base hero health stats
		Battle_Phase.Hero_max_health = Battle_Phase.Hero_max_health + Battle_Phase.FAIRY_ELF_HP_BONUS
		
		# Add the Fairy Elf min/max skill power class specific attributes
		Battle_Phase.Hero_min_skill_power = Battle_Phase.Hero_min_skill_power + Battle_Phase.FAIRY_ELF_MIN_SKILL_POWER
		Battle_Phase.Hero_max_skill_power = Battle_Phase.Hero_max_skill_power + Battle_Phase.FAIRY_ELF_MAX_SKILL_POWER
		
		# Add the Fairy Elf magic bonus attribute to the base magicka stats
		Battle_Phase.Hero_max_magic = Battle_Phase.Hero_max_magic + Battle_Phase.FAIRY_ELF_MAGIC_BONUS
		
class Hero_Spells(object) :
	""" Class for hero Spells """
	
	def __init__(self) :
		""" Hero spells class constructor """
		
	def Heal_Spell(self) :
		# Function to be implemented later!
		None
		
	def Fire_Spell(self) :
		# Function to be implemented later!
		None
		
	def Ice_Spell(self) :
		# Function to be implemented later!
		None
		
	def Lightning_Spell(self) :
		# Function to be implemented later!
		None
		

			