import tcod as libtecod

from input_handlers import handle_keys
from entity import Entity

def main():
  screen_width = 80
  screen_height = 50

  player = Entity(int(screen_height / 2), int(screen_height / 2), '@', libtecod.white)
  npc = Entity(int(screen_height / 2 - 5), int(screen_height / 2), '@', libtecod.yellow)
  entities = [npc, player]

  libtecod.console_set_custom_font('arial10x10.png', libtecod.FONT_TYPE_GREYSCALE | libtecod.FONT_LAYOUT_TCOD)

  libtecod.console_init_root(screen_width, screen_height, 'roguelike_python_tcod', False)

  con = libtecod.console_new(screen_width, screen_height)

  key = libtecod.Key()
  mouse = libtecod.Mouse()

  while not libtecod.console_is_window_closed():
    libtecod.sys_check_for_event(libtecod.EVENT_KEY_PRESS, key, mouse)

    libtecod.console_set_default_foreground(con, libtecod.white)
    libtecod.console_put_char(con, player.x, player.y, '@', libtecod.BKGND_NONE)
    libtecod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    libtecod.console_set_default_foreground(0, libtecod.white)
    libtecod.console_put_char(0, player.x, player.y, '@', libtecod.BKGND_NONE)
    libtecod.console_flush()

    libtecod.console_put_char(con, player.x, player.y, ' ', libtecod.BKGND_NONE)
    libtecod.console_put_char(0, player.x, player.y, ' ', libtecod.BKGND_NONE)

    action = handle_keys(key)

    move = action.get('move')
    exit = action.get('exit')
    fullscreen = action.get('fullscreen')

    if move:
      dx, dy = move
      player.move(dx, dy)

    if exit:
      return True

    if fullscreen:
      libtecod.console_set_fullscreen(not libtecod.console_is_fullscreen)

if __name__ == '__main__':
  main()