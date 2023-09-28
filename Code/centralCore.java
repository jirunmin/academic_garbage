import java.util.*;
public class centralCore{
    static int N = 100010,M = N * 2,idx,n;
    static int[] h = new int[N];
    static int[] e = new int[M];//存的是双倍，所以是M
    static int[] ne = new int[M];//存的是双倍，所以是M
    static boolean[] st = new boolean[N];
    static int ans = N; //一开始将最大值赋值成N,最大了
    /***
     * 邻接表，存储方法
     * 邻接表不用管执行顺序，只需要知道每个节点能够执行到每个多少个节点就行
     * 比如案例中4 3 , 4 6 ,头结点4插入两个节点3和6,所以执行到4就能够执行3和6,
     * 固定的，邻接表就是这样子的
     ***/
    public static void add(int a,int b){
        e[idx] = b;
        ne[idx] = h[a];
        h[a] = idx++;
    }
    //返回的是当前子树的数量,比如1下面的所有数量包括自己就是9
    public static int dfs(int u){
        int res = 0;//连通块中的最大值这个其实就是ans，到时候跟ans比较大小，小的话就赋值给ans的
        st[u] = true;//将这个删除的点标记，下次不在遍历
        int sum = 1;//将删除的点也算上是初始值就是1;到时候有利于求n-sum;

        //单链表遍历
        for(int i = h[u];i != -1 ; i = ne[i]){
            int j = e[i];//然后将每一个的指向的点用变量表示出来
            if(!st[j]){ //然后如果是没用过，没被标记过的，就可以执行
                int s = dfs(j);//然后递归他的邻接表上面所有能够抵达的点
                //然后返回的数量是他所删除的点下面的连通块的大小
                res = Math.max(res,s); //然后和res比较一下大小，谁大谁就是最大连通块
                sum += s; //这里是将每递归一个点，就增加一个返回的s，就可以将这个值作为返回值成为最大连通块
            }
        }
        /***
         * 因为邻接表表中只是往下面执行，删除的点的上面的连通块可能是最大的连通块，
         * 所以需要用总数减去我们下面所统计出来的最大的连通块
         * 然后将最大的连通块的值赋值给res
         * **/
        res = Math.max(res,n-sum);
        //然后将每个次的最大值进行比较，留下最小的最大值
        ans = Math.min(res,ans);
        return sum;
    }
    public static void main(String[] ags){
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        //这里是将每一个头节点都赋值成-1
        for(int i = 1 ; i < N ; i++ ){
            h[i] = -1;
        }
        //案例输入输出
        for(int i = 0 ; i < n - 1 ; i ++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            //因为是无向边，所以就两个数同时指向对方
            add(a,b);
            add(b,a);
        }
        dfs(1);//从1开始
        //最后输出的是最小的最大值
        System.out.println(ans);
    }
}


