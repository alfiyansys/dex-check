from dexec.notifications import NotificationProviderInterface


class ConsoleNotificationProvider(NotificationProviderInterface):

    def send(self, msg: str) -> bool:
        # print(msg)
        return True
