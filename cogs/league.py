import discord
from discord.ext import commands
import configparser
from riotwatcher import RiotWatcher

class League:
	"""Commands that use the Riot API"""

	def __init__(self, bot):
		self.bot = bot
		self.config = configparser.ConfigParser()
		self.config.read('../red_config.ini')
		self.riot = RiotWatcher(self.config['api_keys']['riot'])

	def getId(self, summoner):
		return self.riot.get_summoner(name=summoner)['id']

	@commands.command()
	async def masterypages(self, summoner : str):
		"""Gets the mastery page names for summoner"""
		sId = self.getId(summoner)
		pages = self.riot.get_mastery_pages([sId])[str(sId)]['pages']
		output = "These are the mastery pages for **" + summoner + "**:\n"
		output += pages[0]['name']
		for page in pages[1:]:
			output += ", " + page['name']
		output += "\n\nNow type `masteries \"" + summoner + "\" \"<mastery-page-name>\"` to get more details!"
		await self.bot.say(output) 

	@commands.command()
	async def masteries(self, summoner : str, pagename : str):
		"""Gets the mastery pages for summoner"""
		sId = self.getId(summoner)
		pages = self.riot.get_mastery_pages([sId])[str(sId)]['pages']
		page = next(p for p in pages if p['name'] == pagename)

		if page == None:
			await self.bot.say(summoner + " has no mastery page named " + pagename)
		else:
			output = "**" + page['name'] + "**\n"
			for masteryObj in page['masteries']:
				mastery = self.riot.static_get_mastery(masteryObj['id'])['name']
				output += "\n" + str(masteryObj['rank']) + " point" + ("s" if masteryObj['rank'] > 1 else "") + " in *" + mastery + "*"
			await self.bot.say(output)

def setup(bot):
	bot.add_cog(League(bot))