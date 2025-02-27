#client.XXXX <border> <background> <text> [<indicator> [<child_border>]]
focused_border = input("Enter the focused border: ")
unfocused_border = input("Enter the unfocused border: ")
inactive_border = input("Enter the inactive border: ")
focused_background = input("Enter the focused background: ")
unfocused_background = input("Enter the unfocused background: ")
inactive_background = input("Enter the inactive background: ")
focused_text = input("Enter the focused text: ")
unfocused_text = input("Enter the unfocused text: ")
inactive_text = input("Enter the inactive text: ")
swaysettings = (f"""
client.focused          #{focused_border}  #{focused_background} #{focused_text} 
client.focused_inactive #{inactive_border} #{inactive_background} #{inactive_text}
client.unfocused        #{unfocused_border} #{unfocused_background} #{unfocused_text}""")
f = open("colorscheme", "a")
f.write(swaysettings)
f.close()

