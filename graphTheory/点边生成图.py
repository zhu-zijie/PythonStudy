import networkx as nx
from itertools import combinations
import time
from graph_utils import GraphGenerator, visualize_graphs


class EdgeGraphGenerator(GraphGenerator):
    def generate(self, num_vertices, num_edges):
        """生成具有指定顶点数和边数的非同构图"""
        # 检查边数是否合法
        max_edges = num_vertices * (num_vertices - 1) // 2
        if num_edges > max_edges:
            raise ValueError(f"边数超过最大可能值 {max_edges}")

        # 所有可能的边
        all_possible_edges = list(combinations(range(num_vertices), 2))

        # 设置超时时间
        start_time = time.time()

        # 从所有可能的边中选择num_edges条边
        for edges in combinations(all_possible_edges, num_edges):
            # 检查是否超时或达到最大图数
            if self.check_limits(start_time):
                print(f"已达到限制条件（时间: {time.time() - start_time:.1f}秒, 图数量: {len(self.unique_graphs)}）")
                break

            graph = nx.Graph()
            graph.add_nodes_from(range(num_vertices))
            graph.add_edges_from(edges)

            self.is_unique(graph)

        return self.unique_graphs


def main():
    # 用户输入顶点数和边数
    num_vertices = int(input("请输入顶点数: "))

    max_edges = num_vertices * (num_vertices - 1) // 2
    print(f"对于 {num_vertices} 个顶点，最多可以有 {max_edges} 条边")

    num_edges = int(input(f"请输入边数 (0-{max_edges}): "))

    # 设置限制参数，提供默认值
    max_graphs_input = input("最多生成多少个图 (默认: 30): ")
    max_graphs = 30 if max_graphs_input == "" else int(max_graphs_input)

    timeout_input = input("计算超时时间（秒）(默认: 30): ")
    timeout = 30 if timeout_input == "" else int(timeout_input)

    print(f"生成具有 {num_vertices} 个顶点和 {num_edges} 条边的非同构图...")
    generator = EdgeGraphGenerator(max_graphs, timeout)
    graphs = generator.generate(num_vertices, num_edges)
    print(f"共找到 {len(graphs)} 个非同构图")

    visualize_graphs(graphs)


# 执行主函数
if __name__ == "__main__":
    main()
