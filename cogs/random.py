import discord
from discord.ext import commands

class Random:
	"""Random commands"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def breadstairs(self):
		"""Breadstairs."""
		await self.bot.say("https://pbs.twimg.com/media/Csg4iQfW8AAjm9b.jpg:large")

def setup(bot):
	bot.add_cog(Random(bot))