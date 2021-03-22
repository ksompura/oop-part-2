nums = [2,63,854,43,1,23,78]
print(max(nums))
print(min(nums))

names = ["Arya", "Samson", "Dora","Tim","Ollivander"]
# min(len(name) for name in names) # 3

#find longest name
print(max(names,key= lambda n: len(n)))
print(min(names,key= lambda n: len(n)))

playlist = [

	{"title":"You Shook Me All Night Long", "artist":["AC/DC"], "duration":3.5},
	{"title":"You Spin Me Round (Like a Record)", "artist":["Dead or Alive"], "duration":3.4},
	{"title":"Everbody Wants To Rule The World", "artist":["Tears For Fears"], "duration":4.2}]


#find the longest shortest song
print(min(playlist,key= lambda s: s["duration"])["title"])
