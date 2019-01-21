from time import sleep

class PageWait(object):
    def __init__(self,elem,timeout=10):
        """
        wait element display
        :param elem:
        :param timeout:
        """
        try:
            timeout_int = int(timeout)
        except TypeError:
            raise ValueError("Type 'timeout' error, must be type int()")

        for i in range(timeout_int):
            if elem is not None:
                if elem.is_displayed() is True:
                    break
                else:
                    sleep(1)
            else:
                sleep(1)
        else:
            raise TimeoutError("Timeout,element invisible")