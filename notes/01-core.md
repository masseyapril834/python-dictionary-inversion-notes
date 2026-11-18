# Invert a mapping without losing collisions: implementation

## What the example does

Multiple keys may map to the same value. Collect keys into lists rather than silently dropping collisions; source values must be strings.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "a": "red",
  "b": "blue",
  "c": "red"
}
```

Expected result:

```json
{
  "blue": [
    "b"
  ],
  "red": [
    "a",
    "c"
  ]
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
