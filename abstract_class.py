from abc import abstractmethod, ABC


class sports(ABC):
    @abstractmethod
    def doing(self):
        pass

    def rest(self):
        print('needed')


obj = sports()
# sports is a abstract class
