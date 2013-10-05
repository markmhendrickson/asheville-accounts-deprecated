from test.base import UnitTest
from shared.helpers import create_uuid


class TestHelpers(UnitTest):

    def test_create_uuid(self):
        "Tests that the create_uuid method makes random uuid's"
        one = create_uuid()
        two = create_uuid()
        assert type(one) == str
        assert one != two
        assert len(two) == 36
