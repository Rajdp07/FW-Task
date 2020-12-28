
import commands.todos

commands_dict = {
  'add': todos.add_item,
  'show': todos.show_items,
  'delete': todos.remove_item,
  'report': todos.incomplete_item
}