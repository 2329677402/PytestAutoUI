#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 7:50 PM
@ Author      : Poco Ray
@ File        : selector_util.py
@ Description : Selector tool class, used to process and convert various types of selectors.
"""
import re
from typing import Tuple
from selenium.webdriver.common.by import By


class SelectorUtil:
    """ Selector tool class. """

    # Supported locator mapping.
    LOCATOR_MAP = {
        'id': By.ID,
        'name': By.NAME,
        'css_selector': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'link': By.LINK_TEXT,
        'partial_link': By.PARTIAL_LINK_TEXT,
        'tag': By.TAG_NAME,
        'class': By.CLASS_NAME
    }

    @staticmethod
    def is_valid_by(by: str) -> bool:
        """
        Check if the locator is valid.

        :param by: Locator type.
        :return: Whether the locator is valid.
        """
        valid_by = [
            'css_selector', 'id', 'name', 'xpath',
            'link', 'partial_link', 'tag', 'class'
        ]
        return by.lower() in valid_by

    @staticmethod
    def is_xpath_selector(selector: str) -> bool:
        """
        Check if the selector is an XPath.

        :param selector: Selector string.
        :return: Whether the selector is an XPath.
        """
        return selector.strip().startswith(('/', './/', '('))

    @staticmethod
    def process_contains_selector(selector: str) -> Tuple[str, str]:
        """
        Process the :contains() selector.

        :param selector: CSS selector string.
        :return: Processed selector and locator type.
        """
        # Extract the text from the :contains() selector.
        contains_pattern = r':contains\([\'\"](.*?)[\'\"]\)'
        if ':contains(' in selector:
            text = re.search(contains_pattern, selector).group(1)
            base_selector = re.sub(contains_pattern, '', selector).strip()

            # Convert the :contains() selector to XPath.
            if base_selector:
                # If there is a base selector, search for the text within the base selector.
                xpath = (
                    f"//{base_selector}["
                    f"contains(normalize-space(.), '{text}') or "
                    f"contains(normalize-space(text()), '{text}') or "
                    f".//text()[contains(normalize-space(.), '{text}')] or "
                    f"@*[contains(normalize-space(.), '{text}')]"
                    f"]"
                )
            else:
                # If there is no base selector, search for the text in the entire document.
                xpath = (
                    f"//*["
                    f"contains(normalize-space(.), '{text}') or "
                    f"contains(normalize-space(text()), '{text}') or "
                    f".//text()[contains(normalize-space(.), '{text}')] or "
                    f"@*[contains(normalize-space(.), '{text}')]"
                    f"]"
                )
            return xpath, 'xpath'

        return selector, 'css_selector'

    @classmethod
    def get_selenium_locator(cls, selector: str, by: str = 'css_selector') -> Tuple[str, str]:
        """
        Get the Selenium locator.
        :param selector: Selector string.
        :param by: Locator type.
        :return: Tuple of locator type and selector string.
        """
        by = by.lower()

        # Check if the locator is valid.
        if not cls.is_valid_by(by):
            raise ValueError(f"Not supported locator type: '{by}'.")

        # Handle XPath selector.
        if cls.is_xpath_selector(selector):
            return By.XPATH, selector

        # Handle :contains() selector.
        if by == 'css_selector' and ':contains(' in selector:
            selector, by = cls.process_contains_selector(selector)
            return By.XPATH, selector

        # Return the locator type and selector.
        return cls.LOCATOR_MAP[by], selector
