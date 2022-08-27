import unittest
from datetime import date
from dsny_holidays import is_dsny_holiday


class DSNYHolidayTests(unittest.TestCase):
    def test_non_holiday_output_format(self):
        # Check output format when NOT a holiday
        self.assertEqual(len(is_dsny_holiday(date(2017, 5, 1))), 2, 'There were not 2 returned values')
        self.assertIsInstance(is_dsny_holiday(date(2017, 5, 1))[0], bool, 'The first value returned was not a boolean')
        self.assertIsInstance(is_dsny_holiday(date(2017, 5, 1))[1], str, 'The first value returned was not a string')

    def test_holiday_output_format(self):
        # Check output format when it IS a holiday
        self.assertEqual(len(is_dsny_holiday(date(2075, 1, 1))), 2, 'There were not 2 returned values')
        self.assertIsInstance(is_dsny_holiday(date(2075, 1, 1))[0], bool, 'The first value returned was not a boolean')
        self.assertIsInstance(is_dsny_holiday(date(2075, 1, 1))[1], str, 'The first value returned was not a string')

    def test_should_not_call_second_weekly_holiday_a_holiday(self):
        # Veterans Day 2017- there WAS pickup because election day was the same week
        self.assertFalse(is_dsny_holiday(date(2017, 11, 10))[0], 'Veterans Day 2017 should NOT be a holiday')

    def test_should_catch_observed_dates(self):
        # Check that when a holiday is on a Saturday, Friday is caught as an observed holiday, and when it's Sunday,
        # Monday is caught
        # Jan 1 2011 was a Saturday, catch 12/31 as the observed date
        self.assertTrue(is_dsny_holiday(date(2010, 12, 31))[0], 'NYE 2010 should be observed as New Years Day 2011.')
        # July 4, 2021 is a Sunday
        self.assertTrue(is_dsny_holiday(date(2021, 7, 5))[0], 'July 4th 2021 should be observed on Monday, July 5th.')
        # Feb 12, 2017 was a Sunday, Abe Lincoln's bday observed 13 Feb 2017
        self.assertTrue(is_dsny_holiday(date(2017, 2, 13))[0], "Abraham Lincoln's Birthday observed Feb 13, 2017")

    def test_non_holidays_should_not_be_holidays(self):
        self.assertFalse(is_dsny_holiday(date(2021, 2, 5))[0], "Vince's birthday- shockingly- is NOT a holiday.")
        self.assertFalse(is_dsny_holiday(date(2016, 12, 31))[0], 'NYE 2016 failed')

    def test_holidays_should_be_holidays(self):
        # Using published 2021 calendar of holidays:
        self.assertTrue(is_dsny_holiday(date(2021, 1, 1))[0], 'New Years Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 1, 18))[0], 'MLK Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 2, 12))[0], 'Lincoln Birthday 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 2, 15))[0], 'Presidents Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 5, 31))[0], 'Memorial Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 7, 4))[0], 'Independence Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 9, 6))[0], 'Labor Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 10, 11))[0], "Indigenous Peoples' Day 2021 failed")
        self.assertTrue(is_dsny_holiday(date(2021, 11, 2))[0], 'Election Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 11, 11))[0], 'Veterans Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 11, 25))[0], 'Thanksgiving Day 2021 failed')
        self.assertTrue(is_dsny_holiday(date(2021, 12, 25))[0], 'Christmas Day 2021 failed')

        # Using published 2018 calendar of holidays:
        self.assertTrue(is_dsny_holiday(date(2018, 1, 1))[0], 'New Years Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 1, 15))[0], 'MLK Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 2, 12))[0], 'Lincoln Birthday 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 2, 19))[0], 'Presidents Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 5, 28))[0], 'Memorial Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 7, 4))[0], 'Independence Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 9, 3))[0], 'Labor Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 10, 8))[0], "Indigenous Peoples' Day 2018 failed")
        self.assertTrue(is_dsny_holiday(date(2018, 11, 6))[0], 'Election Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 11, 12))[0], 'Veterans Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 11, 22))[0], 'Thanksgiving Day 2018 failed')
        self.assertTrue(is_dsny_holiday(date(2018, 12, 25))[0], 'Christmas Day 2018 failed')

    def testCorrectHolidayNamesShouldBeReturned(self):
        self.assertEqual(is_dsny_holiday(date(2021, 1, 1))[1], 'New Years Day', 'New Years Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 1, 18))[1], 'Martin Luther King Day', 'MLK Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 2, 12))[1], "Abraham Lincoln's Birthday",
                         "Lincoln's Birthday failed")
        self.assertEqual(is_dsny_holiday(date(2021, 2, 15))[1], "Presidents' Day", "Presidents' Day failed")
        self.assertEqual(is_dsny_holiday(date(2021, 5, 31))[1], 'Memorial Day', 'Memorial Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 7, 4))[1], 'Independence Day', 'Independence Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 9, 6))[1], 'Labor Day', 'Labor Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 10, 11))[1], "Indigenous Peoples' Day",
                         "Indigenous Peoples' Day failed")
        self.assertEqual(is_dsny_holiday(date(2021, 11, 2))[1], 'Election Day', 'Election Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 11, 11))[1], 'Veterans Day', 'Veterans Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 11, 25))[1], 'Thanksgiving Day', 'Thanksgiving Day failed')
        self.assertEqual(is_dsny_holiday(date(2021, 12, 25))[1], 'Christmas Day', 'Christmas Day failed')

    def testNoHolidayNameShouldBeReturnedWhenNotAHoliday(self):
        self.assertEqual(is_dsny_holiday(date(2021, 3, 29))[1], '', 'Non-holidays should not return a holiday name.')


if __name__ == '__main__':
    unittest.main()