import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (6, 36)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (4, 16), (6, 24)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter