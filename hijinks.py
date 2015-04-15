import mechanize
br = mechanize.Browser()
# br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)

response = br.open("https://murmuring-headland-7671.herokuapp.com/users//add/")
print response.read()

for form in br.forms():
    print("Form Name: %s" % form.name)
    print form
