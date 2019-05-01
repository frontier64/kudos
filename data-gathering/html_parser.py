
import scrapy
import re
#USE SCRAPY
class PhysicsSpider(scrapy.Spider):
	name = 'hi'
	#custom_settings = {'LOG_LEVEL': 'CRITICAL',}

	start_urls = ['http://www.physicsgre.com/viewtopic.php?f=3&t=145205']
	def parse(self, response):
		id = 0
		posts = response.css('div.postbody').css('div.content')
		i = 0
		file = open("output.txt", "w+")

		for post in posts:
			text = post.css('*::text')
			l = '\n'.join(map(str, text.getall()))
			print(text.getall())
			file.write("\n\nid:")
			file.write(str(id) + "\n")
			file.write(str(l))

			#Overall GPA
			matcher = re.compile(r'Overall.GPA\s?:\s?(\d\.\d\d?)')
			s = matcher.search(l)
			if s:
				gpa = s.group(1)
			else:
				gpa = "NONE"

			#GRE Scores
			matcher = re.compile(r'GRE Scores.*:.*Q:\s?(\d*).*V:\s?(\d*).*W:\s?(\d*).*P:\s?(\d*)')
			s = matcher.search(l);
			if s:
				q = s.group(1)
				v = s.group(2)
				w = s.group(3)
				p = s.group(4)
			else:
				q = "NONE"
				v = "NONE"
				w = "NONE"
				p = "NONE"
			yield {
				'id': id,
				'gpa': gpa,
				'scores':
					{
					'Q':q,
					'V':v,
					'W':w,
					'P':p,
					}
			}
			id+=1
			i+=1
			if i > 5:
				break
		file.close()