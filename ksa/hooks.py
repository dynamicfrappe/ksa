from . import __version__ as app_version

app_name = "ksa"
app_title = "Ksa"
app_publisher = "8848 Digital LLP"
app_description = "Regional Compliance app for Saudi Arabia"
app_email = "contact@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ksa/css/ksa.css"
# app_include_js = "/assets/ksa/js/ksa.js"

# include js, css files in header of web template
# web_include_css = "/assets/ksa/css/ksa.css"
# web_include_js = "/assets/ksa/js/ksa.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ksa/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ksa.utils.jinja_methods",
#	"filters": "ksa.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ksa.install.before_install"
after_install = "ksa.saudi_arabia.setup.setup"
after_migrate = "ksa.saudi_arabia.setup.add_symbol"

# Uninstallation
# ------------

# before_uninstall = "ksa.uninstall.before_uninstall"
# after_uninstall = "ksa.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ksa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Company": {
                "on_trash": ["ksa.saudi_arabia.utils.delete_vat_settings_for_company"],
                "after_insert": ["ksa.saudi_arabia.wizard.operations.setup_tax_templates.setup_templates",
                              "ksa.saudi_arabia.setup.create_company_settings"]
        },
        "Sales Invoice": {
		"on_submit": [
                        "ksa.saudi_arabia.utils.create_qr_code",
		],
		"on_cancel": [
			"ksa.saudi_arabia.utils.delete_qr_code_file"
		]
	},
        "POS Invoice": {"on_submit": ["ksa.saudi_arabia.utils.create_qr_code"]},

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ksa.tasks.all"
#	],
#	"daily": [
#		"ksa.tasks.daily"
#	],
#	"hourly": [
#		"ksa.tasks.hourly"
#	],
#	"weekly": [
#		"ksa.tasks.weekly"
#	],
#	"monthly": [
#		"ksa.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ksa.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ksa.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ksa.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ksa.auth.validate"
# ]
