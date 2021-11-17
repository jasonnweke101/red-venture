from random import choice as c
from random import sample as s
from time import sleep as idle 


class Robot:
    
  def __init__(self, name):

    self.name = name
    self.tasks = [
    {
      "description": 'do the dishes',
      "eta": 1000,
    },
    
    {
      "description": 'sweep the house',
      "eta": 3000,
    },
    
    {
      "description": 'do the laundry',
      "eta": 10000,
    },
    
    {
      "description": 'take out the recycling',
      "eta": 4000,
    },
    
    {
      "description": 'make a sammich',
      "eta": 7000,
    },{
      "description": 'mow the lawn',
      "eta": 20000,
    },
    
    {
      "description": 'rake the leaves',
      "eta": 18000,
    },
    
    {
      "description": 'give the dog a bath',
      "eta": 14500,
    },
    
    {
      "description": 'bake some cookies',
      "eta": 8000,
    },
    
    {
      "description": 'wash the car',
      "eta": 20000,
    },
  ]
    self.specific_Tasks = s(self.tasks, 5)
  

  """  print(c(tasks))
    print(tasks[2]["eta"])
  
   def assign_Tasks(self):
    return (UNIPEDAL := c(self.tasks), BIPEDAL := c(self.tasks), 
    QUADRUPEDAL := c(self.tasks), ARACHNID := c(self.tasks), 
    RADIAL := c(self.tasks), AERONAUTICAL := c(self.tasks) )
  
  def do_Task(self):
    print(self.name)
  """ 
class Unipedal(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

class Bipedal(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

class Quadrupedal(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

class Arachnid(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

class Radial(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

class Aeronautical(Robot):
  def __init__(self, name):
    super().__init__(name)
    self.robot_tasks = s(self.tasks, 5)
    self.score = 0

  
def create_robots(name, robot_type):
  if robot_type == "Unipedal":
    return Unipedal(name)
  if robot_type == "Bipedal":
    return Bipedal(name)
  if robot_type == "Quadrupedal":
    return Quadrupedal(name)
  if robot_type == "Arachnid":
    return Arachnid(name)
  if robot_type == "Radial":
    return Radial(name)
  if robot_type == "Aeronautical":
    return Aeronautical(name)
  

robot = create_robots("Jason", "Quadrupedal")
print(robot.score)
print(robot.robot_tasks)

#[globals() str("sdd"+ y ) = y for y in range(6)]
#Robot1 = Robot("Nweke", "Wazo")
def is_robot_present(name, robots):
  for robot in robots:
    if robot.name == name:
      return True
  return False

def get_robot_index(name, robots):
  i = 0
  for robot in robots:
    if robot.name == name:
      return i
    i+=1
  return -1
robots = []
while True:
  print("\ngg")
  print("What do you want to do?")
  print("Type 'A' for Assign tasks to robot")
  print("Type 'C' for create new robots")
  print("Type 'L' to display all robots and their scores")
  act = input().upper()
  if act == "A":
    print("Type the robot's name you want to assign a task")
    robots_name = input()
    if is_robot_present(robots_name, robots):
      print("State the task below: ")
      task = input()
      r_index = get_robot_index(robots_name, robots)
      if task in robots[r_index].robot_tasks:
        robots[r_index].score += robots[r_index].tasks["eta"]
        print("Robots score inreased by", str(robots[r_index].tasks["eta"]), "points")
      else:
        print(robots_name, "does not have that task")
    else:
      print("Robot's name not present")
  elif act == "C":
    print("Whats the robots name? ")
    name = input()
    if not is_robot_present(name, robots):
      print("Whats the robot type?")
      robot_type = input()
      robot = create_robots(name, robot_type)
      if robot == None:
        print("robot type doesn't exist")
      else:
        robots.append(robot)
        print("Successfully created robot! ")
    else:
      print("Robot's name already exists")
  elif act == "L":
    if robots:
      for robot in robots:
        print(robot.name, robot.score)
    else:
      print("Leaderboard is currently empty")




