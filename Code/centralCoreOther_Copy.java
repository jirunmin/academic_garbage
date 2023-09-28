import java.io.*;

public class centralCoreOther_Copy {
    static final int N = 100010;
    static int n, idx, res;
    static int[] h = new int[N], e = new int[N * 2], ne = new int[N * 2];
    static boolean[] status = new boolean[N];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StreamTokenizer st = new StreamTokenizer(br);
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


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
        res = res<max?res:max;
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


