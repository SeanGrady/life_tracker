import unittest
from life_tracker.backend.cronometer import snake_case_cronometer_column_name


class TestSnakeCaseColumnName(unittest.TestCase):
    def test_one_word(self):
        original_field_name = 'Date'
        target_field_name = 'date'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)

    def test_no_parens(self):
        original_field_name = 'Food Name'
        target_field_name = 'food_name'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)

    def test_one_paren(self):
        original_field_name = 'Caffeine (mg)'
        target_field_name = 'caffeine_mg'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)

    def test_two_parens(self):
        original_field_name = 'B5 (Pantothenic Acid) (mg)'
        target_field_name = 'b5_pantothenic_acid_mg'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)
    
    def test_hyphen(self):
        original_field_name = 'Trans-Fats (g)'
        target_field_name = 'trans_fats_g'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)

    def test_microgram_nonsense(self):
        original_field_name = 'B12 (Cobalamin) (µg)'
        target_field_name = 'b12_cobalamin_ug'
        new_field_name = snake_case_cronometer_column_name(original_field_name)
        self.assertEqual(new_field_name, target_field_name)


if __name__ == '__main__':
    unittest.main()
