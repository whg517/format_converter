from format_converter import Writer


def test_format_dict_list():
    data = [{"name": "foo", "age": 15},
            {"name": "foo1"}]
    writer = Writer(data, None)
    assert writer.data == [{"name": "foo", "age": 15},
                           {"name": "foo1", "age": ''}]


def test_format_dict_data():
    data = {"name": "foo",
            "age": 15}
    writer = Writer(data, None)
    assert writer.data == [data]
