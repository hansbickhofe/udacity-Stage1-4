# My modified Version of the example Script
def make_page_header(styletype):
	# create Pageheader function with Style selector
		# define common Style
	common_style = """
		<style type="text/css">
		* {
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
			-ms-box-sizing: border-box;
			-webkit-flex-wrap: wrap; 
			box-sizing: border-box;
		}	
		.concept-title {
			background-color: rgb(255, 203, 0);
			padding-top: 10px;
			padding-left: 20px;
			padding-right: 20px;
			padding-bottom: 5px;
			border-radius: 15px;
			margin-top: 5px;
			margin-bottom: 5px;
			min-width: 100%;
		}
		.concept-description {
			font-weight: normal;
			font-size: smaller;
			background-color: rgb(170, 190, 250);
			padding-left: 35px;
			padding-right: 35px;
			padding-top: 5px;
			padding-bottom: 5px ;
			margin-bottom: 8px;
			min-width: 100%;
		}		
	"""
	
	# define two sample Styles big and small 
	styles = ["""
		.concept {
			font-family: sans-serif;
			font-weight: bolder;
			font-size: large;
			padding-left: 30px;
			max-width: 80%;
			display: -webkit-flex; /* Safari */
			display: flex;   
			flex-wrap: wrap;
			}
		</style>""",
		"""
		.concept {
			font-family: sans-serif;
			font-size: small;
			padding-left: 30px;
			max-width: 80%;
			display: -webkit-flex; /* Safari */
			display: flex;   
			flex-wrap: wrap;
		}
		</style>"""
		]
	# Select Big Style if defined, all others point to small Style
	if styletype == "big":
		selected_style = common_style + styles[0]
	else:
		selected_style = common_style + styles[1]			
		
	# create complete Header
	headerHTML = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Udacity Stage2: Notes generated with script</title>
		<link rel="stylesheet" href="http://normalize-css.googlecode.com/svn/trunk/normalize.css" />""" + selected_style + """
		<link rel="icon" href="favicon.ico" sizes="16x16" type="image/png">
	</head>
	<body>
	"""	
	return headerHTML
	
def generate_concept_HTML(concept_title, concept_description):
	while True:
		html_text_1 = '''
	<div class="concept">
		<div class="concept-title">
			''' + concept_title
		html_text_2 = '''
		</div>
		<div class="concept-description">
			''' + concept_description
		html_text_3 = '''
		</div>
	</div>
	<br>
	''' # added <br> Tag to seperate conecepts
		full_html_text = html_text_1 + html_text_2 + html_text_3
		return full_html_text
		break
    
	
def make_page_footer():
	# make Pagefooter function
	footerHTML = "</body></html>"
	return footerHTML	

def make_HTML(concepts,style):
	# make Pagecontent function
	HTML = ""
	HTML += make_page_header(style) # first make Pageheader
	
	# create Content
	for concept in concepts:
		HTML += generate_concept_HTML(concept[0],concept[1])
	
	HTML += make_page_footer() # add Pagefooter
	return HTML

	
# My pagecontent - Example extended
EXAMPLE_CONCEPT = [["Computers","""
Unlike to most machines that were <strong>constructed</strong> 
for one or more specific functions, a computer can be <strong>
programmed</strong> to solve tasks of many different types."""]]
EXAMPLE_CONCEPT.append(["Programms","""
A program consists of a <strong>sequence</strong> of operating procedures which 
result in a more or less meaningful Programm at the end. <br>
This could be an editor, a spreadsheetcalculation or even a game."""])
EXAMPLE_CONCEPT += [["Programming Languages","""
There are different languages to tell the computer how <strong>to do</strong>
something. <br>Examples of common used languages are python, php, java, c(c++), 
javascript or go. <br>The choice of language is mostly dependent on the type of program you 
plan to create."""]]



print make_HTML(EXAMPLE_CONCEPT,"big") # select Big Style
