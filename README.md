# mouse_shaker
Module for automatic mouse shaking

## Installation

```bash
pip install https://github.com/kenichdietrich/mouse_shaker.git
```

## Usage

From terminal, it only takes one argument

```bash
mouse-shaker 5 # default in seconds
mouse-shaker 10s # 's' for seconds
mouse-shaker 1min # 'min' for minutes
mouse-shaker 2.5min
```

From python, you can use `shake_mouse` function

```python
from mouse_shaker import shake_mouse

shake_mouse(25) # it takes duration in seconds
```

Press `CTRL+C` to stop shaking.