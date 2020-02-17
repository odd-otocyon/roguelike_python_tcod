import tcod as libtecod

def main():
  screen_width = 80
  screen_height = 50

  libtecod.console_set_custom_font('arial10x10.png', libtecod.FONT_TYPE_GREYSCALE | libtecod.FONT_LAYOUT_TCOD)

  libtecod.console_init_root(screen_width, screen_height, 'roguelike_python_tcod', False)

  while not libtecod.console_is_window_closed():
    libtecod.console_set_default_foreground(0, libtecod.white)
    libtecod.console_put_char(0, 1, 1, '@', libtecod.BKGND_NONE)
    libtecod.console_flush()

    key = libtecod.console_check_for_keypress()

    if key.vk == libtecod.KEY_ESCAPE:
      return True

if __name__ == '__main__':
  main()