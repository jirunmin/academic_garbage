import java.util.Scanner;
public class _2_2AddNum {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();

        int sum = n;
        System.out.print(n);
        for(int i=n+1; i<=m; i++){
            System.out.print(" + " + i);
            sum += i;
        }

        System.out.println(" = " + sum);
    }
}
