import java.util.Scanner;
public class _2_3AddNum {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int m = scanner.nextInt();

        int sum = n;
        System.out.print(n);
        for(int i=n+k; i<=m; i+=k){
            System.out.print(" + " + i);
            sum += i;
        }

        System.out.println(" = " + sum);
    }
}
