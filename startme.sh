python asker.py
if test -d "$HOME/.config/sway/"; then
  rm $HOME/.config/sway/colorscheme
  echo "Add the lines \'include colorscheme\' to your sway config"
  mv colorscheme $HOME/.config/sway/
fi
