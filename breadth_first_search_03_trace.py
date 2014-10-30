# BFS algorithm. Shows trace. 


graph = {
    "1": ["2", "3"],
    "2": ["1", "4", "5"],
    "3": ["1", "6", "7"],
    "4": ["2", "8", "9"],
    "5": ["2"],
    "6": ["3", "10", "11"],
    "7": ["3"],
    "8": ["4"],  
    "9": ["4","12"],
    "10": ["6", "13", "14"], 
    "11": ["6"],
    "12": ["9"],
    "13": ["10"],
    "14": ["10"]
    }
 

class my_queue: #implementation of a queue
	
	def __init__(self):
		self.holder = []		
	def enqueue(self,value):
		self.holder.append(value)		
	def dequeue(self):
		value = None
		try:
			value = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass			
		return value	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result

path_queue = my_queue() # now we make a queue


def bfs(graph, start, end, q):
	q.enqueue([start])	
	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		print(tmp_path)
		if last_node == end:
			print("Desired path: %s" % tmp_path)
		for i in graph[last_node]:
			if i not in tmp_path:
				new_path = []
				new_path = tmp_path + [i]
				q.enqueue(new_path)

bfs(graph,"1","14",path_queue)





