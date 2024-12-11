#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/10/2024 5:45 PM
@ Author      : Administrator
@ File        : custom_webelement.py
@ Description : Custom WebElement class.
"""
import os
from datetime import datetime
from typing import ClassVar, Union
from common.setting import Settings
from utils.log_tool.log_control import INFO, ERROR, WARNING
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException


class CustomWebElement(WebElement):
    _settings: ClassVar[Settings] = Settings()
    screenshots_path = _settings.global_config['screenshots_dir']

    def screenshot(self, name: str = None) -> Union[str, None]:
        """
        Take a screenshot of the current element and save it to the specified file.

        :param name: The name of the file to save the screenshot to.
        :return: Screenshot file full path.
        """
        try:
            # Wait for the element to be visible
            self._parent.execute_script("return arguments[0].complete && arguments[0].naturalHeight !== 0", self)

            # Ensure the directory exists.
            screenshots_dir = self.screenshots_path
            os.makedirs(screenshots_dir, exist_ok=True)

            # Generate file name.
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"

            # Use absolute paths.
            filepath = os.path.join(screenshots_dir, filename)

            if not filename.lower().endswith(".png"):
                WARNING.logger.warning("The screenshot file extension is not '.png'. It is recommended to use '.png'.")
            png = self.screenshot_as_png
            try:
                with open(filepath, "wb") as f:
                    f.write(png)
            except OSError as e:
                ERROR.logger.error(f"Failed to save screenshot to {filename}, error message: {e}")
                return None
            finally:
                del png

            # Log success message
            INFO.logger.info(f"Screenshot saved to: {filepath}")
            return filepath
        except WebDriverException as e:
            # Log error message
            ERROR.logger.error(f"Failed to take screenshot: {str(e)}")
            return None
        except Exception as e:
            # Log any other exceptions
            ERROR.logger.error(f"An unexpected error occurred: {str(e)}")
            return None
