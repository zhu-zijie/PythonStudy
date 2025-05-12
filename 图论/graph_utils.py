import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time


class GraphGenerator:
    """图生成器基类"""

    def __init__(self, max_graphs=30, timeout=30):
        self.max_graphs = max_graphs
        self.timeout = timeout
        self.unique_graphs = []
        self.seen_hashes = set()

    def is_unique(self, graph):
        """检查图是否已经存在（包括同构检查）"""
        # 先用快速签名过滤
        sig = get_graph_signature(graph)
        if sig not in self.seen_hashes:
            # 在通过严格同构检查
            for existing_graph in self.unique_graphs:
                if nx.is_isomorphic(graph, existing_graph):
                    return False

            self.seen_hashes.add(sig)
            self.unique_graphs.append(graph)
            return True
        return False

    def check_limits(self, start_time):
        """检查是否达到限制条件"""
        return time.time() - start_time > self.timeout or len(self.unique_graphs) >= self.max_graphs


def visualize_graphs(graphs, max_display=20):
    if len(graphs) > max_display:
        print(f"图数量过多，仅显示前 {max_display} 个")
        graphs = graphs[:max_display]

    num_graphs = len(graphs)
    cols = min(4, num_graphs)
    rows = (num_graphs + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))
    if rows == 1 and cols == 1:
        axes = np.array([axes])
    axes = axes.flatten()

    for i, G in enumerate(graphs):
        if i < len(axes):
            ax = axes[i]
            pos = nx.spring_layout(G, seed=42, iterations=50)
            nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue',
                    node_size=500, font_weight='bold')
            if hasattr(ax, "set_title"):
                ax.set_title(f"Graph {i + 1}")

    # 隐藏多余的子图
    for ax in axes[num_graphs:]:
        if hasattr(ax, 'set_visible'):
            ax.set_visible(False)

    plt.tight_layout()
    plt.show()


def get_graph_signature(g):
    """统一的图签名生成函数"""
    # 结合两种方法的优点
    return (tuple(sorted([g.degree(n) for n in g.nodes()])),
            tuple(sorted(tuple(sorted(g.neighbors(n))) for n in sorted(g.nodes()))))
