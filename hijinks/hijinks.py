import mechanize
import requests

br = mechanize.Browser()
# br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)

# Wow. It is a  featured comment!

# response = br.open("https://murmuring-headland-7671.herokuapp.com/users//add/")
# print response.read()

# for form in br.forms():
#     print("Form Name: %s" % form.name)
#     print form


# Form Name: None
# <POST https://murmuring-headland-7671.herokuapp.com/users/0/edit/ application/x-www-form-urlencoded
#   <HiddenControl(csrfmiddlewaretoken=CJAp06jmjwMq1xBnQQbFa7sTagYPrSHv) (readonly)>
#   <TextControl(first_name=)>
#   <TextControl(last_name=)>
#   <TextControl(email=)>
#   <TextareaControl(bio=)>
#   <SubmitControl(<None>=Save) (readonly)>>
