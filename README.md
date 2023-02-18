# Replicating Strawberry issue #445

Issue here
- https://github.com/strawberry-graphql/strawberry/issues/445

## Steps to reproduce

1. Clone this repo
2. Create a virtual environment with python 3.8.0

```commandline
virtualenv venv -p $(which python3.8)
source venv/bin/activate
```

3. Install requirements

```commandline
pip3 install -r requirements.txt
```

4. Run the pytest.

flpStrrr swapped the position of the generic A and B in the strawberry data model Edge, and he was able to get errors.

As noted by Patrick, the creator of strawberry in the sprint

- https://hackmd.io/@patrickpy/SJdEUmR6j

It seems that the error is no longer there.

We validated this, and in short, with 

- Python Version `3.8` (same version used by reporter flpStrri)
- Strawberry Version: `0.158` (latest version as of 18 Feb 2023)

We are unable to replicate the issue. Swapping the generics would not result in an error.

```commandline
(venv) ➜  replicate_generic_ordering_strawberry git:(master) ✗ pytest test_generic_ordering.py 
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.8.0, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/gohchangmingclement/Desktop/ship_it_parrot/replicate_generic_ordering_strawberry
collected 2 items                                                                                                                                                                   

test_generic_ordering.py ..                                                                                                                                                   [100%]

================================================================================= warnings summary ==================================================================================
test_generic_ordering.py::test_should_pass_order_one
test_generic_ordering.py::test_should_pass_order_two
  /Users/gohchangmingclement/Desktop/ship_it_parrot/replicate_generic_ordering_strawberry/venv/lib/python3.8/site-packages/strawberry/types/fields/resolver.py:128: DeprecationWarning: Argument name-based matching of 'info' is deprecated and will be removed in v1.0. Ensure that reserved arguments are annotated their respective types (i.e. use value: 'DirectiveValue[str]' instead of 'value: str' and 'info: Info' instead of a plain 'info').
    warnings.warn(warning)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================================================== 2 passed, 2 warnings in 0.13s ===========================================================================
```