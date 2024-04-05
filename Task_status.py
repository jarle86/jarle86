'''5. *Gestión de lista de tareas:*
   Crea una lista que contenga varias tareas pendientes. 
   Permite al usuario agregar nuevas tareas a la lista, 
   marcar tareas como completadas y eliminar tareas de la lista. 
   Asegúrate de utilizar una lista para almacenar las tareas 
   y manejar correctamente las operaciones de agregar, 
   modificar y eliminar elementos.
   '''

task_list = ['tomar agua', 'cepilarse', 'banarse', 'desayunar',\
              'comer', 'dormir']

task_done = []

task_pending = ['comer']

#request the user to add a new task

new_task = input("Create a new task or check it status: ")

if new_task in task_pending or new_task in task_done:
    if new_task not in task_list: #Evaluate if the task already exist if not it will be created
        task_list.append(new_task)
        task_pending.append(new_task)
        print(task_list)
        print(task_pending)
        print(f'the new task {new_task} has been added to the pending task')
    elif new_task in task_done:
        print("This task has been completed!")
    elif new_task in task_pending:
        print("this taks is pending")
        print(task_pending)
else:
    task_pending.append(new_task)

#complete task from list

compeleted_task = input('Wich task would you like to complete? ')

if compeleted_task in task_list and compeleted_task in task_pending:
    task_done.append(compeleted_task)
    task_list.remove(compeleted_task)
    task_pending.remove(compeleted_task)
    print(task_done)
else:
    print("the task does not exist or was already completed") 

