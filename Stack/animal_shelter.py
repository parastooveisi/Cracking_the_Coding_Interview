# Explanation to the problem: https: // www.youtube.com/watch?v = un3ynLwYZVU


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal):
        if animal == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_dogs(self):
        return self.dogs.pop(0)

    def dequeue_cats(self):
        return self.cats.pop(0)

    def dequeue_any(self):
        if not len(self.cats):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()


a = AnimalShelter()
a.enqueue("dog")
a.enqueue("cat")
a.enqueue("dog")
a.enqueue("dog")
a.enqueue("cat")
print(a.dequeue_any())
print(a.dequeue_any())
