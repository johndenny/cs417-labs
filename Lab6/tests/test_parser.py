from parser import parse_product_basic, parse_availability
from conftest import *

def test_parse_product_basic_extracts_id(valid_product):
    # Arrange

    #Act
    result = parse_product_basic(valid_product)

    assert result["id"] == valid_product["id"]

def test_parse_product_basic_extracts_name(valid_product):
    result = parse_product_basic(valid_product)
    assert result['id'] == valid_product["id"]

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    result = parse_product_basic(valid_product)
    assert result.keys() == {"id", "name"}