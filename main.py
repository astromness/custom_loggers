from custom_loggers import CustomLogger,ColoredFormatter,Colors
from argparse import ArgumentParser

def main():
    CustomLogger.inclusive = True
    CustomLogger.global_log_level = 0
    CustomLogger.use_global_log_level_default = True

    ColoredFormatter.assign_level_color("yup", Colors.Foreground255(226))

    logger = CustomLogger("testLogger")
    logger2 = CustomLogger("test2logger")
    logger3 = CustomLogger("channel_tester", channel="NewChannel")
    logger4 = CustomLogger("channel_tester2", channel="NewChannel")
    logger3.info("channel test on")
    logger4.info("channel test on")
    CustomLogger.channel_disabled("NewChannel", True)
    logger3.info("channel test off")
    logger4.info("channel test off")
    logger2.add_level("yup", 1, True)
    logger2.log("yup", "original message")
    logger.yup("my new message")
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
    CustomLogger.logging_disabled = False

    class NewLogger(CustomLogger):
        use_global_log_level_default = True
        inclusive = False
        default_colored_format = '%(levelname)-8s: %(message)s'
        has_run_once = False

        CustomLogger.add_level("NEWLEVEL", 1)
        ColoredFormatter.assign_level_color("NEWLEVEL", Colors.Foreground255(77))

        def newlevel(self, msg):
            self.log("NEWLEVEL", msg)

    logger = NewLogger("TestLogger")
    logger.newlevel("this shows your new level")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ap=ArgumentParser()
    ap.add_argument("--show_colors","-s",required=False,default=False,action="store_true")
    arguments=ap.parse_args()

    if arguments.show_colors:
        Colors.print_16_colors()
        Colors.print_255_colors()
    else:
        main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
