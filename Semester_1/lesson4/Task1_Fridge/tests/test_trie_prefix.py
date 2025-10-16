import pytest

from ..trie_prefix import TriePrefix


@pytest.fixture
def trie():
    words = ['пельмени', 'пельмени уральские', 'картофель', 'картошка фри',
             'кофе', 'кофе эспрессо с молоком', 'кофе латте', 'кофе американо']
    return TriePrefix(words)


class TestTriePrefix:
    @pytest.mark.parametrize('prefix, expected', [
        ('п', {'пельмени', 'пельмени уральские'}),
        ('карто', {'картофель', 'картошка фри'}),
        ('кофе', {'кофе', 'кофе эспрессо с молоком', 'кофе латте', 'кофе американо'}),
        ('пельмени', {'пельмени', 'пельмени уральские'}),
        ('картошка', {'картошка фри'}),
        ('кофе эспрессо', {'кофе эспрессо с молоком'}),
    ])
    def test_search(self, trie, prefix, expected):
        assert trie.search(prefix) == expected
