import numpy as np
from manim import *


class intro(Scene):
    def construct(self):
        underlined_name = Text('404', font='Monospace', color='RED').scale(2).move_to([-1.5, 0.25, 0])
        not_underlined_name = Text('Engineering', font='Monospace', color='RED').scale(0.75).move_to([1.375, 0, 0])

        a = Underline(underlined_name, color='RED')

        title = Text('0001-Project_EOT', font='Monospace', color='White').scale(0.5).move_to([0, -2, 0])

        self.play(Write(underlined_name), run_time=1.5)
        self.play(Write(a))
        self.wait(0.5)
        self.play(Write(not_underlined_name), run_time=1)
        self.wait(0.5)
        self.play(Write(title), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(underlined_name), FadeOut(a), FadeOut(not_underlined_name), FadeOut(title), run_time=1)

        self.wait(1)

class scene1(Scene):
    def construct(self):
        requirements = Text('''
        Required Steps to Complete Project: 
          1. Create the Bubble Sort Algorithm.
          2. Create the Selection Sort Algorithm
          3. Apply the Bubble Sort algorithm to 1000 arrays each with 500 elements.
          4. Apply the Bubble Sort algorithm to 1000 arrays each with 2500 elements.
          5. Apply the Bubble Sort algorithm to 1000 arrays each with 5000 elements.
          6. Apply the Selection Sort algorithm to 1000 arrays each with 500 elements.
          7. Apply the Selection Sort algorithm to 1000 arrays each with 2500 elements.
          8. Apply the Selection Sort algorithm to 1000 arrays each with 5000 elements.
          9. Create a graph of the data and determine a best fit line for each function.''', font='Monospace', color='White').scale(0.325).move_to([0, 0, 0])

        self.play(Write(requirements), run_time=15)
        self.wait(1)
        self.play(FadeOut(requirements), run_time=5)

# Bubble Sort Algorithm
class scene2(Scene):
    SORT_WAIT_TIME = 0.2
    def construct(self):
        bubble_sort = Text('''
        Bubble Sort:
          Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
          compares adjacent elements and swaps them if they are in the wrong order. 
        ''', font='Monospace', color='White').scale(0.325).move_to([-1.5, 2, 0])

        self.input_array = [2,9,1,4,7,8,6,5,3]
        self.indexes = [i for i in range(len(self.input_array))]
        self.tex_array = self.wrap_input_array()
        self.v_array = VGroup(*self.tex_array).arrange(buff=LARGE_BUFF)
        
        self.circles = [Circle() for i in self.input_array]
        
        for index,c in enumerate(self.circles):
            c.surround(self.v_array[index])
            self.v_array[index].add(c)

        example_text = Text('Example Array: ', font='Monospace', color='White').scale(0.325).move_to([-1.5, 1, 0])

        # Show the description of the algorithm
        self.play(Write(bubble_sort), run_time=10)
        self.wait(1)
        self.play(FadeOut(bubble_sort), run_time=5)
        self.wait(0.25)

        # Show example of how the sort works
        self.play(Write(example_text), run_time=1)
        self.play(Create(self.v_array))
        self.wait(1)
        self.bubble_sort()
        self.play(FadeOut(example_text), FadeOut(self.v_array), run_time=1)
        self.wait(1)

        # Show the code for the algorithm in c++
        c = "assets/c++/bubble_sort.cpp"
        code = Code(c, font='Monospace', color='White').scale(0.5).move_to([-1.5, 2, 0])
        self.play(Write(code), run_time=10)
        self.wait(1)
        self.play(FadeOut(code), run_time=5)
        self.wait(1)

        # Show the data for the algorithm over 500, 2500, and 5000 elements
        data = Text('''
        Data:
          The data for the Bubble Sort algorithm is shown below. 
          The data shows the time it takes to sort 1000 arrays with 500, 2500, and 5000 elements.''', font='Monospace', color='White').scale(0.325).move_to([-1, 2, 0])
        table = Table(
            [['500', '436.45'], ['2500', '9673.83'], ['5000', '39452.43']], col_labels=[Text('Number of Elements'), Text('Time (ms)')], include_outer_lines=True).scale(0.5).move_to([0, -1, 0])
        self.play(Write(data), run_time=10)
        self.play(Write(table), run_time=5)
        self.wait(5)
        self.play(FadeOut(data), table.animate.move_to([3, -1, 0]), run_time=5)
        self.wait(1)

        # Show the graph of the data
        graph_text = Text('''
        Graph:
          The graph of the data is shown below. 
          The graph shows the time it takes to sort 1000 arrays with 500, 2500, and 5000 elements.''', font='Monospace', color='White').scale(0.325).move_to([-1, 2, 0])
        graph_data = [[500, 436.45], [2500, 9673.83], [5000, 39452.43]]
        graph = Axes(
            x_range=[0, 5000, 500],
            y_range=[0, 40000, 5000],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": False},
            tips=False,
        )
        graph_label = graph.get_axis_labels(x_label=Text("Number of Elements"), y_label=Text("Time (ms)"))
        graph.add(graph_label)
        graph_points = []
        for point in graph_data:
            graph_points.append(Dot().move_to(graph.coords_to_point(point[0], point[1])))
        graph.add(*graph_points)
        graph.add(*[Line(graph_points[i].get_center(), graph_points[i+1].get_center()) for i in range(len(graph_points)-1)])
        graph.scale(0.5).move_to([-3, -1, 0])
        self.play(Write(graph_text), run_time=5)
        self.play(Write(graph), run_time=10)
        self.wait(5)
        self.play(FadeOut(graph), FadeOut(graph_text), FadeOut(table), run_time=5)
        self.wait(1)

    def wrap_input_array(self):
        return [Tex(str(i))
            for i in self.input_array
        ]
    
    def bubble_sort(self):
        for i in range(len(self.input_array)):
            for j in range(len(self.input_array) - i - 1):
                if (self.input_array[j] > self.input_array[j+1]):
                    self.act(j,j+1)
    def act(self,i,j):
        self.play(Swap(self.v_array[self.indexes[i]],self.v_array[self.indexes[j]] ))
        self.wait(scene2.SORT_WAIT_TIME)
        scene2.SORT_WAIT_TIME*=0.7
        self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
        self.indexes[i],self.indexes[j] = self.indexes[j],self.indexes[i]

# Selection Sort Scene
class scene3(Scene):
    def construct(self):
        pass

# Final Thoughs Scene
class scene4(Scene):
    def construct(self):
        pass

# Closing Scene
class scene5(Scene):
    def construct(self):
        pass

