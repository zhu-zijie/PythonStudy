import networkx as nx
import time
from graph_utils import GraphGenerator, visualize_graphs


class RegularGraphGenerator(GraphGenerator):
    def generate(self, num_vertices, degree):
        """生成具有指定顶点数和度数的非同构正则图"""
        # 检查参数有效性
        if num_vertices * degree % 2 != 0:
            raise ValueError(f"正则图要求 顶点数*度数 为偶数")

        if degree >= num_vertices:
            if degree == num_vertices - 1:
                # 完全图
                graph = nx.complete_graph(num_vertices)
                return [graph]
            else:
                raise ValueError(f"度数必须小于顶点数")

        # 使用NetworkX的内置函数生成正则图
        start_time = time.time()
        regular_graphs = list(nx.generators.random_graphs.random_regular_graph(degree, num_vertices, seed=None)
                              for _ in range(min(10, self.max_graphs)))

        # 去除同构的图
        for G in regular_graphs:
            self.is_unique(G)
            if self.check_limits(start_time):
                break

        return self.unique_graphs

    def generate_combinatorial(self, num_vertices, degree):
        """使用组合方法生成正则图"""
        start_time = time.time()
        num_edges = (num_vertices * degree) // 2

        # 使用NetworkX的图形生成器
        for i in range(1000):  # 尝试多次
            if self.check_limits(start_time):
                break

            # 创建一个随机图作为起点
            graph = nx.gnm_random_graph(num_vertices, num_edges)

            # 调整图使其变为正则图
            for _ in range(100):  # 尝试调整多次
                irregular_nodes = [n for n, d in graph.degree() if d != degree]
                if not irregular_nodes:
                    # 图已经是正则的
                    break

                # 选择度数不正确的节点进行调整
                for node in irregular_nodes:
                    current_degree = graph.degree(node)

                    if current_degree > degree:
                        # 删除一条边
                        neighbors = list(graph.neighbors(node))
                        if neighbors:
                            graph.remove_edge(node, neighbors[0])
                    elif current_degree < degree:
                        # 添加一条边
                        non_neighbors = [n for n in graph.nodes() if n != node and not graph.has_edge(node, n)
                                         and graph.degree(n) < degree]
                        if non_neighbors:
                            graph.add_edge(node, non_neighbors[0])

            # 检查图是否正则图
            if all(d == degree for n, d in graph.degree()):
                self.is_unique(graph)

        return self.unique_graphs


def main():
    # 用户输入顶点数和度数
    num_vertices = int(input("请输入顶点数: "))
    degree = int(input(f"请输入顶点的度数 (必须小于{num_vertices}): "))

    # 检查是否满足n*k为偶数
    if num_vertices * degree % 2 != 0:
        print(f"错误: 顶点数({num_vertices}) * 度数({degree}) = {num_vertices * degree}，不是偶数。")
        print("根据图论，正则图要求 顶点数*度数 为偶数。")
        return

    # 设置限制参数
    max_graphs_input = input("最多生成多少个图 (默认: 30): ")
    max_graphs = 30 if max_graphs_input == "" else int(max_graphs_input)

    timeout_input = input("计算超时时间（秒）(默认: 30): ")
    timeout = 30 if timeout_input == "" else int(timeout_input)

    print(f"生成具有 {num_vertices} 个顶点，度数为 {degree} 的非同构正则图...")
    generator = RegularGraphGenerator(max_graphs, timeout)
    graphs = generator.generate(num_vertices, degree)
    print(f"共找到 {len(graphs)} 个非同构正则图")

    visualize_graphs(graphs)


# 执行主函数
if __name__ == "__main__":
    main()
