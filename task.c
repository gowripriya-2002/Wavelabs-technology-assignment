#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_NODES 101
#define INFINITY INT_MAX

typedef struct {
    int source;
    int target;
    int time;
} Edge;

int networkDelayTime(Edge times[], int n, int k) {
    int dist[MAX_NODES];
    bool visited[MAX_NODES];

    // Step 1: Initialize distance array
    for (int i = 1; i <= n; i++) {
        dist[i] = INFINITY;
        visited[i] = false;
    }
    dist[k] = 0;

    // Step 2: Process each node
    for (int i = 1; i <= n; i++) {
        int minDist = INFINITY;
        int minNode = -1;

        // Step 3: Find the node with minimum distance
        for (int j = 1; j <= n; j++) {
            if (!visited[j] && dist[j] < minDist) {
                minDist = dist[j];
                minNode = j;
            }
        }

        // Step 4: Mark the node as visited
        visited[minNode] = true;

        // Step 5: Update distances for neighbors
        for (int j = 0; j < n; j++) {
            if (times[j].source == minNode) {
                int neighbor = times[j].target;
                int travelTime = times[j].time;
                int newDist = dist[minNode] + travelTime;

                if (newDist < dist[neighbor]) {
                    dist[neighbor] = newDist;
                }
            }
        }
    }

    // Step 6: Check for unreachable nodes
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INFINITY) {
            return -1;
        }
    }

    // Step 7: Return the maximum distance
    int maxDist = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] > maxDist) {
            maxDist = dist[i];
        }
    }

    return maxDist;
}

int main() {
    Edge times[] = {
        {2, 1, 1},
        {2, 3, 1},
        {3, 4, 1}
    };
    int n = 4;
    int k = 2;

    int result = networkDelayTime(times, n, k);
    printf("Minimum time for all nodes to receive the signal: %d\n", result);

    return 0;
}