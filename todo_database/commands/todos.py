import json
from datetime import datetime
list_name='lists.json'

def set_list(list_name):
  
  return list_name

def get_data(list_file_name):
  
  with open('lists.json', 'r') as json_file:
    data = json.load(json_file)
  return data

def update_data(list_file_name, new_data):
  with open('lists.json', 'w') as json_file:
    json.dump(new_data, json_file, sort_keys=True, indent=True)

def add_item(args):
  data=get_data(list_name)
  title=args
  print("Name",title)
  data.append({
    'Name': title,
    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
  })
  with open('lists.json', 'w') as json_file:
    json.dump(data, json_file, sort_keys=True, indent=True)

def show_items(args):
  
  data = get_data(list_name)
  if (len(data) == 0):
    print('No data in the list, why dont you add one?')
  else:
    for index, todo_item in enumerate(data):
      print('[',index + 1,']', todo_item['Name'])

   



def remove_item(args):
  """
  Remove a todo item
  """
  list_name = set_list(args[0])
  if (not list_name):
    return
  item_id = int(args[0])
  data = get_data(list_name)
  if(len(data)<item_id):
    print("No data found")
  else:
  
    print('Deleted #',item_id)
    data.pop(item_id - 1)
    update_data(list_name, data)



def incomplete_item(args):
  """
  Mark a todo item as incomplete
  """
  data = get_data(list_name)
  complete = 0
  pending=0
  if (len(data) == 0):
    print('No data in the list, why dont you add one?')
  else:
    
    print('No. of data existing:',len(data))
