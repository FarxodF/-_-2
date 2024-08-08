import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        self.distance += self.speed * 10

    def walk(self):
        self.distance += self.speed * 1


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            runner.distance = 0
            while runner.distance < self.distance:
                runner.run()
            results[len(results) + 1] = runner.name
        return results


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[len(results)] == "Ник")


if __name__ == "__main__":
    unittest.main()
