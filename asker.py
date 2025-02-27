#client.XXXX <border> <background> <text> [<indicator> [<child_border>]]
def sametextandinactive():
    focused_border = input("Enter the focused border: ")
    unfocused_border = input("Enter the unfocused border: ")
    focused_background = input("Enter the focused background: ")
    unfocused_background = input("Enter the unfocused background: ")
    text_color = input("Enter the text color: ")
    swaysettings = (f"""
    client.focused          #{focused_border}  #{focused_background} #{text_color} 
    client.focused_inactive #{unfocused_border} #{unfocused_background} #{text_color}
    client.unfocused        #{unfocused_border} #{unfocused_background} #{text_color}""")
    f = open("colorscheme", "a")
    f.write(swaysettings)
    f.close()

def changebartoo():
    focused_border = input("Enter the focused border: ")
    unfocused_border = input("Enter the unfocused border: ")
    focused_background = input("Enter the focused background: ")
    unfocused_background = input("Enter the unfocused background: ")
    text_color = input("Enter the text color: ")
    swaysettings = (f"""
    client.focused          #{focused_border}  #{focused_background} #{text_color} 
    client.focused_inactive #{unfocused_border} #{unfocused_background} #{text_color}
    client.unfocused        #{unfocused_border} #{unfocused_background} #{text_color}""")
    swaybarsettings = (f"""
    bar {{
        position top 
        mode dock 
        status_command while ~/.config/sway/status.sh; do sleep 1; done
        colors {{
            statusline #{text_color}
            background #{unfocused_background}
        inactive_workspace #{unfocused_border} #{unfocused_background} #{text_color}
            focused_workspace #{focused_border} #{unfocused_background} #{text_color}
        }}
    }}""")
    f = open("colorscheme", "a")
    f.write(swaysettings)
    f.write(swaybarsettings)
    f.close()
if __name__ == "__main__":
    print("If you wish to change both the swaybar and the sway config, press 1. Else, press anything else: ")
    choice = int(input())
    if choice == 1:
        changebartoo()
    else:
        sametextandinactive
