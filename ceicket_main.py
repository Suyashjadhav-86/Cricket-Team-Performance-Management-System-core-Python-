# Cricket Team Performance Management System

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, runs):
        self.scores.append(runs)

    def total_runs(self):
        return sum(self.scores)

    def average_runs(self):
        if len(self.scores) == 0:
            return 0
        return self.total_runs() / len(self.scores)

    def best_score(self):
        if len(self.scores) == 0:
            return 0
        return max(self.scores)

    def performance(self):
        avg = self.average_runs()
        if avg >= 70:
            return "Excellent"
        elif avg >= 40:
            return "Good"
        elif avg >= 20:
            return "Average"
        else:
            return "Poor"


def save_to_file(players):
    try:
        with open("players_data.txt", "w") as file:
            for p in players:
                file.write(p.name + "," + ",".join(map(str, p.scores)) + "\n")
        print("Data saved successfully.")
    except Exception as e:
        print("Error while saving data:", e)


def load_from_file():
    players = []
    try:
        with open("players_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                player = Player(data[0])
                for run in data[1:]:
                    player.add_score(int(run))
                players.append(player)
    except FileNotFoundError:
        print("No saved data found.")
    return players


# Main Program
players = load_from_file()

while True:
    print("\n----- Cricket Team Menu -----")
    print("1. Add Player")
    print("2. Add Score to Player")
    print("3. View Player Report")
    print("4. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter player name: ")
        players.append(Player(name))
        print("Player added successfully.")

    elif choice == "2":
        try:
            name = input("Enter player name: ")
            runs = int(input("Enter runs scored: "))

            found = False
            for p in players:
                if p.name == name:
                    p.add_score(runs)
                    print("Score added.")
                    found = True
                    break

            if not found:
                print("Player not found.")

        except ValueError:
            print("Invalid input. Runs must be a number.")

    elif choice == "3":
        name = input("Enter player name: ")
        for p in players:
            if p.name == name:
                print("\nPlayer:", p.name)
                print("Scores:", p.scores)
                print("Total Runs:", p.total_runs())
                print("Average Runs:", round(p.average_runs(), 2))
                print("Best Score:", p.best_score())
                print("Performance:", p.performance())
                break
        else:
            print("Player not found.")

    elif choice == "4":
        save_to_file(players)
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
