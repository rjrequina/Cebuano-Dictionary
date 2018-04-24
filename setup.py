from distutils.core import setup


setup(
  name = 'cebdict',
  packages = ['cebdict'],
  version = '2.1',
  description = "A Cebuano Dictionary based on Wolff's Dictionary",
  author = 'Arjemariel Requina',
  author_email = 'rjrequina@gmail.com',
  url = 'https://github.com/ajrequina/Cebuano-Dictionary',
  download_url = 'https://github.com/ajrequina/Cebuano-Dictionary/archive/1.0.tar.gz',
  keywords = ['pos-tag dictionary', 'cebuano-dictionary'],
  classifiers = [],
  data_files=[
  	('data', ['cebdict/data/cebposdict.txt']),
  	('data/function_words', [
  		'cebdict/data/function_words/CONJ.txt', 
  		'cebdict/data/function_words/DET.txt',
  		'cebdict/data/function_words/PART.txt',
  		'cebdict/data/function_words/PRON.txt'
  	])
  ]
)