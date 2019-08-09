import functools
import json

HTTP_GET = 'GET'
HTTP_POST = 'POST'


class Router:
    def __init__(self):
        self._routes = {
            HTTP_GET: {},
            HTTP_POST: {},
        }

    def add_route(self, request_method, url, handler_name):
        self._routes[request_method][url] = handler_name

    def resolve_request_handler(self, request_method, url):
        try:
            return self._routes[request_method][url]
        except KeyError:
            raise ValueError(f'Invalid route: {request_method} {url}')


class Request:
    def __init__(self, payload=None):
        self._data = {} if payload is None else json.loads(payload)

    def get(self, param_name):
        return self._data.get(param_name)


class Application:
    _router = Router()

    def get(self, url, payload=None):
        return self._process_request(HTTP_GET, url, payload)

    def post(self, url, payload):
        return self._process_request(HTTP_POST, url, payload)

    @classmethod
    def http_get(cls, url):
        return cls._http_request_handler_decorator(HTTP_GET, url)

    @classmethod
    def http_post(cls, url):
        return cls._http_request_handler_decorator(HTTP_POST, url)

    def _process_request(self, request_method, url, payload=None):
        handler_name = self._router.resolve_request_handler(request_method, url)
        handler = getattr(self, handler_name)
        request = Request(payload)
        response = handler(request)
        return json.dumps(response)

    @classmethod
    def _http_request_handler_decorator(cls, request_method, url):
        def decorator(func):
            cls._router.add_route(request_method, url, func.__name__)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator


http_get = Application.http_get
http_post = Application.http_post


class User:
    def __init__(self, balance=0, name=None, owed_by=None, owes=None):
        self.balance = balance
        self.name = name
        self.owed_by = {} if owed_by is None else owed_by
        self.owes = {} if owes is None else owes

    def lend(self, amount, borrower_name):
        my_debt = self.owes.pop(borrower_name, 0)
        borrower_debt = self.owed_by.pop(borrower_name, 0)
        if my_debt > amount:
            self.owes[borrower_name] = my_debt - amount
        elif amount > my_debt - borrower_debt:
            self.owed_by[borrower_name] = borrower_debt + amount - my_debt

        self.balance += amount

    def borrow(self, amount, lender_name):
        my_debt = self.owes.pop(lender_name, 0)
        lender_debt = self.owed_by.pop(lender_name, 0)
        if lender_debt > amount:
            self.owed_by[lender_name] = lender_debt - amount
        elif amount > lender_debt - my_debt:
            self.owes[lender_name] = amount - lender_debt + my_debt

        self.balance -= amount

    def as_dict(self):
        return {
            'balance': self.balance,
            'name': self.name,
            'owed_by': self.owed_by,
            'owes': self.owes,
        }


class UsersDatabase:
    def __init__(self, users):
        self._users = users

    def filter_by_names(self, names=None):
        if names is None:
            return self

        users = list(filter(lambda user: user.name in names, self._users))
        return UsersDatabase(users)

    def first(self):
        try:
            return self._users[0]
        except IndexError:
            return None

    def find_by_name(self, name):
        return self.filter_by_names([name]).first()

    def add(self, user):
        self._users.append(user)

    def transfer(self, lender_name, borrower_name, amount):
        lender = self.find_by_name(lender_name)
        borrower = self.find_by_name(borrower_name)
        lender.lend(amount, borrower_name)
        borrower.borrow(amount, lender_name)

    @staticmethod
    def from_list(data):
        return UsersDatabase([User(**user) for user in data])

    def as_list(self):
        return [user.as_dict() for user in self._users]


class RestAPI(Application):
    def __init__(self, database):
        self.database = UsersDatabase.from_list(database.get('users'))

    @http_get('/users')
    def get_users(self, request):
        names = request.get('users')
        return {'users': self.database.filter_by_names(names).as_list()}

    @http_post('/add')
    def add_user(self, request):
        name = request.get('user')
        self.database.add(User(name=name))
        return self.database.find_by_name(name).as_dict()

    @http_post('/iou')
    def transfer(self, request):
        lender_name = request.get('lender')
        borrower_name = request.get('borrower')
        self.database.transfer(
            lender_name,
            borrower_name,
            request.get('amount')
        )
        return {'users': self.database.filter_by_names([lender_name, borrower_name]).as_list()}
