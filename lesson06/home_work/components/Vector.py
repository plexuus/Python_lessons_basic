class Vector:
    @staticmethod
    def len(exit_x: float, exit_y: float, entry_x: float, entry_y: float):
        return ((entry_x - exit_x)**2 + (entry_y - exit_y)**2)**0.5