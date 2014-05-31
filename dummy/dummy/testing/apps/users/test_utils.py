from dummy.apps.users.utils import bubble_sort


class TestLoginForm:

    def test_sort_list(self, client):
        sequence = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 10, 1, 11, -1, -1.56, -3]
        result = bubble_sort(sequence)
        assert result == [-3, -1.56, -1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 11]
