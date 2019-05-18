from typing import List, Dict


class Team:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__wins = 0
        self.__losses = 0
        self.__draws = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def wins(self) -> int:
        return self.__wins

    @property
    def losses(self) -> int:
        return self.__losses

    @property
    def draws(self) -> int:
        return self.__draws

    @property
    def matches(self) -> int:
        return self.wins + self.losses + self.draws

    @property
    def points(self) -> int:
        return 3 * self.wins + self.draws

    def add_win(self) -> None:
        self.__wins += 1

    def add_loss(self) -> None:
        self.__losses += 1

    def add_draw(self) -> None:
        self.__draws += 1

    def __repr__(self) -> str:
        template = 'Team(name={!r}, wins={!r}, losses={!r}, draws={!r}, points={!r})'
        return template.format(self.name, self.wins, self.losses, self.draws, self.points)


class TeamsRepository:
    def __init__(self) -> None:
        self.__teams: Dict[str, Team] = {}

    def find_or_create(self, name: str) -> Team:
        return self.__teams.setdefault(name, Team(name))

    def find_all(self) -> List[Team]:
        return [team for team in self.__teams.values()]


def parse_results(results: List[str]) -> List[Team]:
    repository = TeamsRepository()

    for result in results:
        team_a_name, team_b_name, outcome = result.split(';')
        team_a = repository.find_or_create(team_a_name)
        team_b = repository.find_or_create(team_b_name)

        if outcome == 'win':
            team_a.add_win()
            team_b.add_loss()
        elif outcome == 'loss':
            team_a.add_loss()
            team_b.add_win()
        elif outcome == 'draw':
            team_a.add_draw()
            team_b.add_draw()

    return repository.find_all()


def create_table_header() -> str:
    return 'Team                           | MP |  W |  D |  L |  P'


def create_table_row(team: Team) -> str:
    template = '{:30} | {:-2} | {:-2} | {:-2} | {:-2} | {:-2}'
    return template.format(team.name, team.matches, team.wins, team.draws, team.losses, team.points)


def tally(results: List[str]) -> List[str]:
    teams = parse_results(results)
    sorted_teams = sorted(teams, key=lambda t: (-t.points, t.name))

    table = [create_table_header()]
    for team in sorted_teams:
        table.append(create_table_row(team))

    return table
