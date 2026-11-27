# Ordered batch processing for Invert a mapping without losing collisions

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
{
  "a": "red",
  "b": "blue",
  "c": "red"
}
```

Result:
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

## Case 2

Input:
```json
{}
```

Result:
```json
{}
```

## Case 3

Input:
```json
{
  "x": "same"
}
```

Result:
```json
{
  "same": [
    "x"
  ]
}
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Multiple keys may map to the same value. Collect keys into lists rather than silently dropping collisions; source values must be strings.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
