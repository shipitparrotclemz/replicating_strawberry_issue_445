import typing
import strawberry


def test_should_pass_order_one():
    A = typing.TypeVar("A")
    B = typing.TypeVar("B")

    @strawberry.type
    class Edge(typing.Generic[A, B]):
        info: A
        node: B

    @strawberry.type
    class Query:
        @strawberry.field
        def example(self, info) -> Edge[int, str]:
            return Edge(node="string", info=1)

    schema = strawberry.Schema(query=Query)
    assert not schema.execute_sync(
        """{
        example {
            __typename
            ... on IntStrEdge {
                node
                info
            }
        }
    }"""
    ).errors


def test_should_pass_order_two():
    A = typing.TypeVar("A")
    B = typing.TypeVar("B")

    @strawberry.type
    class Edge(typing.Generic[A, B]):
        node: B
        info: A  # SWAPED THE POSITION

    @strawberry.type
    class Query:
        @strawberry.field
        def example(self, info) -> Edge[int, str]:
            return Edge(node="string", info=1)

    schema = strawberry.Schema(query=Query)
    assert not schema.execute_sync(
        """{
        example {
            __typename
            ... on IntStrEdge {
                node
                info
            }
        }
    }"""
    ).errors


if __name__ == "__main__":
    test_should_pass_order_one()
    test_should_pass_order_two()