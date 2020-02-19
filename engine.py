import tcod as libtecod

from input_handlers import handle_keys

def main():
  screen_width = 80
  screen_height = 50

  player_x = int(screen_width / 2)
  player_y = int(screen_height / 2)

  libtecod.console_set_custom_font('arial10x10.png', libtecod.FONT_TYPE_GREYSCALE | libtecod.FONT_LAYOUT_TCOD)

  libtecod.console_init_root(screen_width, screen_height, 'roguelike_python_tcod', False)

  key = libtecod.Key()
  mouse = libtecod.Mouse()

  while not libtecod.console_is_window_closed():
    libtecod.sys_check_for_event(libtecod.EVENT_KEY_PRESS, key, mouse)

    libtecod.console_set_default_foreground(0, libtecod.white)
    libtecod.console_put_char(0, player_x, player_y, '@', libtecod.BKGND_NONE)
    libtecod.console_flush()

    action = handle_keys(key)

    move = action.get('move')
    exit = action.get('exit')
    fullscreen = action.get('fullscreen')

    if move:
      dx, dy = move
      player_x += dx
      player_y += dy

    if exit:
      return True

    if fullscreen:
      libtecod.console_set_fullscreen(not libtecod.console_is_fullscreen)

if __name__ == '__main__':
  main()