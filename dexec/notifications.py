from abc import abstractmethod, ABC


class NotificationProviderInterface(ABC):
    @abstractmethod
    def send(self, msg: str) -> bool:
        pass
