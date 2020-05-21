import os 
import shutil

__banner__ = """

███╗   ███╗██╗   ██╗███████╗██╗██╗  ████████╗███████╗██████╗ 
████╗ ████║╚██╗ ██╔╝██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║ ╚████╔╝ █████╗  ██║██║     ██║   █████╗  ██████╔╝
██║╚██╔╝██║  ╚██╔╝  ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║   ██║   ██║     ██║███████╗██║   ███████╗██║  ██║
╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝
	Make Your Life easier! | Trippingcarpet
"""
print(__banner__)
print('*'*60)
print("""
1.Choose own directories
2.Make auto filtering(recommend)
""")
print('*'*60)
option = input('Select(1/2): ')
print('*'*60)

if option == '2':

	path = input('Enter path: ')
	path = os.path.join(path)

	files = os.listdir(path)

	def makeJoinPNG():
		
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.png') or x.endswith('.jpg') or x.endswith('.jpeg') or x.endswith('.ico') or x.endswith('.gif') or x.endswith('.svg'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'images/'))
					count += 1
				except:
					print('One of files already exists. Y it will delete dublicate N it will continue working.')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						dublicate += 1
						os.remove(os.path.join(path,x))
						continue
					else:
						continue

		print('Moved {} image files. Deleted dublicates {}' .format(count, dublicate))


	def makejoinARC():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.deb') or x.endswith('.rar') or x.endswith('.zip') or x.endswith('.xz'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'archives/'))
					count += 1
				except:
					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						dublicate += 1
						os.remove(os.path.join(path,x))
						continue

					else:
						break;

		print('Moved {} archive. Deleted dublicates {} ' .format(count, dublicate))

	def makejoinVID():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.mkv') or x.endswith('.webm') or x.endswith('.mp4'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'videos/'))
					count += 1
				except:
					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						os.remove(os.path.join(path,x))
						dublicate += 1
						continue

					else:
						break;

		print('Moved {} video files. Deleted dublicates {}' .format(count, dublicate))

	def makejoinCODE():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.py') or x.endswith('.html') or x.endswith('.css') or x.endswith('.cpp') or x.endswith('.js') or x.endswith('.jar') or x.endswith('.log') or x.endswith('.php'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'codes/'))
					count += 1
				except:
					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						os.remove(os.path.join(path,x))
						dublicate += 1
						continue

					else:
						break;

		print('Moved {} code files. Deleted dublicates {}' .format(count, dublicate))

	def makejoinDOC():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.ppt') or x.endswith('.pptx') or x.endswith('.docx') or x.endswith('.xls') or x.endswith('.ACCDB'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'documents/'))
					count += 1
				except:
					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						os.remove(os.path.join(path,x))
						dublicate += 1
						continue

					else:
						break;

		print('Moved {} doc files. Deleted dublicates {}' .format(count, dublicate))

	def makejoinBOOK():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.pdf'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'books/'))
					count += 1
				except:

					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						os.remove(os.path.join(path,x))
						dublicate += 1
						continue

					else:
						break;

		print('Moved {} books files. Deleted dublicates {}' .format(count, dublicate))

	def makejoinMUS():
		count = 0
		dublicate = 0

		for x in files:

			if x.endswith('.mp3'):
				try:
					shutil.move(os.path.join(path,x), os.path.join(path,'musics/'))
					count += 1
				except:

					print('One of files already exists')

					l = input('Continue(Y/N)?: ')

					if l == 'Y':
						os.remove(os.path.join(path,x))
						dublicate += 1
						continue

					else:
						break;

		print('Moved {} mp3 files. Deleted dublicates {}' .format(count, dublicate))

	if not os.path.exists(os.path.join(path,'images/')):
	    os.mkdir(os.path.join(path,'images/'))
	    
	    makeJoinPNG()
	    

	if not os.path.exists(os.path.join(path,'archives/')):
		try:
			os.mkdir(os.path.join(path,'archives/'))

		except:
			print('File already created')

		makejoinARC()

	if not os.path.exists(os.path.join(path,'videos/')):
		
		try:
			os.mkdir(os.path.join(path,'videos/'))
			makejoinVID()
		except:
			print('File already created')

	if not os.path.exists(os.path.join(path,'codes/')):
		
		try:
			os.mkdir(os.path.join(path,'codes/'))
			makejoinCODE()
		except:
			print('File already created')

	if not os.path.exists(os.path.join(path,'documents/')):
		try:
			os.mkdir(os.path.join(path,'documents/'))
			makejoinDOC()
		except:
			print('File already created')

	if not os.path.exists(os.path.join(path,'books/')):
		try:
			os.mkdir(os.path.join(path,'books/'))
			makejoinBOOK()
		except:
			print('File already created')


	if not os.path.exists(os.path.join(path,'musics/')):
		try:
			os.mkdir(os.path.join(path,'musics/'))
			makejoinMUS()
		except:
			print('File already created')
		
	else:
		print('There are folder with content. Do you wanna add in it?(Y/N)')

		x = input()

		if x == 'Y':

			makeJoinPNG()
			makejoinARC()
			makejoinVID()
			makejoinCODE()
			makejoinDOC()
			makejoinBOOK()
			makejoinMUS()

		else:
			print('Okay Program end work...')



elif option == "1":
	print('')
	print('*'*60)
	print('Write 0 if you don`t want to filter that format.None Dublicate deleteable.')
	print('*'*60)
	print('')

	path   = input('Select path to filter folder: ')
	images = input('Select folder where move images: ')
	musics = input('Select folder where move musics or audio files: ')
	codes = input('Select folder where move codes: ')
	arc = input('Select folder where move archives: ')
	books = input('Select folder where move books(PDF): ')
	documents = input('Select folder where move documents: ')
	
	files = os.listdir(path)
	images_score = 0
	code_score   = 0
	text_score   = 0
	mp3_score    = 0
	png_score    = 0
	arc_score    = 0
	books_score  = 0
	docs_score   = 0
	 
	for file in files:

		if images != '0' and file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('png'):
			
			if file.endswith('.jpg') or file.endswith('.jpeg') :
				try:
					shutil.move(os.path.join(path, file),os.path.join(images))

				except:
					continue

				finally:
					print('Something goes wrong! But program continue working...')

				images_score += 1

			elif file.endswith('.png') or file.endswith('.ico'):
				try:
					shutil.move(os.path.join(path, file),os.path.join(images))

				except:
					continue

				finally:
					print('Something goes wrong! But program continue working...')

				png_score += 1

		if codes != '0' and file.endswith('.py') or file.endswith('.html') or file.endswith('.css') or file.endswith('.cpp') or file.endswith('.js') or file.endswith('.jar') or file.endswith('.log') or file.endswith('.php'):

			if file.endswith('.html'):
				try:
					shutil.move(os.path.join(path, file),os.path.join(codes))

				except:
					continue

				code_score += 1

			elif file.endswith('.css'):
				try:
					shutil.move(os.path.join(path, file),os.path.join(codes))

				except:
					continue

				code_score += 1

			elif file.endswith('.py'):
				try:
					shutil.move(os.path.join(path, file),os.path.join(codes))

				except:
					continue

				code_score += 1

			else:

				try:
					shutil.move(os.path.join(path, file),os.path.join(codes))

				except:
					continue

				code_score += 1

		if arc != "0" and file.endswith('.xz') or file.endswith('.rar') or file.endswith('.zip') or file.endswith('.deb'): 

			try:
				shutil.move(os.path.join(path, file),os.path.join(arc))

			except:
				continue

			arc_score += 1

		
		if musics != "0" and file.endswith('.mp3') or file.endswith('.m4a') or file.endswith('.mp4'):

			if file.endswith('.mp3'):
				try:
					shutil.move(os.path.join(path,file), os.path.join(musics))	 #your directory if you want

				except:
					continue

				mp3_score += 1


			elif file.endswith('.m4a'):
				try:
					shutil.move(os.path.join(path,file), os.path.join(musics))	#your directory if you want

				except:
					continue

				mp3_score += 1

			elif file.endswith('.mp4'):
				try:
					shutil.move(os.path.join(path,file), os.path.join(musics))	#your directory if you want

				except:
					continue

				mp3_score += 1
		
		if books != "0" and file.endswith('.pdf') or file.endswith('.PDF'):
			try:
				shutil.move(os.path.join(path, file),os.path.join(books))
			except:
				continue

			books_score += 1

		if documents != "0" and file.endswith('.ppt') or file.endswith('.pptx') or file.endswith('.docx') or file.endswith('.xls') or file.endswith('.ACCDB'):
			try:
				shutil.move(os.path.join(path, file),os.path.join(documents))
			except:
				continue

			docs_score += 1


	#output info
	print('')
	print('*' * 60)
	if codes != '0':
		print('Moved {} code files.' .format(code_score))
	if images != '0':
		print('Moved {} jpg files.' .format(images_score))
		print('Moved {} png files.' .format(png_score))
	if arc != '0':
		print('Moved {} archive files.' .format(arc_score))
	if musics != '0':
		print('Moved {} mp3/4 and m4a files'.format(mp3_score))
	if books != '0':
		print('Moved {} pdf files'.format(books_score))
	if documents != '0':
		print('Moved {} documents'.format(mp3_score))

	if codes == '0' and images == '0' and arc == '0' and musics == '0' and books == '0' and documents == '0':
		print('No Paths selected')

	print('*' * 60)



