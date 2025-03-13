from abc import ABC, abstractmethod

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(UIFactory):
    def create_button(self):
        return "This is a Windows button"
    
    def create_checkbox(self):
        return "This is a Windows checkbox"

class MacOSFactory(UIFactory):
    def create_button(self):
        return "This is a MacOS button"
    
    def create_checkbox(self):
        return "This is a MacOS checkbox"


if __name__ == "__main__":
    windows = WindowsFactory()
    macos = MacOSFactory()

    windows.create_button()
    windows.create_checkbox()

    macos.create_button()
    macos.create_checkbox()

    print(windows.create_button())
    print(windows.create_checkbox())
    print(macos.create_button())
    print(macos.create_checkbox())