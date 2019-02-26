# More complete stub for typing module.
#
# Use [typing fixtures/typing-full.pyi] to use this instead of lib-stub/typing.pyi
# in a particular test case.
#
# Many of the definitions have special handling in the type checker, so they
# can just be initialized to anything.

from abc import abstractmethod, ABCMeta

class GenericMeta(type): pass

cast = 0
overload = 0
Any = 0
Union = 0
Optional = 0
TypeVar = 0
Generic = 0
Protocol = 0
Tuple = 0
Callable = 0
_promote = 0
NamedTuple = 0
Type = 0
no_type_check = 0
ClassVar = 0
NoReturn = 0
NewType = 0

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)
U = TypeVar('U')
V = TypeVar('V')
S = TypeVar('S')

# Note: definitions below are different from typeshed, variances are declared
# to silence the protocol variance checks. Maybe it is better to use type: ignore?

@runtime
class Container(Protocol[T_co]):
    @abstractmethod
    # Use int because bool isn't in the default test builtins
    def __contains__(self, arg: object) -> int: pass

@runtime
class Sized(Protocol):
    @abstractmethod
    def __len__(self) -> int: pass

@runtime
class Iterable(Protocol[T_co]):
    @abstractmethod
    def __iter__(self) -> 'Iterator[T_co]': pass

@runtime
class Iterator(Iterable[T_co], Protocol):
    @abstractmethod
    def __next__(self) -> T_co: pass

class Generator(Iterator[T], Generic[T, U, V]):
    @abstractmethod
    def send(self, value: U) -> T: pass

    @abstractmethod
    def throw(self, typ: Any, val: Any=None, tb: Any=None) -> None: pass

    @abstractmethod
    def close(self) -> None: pass

    @abstractmethod
    def __iter__(self) -> 'Generator[T, U, V]': pass

class AsyncGenerator(AsyncIterator[T], Generic[T, U]):
    @abstractmethod
    def __anext__(self) -> Awaitable[T]: pass

    @abstractmethod
    def asend(self, value: U) -> Awaitable[T]: pass

    @abstractmethod
    def athrow(self, typ: Any, val: Any=None, tb: Any=None) -> Awaitable[T]: pass

    @abstractmethod
    def aclose(self) -> Awaitable[T]: pass

    @abstractmethod
    def __aiter__(self) -> 'AsyncGenerator[T, U]': pass

@runtime
class Awaitable(Protocol[T_co]):
    @abstractmethod
    def __await__(self) -> Generator[Any, Any, T_co]: pass

class AwaitableGenerator(Generator[T, U, V], Awaitable[V], Generic[T, U, V, S], metaclass=ABCMeta):
    pass

class Coroutine(Awaitable[V], Generic[T, U, V]):
    @abstractmethod
    def send(self, value: U) -> T: pass

    @abstractmethod
    def throw(self, typ: Any, val: Any=None, tb: Any=None) -> None: pass

    @abstractmethod
    def close(self) -> None: pass

@runtime
class AsyncIterable(Protocol[T_co]):
    @abstractmethod
    def __aiter__(self) -> 'AsyncIterator[T_co]': pass

@runtime
class AsyncIterator(AsyncIterable[T_co], Protocol):
    def __aiter__(self) -> 'AsyncIterator[T_co]': return self
    @abstractmethod
    def __anext__(self) -> Awaitable[T_co]: pass

class Sequence(Iterable[T_co], Container[T_co]):
    @abstractmethod
    def __getitem__(self, n: Any) -> T_co: pass

class Mapping(Iterable[T], Generic[T, T_co], metaclass=ABCMeta):
    def __getitem__(self, key: T) -> T_co: pass
    @overload
    def get(self, k: T) -> Optional[T_co]: pass
    @overload
    def get(self, k: T, default: Union[T_co, V]) -> Union[T_co, V]: pass
    def values(self) -> Iterable[T_co]: pass  # Approximate return type
    def __len__(self) -> int: ...
    def __contains__(self, arg: object) -> int: pass

class MutableMapping(Mapping[T, U], metaclass=ABCMeta):
    def __setitem__(self, k: T, v: U) -> None: pass

class SupportsInt(Protocol):
    def __int__(self) -> int: pass

def runtime(cls: T) -> T:
    return cls

class ContextManager(Generic[T]):
    def __enter__(self) -> T: pass
    # Use Any because not all the precise types are in the fixtures.
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> Any: pass

TYPE_CHECKING = 1
