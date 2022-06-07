from abc import abstractmethod, ABC


class sports(ABC):
    @abstractmethod
    def doing(self):
        pass

class runn(sports):
    def doing(self):
        print("walk really fast")


obj = runn()
obj.doing()
# sports is a abstract class
