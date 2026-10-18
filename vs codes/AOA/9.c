#include <stdbool.h>
#include <stdio.h>

int isSafe(int v, bool graph[][4], int color[], int c, int n) {
    for (int i = 0; i < n; i++) {
        if (graph[v][i] && c == color[i])
            return 0; // Neighbor already has this color
    }
    return 1;
}

int graphColoringUtil(bool graph[][4], int m, int color[], int v, int n) {
    if (v == n)
        return 1; // All vertices are colored

    for (int c = 1; c <= m; c++) {
        if (isSafe(v, graph, color, c, n)) {
            color[v] = c; // Try this color

            if (graphColoringUtil(graph, m, color, v + 1, n))
                return 1;

            color[v] = 0; // Backtrack
        }
    }
    return 0;
}

void graphColoring(bool graph[][4], int m, int n) {
    int color[4] = {0};

    if (!graphColoringUtil(graph, m, color, 0, n)) {
        printf("Solution does not exist for %d colors.\n", m);
        return;
    }

    printf("Solution exists with %d colors:\n", m);
    for (int i = 0; i < n; i++) {
        printf("Vertex %d ---> Color %d\n", i, color[i]);
    }
}

int main(void) {
    int n, m;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of colors: ");
    scanf("%d", &m);

    bool graph[4][4] = {0};
    int temp[4][4] = {0};

    printf("Enter adjacency matrix (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &temp[i][j]);
            graph[i][j] = temp[i][j] != 0;
        }
    }

    graphColoring(graph, m, n);
    return 0;
}