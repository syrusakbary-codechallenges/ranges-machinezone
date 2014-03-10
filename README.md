Clone
=====

You have to run this command for clone the repository:

```
git clone https://github.com/SyrusAkbary/ranges-machinezone.git
```

Usage
=====

```python
from ranges import Range

r = Range()
# Add a range
r.addRange(10, 20)
# Query a range
r.queryRange(10, 20)
# Delete a range
r.deleteRange(10, 20)
```

Testing
=======

For execute the tests type this in your favorite shell:

```
python tests.py
```