class FileLoad:
	def __init__(self):
		print('FileLoad init...')
		
	def __del__(self):
		print('FileLoad delete...')				
		
	def load_list(self, file):
	    conf = open(file)
	    list = []
	    for line in conf:
	        list.append(line.strip())
	    conf.close()
	    return list		
	    
	def load_dict(self, file):
	    conf = open(file)
	    dict = {}
	    for line in conf:
	        if len(line.strip()) > 0:
	            l = line.split(',')
	            dict[l[0].strip()] = l[1].strip()
	    conf.close()
	    return dict	    
