print("Hello my name is chance :-)")

programming_languages = "Python", "Java", "C++", "C#"

for language in programming_languages:
	print(language)


game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0],]



def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game):
			print(count, row)
		return game_map
	except IndexError:
		print("Did you attempt to play a row or column outside the range of 0, 1, or 2? (Index Error)")
		return False
	except Exception as e:
		print(str(e))
		return False
	

game = game_board(game, player=1, row=3, column=1)