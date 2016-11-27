from collections import deque
import copy


class MaxFlow(object):

    def __init__(self, T, s, t):
        self._num_nodes = len(T)
        self._T = copy.deepcopy(T)
        self._curr_T = [[0] * self._num_nodes for i in range(self._num_nodes)]
        self._s = s
        self._t = t

    def find_max_flow(self):
        while True:
            T_res = self.get_residual_flow()
            path, c = MaxFlow.find_shortest_path(T_res, self._s, self._t)
            if path is None:
                break
            self.augment_flow(path, c)

        total_capacity = reduce(lambda x, y: x+y, self._curr_T[self._s])
        return total_capacity

    def print_flow_network(self):
        for i in self._curr_T:
            print i

    def get_residual_flow(self):
        T_residual = [[0] * self._num_nodes for i in range(self._num_nodes)]
        for i in range(self._num_nodes):
            for j in range(i):
                if self._curr_T[i][j] > 0:
                    T_residual[i][j] = self._T[i][j] - self._curr_T[i][j]
                    T_residual[j][i] = self._curr_T[i][j] + self._T[j][i]
                elif self._curr_T[j][i] > 0:
                    T_residual[j][i] = self._T[j][i] - self._curr_T[j][i]
                    T_residual[i][j] = self._curr_T[j][i] + self._T[i][j]
                else:
                    T_residual[i][j] = self._T[i][j]
                    T_residual[j][i] = self._T[j][i]
        return T_residual

    def augment_flow(self, path, c):
        for i, j in zip(path[:-1], path[1:]):
            self._curr_T[i][j] += c

    @staticmethod
    def find_shortest_path(T_residual, s, t):
        """
        :param T_residual: T[i][j] is capacity from i to j
        :param s: origin
        :param t: destination
        :return: path from s to t, in the format [s, i1, i2, i3, ..., t
            and the amount of flow
        """
        parent_map = {}  # key is node_id, value is parent's node_id
        explored_nodes = deque([s])
        explored_nodes_set = set([s])
        if_found = False
        while explored_nodes and (not if_found):
            curr_node = explored_nodes.popleft()
            for child_node, capacity in enumerate(T_residual[curr_node]):
                if capacity > 0 and (child_node not in explored_nodes_set):
                    explored_nodes.append(child_node)
                    explored_nodes_set.add(child_node)
                    parent_map[child_node] = curr_node
                    if child_node == t:
                        if_found = True
        if not if_found:
            return None, None
        min_capacity = float('inf')
        path = [t]
        curr_node = t
        while curr_node != s:
            curr_node_parent = parent_map[curr_node]
            if T_residual[curr_node_parent][curr_node] < min_capacity:
                min_capacity = T_residual[curr_node_parent][curr_node]
            path.insert(0, curr_node_parent)
            curr_node = curr_node_parent
        return path, min_capacity