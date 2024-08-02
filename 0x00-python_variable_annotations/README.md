<!-- README for Python Tasks -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h2 {
            color: #2c3e50;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, "Courier New", monospace;
        }
    </style>
</head>
<body>

<h2>Task 0: Add Function</h2>
<p>Adds two floating-point numbers.</p>
<pre><code>def add(a: float, b: float) -> float:
    return a + b
</code></pre>

<h2>Task 1: Concat Function</h2>
<p>Concatenates two strings.</p>
<pre><code>def concat(str1: str, str2: str) -> str:
    return str1 + str2
</code></pre>

<h2>Task 2: Floor Function</h2>
<p>Computes the floor of a floating-point number.</p>
<pre><code>def floor(a: float) -> int:
    return int(a)
</code></pre>

<h2>Task 3: To Str Function</h2>
<p>Converts a floating-point number to a string.</p>
<pre><code>def to_str(n: float) -> str:
    return str(n)
</code></pre>

<h2>Task 4: Variable Annotations</h2>
<p>Examples of variable annotations.</p>
<pre><code>a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = 'Holberton'
</code></pre>

<h2>Task 5: Sum List Function</h2>
<p>Computes the sum of a list of floating-point numbers.</p>
<pre><code>from typing import List

def sum_list(input_list: List[float]) -> float:
    return float(sum(input_list))
</code></pre>

<h2>Task 6: Sum Mixed List Function</h2>
<p>Computes the sum of a list of integers and floating-point numbers.</p>
<pre><code>from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
</code></pre>

<h2>Task 7: To KV Function</h2>
<p>Converts a key and its value to a tuple of the key and the square of its value.</p>
<pre><code>from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
</code></pre>

<h2>Task 8: Make Multiplier Function</h2>
<p>Creates a multiplier function.</p>
<pre><code>from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
</code></pre>

<h2>Task 9: Element Length Function</h2>
<p>Computes the length of a list of sequences.</p>
<pre><code>from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
</code></pre>

<h2>Task 10: Safe First Element Function</h2>
<p>Retrieves the first element of a sequence if it exists.</p>
<pre><code>from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
</code></pre>

<h2>Task 11: Safely Get Value Function</h2>
<p>Retrieves a value from a dictionary using a given key.</p>
<pre><code>from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    if key in dct:
        return dct[key]
    else:
        return default
</code></pre>

<h2>Task 12: Zoom Array Function</h2>
<p>Creates multiple copies of items in a tuple.</p>
<pre><code>from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in

array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
</code></pre>

</body>
</html>
