class Counter:
    def __init__(self):
        self._count = 0
        self._open = False

    def __enter__(self):
        self._open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._open = False
        return False

    def add(self):
        if not self._open:
            raise Exception("Resource not opened in try-with-resources")
        self._count += 1

    def get_count(self):
        return self._count

def add_new_animal_with_counter(registry, counter):
    try:
        add_new_animal(registry)
        counter.add()
    except Exception as e:
        print(e)