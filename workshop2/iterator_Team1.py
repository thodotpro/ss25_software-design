from abc import ABC, abstractmethod

class App:
    def __init__(self):
        self.playlist = MyFirstPlaylist()
        self.next = Next(self.playlist)
        self.back = Back(self.playlist)
        self.running = True

    def run(self):
        print("Hello!")

        current = self.playlist.database[self.playlist.position]
        print(f"Now playing: {current[0]} by {current[1]}")

        while self.running:

            command = input("(n)ext, (b)ack, (c)urrent, (q)uit: ").lower()

            if command not in ["n", "b", "c", "q"]:
                command = input("(n)ext, (b)ack, (c)urrent, (q)uit: ").lower()

            if command == "n":
                self.next.traverse()
                current = self.playlist.database[self.playlist.position]
                print(f"Now playing: {current[0]} by {current[1]}")

            elif command == "b":
                self.back.traverse()
                current = self.playlist.database[self.playlist.position]
                print(f"Now playing: {current[0]} by {current[1]}")

            elif command == "c":
                print(f"Now playing: {current[0]} by {current[1]}")

            elif command == "q":
                print("Goodbye!")
                self.running = False
                quit()

class Data:
    def __init__(self):
        self.database = None
        self.iterator = None
        self.position = 0

    def set_data(self, data):
        self.database = data
        return True, self.database
    
    def set_iterator(self, iterator):
        self.iterator = iterator
        return True, self.iterator

class MyFirstPlaylist(Data):
    def __init__(self):
        super().__init__()
        _, self.playlist = self.create_playlist()
        self.database = self.playlist

    def create_playlist(self):
        my_first_playlist = [
            ["Song 1", "Artist 1"],
            ["Song 2", "Artist 2"],
            ["Song 3", "Artist 3"],
            ["Song 4", "Artist 4"],
            ["Song 5", "Artist 5"]
        ]
        return True, my_first_playlist

class Iterator(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def traverse(self):
        pass

class Back(Iterator):
    def __init__(self, data):
        super().__init__(data)

    def traverse(self):
        self.data.position = len(self.data.database) - 1 if self.data.position == 0 else self.data.position - 1
        return True, self.data.position

class Next(Iterator):
    def __init__(self, data):
        super().__init__(data)

    def traverse(self):
        self.data.position = 0 if self.data.position == len(self.data.database) - 1 else self.data.position + 1
        return True, self.data.position
    
if __name__ == "__main__":
    app = App()
    app.run()