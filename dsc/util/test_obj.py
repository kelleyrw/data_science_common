import unittest

from .obj import StructLikeREPR, classproperty


class TestObj(unittest.TestCase):
    def test_StructLikeREPR(self):

        with self.subTest("<=3 params"):

            class Foo(StructLikeREPR):
                foo: str = "foo value"
                bar: str = "bar value"
                baz: int = 42

            r = Foo.__str__(Foo)
            print(r)
            self.assertEqual(r, "Foo(foo: foo value, bar: bar value, baz: 42)")

        with self.subTest(">= 4 params"):

            class Foo(StructLikeREPR):
                foo: str = "foo value"
                bar: str = "bar value"
                baz: int = 42
                baxxx: int = 7

            r = Foo.__str__(Foo)
            print(r)
            self.assertEqual(
                r,
                "Foo(\n"
                "  foo  : foo value\n"
                "  bar  : bar value\n"
                "  baz  : 42\n"
                "  baxxx: 7\n"
                ")",
            )

        with self.subTest("adding classproperty"):

            class Foo(StructLikeREPR):
                foo: str = "foo value"
                bar: str = "bar value"
                baz: int = 42
                baxxx: int = 7

                @classproperty
                def bar_property(cls):
                    return "property " + cls.bar

            r = Foo.__str__(Foo)
            print(r)
            self.assertEqual(
                r,
                "Foo(\n"
                "  foo         : foo value\n"
                "  bar         : bar value\n"
                "  baz         : 42\n"
                "  baxxx       : 7\n"
                "  bar_property: property bar value\n"
                ")",
            )


if __name__ == "__main__":
    unittest.main()
