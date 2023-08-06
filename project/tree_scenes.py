from manim import *
import networkx as nx

config.media_width = "75%"
config.verbosity = "WARNING"


class GamePrediction(Scene):
    def construct(self):

        tree_layout_scale = 4
        table_scale = 0.2

        # Tables

        cross = (
            VGroup(Line(UP + LEFT, DOWN + RIGHT), Line(UP + RIGHT, DOWN + LEFT))
            .set_color(RED)
            .scale(0.5)
        )
        circle = Circle().set_color(BLUE).scale(0.5)
        blank = Circle().set_color(BLACK).scale(0.5)

        base_table = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        first_loss_table = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), circle.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        base_min_table = first_loss_table.copy()

        second_loss_table = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), circle.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        third_loss_table = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), circle.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        tie_table = (
            MobjectTable(
                [
                    [circle.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        min_loss_table_1 = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), cross.copy(), circle.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        min_loss_table_2 = (
            MobjectTable(
                [
                    [blank.copy(), cross.copy(), cross.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), circle.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        min_win_table = (
            MobjectTable(
                [
                    [cross.copy(), cross.copy(), blank.copy()],
                    [cross.copy(), circle.copy(), circle.copy()],
                    [cross.copy(), blank.copy(), blank.copy()],
                ]
            )
            .add_background_rectangle(color=BLACK, opacity=1)
            .scale(table_scale)
        )

        # Trees

        G = nx.Graph()
        G.add_node(0)

        nodes = [0, 1, 2, 3, 4]
        edges = [(0, 1), (0, 2), (0, 3), (0, 4)]

        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge[0], edge[1])

        # Search trees

        base_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_config={
                1: {"fill_color": BLACK},
                2: {"fill_color": BLACK},
                3: {"fill_color": BLACK},
                4: {"fill_color": BLACK},
            },
            edge_config={
                (0, 1): {"stroke_color": BLACK},
                (0, 2): {"stroke_color": BLACK},
                (0, 3): {"stroke_color": BLACK},
                (0, 4): {"stroke_color": BLACK},
            },
            vertex_mobjects={0: base_table},
        )

        second_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: base_table,
                1: first_loss_table,
                2: second_loss_table,
                3: third_loss_table,
                4: tie_table,
            },
        )

        turn_next = Text("MAX (O)").scale(0.6)
        focus = Square(color=YELLOW).scale(0.7)

        turn = Text("¿En qué consiste anticipar el juego?")
        players = Text("Max (O) v/s Min (X)").next_to(turn, DOWN)

        win = Text("Victoria", color=BLUE)
        loss = Text("Derrota", color=RED).next_to(win, DOWN)
        tie = Text("Empate", color=YELLOW).next_to(loss, DOWN)
        none_of_above = Text("No terminal").next_to(tie, DOWN)

        utilities_group = (
            VGroup(win, loss, tie, none_of_above).scale(0.4).move_to(2 * UP + 4 * RIGHT)
        )

        # Animations

        self.play(Create(turn))
        self.wait(2)
        self.play(Transform(turn, players))
        self.wait(2)
        self.play(Transform(turn, turn_next))
        self.play(FadeIn(base_tree), turn.animate.shift(3 * UP))
        self.wait(2)

        self.play(Transform(base_tree, second_tree))
        self.wait(2)

        self.play(Create(win))
        self.wait(2)
        self.play(Create(loss))
        self.wait(2)
        self.play(Create(tie))
        self.wait(2)
        self.play(Create(none_of_above))

        focus.move_to(first_loss_table.get_center())

        self.play(FadeIn(focus))
        stamps_group = VGroup()
        stamp1 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp1)
        self.play(FadeIn(stamp1))

        self.play(focus.animate.move_to(second_loss_table.get_center()))
        stamp2 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp2)
        self.play(FadeIn(stamp2))

        self.play(focus.animate.move_to(third_loss_table.get_center()))
        stamp3 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp3)
        self.play(FadeIn(stamp3))

        self.play(focus.animate.move_to(tie_table.get_center()))
        stamp4 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp4)
        self.play(FadeIn(stamp4))
        self.play(focus.animate.move_to(first_loss_table.get_center()))

        self.wait(2)

        self.play(
            FadeOut(base_tree),
            first_loss_table.animate.move_to(base_table.get_center()),
            FadeOut(stamps_group),
            FadeOut(focus),
            FadeOut(turn),
            runtime=0.1,
        )

        # Trees

        G = nx.Graph()
        G.add_node(0)

        nodes = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (0, 3)]

        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge[0], edge[1])

        # Search trees

        base_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_config={
                1: {"fill_color": BLACK},
                2: {"fill_color": BLACK},
                3: {"fill_color": BLACK},
            },
            edge_config={
                (0, 1): {"stroke_color": BLACK},
                (0, 2): {"stroke_color": BLACK},
                (0, 3): {"stroke_color": BLACK},
            },
            vertex_mobjects={0: base_min_table},
        )

        second_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: base_min_table,
                1: min_loss_table_1,
                2: min_loss_table_2,
                3: min_win_table,
            },
        )

        turn = Text("MIN (X)").scale(0.6).shift(3 * UP)
        focus = Square(color=YELLOW).scale(0.7)

        # Animations

        self.play(FadeIn(turn), Transform(first_loss_table, base_tree))
        self.play(Transform(base_tree, second_tree))
        self.wait(3)

        focus.move_to(min_loss_table_1.get_center())

        self.play(FadeIn(focus))
        self.wait(3)

        stamps_group = VGroup()
        stamp1 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp1)
        self.play(FadeIn(stamp1))
        self.wait(3)

        self.play(focus.animate.move_to(min_loss_table_2.get_center()))
        self.wait(3)
        stamp2 = Text("?").scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp2)
        self.play(FadeIn(stamp2))
        self.wait(3)


        self.play(focus.animate.move_to(min_win_table.get_center()))
        self.wait(3)
        stamp3 = cross.copy().scale(0.5).next_to(focus, DOWN)
        stamps_group.add(stamp3)
        self.play(FadeIn(stamp3), focus.animate.set_color(RED))
        self.wait(3)
        self.play(focus.animate.move_to(base_min_table.get_center()))
        self.wait(3)
        stamp4 = cross.copy().scale(0.5).next_to(focus, LEFT)
        stamps_group.add(stamp4)
        self.play(FadeIn(stamp4))
        self.wait(3)
        self.play(focus.animate.move_to(min_loss_table_1.get_center()))
        self.wait(3)
        self.play(focus.animate.set_color(YELLOW))
        self.wait(3)


class MinimaxValue(Scene):
    def construct(self):
        # Trees
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

        base_max_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_config={
                1: {"fill_color": BLACK},
                2: {"fill_color": BLACK},
                3: {"fill_color": BLACK},
                4: {"fill_color": BLACK},
                5: {"fill_color": BLACK},
                6: {"fill_color": BLACK},
                7: {"fill_color": BLACK},
                8: {"fill_color": BLACK},
                9: {"fill_color": BLACK},
            },
            edge_config={
                (0, 1): {"stroke_color": BLACK},
                (0, 2): {"stroke_color": BLACK},
                (0, 3): {"stroke_color": BLACK},
                (1, 4): {"stroke_color": BLACK},
                (2, 5): {"stroke_color": BLACK},
                (3, 6): {"stroke_color": BLACK},
                (1, 7): {"stroke_color": BLACK},
                (2, 8): {"stroke_color": BLACK},
                (3, 9): {"stroke_color": BLACK},
            },
            vertex_mobjects={0: question_dot.copy()},
        ).shift(UP)

        second_max_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_config={
                4: {"fill_color": BLACK},
                5: {"fill_color": BLACK},
                6: {"fill_color": BLACK},
                7: {"fill_color": BLACK},
                8: {"fill_color": BLACK},
                9: {"fill_color": BLACK},
            },
            edge_config={
                (1, 4): {"stroke_color": BLACK},
                (2, 5): {"stroke_color": BLACK},
                (3, 6): {"stroke_color": BLACK},
                (1, 7): {"stroke_color": BLACK},
                (2, 8): {"stroke_color": BLACK},
                (3, 9): {"stroke_color": BLACK},
            },
            vertex_mobjects={
                0: question_dot.copy(),
                1: question_dot.copy(),
                2: question_dot.copy(),
                3: question_dot.copy(),
            },
        ).shift(UP)

        third_max_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: question_dot.copy(),
                1: question_dot.copy(),
                2: question_dot.copy(),
                3: question_dot.copy(),
                4: pos_dot.copy(),
                5: neg_dot.copy(),
                6: pos_dot.copy(),
                7: zero_dot.copy(),
                8: zero_dot.copy(),
                9: pos_dot.copy(),
            },
        ).shift(UP)

        fourth_max_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: question_dot.copy(),
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
        ).shift(UP)

        fifth_max_tree = Graph(
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
        ).shift(UP)

        level1 = Text("h = 0: MAX").scale(0.6).shift(5 * LEFT + 2 * UP)
        level2 = Text("h = 1: MIN").scale(0.6).next_to(level1, 3 * DOWN)
        level3 = Text("h = 2: MAX").scale(0.6).next_to(level2, 3 * DOWN)

        # Score function

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}", r"\usepackage{amssymb}")

        minimax_function = MathTex(
            r"\text{minimax($s$)} = ",
            r"""\begin{cases}
                                 utility(s) \qquad &\text{si $s$ es terminal} \cr
                                 max\{minimax(\text{$s'$): $s'$ hijo de }$s$\}\qquad &\text{si es el turno de Max en $s$} \cr
                                 min\{minimax(\text{$s'$): $s'$ hijo de }$s$\}\qquad &\text{si es el turno de Min en $s$} \cr
                                 \end{cases}""",
            tex_template=template,
        ).scale(0.7)

        utility_function = MathTex(
            r"\text{utility($s$)} = ",
            r"""\begin{cases}
                                 1 \qquad &\text{si $s$ es una victoria de Max} \cr
                                 -1 \qquad &\text{si $s$ es una derrota de Max} \cr
                                 0 \qquad &\text{si $s$ es un empate} \cr 
                                 \end{cases}""",
            tex_template=template,
        ).scale(0.7)
        minimax = Text(
            "En caso de llevar a tableros no terminales, simular la elección de Min en ese escenario"
        ).scale(0.4)
        utility = Text(
            "Verificar si las jugadas disponibles llevan a una victoria, derrota o un empate"
        ).scale(0.4)

        utility.next_to(minimax, UP)
        utility_function.next_to(minimax_function, UP)

        functions_group = VGroup(utility, minimax)
        evaluation_max = Text("Dos formas de evaluar un estado").scale(0.6)

        focus = Rectangle(color=YELLOW, width=6, height=0.5)
        focus.move_to(utility_function.get_center() + 1.2 * RIGHT + 0.5 * UP)

        minimax_focus = Rectangle(color=YELLOW, width=10, height=0.5)
        minimax_focus.move_to(minimax_function.get_center() + 1.25 * RIGHT + 0.5 * UP)

        title = Text("Cálculo de la utilidad de un nodo").scale(0.6).shift(3 * UP)

        # Animations

        self.play(Create(evaluation_max))
        self.wait()
        self.play(Transform(evaluation_max, functions_group))
        self.wait()
        self.play(FadeOut(evaluation_max), FadeIn(title))
        self.wait()
        self.play(FadeIn(utility_function), FadeIn(minimax_function))
        self.wait()
        self.play(FadeIn(focus))
        self.wait()
        self.play(focus.animate.shift(0.5 * DOWN))
        self.wait()
        self.play(focus.animate.shift(0.5 * DOWN))

        self.play(FadeOut(focus))

        self.play(FadeIn(minimax_focus))
        self.wait()
        self.play(minimax_focus.animate.shift(0.5 * DOWN))
        self.wait()
        self.play(minimax_focus.animate.shift(0.5 * DOWN))
        self.wait()
        self.play(FadeOut(minimax_focus), FadeOut(utility_function))

        self.play(minimax_function.animate().next_to(base_max_tree, 4 * DOWN))
        self.wait()

        self.play(
            FadeIn(base_max_tree), FadeIn(level1), level1.animate().set_color(YELLOW)
        )
        self.wait()

        self.play(
            Transform(base_max_tree, second_max_tree),
            FadeIn(level2),
            level2.animate().set_color(YELLOW),
            level1.animate().set_color(WHITE),
        )
        self.wait()

        self.play(
            Transform(base_max_tree, third_max_tree),
            FadeIn(level3),
            level2.animate().set_color(WHITE),
            level3.animate().set_color(YELLOW),
        )
        self.wait()

        self.play(
            Transform(base_max_tree, fourth_max_tree),
            level2.animate().set_color(YELLOW),
            level3.animate().set_color(WHITE),
        )
        self.wait()

        self.play(
            Transform(base_max_tree, fifth_max_tree),
            level2.animate().set_color(WHITE),
            level1.animate().set_color(YELLOW),
        )
        self.wait()


class EvaluationFunction(Scene):
    def construct(self):

        tree_layout_scale = 4
        table_scale = 0.2

        # Tables

        cross = (
            VGroup(Line(UP + LEFT, DOWN + RIGHT), Line(UP + RIGHT, DOWN + LEFT))
            .set_color(RED)
            .scale(0.5)
        )
        circle = Circle().set_color(BLUE).scale(0.5)
        blank = Circle().set_color(BLACK).scale(0.5)

        base_table = MobjectTable(
            [
                [blank.copy(), cross.copy(), blank.copy()],
                [cross.copy(), circle.copy(), circle.copy()],
                [cross.copy(), blank.copy(), blank.copy()],
            ]
        ).add_background_rectangle(color=BLACK, opacity=1)

        first_loss_table = MobjectTable(
            [
                [blank.copy(), cross.copy(), blank.copy()],
                [cross.copy(), circle.copy(), circle.copy()],
                [cross.copy(), blank.copy(), circle.copy()],
            ]
        ).add_background_rectangle(color=BLACK, opacity=1)

        second_loss_table = MobjectTable(
            [
                [blank.copy(), cross.copy(), blank.copy()],
                [cross.copy(), circle.copy(), circle.copy()],
                [cross.copy(), circle.copy(), blank.copy()],
            ]
        ).add_background_rectangle(color=BLACK, opacity=1)

        third_loss_table = MobjectTable(
            [
                [blank.copy(), cross.copy(), circle.copy()],
                [cross.copy(), circle.copy(), circle.copy()],
                [cross.copy(), blank.copy(), blank.copy()],
            ]
        ).add_background_rectangle(color=BLACK, opacity=1)

        tie_table = MobjectTable(
            [
                [circle.copy(), cross.copy(), blank.copy()],
                [cross.copy(), circle.copy(), circle.copy()],
                [cross.copy(), blank.copy(), blank.copy()],
            ]
        ).add_background_rectangle(color=BLACK, opacity=1)

        # Trees

        G = nx.Graph()
        G.add_node(0)

        nodes = [0, 1, 2, 3, 4]
        edges = [(0, 1), (0, 2), (0, 3), (0, 4)]

        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge[0], edge[1])

        # Search trees

        base_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_config={
                1: {"fill_color": BLACK},
                2: {"fill_color": BLACK},
                3: {"fill_color": BLACK},
                4: {"fill_color": BLACK},
            },
            edge_config={
                (0, 1): {"stroke_color": BLACK},
                (0, 2): {"stroke_color": BLACK},
                (0, 3): {"stroke_color": BLACK},
                (0, 4): {"stroke_color": BLACK},
            },
            vertex_mobjects={0: base_table.copy().scale(table_scale)},
        ).shift(0.7 * UP)

        second_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: base_table.copy().scale(table_scale),
                1: first_loss_table.copy().scale(table_scale),
                2: second_loss_table.copy().scale(table_scale),
                3: third_loss_table.copy().scale(table_scale),
                4: tie_table.copy().scale(table_scale),
            },
        ).shift(0.7 * UP)

        third_tree = Graph(
            list(G.nodes),
            list(G.edges),
            layout="tree",
            root_vertex=0,
            labels=False,
            layout_scale=tree_layout_scale,
            vertex_mobjects={
                0: base_table.copy().scale(table_scale),
                1: first_loss_table.copy().scale(table_scale),
                2: second_loss_table.copy().scale(table_scale),
                3: third_loss_table.copy().scale(table_scale),
                4: tie_table.copy().scale(table_scale),
            },
        ).shift(0.7 * UP)

        # Score function (with h and eval function)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}", r"\usepackage{amssymb}")

        minimax_function = MathTex(
            r"\text{minimax($s$, $h$)} = ",
            r"""\begin{cases}
                                 utility(s) \qquad &\text{si $s$ es terminal} \cr
                                 eval(s) \qquad &\text{si $h = 0$} \cr
                                 max\{minimax(\text{$s'$, $h-1$): $s'$ hijo de }$s$\}\qquad &\text{si es el turno de Max en $s$} \cr
                                 min\{minimax(\text{$s'$, $h-1$): $s'$ hijo de }$s$\}\qquad &\text{si es el turno de Min en $s$} \cr
                                 \end{cases}""",
            tex_template=template,
        ).scale(0.7)

        title = Text("Detalle final: Nuevamente tenemos problemas de escala").scale(0.6)
        title2 = Text("Podemos modificar el valor minimax").scale(0.6)
        title3 = Text("Nuevo valor Minimax").scale(0.6).shift(3.6 * UP)

        evaluation_function = Text(
            "Función de evaluación: Estimación sobre el valor de un tablero"
        ).scale(0.4)
        evaluation_function.next_to(minimax_function, DOWN)

        # Animations
        self.play(Create(title))
        self.wait()
        self.play(Transform(title, title2))
        self.wait()
        self.play(Transform(title, title3))
        self.wait()
        self.play(FadeIn(minimax_function))
        self.wait()
        self.play(Create(evaluation_function))
        self.wait()
        self.play(FadeOut(minimax_function), FadeOut(evaluation_function))

        tree = base_tree.copy()

        eval_function = MathTex(
            r"eval = \text{opciones de victoria Max} - \text{opciones de victoria Min}"
        ).scale(0.7)
        eval_function.next_to(title, DOWN)

        self.play(FadeIn(tree), FadeIn(eval_function))
        self.wait()
        self.play(Transform(tree, second_tree))
        self.wait()

        evaluation_square = Square(color=YELLOW).scale(0.7)

        evaluation_square.shift(0.6 * DOWN + 4 * RIGHT)
        first_evaluation = MathTex(r"eval = 2 - 2 = 0").scale(0.7)
        first_evaluation.next_to(evaluation_square, DOWN)

        self.play(FadeIn(evaluation_square), FadeIn(first_evaluation))
        self.wait()

        self.play(FadeOut(evaluation_square), FadeOut(first_evaluation))
        evaluation_square.shift(8 * LEFT)
        second_evaluation = MathTex(r"eval = 2 - 1 = 1").scale(0.7)
        second_evaluation.next_to(evaluation_square, DOWN)
        self.wait()

        evaluation_square.set_color(GREEN)
        self.play(
            FadeIn(evaluation_square),
            FadeIn(second_evaluation),
            Transform(tree, third_tree),
        )
        self.wait()
