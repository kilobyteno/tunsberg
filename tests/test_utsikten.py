import pytest

from tunsberg.utsikten import format_version_tag


class TestFormatVersionTag:
    def test_returns_correctly_formatted_tag_name(self):
        """Returns correctly formatted tag name"""
        assert format_version_tag('1.2.3') == '1.2.3'

    def test_raises_value_error_when_tag_name_is_not_formatted_correctly(self):
        """Raises ValueError when tag name is not formatted correctly"""
        with pytest.raises(ValueError):
            format_version_tag('1.2.3.4')

    def test_rejects_tag_name_with_only_two_numbers(self):
        """Rejects tag name with only two numbers"""
        with pytest.raises(ValueError):
            format_version_tag('1.2')

    def test_rejects_tag_name_with_non_numeric_characters(self):
        """Rejects tag name with non-numeric characters"""
        with pytest.raises(ValueError):
            format_version_tag('1.2.a')
