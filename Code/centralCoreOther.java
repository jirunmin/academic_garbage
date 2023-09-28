import java.io.*;

public class centralCoreOther {
    static final int N = (int)1e5 + 10;
    static int n, idx, res;
    static int[] h = new int[N], e = new int[N << 1], ne = new int[N << 1];
    static boolean[] status = new boolean[N];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StreamTokenizer st = new StreamTokenizer(br);

    static {
        res = N;
    }

    static void init(int[] h, int n) {
        for (int i = 1; i <= n; ++i) {
            h[i] = -1;
        }
    }

    static void add(int a, int b) {
        e[idx] = b;
        ne[idx] = h[a];
        h[a] = idx++;
    }

    static int dfs(int u) {
        int s, sum = 1, max = 0;
        for (int i = h[u]; i > -1; i = ne[i]) {
            if (!status[e[i]]) {
                status[e[i]] = true;
                s = dfs(e[i]);
                max = Math.max(max, s);
                sum += s;
            }
        }
        max = Math.max(max, n - sum);
        res = Math.min(res, max);
        return sum;
    }

    public static void main(String[] args) throws IOException {
        st.nextToken();
        n = (int)st.nval;
        init(h, n);
        int a, b;
        for (int i = 1; i < n; ++i) {
            st.nextToken();
            a = (int)st.nval;
            st.nextToken();
            b = (int)st.nval;
            add(a, b);
            add(b, a);
        }
        dfs(1);
        bw.write(res + "");
        bw.close();
    }
}


