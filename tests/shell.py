from dogtail import tree

shell = tree.root.child(name="sugar-session", roleName="application")

# Complete the intro screen
done_button = shell.child(name="Done", roleName="push button")
done_button.click()

# Switch to the home list view
#radio_button = shell.child(name="List view", roleName="radio button")
#radio_button.click()