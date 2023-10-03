import java.util.Scanner;

public class _1ArithmeticSum {

    public static int summation(int a1, int d, int an)
    {
        int res = a1;

        System.out.print(a1);
        for(int i=a1+d; i<=an; i+=d) {
            System.out.print(" + " + i);
            res += i;
        }

        System.out.print(" = ");
        return res;
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int i = scanner.nextInt();
        int k = scanner.nextInt();
        int j = scanner.nextInt();

        System.out.println(summation(i, k, j));
    }
}
