# Custom Loggers
A module that extends the standard python logging module
___

In the standard python logging module there are things that are difficult to accomplish without quite a bit of overhead. 
These classes are meant to simplify that overhead and to be extended for specific use.

# Classes
___
## CustomLogger
```python
from custom_loggers import CustomLogger
```


Extends the logging.Logger class
This is the primary class you will use/inherit

### examples
#### general use:
```python
from custom_loggers import CustomLogger, ColoredFormatter, Foreground255
#setting class level settings
CustomLogger.inclusive = True
CustomLogger.global_log_level = 0
CustomLogger.use_global_log_level_default=True

#assigning a color for a new level which is defined below
ColoredFormatter.assign_level_color("NEWLEVEL", Foreground255(226))

logger = CustomLogger("testLogger")
logger2 = CustomLogger("test2logger")
logger3 = CustomLogger("channel_tester", channel="NewChannel")
logger4 = CustomLogger("channel_tester2", channel="NewChannel")
logger3.info("channel test on")
logger4.info("channel test on")
CustomLogger.channel_disabled("NewChannel", True)
logger3.info("channel test off")
logger4.info("channel test off")
logger2.add_level("NEWLEVEL", 1, True)
logger2.log("NEWLEVEL", "original message")
logger.newlevel("my new message")
logger.log("trace", "just checking")
logger.error("Hello")
logger.info("Hello")
logger.debug("Hello")
logger.warning("Hello")
logger.critical("Hello")
try:
    raise ValueError("This is a complex error")
except Exception as e:
    logger.exception("An exception occurred")
logger.disabled = True
logger.info("This should not print because is disabled")
logger.disabled = False
CustomLogger.logging_disabled = True
logger.info("Should be disabled")
logger2.info("Should be disabled")
logger3.info("Should be disabled")
logger4.info("Should be disabled")
```
#### Extending
```python
from custom_loggers import CustomLogger,ColoredFormatter,Foreground255

class NewLogger(CustomLogger):
    use_global_log_level_default = True
    inclusive = False
    default_colored_format = '%(levelname)-8s: %(message)s'
    has_run_once=False

    CustomLogger.add_level("NEWLEVEL", 1)
    ColoredFormatter.assign_level_color("NEWLEVEL", Foreground255(77))

    def newlevel(self,msg):
        self.log("NEWLEVEL", msg)

logger=NewLogger("TestLogger")
logger.newlevel("this shows your new level")
```


### class attributes
These values affect every instance of CustomLogger

`logging_disabled`: bool enables or disables ALL Logging from CustomLogger

`default_logging_level`: int the logging level assigned to each logger by default


`use_global_log_level_default`: the default value of use_global_log which is used when comparing a loging event with the 
log leve this determines whether we compare with the instance or with the global log_level

`global_log_level`: int the current log level for all instances. (only effective when use_global_log_level is True)

`inclusive`: bool when calculating whether to log or not if inclusive is True we'll accept the set log level and below
    if false only loglevel matching the exact level will log

`default_colored_formatter`:Formatter when creating an instance with add_formatter is True this is the class used to
    create the formatter

`default_colored_format`:str the format string that the formatter will use

`default_asctime_format`:str the asctime format the formatter will use


## ColoredFormatter
```python
from custom_loggers import ColoredFormatter
```
For all things colored

There are 3 Things to note here:
### 1: Windows
Color text doesn't work on all terminals primarily you will find issues in Windows CMD and Powershell.
By default, colors will not attempt to print on Windows you can override this by setting WINDOWS_OVERRIDE=True
```python
from custom_loggers import ColoredFormatter
ColoredFormatter.WINDOWS_OVERRIDE = True
```
There are tools to add ANSI support to Windows terminals in which case colors *may work*.

### 2: Additional Formatting
ColoredFormatter adds three additional formatting options for your logging format.

All three are associated with getting the script that calls one of a CustomLogger.log methods. It grabs the script 
location and assigns this to these formatting names. These are similar to 'filepath', 'filename', 'lineno' but could be 
different. These will be more accurate for CustomLoggers. 
`scriptpath` : the full path to the script that called log
`scriptname` : the file name of the script
`scriptline` : the line number of the script

As a side note if you use a plugin for your IDE you may be able to get the filename and line number to have be a 
hyperlink in the IDE's terminal. For example in PyCharm if you use the below format {scriptname}, line {scriptline}
and install the Awesome Console plugin. each of those references will take you directly to the script.

```python
from custom_loggers import CustomLogger

CustomLogger.default_colored_format = '%(asctime)s [%(scriptname)s, line %(scriptline)-3s] %(levelname)-8s %(name)s: %(message)s'
# Will output like this
# 21-04-29 08:39 [main.py, line 15 ] INFO     channel_tester: channel test on
# 21-04-29 08:39 [main.py, line 16 ] INFO     channel_tester2: channel test on
# 21-04-29 08:39 [main.py, line 23 ] TRACE    testLogger: just checking
# 21-04-29 08:39 [main.py, line 24 ] ERROR    testLogger: Hello
# 21-04-29 08:39 [main.py, line 25 ] INFO     testLogger: Hello
# 21-04-29 08:39 [main.py, line 26 ] DEBUG    testLogger: Hello
# 21-04-29 08:39 [main.py, line 27 ] WARNING  testLogger: Hello
# 21-04-29 08:39 [main.py, line 28 ] WARNING  testLogger: Hello
```

### 3:
Assigning Colors to level is done like below:
```python
from custom_loggers import ColoredFormatter
from custom_loggers import Colors

ColoredFormatter.assign_level_color("LEVELNAME",Colors.ForeGroundColors.GREEN)
```
Colored formatter has an assign_level_color method used to assign foreground and background colors. This is done via 
the Colors module discussed below. the color can be a string (usually a color escape color which is put in front of 
the log line which starts the color print)

## Colors
```python
from custom_loggers import Colors
```
or directly with the class you are looking for
```python
from custom_loggers import ForeGroundColors, BackGroundColors, Foreground255, Background255 
from custom_loggers import print_16_colors,print_255_colors
```

Colors is an internal module for getting and combining colors and font styles.
This is done by generating the color escape codes and assigning them to the SequenceName class.

## 16 - colors
The standard 16 colors supported by the majority of mondern terminals are found in:
```python
from custom_loggers import Colors

Colors.ForeGroundColors
Colors.BackGroundColors

#colors are accessed by:
Colors.ForeGroundColors.BLUE

#You can visually see the colors like so
Colors.print_16_colors()

```

## 256 - colors
These colors may not be supported in all terminals, but give you the most variety:
```python
from custom_loggers import Colors
Colors.Foreground255
Colors.Background255

#These are accessed by assigning which color you want.
Colors.Foreground255(77)

#These can also be vissually seen like so
Colors.print_255_colors()

```

#### Color Printout
![color_printout](https://github.com/astromness/custom_loggers/blob/main/Assets/colors_pic.png?raw=true)


