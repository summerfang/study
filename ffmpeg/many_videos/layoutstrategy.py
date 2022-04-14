from abc import ABC, abstractclassmethod

class LayoutStrategy(ABC):
    @abstractclassmethod
    def layout_select(self):
        pass

class FourPanelistLayout(LayoutStrategy):
    def layout_select(self):
        return "FourPanelistLayout"