import unittest

from day_9_solution import update_head, update_tail


class RopeTests(unittest.TestCase):
    def test_update_head(self):
        head_coords = (1, 1)

        # Test up
        new_head_pos = update_head(head_coords=head_coords, instruction="U 3")
        self.assertEqual(new_head_pos, (1, 4))

        # Test down
        head_coords = (5, 5)
        new_head_pos = update_head(head_coords=head_coords, instruction="D 2")
        self.assertEqual(new_head_pos, (5, 3))

        # Test right
        head_coords = (2, 2)
        new_head_pos = update_head(head_coords=head_coords, instruction="R 3")
        self.assertEqual(new_head_pos, (5, 2))

        # Test left
        head_coords = (3, 3)
        new_head_pos = update_head(head_coords=head_coords, instruction="L 3")
        self.assertEqual(new_head_pos, (0, 3))

    def test_update_tail_no_tail_change(self):
        # Head above - unchanged tail
        head_coords = (1, 2)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

        # Head above - unchanged tail
        head_coords = (1, 1)
        tail_coords = (1, 2)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

        # Head the right - unchanged tail
        head_coords = (2, 1)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

        # Head the right - unchanged tail
        head_coords = (1, 1)
        tail_coords = (2, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

        # Top right - unchanged tail
        head_coords = (2, 2)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

        # Top left - unchanged tail
        head_coords = (1, 3)
        tail_coords = (2, 2)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(tail_coords, new_tail)

    def test_update_tail(self):
        # Two above - move tail
        head_coords = (1, 3)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (1, 2))
 
        # Two below  move tail
        head_coords = (1, 1)
        tail_coords = (1, 3)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (1, 2))

        # Two right  move tail
        head_coords = (3, 1)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (2, 1))

        # Two left  move tail
        head_coords = (5, 1)
        tail_coords = (3, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (4, 1))

        # Top right pull -  move tail
        head_coords = (2, 3)
        tail_coords = (1, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (2, 2))

        # Top left pull -  move tail
        head_coords = (2, 3)
        tail_coords = (3, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (2, 2))

        # Bottom right pull -  move tail
        head_coords = (3, 3)
        tail_coords = (2, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (3, 2))

        # Bottom left pull -  move tail
        head_coords = (2, 3)
        tail_coords = (3, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (2, 2))

        # Right-ways pull - move tail
        head_coords = (4, 2)
        tail_coords = (2, 1)
        new_tail = update_tail(head_coords, tail_coords)
        self.assertEqual(new_tail, (3, 2))



if __name__ == "__main__":
    unittest.main()

