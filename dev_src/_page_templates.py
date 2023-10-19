from data_types import Template
__all__ = [
	"directory_explorer_header",
	"global_script",
	"file_list",
	"upload_form",
	"file_list_script",
	"video_script",
	"zip_script",
	"admin_page",
	"error_page",
	"theme_script",
	"login_page"
]


# ---------------------------x--------------------------------

# PAGE TEMPLATES
##############################################################


enc = "utf-8"


class config:
	dev_mode = True
	file_list = {}

pt_config = config()



def _get_template(path):
	if pt_config.dev_mode:
		with open(path, encoding=enc) as f:
			return f.read()
		
	return pt_config.file_list[path]

def get_template(path):
	return Template(_get_template(path))


def directory_explorer_header():
	return get_template("html_page.html")



def style_css():
	return _get_template("html_style.css")






def global_script():
	return get_template("global_script.js")

def assets_script():
	return get_template("html_script.js")

def file_list_script():
	return get_template("html_file_list.js")

def upload_form():
	return _get_template("html_upload.html")

def video_script():
	return get_template("html_vid.html")

def zip_script():
	return get_template("html_zip_page.html")

def admin_page():
	return get_template("html_admin.html")

def error_page():
	return directory_explorer_header() + get_template("html_error.html")

def theme_script():
	return get_template("html_theme_script.js")
	
def login_page():
	return get_template("html_login.html")

def signup_page():
	return get_template("html_signup.html")

#directory_explorer_header()

