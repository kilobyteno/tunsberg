import pytest

from tunsberg.utsikten import format_version_tag


class TestFormatVersionTag:
    def test_returns_correctly_formatted_tag_name(self):
        """Returns correctly formatted tag name"""
        # Arrange
        name = '1.2.3'

        # Act
        result = format_version_tag(name)

        # Assert
        assert result == name

    def test_raises_no_error_when_tag_name_is_correctly_formatted(self):
        """Raises no error when tag name is correctly formatted"""
        # Arrange
        name = '1.2.3'

        # Act & Assert
        try:
            format_version_tag(name)
        except ValueError:
            pytest.fail('Unexpected ValueError')

    def test_accepts_string_input(self):
        """Accepts string input"""
        # Arrange
        name = '1.2.3'

        # Act
        result = format_version_tag(name)

        # Assert
        assert isinstance(result, str)

    def test_raises_value_error_when_tag_name_is_not_formatted_correctly(self):
        """Raises ValueError when tag name is not formatted correctly"""
        # Arrange
        name = '1.2.3.4'

        # Act & Assert
        with pytest.raises(ValueError):
            format_version_tag(name)

    def test_rejects_tag_name_with_only_two_numbers(self):
        """Rejects tag name with only two numbers"""
        # Arrange
        name = '1.2'

        # Act & Assert
        with pytest.raises(ValueError):
            format_version_tag(name)

    def test_rejects_tag_name_with_non_numeric_characters(self):
        """Rejects tag name with non-numeric characters"""
        # Arrange
        name = '1.2.a'

        # Act & Assert
        with pytest.raises(ValueError):
            format_version_tag(name)
