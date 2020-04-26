import tcod as libtecod

from input_handlers import handle_keys
from entity import Entity
from render_functions import render_all, clear_all
from map_objects.game_map import GameMap

def main():
  screen_width = 80
  screen_height = 50
  map_width = 80
  map_height = 45

  colors = {
    'dark_wall': libtecod.Color(0, 0, 100),
    'dark_ground': libtecod.Color(50, 50, 150)
  }

  player = Entity(int(screen_height / 2), int(screen_height / 2), '@', libtecod.white)
  npc = Entity(int(screen_height / 2 - 5), int(screen_height / 2), '@', libtecod.yellow)
  entities = [npc, player]

  libtecod.console_set_custom_font('arial10x10.png', libtecod.FONT_TYPE_GREYSCALE | libtecod.FONT_LAYOUT_TCOD)

  libtecod.console_init_root(screen_width, screen_height, 'roguelike_python_tcod', False)

  con = libtecod.console_new(screen_width, screen_height)

  game_map = GameMap(map_width, map_height)
  game_map.make_map()

  key = libtecod.Key()
  mouse = libtecod.Mouse()

  while not libtecod.console_is_window_closed():
    libtecod.sys_check_for_event(libtecod.EVENT_KEY_PRESS, key, mouse)

    render_all(con, entities, game_map, screen_width, screen_height, colors)

    libtecod.console_flush()    

    clear_all(con, entities)

    action = handle_keys(key)

    move = action.get('move')
    exit = action.get('exit')
    fullscreen = action.get('fullscreen')

    if move:
      dx, dy = move

      if not game_map.is_blocked(player.x + dx, player.y + dy):
        player.move(dx, dy)

    if exit:
      return True

    if fullscreen:
      libtecod.console_set_fullscreen(not libtecod.console_is_fullscreen)

if __name__ == '__main__':
  main()