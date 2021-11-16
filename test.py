from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./scenarios")
bot.sort_replies()


def qwe(text):
		if text == '/quit':
				quit()

		reply = bot.reply("localuser", text)
		print('Bot>', reply)


while True:
		qwe(input())
