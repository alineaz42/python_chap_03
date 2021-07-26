story = "Once upon a time there was a stupid little brat name Ali Neaz"

# print(story[0])
# print(story[0:])
# print(story[:61])
# print(story[0::2])
# print(story[::3])
# print(story[::4])
# _____________________string functions _____________________
# 01
storyLen = len(story)
# print(storyLen)
# 02
# print(story.endswith("Neaz"))
# 03
# print(story.count("a"))  # can be done also for word
# 04
story = "once upon a time there was a stupid little brat name Ali Neaz"

# print(story.capitalize())
# 05
print(story.find("Ali"))
print(story.find("Once"))  # -1 means false
print(story.find("once"))
# 06
print(story.replace("Ali", "Neaz"))
print(story.replace("t", "S"))
