import datetime
from project import Project


def main():
    projects = load_projects("projects.txt")
    while True:
        choice = menu()
        if choice == "l":
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == "a":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


def menu():
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    return input(">>> ").lower()


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            parts = line.strip().split("\t")
            name, start_date, priority, cost_estimate, percent_complete = parts
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            percent_complete = int(percent_complete)
            projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            start_date = project.start_date.strftime("%d/%m/%Y")
            file.write(f"{project.name}\t{start_date}\t{project.priority}\t{project.cost_estimate}\
            t{project.percent_complete}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects: ")
    for index, project in enumerate(incomplete_projects):
        print(f"{index} {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.estimate:.2f}, completion: {project.completion}%")

    print("Completed projects: ")
    for index, project in enumerate(completed_projects):
        print(f"{index} {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.estimate:.2f}, completion: {project.completion}%")



def filter_projects_by_date(projects, date):
    filtered_projects = sorted([project for project in projects if project.start_date > date])
    for project in filtered_projects:
        print(project)


def add_new_project():
    name = input("Let's add a new project\nName: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i + 1}: {project}")
    index = int(input("Project choice: ")) - 1
    if 0 <= index < len(projects):
        project = projects[index]
        print(f"Current project details: {project}")
        print("Update project details: ")
        name = input(f"Name (current: {project.name}): ")
        if name:
            project.name = name

        date_str = input(f"Start date (current: {project.start_date.strftime('%d/%m/%Y')}): ")
        if date_str:
            project.start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()

        priority = input(f"Priority (current: {project.priority}): ")
        if priority:
            project.priority = int(priority)

        cost_estimate = input(f"Cost estimate (current: ${project.cost_estimate:.2f}): ")
        if cost_estimate:
            project.cost_estimate = float(cost_estimate)

        percent_complete = input(f"Percent complete (current: {project.percent_complete}%): ")
        if percent_complete:
            project.percent_complete = int(percent_complete)
    else:
        print("Invalid project number.")

main()
