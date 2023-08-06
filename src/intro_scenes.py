from manim import *
import networkx as nx

config.media_width = "75%"
config.verbosity = "WARNING"


class Greetings(Scene):
    def construct(self):
        tree_layout_scale = 3

        G = nx.Graph()
        G.add_node(0)

        nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6), (1, 7), (2, 8), (3, 9)]

        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge[0], edge[1])

        # Search trees

        pos_dot = LabeledDot(label=Text("+1", font_size=16, color=BLACK), radius=0.2)
        neg_dot = LabeledDot(label=Text("-1", font_size=16, color=BLACK), radius=0.2)
        zero_dot = LabeledDot(label=Text("0", font_size=16, color=BLACK), radius=0.2)
        question_dot = LabeledDot(
            label=Text("?", font_size=16, color=BLACK), radius=0.2
        )

        title = Text("Búsqueda minimax").scale(0.6).shift(3 * UP)

        tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: pos_dot.copy(),
                1: zero_dot.copy(),
                2: neg_dot.copy(),
                3: pos_dot.copy(),
                4: pos_dot.copy(),
                5: neg_dot.copy(),
                6: pos_dot.copy(),
                7: zero_dot.copy(),
                8: zero_dot.copy(),
                9: pos_dot.copy(),
            },
        )

        self.add(tree, title)
        self.wait(2)


class Memory(Scene):
    def construct(self):

        table_scale = 0.3

        # Tables

        cross = (
            VGroup(Line(UP + LEFT, DOWN + RIGHT), Line(UP + RIGHT, DOWN + LEFT))
            .set_color(RED)
            .scale(0.5)
        )

        circle = Circle().set_color(BLUE).scale(0.5)
        blank = Square().set_color(BLACK).scale(0.5)

        loss_token = cross.copy().set_color(BLACK)
        win_token = circle.copy().set_color(BLACK)
        center_token = circle.copy().set_color(BLACK)

        almost_loss = (
            MobjectTable(
                [
                    [loss_token, cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        almost_win = (
            MobjectTable(
                [
                    [win_token, cross.copy(), cross.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), circle.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
            .next_to(almost_loss, 3 * DOWN)
        )

        take_center = (
            MobjectTable(
                [
                    [blank, blank.copy(), blank.copy()],
                    [blank.copy(), center_token, blank.copy()],
                    [blank.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
            .next_to(almost_win, 3 * DOWN)
            .shift(2 * LEFT)
        )

        tables = VGroup(almost_win, almost_loss).shift(2 * LEFT)
        focus = Square(color=YELLOW).scale(0.3).move_to(loss_token.get_center())

        loss_rule = (
            Text("Bloquear opciones de victoria del oponente")
            .scale(0.4)
            .next_to(almost_loss, RIGHT)
        )
        win_rule = (
            Text("Tomar opciones de victoria").scale(0.4).next_to(almost_win, RIGHT)
        )
        why_bother = Text("¿Por qué molestarnos en predecir?")
        memory = Text("¡Usemos memoria!").next_to(why_bother, DOWN)
        why_bother_group = VGroup(why_bother, memory)
        memory_title = Text("Solución con reglas en memoria").scale(0.6)

        # Animations

        self.play(Create(why_bother_group), runtime=5)
        self.wait(2)
        self.play(Transform(why_bother_group, memory_title))
        self.play(why_bother_group.animate().shift(3 * UP))
        self.play(FadeIn(tables))
        self.play(FadeIn(focus))
        self.play(loss_token.animate.set_color(RED))
        self.play(Create(loss_rule))
        self.wait(2)
        self.play(focus.animate().move_to(win_token.get_center()))
        self.play(win_token.animate().set_color(BLUE))
        self.play(Create(win_rule))
        self.wait(2)
        tables.add(take_center)
        self.play(
            FadeOut(why_bother_group),
            focus.animate().shift(3 * UP),
            tables.animate().shift(3 * UP),
            win_rule.animate().shift(3 * UP),
            loss_rule.animate().shift(3 * UP),
            runtime=0.5,
        )
        take_center_rule = (
            Text("Tomar el centro del tablero").scale(0.4).next_to(take_center, RIGHT)
        )
        self.play(
            focus.animate().move_to(center_token.get_center()),
            center_token.animate.set_color(BLUE),
        )
        self.play(Create(take_center_rule))
        self.wait(2)
        etc = Text("etc...").scale(0.6).next_to(tables, 3 * DOWN)
        self.play(FadeIn(etc), FadeOut(focus))
        self.wait(2)


class MemoryProblem(Scene):
    def construct(self):
        table_scale = 0.3

        # Tables

        cross = (
            VGroup(Line(UP + LEFT, DOWN + RIGHT), Line(UP + RIGHT, DOWN + LEFT))
            .set_color(RED)
            .scale(0.5)
        )

        circle = Circle().set_color(BLUE).scale(0.5)
        blank = Square().set_color(BLACK).scale(0.5)
        red_circle = circle.copy().set_color(RED)

        table = (
            MobjectTable(
                [
                    [circle.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
            .shift(2 * LEFT)
        )

        connect4_table = (
            MobjectTable(
                [
                    [
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                        red_circle.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        blank.copy(),
                        blank.copy(),
                        circle.copy(),
                        red_circle.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        blank.copy(),
                        red_circle.copy(),
                        red_circle.copy(),
                        red_circle.copy(),
                        blank.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                    [
                        circle.copy(),
                        circle.copy(),
                        red_circle.copy(),
                        circle.copy(),
                        red_circle.copy(),
                        blank.copy(),
                        blank.copy(),
                    ],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
            .shift(2 * LEFT)
        )

        problem = Text("Problema: Muchos tableros posibles")
        tictactoe_complexity = Text("Para el gato: 9! = 362.800").next_to(problem, DOWN)
        problem_title = Text("Problema de las reglas en memoria").scale(0.6)

        rule_1 = Text("Regla 1").scale(0.4)
        rule_2 = Text("Regla 2").scale(0.4).next_to(rule_1, DOWN)
        rule_3 = Text("Regla 3").scale(0.4).next_to(rule_2, DOWN)
        dots = Text("...").scale(0.4).next_to(rule_3, DOWN)
        rule_n = Text("Regla n").scale(0.4).next_to(dots, DOWN)

        rules_group = VGroup(rule_1, rule_2, rule_3, dots, rule_n)
        rules_group.next_to(table, 2 * RIGHT)

        tedious = Text("Tedioso...").next_to(table, 2 * RIGHT).scale(0.6)
        super_tedious = (
            Text("Más tedioso aún...").scale(0.6).next_to(connect4_table, 2 * RIGHT)
        )

        other_way = Text("Quizás convenga probar lo de anticipar el juego").scale(0.8)

        # Animations

        self.play(Create(problem))
        self.wait(2)
        self.play(Create(tictactoe_complexity))
        self.wait(2)

        problem_group = VGroup(problem, tictactoe_complexity)
        self.play(Transform(problem_group, problem_title))
        self.play(problem_group.animate().shift(3 * UP))

        self.play(FadeIn(table))
        self.wait(2)
        self.play(Create(rules_group))
        self.wait(2)
        self.play(Transform(rules_group, tedious))
        self.wait(2)
        self.play(
            Transform(table, connect4_table), Transform(rules_group, super_tedious)
        )
        self.wait(2)
        self.clear()
        self.play(Create(other_way))
        self.wait(2)
